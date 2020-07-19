# -*- coding: utf-8 -*-

"""
brikksapi.areatype
"""

from .base import BRIKKS
import json

class AreaType(BRIKKS):
    BASE_PATH = 'area-types'
    URLS = {
        'info': '/{id}',
    }
    AREATYPE_OPT = {'fields': []
                    }

    def __init__(self, id=0, expand=False):
        """
        Represents a Brikks AreaType
        """
        super(AreaType, self).__init__()
        self.id = id
        data = self._get_info()

        self.name = data.get('name')
        self.raw = json.dumps(data)

    def __repr__(self):
        retval = '<brikks.AreaType: {0}>'.format(self.id)
        return retval

    def _get_info(self):
        """
        Get the primary information about a brikks area type.

        Returns:
            `brikks area type`
        """

        path = self._get_id_path('info')
        response = self._GET(path, self.AREATYPE_OPT)

        return response

