# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentReceiptProperty(models.Model):
    _name = 'rent.receipt.property'
    _description = 'Property'
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name) ', 'The name of the property must be unique')
    ]

    name = fields.Char(string='Name', required=True)
    description = fields.Text(
        string='Description',
        translate=True,
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Owner',
        required=True
    )
    street = fields.Char('street')
    city = fields.Char('city')
    zip = fields.Char('zip')
    country_id = fields.Many2one('res.country', string='country')
    type = fields.Selection([
        ('appartement', 'Appartement'),
        ('house', 'House'),
        ('office', 'Office'),
    ], string='type')
