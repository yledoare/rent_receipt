# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import Response, request
from odoo.exceptions import UserError
from io import BytesIO
import base64
import io
from PyPDF2 import PdfFileReader, PdfFileWriter

class RentReceiptLocation(models.Model):
    _name = 'rent.receipt.location'
    _inherit = [
            'mail.thread',
            'mail.activity.mixin',
            'image.mixin',
            ]
    _description = 'Rent receipt location'

    def send_email_with_pdf_attach(self):
      # OK template = self.env.ref('auth_signup.mail_template_user_signup_account_created')
      raise UserError("FIXME")
      template = self.env.ref('rent_receipt_location.mail_template_yld')
      #email_values = {'email_from': self.env.user.email}
      #template.send_mail(self.id, force_send=True, email_values=email_values)
      #template = self.env['mail.template'].browse(self.env.ref('rent_receipt.model_rent_receipt_location').id)
        # Ensure the template exists
      if template:
            # Send the email using the template
        template.send_mail(self.id, force_send=True)
      else:
        raise UserError("Mail Template not found. Please check the template.")
    def action_send_mail(self):
      report_pdf = request.env[ "ir.actions.report" ]._render_qweb_pdf( "rent_receipt.report_rent_receipt_location", [self.id])
      pdf_base64 = base64.b64encode(report_pdf[0])
      attachment_values = {
        'name': "THEFILE.pdf",
        'type': 'binary',
        'datas': pdf_base64,
        'mimetype': 'application/pdf',
      }
      attachment = self.env['ir.attachment'].create(attachment_values)
      ir_values = {
            'name': 'Rent receipt Report',
            'type': 'binary',
            'res_model': 'rent.receipt.location',
            }
      email_template = self.env.ref('rent_receipt.model_rent_receipt_location')
      print(self.customer_id.email)
      print(self.property_id.owner_id.email)
      return True
      # TO be continued

      if email_template:
            email_values = {
                'email_to': self.customer_id.email,
                'email_from': self.property_id.owner_id.email,
                }
            #email_template.attachment_ids = [(4, attachment.id)]
            #email_template.send_mail(self.id, email_values=email_values)
            email_template.send_mail(self.id)
            email_template.attachment_ids = [(5, 0, 0)]

    #name = fields.Char('Name')
    property_id = fields.Many2one('rent.receipt.property', string='Property')
    description = fields.Text('Description')
    customer_id = fields.Many2one('res.partner', string='Customer')
    #seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')
    payment_day = fields.Integer('Payment day')
    amount_charges = fields.Float('Amount charges')
    amount_net = fields.Float('Amount Net')
    currency = fields.Char('Currency', default="Euros")

    amount_net = fields.Float(compute="_compute_total")

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.amount_net = record.amount_charges + record.amount

    @api.depends("amount_charges")
    def _compute_total(self):
        for record in self:
            record.amount_net = record.amount_charges + record.amount

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
