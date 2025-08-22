# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentReceiptLocation(models.Model):
    _name = 'rent.receipt.location'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        'image.mixin',
    ]
    _description = 'Rent receipt location'

    name = fields.Char('Name')
    property_id = fields.Many2one('rent.receipt.property', string='Property')
    description = fields.Text('Description')
    customer_id = fields.Many2one('res.partner', string='Customer')
    seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')
    amount_charges = fields.Float('Amount charges')
    amount_net = fields.Float('Amount Net')
