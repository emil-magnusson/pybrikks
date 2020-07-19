# -*- coding: utf-8 -*-

"""
brikksapi.customertype
"""

from .base import BRIKKS
import json

class CustomerType(BRIKKS):
    BASE_PATH = 'customer-types'
    URLS = {
        'info': '/{id}',
    }
    CUSTOMER_TYPE_OPT = {'fields': ['isEnterprise',]
                    }

    def __init__(self, id=0, expand=False):
        """
        Represents a Brikks CustomerType
        """
        super(CustomerType, self).__init__()
        self.id = id
        data = self._get_info()

        self.name = data.get('name')
        self.isEnterprise = data.get('isEnterprise')
        self.raw = json.dumps(data)

    def __repr__(self):
        retval = '<brikks.CustomerType: {0}>'.format(self.id)
        return retval

    def _get_info(self):
        """
        Get the primary information about a brikks customer type.

        Returns:
            `brikks customer type`
        """

        path = self._get_id_path('info')
        response = self._GET(path, self.CUSTOMER_TYPE_OPT)

        return response

