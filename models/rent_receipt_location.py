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

    #name = fields.Char('Name')
    property_id = fields.Many2one('rent.receipt.property', string='Property')
    description = fields.Text('Description')
    customer_id = fields.Many2one('res.partner', string='Customer')
    #seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')
    amount_charges = fields.Float('Amount charges')
    amount_net = fields.Float('Amount Net')
    name_of_customer = fields.Char(
        string='Customer Name',
        related='customer_id.name')
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
