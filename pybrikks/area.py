# -*- coding: utf-8 -*-

"""
brikksapi.area
"""

from .base import BRIKKS
import json


class Area(BRIKKS):
    BASE_PATH = 'areas'
    URLS = {
        'info': '/{id}',
    }
    AREA_OPT = {'fields': ['available',]
                    }

    def __init__(self, id=0, expand=False):
        """
        Represents a Brikks AreaType
        """
        super(Area, self).__init__()
        self.id = id
        data = self._get_info()

        self.name = data.get('name')
        self.available = data.get('available')
        self.raw = json.dumps(data)

    def __repr__(self):
        retval = '<brikks.AreaType: {0}>'.format(self.id)
        return retval

    def _get_info(self):
        """
        Get the primary information about a brikks area.

        Returns:
            `brikks area`
        """

        path = self._get_id_path('info')
        response = self._GET(path, self.AREA_OPT)

        return response

