# -*- coding: utf-8 -*-
from odoo import models, fields, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_set_as_prospect(self):
        for partner in self.browse(self.env.context['active_ids']):
            tag_id = self.env.ref('general_actions.res_partner_category_prospects')

            partner.write({'category_id': [(4, tag_id.id)]})

    def cron_update_notes(self):
        partner_ids = self.search([('comment', 'not like', 'Updated')], limit=2)

        if partner_ids:
            partner_ids.write({'comment': f"Updated on {fields.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"})


class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    # This is for handle the specific tag delete, avoiding when a tag is deleted been removed from partners.
    def unlink(self):
        for tag in self:
            if tag.id == self.env.ref('general_actions.res_partner_category_prospects').id:
                raise exceptions.UserError(f"Can't delete this record, archive {tag.name} tag instead.")

        return super(ResPartnerCategory, self).unlink()
