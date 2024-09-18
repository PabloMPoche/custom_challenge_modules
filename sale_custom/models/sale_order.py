# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type_id = fields.Many2one(comodel_name='sale.type', string='Sale Type')
    call_no = fields.Char(string='Call ID')
    handle_call = fields.Boolean('Handle Call')

    @api.onchange('sale_type_id')
    def _do_handle_call(self):
        for order in self:
            if order.sale_type_id:
                order.write({'handle_call': order.sale_type_id.handle_call_no})


class SaleType(models.Model):
    _name = 'sale.type'
    _description = 'Sale Type'

    name = fields.Char(string='Sale Type')
    handle_call_no = fields.Boolean(string='Handle Call')
