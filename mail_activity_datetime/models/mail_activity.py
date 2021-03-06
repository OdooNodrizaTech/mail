# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    date_deadline = fields.Datetime(
        string='Date deadline'
    )
