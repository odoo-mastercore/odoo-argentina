##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields

class L10nLatamDocumentType(models.Model):
    _inherit = "l10n_latam.document.type"

    export_to_citi = fields.Boolean(
        help='Set True if this document type and can be imported on RG 3685'
    )
