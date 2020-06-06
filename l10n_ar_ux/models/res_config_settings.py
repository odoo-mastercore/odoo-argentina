# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

try:
    from pyafipws.padron import PadronAFIP
except ImportError:
    PadronAFIP = None

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    l10n_ar_country_code = fields.Char(related='company_id.country_id.code', string='Country Code')

    def refresh_taxes_from_padron(self):
        self.refresh_from_padron("impuestos")

    def refresh_concepts_from_padron(self):
        self.refresh_from_padron("conceptos")

    def refresh_activities_from_padron(self):
        self.refresh_from_padron("actividades")

    @api.model
    def refresh_from_padron(self, resource_type):
        """
        resource_type puede ser "impuestos", "conceptos", "actividades",
        "caracterizaciones", "categoriasMonotributo", "categoriasAutonomo".
        """
        if resource_type == 'impuestos':
            model = 'afip.tax'
        elif resource_type == 'actividades':
            model = 'afip.activity'
        elif resource_type == 'conceptos':
            model = 'afip.concept'
        else:
            raise UserError(_('Resource Type %s not implemented!') % (
                resource_type))
        padron = PadronAFIP()
        separator = ';'
        data = padron.ObtenerTablaParametros(resource_type, separator)
        _logger.warning(data)
        codes = []
        for line in data:
            code, name = line.split(separator)[1:3]
            vals = {
                'code': code,
                'name': name,
                'active': True,
            }
            record = self.env[model].search([('code', '=', code)], limit=1)
            codes.append(code)
            if record:
                record.write(vals)
            else:
                record.create(vals)
        # deactivate the ones that are not in afip
        self.env[model].search([('code', 'not in', codes)]).write(
            {'active': False})
