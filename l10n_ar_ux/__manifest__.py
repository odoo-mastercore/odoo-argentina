{
    'name': 'Argentinian Accounting UX',
    'version': "13.0.1.12.0",
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'ADHOC SA, MASTERCORE SAS',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [
        'account_debit_note',
        'l10n_ar',
        'account_check',
        # for payment group report
        'account_withholding',
        'account_payment_group_document',
    ],
    'data': [
        'data/res_currency_data.xml',
        'data/account_account_tag_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_tax_template_data.xml',
        'views/portal_templates.xml',
        'views/account_move_view.xml',
        'wizard/res_partner_update_from_padron_wizard_view.xml',
        'views/res_partner_view.xml',
        'views/afip_concept_view.xml',
        'views/afip_activity_view.xml',
        'views/afip_tax_view.xml',
        'views/report_invoice.xml',
        'views/res_config_settings_views.xml',
        'reports/account_invoice_report_view.xml',
        'reports/report_payment_group.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'post_init_hook': 'post_init_hook',
}
