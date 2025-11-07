from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    rent_receipt_location_title = fields.Char(string='Title', required=False)
