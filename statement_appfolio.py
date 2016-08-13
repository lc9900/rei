#! /usr/bin/env python
# class for appfolio statements.

import statement_general
import pm

class statementAppfolio(statement_general):
    """class for appolio statement. Inherits from statement class"""

    def __init__(self):
        # Initialize parent class attribute
        statement_general.__init__(self)
        # Appfolio specific attributes are defined here
        self.pm = pm()
        # This list is a list of dictionaries of inc/exp activities.
        # It MUST correlate with self.property_list in terms of index from class statement_general.
        # In other words, the 1st dictionary of activities in self.property_activities MUST
        # belong to the 1st property listed in the self.property_list, so on and so forth.
        # This is a child class attribute because these entries has the most probability to be different
        # between vendors.
        self.property_activities = []

    def writeStatementToDB(self):
        # write the entire statement to database
        pass

    def getPeriod(self, section_raw_list):
        pass

    def getOwner(self, section_raw_list):
        pass

    def getProperty(self, section_raw_list):
        pass

    def getActivity(self, section_raw_list):
        pass

    def getPm(self, section_raw_list):
        pass


    def addPeriod(self, section_raw_list):
        # Sample: 10 Mar 2016-11 Apr 2016

        pass

    def addOwner(self, section_raw_list):
        pass

    def addProperty(self, section_raw_list):
        pass

    def addActivity(self, section_raw_list):
        pass

    def addPm(self, section_raw_list):
        # index 0 is name of property manager
        # index 1 and up are the address
        self.pm.addName(section_raw_list[0])
        self.pm.addAddress(section_raw_list[1:])