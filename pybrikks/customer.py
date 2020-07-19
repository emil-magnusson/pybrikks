# -*- coding: utf-8 -*-

"""
brikksapi.customer
"""

from .base import BRIKKS
from datetime import datetime
import json


class Customer(BRIKKS):
    BASE_PATH = 'customers'
    URLS = {
        'info': '/{id}',
    }
    CUSTOMER_OPT = {'fields': ['addedAt',
                               'updatedAt',
                               'postalAddress',
                               'invoiceAddress',
                               'invoiceTransport',
                               'invoiceGroup',
                               'customerTypeId',
                               'externalId',
                               'email',
                               'invoiceEmail',
                               'phoneNumbers',
                               'isEnterprise'
                               ]
                    }

    def __init__(self, id=0, expand=False):
        """
        Represents a Brikks Customer
        """
        super(Customer, self).__init__()
        self.id = id
        data = self._get_info()

        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        self.addedAt = datetime.strptime(data.get('addedAt'), "%Y-%m-%dT%H:%M:%S%z")
        self.updatedAt = datetime.strptime(data.get('updatedAt'), "%Y-%m-%dT%H:%M:%S%z")
        self.postalAddress = [value for key, value in data.get('postalAddress').items()]
        self.invoiceAddress = [value for key, value in data.get('invoiceAddress').items()]
        self.invoiceTransport = data.get('invoiceTransport').get('name')
        self.invoiceGroup = data.get('invoiceGroup').get('name')
        self.customerTypeId = data.get('customerTypeId')
        self.externalId = data.get('externalId')
        self.email = data.get('email')
        self.invoiceEmail = data.get('invoiceEmail')
        self.phoneNumbers = [number.get('number') for number in data.get('phoneNumbers')]
        self.isEnterprise = data.get('isEnterprise')
        self.raw = json.dumps(data)

    def __repr__(self):
        retval = '<brikks.Customer: {0}>'.format(self.id)
        return retval

    def _get_info(self):
        """
        Get the primary information about a brikks customer.

        Returns:
            `brikks customer`
        """

        path = self._get_id_path('info')
        response = self._GET(path, self.CUSTOMER_OPT)

        return response

