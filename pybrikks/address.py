# -*- coding: utf-8 -*-

"""
brikksapi.address
"""

from .base import BRIKKS
from datetime import datetime
from .customer import Customer

class Address(BRIKKS):
    BASE_PATH = 'addresses'
    URLS = {
        'info': '/{id}',
        'sockets': '/{id}/sockets',
    }
    ADDRESS_OPT = {'fields': ['location',
                              'externalId',
                              'customer',
                              'sockets',
                              'areaID',
                              'firstActivationDate',
                              'activationDelay',
                              'searchableInCustomerPortal',
                              'status', ]
                   }

    def __init__(self, id=0, extend=False):
        """
        Represents a Brikks Address

         Args:
             id (integer): unique address id of a Brikks address.
             extend: Get detailed address data.
        """
        super(Address, self).__init__()

        self.id = id
        data = self._get_info()
        self.addedAt = datetime.strptime(data.get('addedAt'), "%Y-%m-%dT%H:%M:%S%z")
        self.updatedAt = datetime.strptime(data.get('updatedAt'), \
                                           "%Y-%m-%dT%H:%M:%S%z") if data.get('updatedAt') else None
        self.streetName = data.get('streetName')
        self.streetNumber = data.get('streetNumber')
        self.streetEntrance = data.get('streetEntrance')
        self.addressDetail = data.get('addressDetail')
        self.zipCode = data.get('zipCode')
        self.city = data.get('city')
        self.countryCode = data.get('countryCode')
        self.extend = extend
        if self.extend:
            self.latitude = data.get('location').get('lat')
            self.longitude = data.get('location').get('lng')
            self.externalId = data.get('externalId')
            self.socket = self._get_sockets()
            self.areaId = data.get('areaId')
            self.firstActivationDate = data.get('firstActivationDate')
            self.activationDelay = data.get('activationDelay')
            self.searchableInCustomerPortal = data.get('searchableInCustomerPortal')
            self.status = data.get('status')
            self.template = data.get('template')
            self.customer_id = data.get('customer').get('id') if data.get('customer') else None
            self.customer = Customer(id=self.customer_id) if self.customer_id else None


    def __repr__(self):
        retval = '<brikks.AreaType: {0}>'.format(self.id)
        return retval

    def _get_info(self):
        """
        Get the primary information about a brikks address.

        Returns:
            `brikks address`
        """

        path = self._get_id_path('info')
        response = self._GET(path, self.ADDRESS_OPT)

        return response

    def _get_sockets(self):
        """Returns a list of Brikks `Sockets` linked to the specefic address.

         Returns:
             `Sockets` Representing a list of Brikks sockets linked to a address.
         """

        path = self._get_id_path('sockets')
        response = self._GET(path)

        return [Socket(data=socket) for socket in response.get('results')]


class Socket(object):
    """
    Represents a Brikks Socket
    """

    def __init__(self, data):
        self.id = data.get('id')
        self.socketIdentifier = data.get('socketIdentifier')
        self.tag = data.get('tag')
        self.accessPoint = data.get('accessPoint')

    def __repr__(self):
        retval = '<brikks.Socket: {0}>'.format(self.id)
        return retval
