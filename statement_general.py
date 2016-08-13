#! /usr/bin/env python
# Class for vendor statements

import pm
import owner
import address
import activity

class statement_general(object):
    """Parent statement class"""

    def __init__(self):
        # period -- 10 Mar 2016-11 Apr 2016 -- parse into start_date, end_date
        # class pm -- name, address(class)
        # class owner -- name, address(class)
        # property -- address(class)
        # class Income/Expense entries -- Date, Payee/Payer, type, reference, description, income, expense, balance
        # Single statement may contain multiple properties -- identifier is at the top of each page, before inc/exp
        # table, it lists the property.
        # init method sets everything to none. Methods will be used to populate each attribute
        self.statement_file = None

        # property_list is a list of properties(class address objects) listed in the statement
        self.property_list = []

    def getStatementFile(self):
        return self.statement_file

    def addStatementFile(self, statement_file):
        self.statement_file = statement_file







