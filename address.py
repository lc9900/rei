#! /usr/bin/env python
# Use usaddress module
# https://github.com/datamade/usaddress
# Web Interface: https://parserator.datamade.us/usaddress
#
# Example output from usaddress
# 5229	        AddressNumber
# E.	        StreetNamePreDirectional
# 34th	        StreetName
# St.	        StreetNamePostType
# fl	        OccupancyType
# 4th	        OccupancyIdentifier
# Indianapolis	PlaceName
# IN	        StateName
# 46218	        ZipCode

import usaddress
class address(object):
    """class to represent address"""

    def __init__(self, address_str):

        # Retaining the raw string
        self.address_str = address_str
        # # The tag method will try to be a little smarter
        # # it will merge consecutive components, strip commas, & return an address type
        # # expected output: (OrderedDict([('AddressNumber', u'123'), ('StreetName', u'Main'),
        # # ('StreetNamePostType', u'St.'), ('OccupancyType', u'Suite'), ('OccupancyIdentifier', u'100'),
        # ('PlaceName', u'Chicago'), ('StateName', u'IL')]), 'Street Address')
        address_dict = usaddress.tag(address_str)

        # The if conditional is needed to avoid dictionary's key error if the key doesn't exist
        self.addressNumber = address_dict['AddressNumber'] if 'AddressNumber' in address_dict.keys() \
            else raise ValueError('Address AddressNumber not provided')
        # noinspection PyUnreachableCode
        self.streetName = address_dict['StreetName'] if 'StreetName' in address_dict.keys() \
            else raise ValueError('Address StreetName not provided')
        self.streetNamePostType = address_dict['StreetNamePostType'] if 'StreetNamePostType' in address_dict.keys() \
            else raise ValueError('Address StreetNamePostType not provided')
        self.placeName = address_dict['PlaceName'] if 'PlaceName' in address_dict.keys() \
            else raise ValueError('Address PlaceName not provided')
        self.stateName = address_dict['StateName'] if 'StateName' in address_dict.keys() \
            else raise ValueError('Address StateName not provided')

        # Optional values
        self.occupancyIdentifier = address_dict[
            'OccupancyIdentifier'] if 'OccupancyIdentifier' in address_dict.keys() \
            else
        raise ValueError('Address OccupancyIdentifier not provided')
        self.occupancyType = address_dict['OccupancyType'] if 'OccupancyType' in address_dict.keys() \
            else
        raise ValueError('Address OccupancyType not provided')
        self.streetNamePreDirectional = address_dict[
            'StreetNamePreDirectional'] if 'StreetNamePreDirectional' in address_dict.keys() \
            else None
        self.zipCode = address_dict['ZipCode'] if 'ZipCode' in address_dict.keys() else None

    def getAddressString(self):
        return self.address_str

    def getAddressNumber(self):
        return self.addressNumber

    def getStreetNamePreDirectional(self):
        return self.streetNamePreDirectional

    def getStreetName(self):
        return self.streetName

    def getStreetNamePostType(self):
        return self.streetNamePostType

    def getOccupancyIdentifier(self):
        return self.occupancyIdentifier

    def getOccupancyType(self):
        return self.occupancyType

    def getPlaceName(self):
        return self.placeName

    def getStateName(self):
        return self.stateName

    def getZipCode(self):
        return self.zipCode


    def compareAddress(self, target_address):
        """Comparing itself against a target_address object
        If address-parts are the same, then they are the same, and return True.
        Else return False. Some value might be None, like suite or floor, so for those,
        we would only compare if they are not None.
        Zip code comparison is not needed."""
        if self.getAddressNumber() != target_address.getAddressNumber():
            return False
        if (self.getStreetNamePreDirectional() != target_address.getStreetNamePreDirectional() and
            self.getStreetNamePreDirectional() is not None):
            return False
        if self.getStreetName() != target_address.getStreetName():
            return False
        if self.getStreetNamePostType() != target_address.getStreetNamePostType():
            return False
        if (self.getOccupancyIdentifier() != target_address.getOccupancyIdentifier() and
            self.getOccupancyIdentifier() is not None):
            return False
        if (self.getOccupancyType() != target_address.getOccupancyType() and
            self.getOccupancyType() is not None):
            return False
        if self.getPlaceName() != target_address.getPlaceName():
            return False
        if self.getStateName() != target_address.getStateName():
            return False

        # Zip code comparison is not neccessary

        return True

    def printAddressDict(self):
        print "Address Number: %s" % self.getAddressNumber()
        print "getStreetNamePreDirectional: %s" % self.getStreetNamePreDirectional()
        print "Street Name: %s" % self.getStreetName()
        print "Street Type: %s" % self.getStreetNamePostType()
        print "FL/Suite: %s" % self.getOccupancyType()
        print "FL/Suite #: %s" % self.getOccupancyIdentifier()
        print "City/County: %s" % self.getPlaceName()
        print "State: %s" % self.getStateName()
        print "Zip: %s" % self.getZipCode()
