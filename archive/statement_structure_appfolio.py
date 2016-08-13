#!/usr/env python

import statement_structure

class statement_structure_appfolio(statement_structure):
    """statement structure specific to appfolio"""

    def __init__(self):
        statement_structure.__init__(self)
        self.pm_block_end_before = 'Period:'

        self.period_block_start = 'Period:'
        self.period_block_end_before = 'Owner Statement'

        self.owner_block_start = 'Owner Statement'
        self.own_block_end_before = 'Properties'

        self.property_block_start = 'Properties'
        self.property_block_end_before = 'Date'

        self.table_block_start = 'Date'
        self.table_block_columns = ['Date',
                                    'Payee / Payer',
                                    'Type',
                                    'Reference',
                                    'Description',
                                    'Income',
                                    'Expense',
                                    'Balance']
        self.table_block_end_before = 'Total'
        self.page_end_at = "Page [1-100] of [1-100]"


