"""Remove FK references to tag_ret_perc_sicore_aplicada before Odoo tries to
delete the orphaned account.account.tag record."""

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return

    cr.execute("""
        SELECT res_id FROM ir_model_data
        WHERE module = 'l10n_ar_ux'
          AND name = 'tag_ret_perc_sicore_aplicada'
          AND model = 'account.account.tag'
    """)
    row = cr.fetchone()
    if not row:
        return

    tag_id = row[0]
    _logger.info(
        "Cleaning FK references for deprecated tag "
        "l10n_ar_ux.tag_ret_perc_sicore_aplicada (id=%s)", tag_id
    )

    cr.execute("""
        DELETE FROM account_account_tag_account_tax_repartition_line_rel
        WHERE account_account_tag_id = %s
    """, (tag_id,))
    _logger.info("Removed %s tax repartition line references", cr.rowcount)
