# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


def formatted_number(phone):
    number_formatted = ''.join([str(i) for i in phone if i.isdigit()])
    return number_formatted


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_number_ids = fields.One2many(
        comodel_name='res.partner.phones',
        inverse_name='partner_id',
        string='Company Numbers'
    )


class ResPartnerPhones(models.Model):
    _name = 'res.partner.phones'
    _description = 'Res Partner Phones'
    _rec_name = 'phone_number'

    phone_number = fields.Char(string='Phone Number', required=True)
    active_number = fields.Boolean(string='Active', default=True)
    main = fields.Boolean(string='Main Number')
    partner_id = fields.Many2one(string='Partner', comodel_name='res.partner')

    _sql_constraints = [
        (
            'phone_uniq',
            'unique (phone_number)',
            """Phone numbers can't be repeated!"""
        ), (
            'phone_len',
            'CHECK(char_length(phone_number) > 4)',
            """There isn't a number that short. The minimum size is 5 digits."""
        ),
    ]

    @api.constrains('main')
    def _check_phone_number(self):
        for rec in self:
            number = self.search([
                ('partner_id', '=', rec.partner_id.id),
                ('main', '=', True)
            ])

            if len(number) > 1:
                raise ValidationError('There only can be one main number.')

    # This two supers are for handle phone number field for only number and autoformat, make the phone number field as
    # and integer is not a proper way, so I decide to do it as str and format it.
    # Probably there is a better way to handle it.
    def create(self, vals_list):
        vals_list[0]['phone_number'] = formatted_number(vals_list[0]['phone_number'])
        return super(ResPartnerPhones, self).create(vals_list)

    def write(self, vals):
        if 'phone_number' in vals:
            vals['phone_number'] = formatted_number(vals['phone_number'])
        return super(ResPartnerPhones, self).write(vals)
