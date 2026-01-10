# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import base64
from babel.dates import format_datetime
from babel.core import UnknownLocaleError

class RentReceiptLocation(models.Model):
    _name = 'rent.receipt.location'
    _inherit = [
            'mail.thread',
            'mail.activity.mixin',
            'image.mixin',
            ]
    _description = 'Rent receipt location'

    def action_send_mail(self):
        self.ensure_one()
        template = self.env.ref('rent_receipt.mail_template_receipt_location', raise_if_not_found=False)
        if not template:
            raise UserError(_("Mail Template not found. Please check the template."))
        template.send_mail(self.id, force_send=True)

    def send_email_with_pdf_attach(self):
        self.ensure_one()
        template = self.env.ref('rent_receipt.mail_template_receipt_location', raise_if_not_found=False)
        report_action = self.env.ref('rent_receipt.action_report_rent_receipt_location', raise_if_not_found=False)
        if not template or not report_action:
            raise UserError(_("Unable to locate the email template or report definition."))

        pdf_content, _ = report_action._render_qweb_pdf([self.id])
        attachment = self.env['ir.attachment'].create({
            'name': _("Rent receipt %s") % (self.display_name or self.name_of_customer),
            'type': 'binary',
            'datas': base64.b64encode(pdf_content),
            'mimetype': 'application/pdf',
            'res_model': self._name,
            'res_id': self.id,
            'company_id': self.company_id.id,
        })
        try:
            template.send_mail(
                self.id,
                force_send=True,
                email_values={'attachment_ids': [(6, 0, [attachment.id])]},
            )
        finally:
            attachment.unlink()
        return True

    #name = fields.Char('Name')
    property_id = fields.Many2one(
        'rent.receipt.property',
        string='Property',
        check_company=True,
    )
    description = fields.Text('Description')
    customer_id = fields.Many2one('res.partner', string='Customer')
    #seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')
    payment_day = fields.Integer('Payment day')
    amount_charges = fields.Float('Amount charges')
    amount_net = fields.Float('Amount Net')
    current_month = fields.Char(compute="_get_current_month")
    current_year = fields.Char(compute="_get_current_year")
    currency = fields.Char('Currency', default="Euros")
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )

    @api.depends('amount', 'amount_charges')
    def _compute_total(self):
        for record in self:
            record.amount_net = (record.amount_charges or 0.0) + (record.amount or 0.0)

    @api.depends('customer_id.lang')
    def _get_current_year(self):
        for record in self:
            now = fields.Datetime.context_timestamp(record, fields.Datetime.now())
            lang = record.customer_id.lang or self.env.lang or 'en_US'
            try:
                record.current_year = format_datetime(now, "y", locale=lang)
            except UnknownLocaleError:
                record.current_year = now.strftime("%Y")

    @api.depends('customer_id.lang')
    def _get_current_month(self):
        for record in self:
            now = fields.Datetime.context_timestamp(record, fields.Datetime.now())
            lang = record.customer_id.lang or self.env.lang or 'en_US'
            try:
                record.current_month = format_datetime(now, "MMMM", locale=lang)
            except UnknownLocaleError:
                record.current_month = now.strftime("%B")

    name_of_customer = fields.Char(
            string='Customer Name',
            related='customer_id.name')
    email_of_customer = fields.Char(
            string='Customer Email',
            related='customer_id.email')
    zip_of_property = fields.Char(
            string='Zip',
            related='property_id.zip')
    street_of_property = fields.Char(
            string='Street',
            related='property_id.street')
    city_of_property = fields.Char(
            string='City',
            related='property_id.city')
    name_of_owner = fields.Char(
            string='Owner Name',
            related='property_id.owner_id.name')
    zip_of_owner = fields.Char(
            string='Owner Zip',
            related='property_id.owner_id.zip')
    street_of_owner = fields.Char(
            string='Owner Street',
            related='property_id.owner_id.street')
    city_of_owner = fields.Char(
            string='Owner City',
            related='property_id.owner_id.city')
    email_of_owner = fields.Char(
            string='Owner Email',
            related='property_id.owner_id.email')
