#! /usr/env python

###############################################################
# Statement Structure
###############################################################
statement_structure_appfolio = {
    'pm_block_end_before': 'Period:',

    'period_block_start': 'Period:',
    'period_block_end_before': 'Owner Statement',

    'owner_block_start': 'Owner Statement',
    'owner_block_end_before': 'Properties',

    'property_block_start': 'Properties',
    'property_block_end_before': 'Date',

    'table_block_start': 'Date',
    'table_block_ignore': ['Beginning Cash']
    'table_block_columns': ['Date',
                            'Payee / Payer',
                            'Type',
                            'Reference',
                            'Description',
                            'Income',
                            'Expense',
                            'Balance'],
    'table_block_income_indices': [5],
    'table_block_expense_indices': [6],
    'table_block_end_before':'Total',
    'page_end_at': "Page [1-100] of [1-100]"
}
