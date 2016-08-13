#! /usr/env python
import address

class pm(object):
    """Class for property manager"""

    def __init__(self):
        self.name = None
        self.address = None

    def addName(self, name):
        self.name = name

    def addAddress(self, address_list):

        # address_list is a list of multiple elements containing the address
        address_str = ' '.join(address_list)
        self.address = address(address_str)

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address