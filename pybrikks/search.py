# -*- coding: utf-8 -*-

"""
brikksapi.search
"""

from .base import BRIKKS


class Search(BRIKKS):
    """
    Search functionality
    """
    BASE_PATH = ''
    URLS = {
        'address': 'addresses/',

    }

    def address(self, **kwargs):
        """
        Search for address.

        Args:
            streetName: string.
            streetNumber: integer
            City: string
            (A wildcard character * can be added in the end)

        Returns:
            Response
        """
        path = self._get_path('address')

        response = self._GET(path, kwargs)

        return response


