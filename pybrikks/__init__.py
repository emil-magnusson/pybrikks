# -*- coding: utf-8 -*-

"""
brikksapi


*pybrikks* is a wrapper, written in Python

"""

__title__ = 'pybrikks'
__version__ = '0.9'
__author__ = 'Emil Magnusson'
__copyright__ = 'Copyright (c) 2020'
__license__ = 'The MIT License (MIT)'

import os

from .base import APIKeyError,URIKeyError
from .address import Address
from .area import Area
from .areatype import AreaType
from .customer import Customer
from .customertype import CustomerType
from .search import Search


__all__ = ['APIKeyError',
            'Address',
            'Area',
            'AreaType',
            'Customer',
            'CustomerType',
            'Search',
           ]

API_KEY = os.environ.get('BRIKKS_API_KEY', None)
BASE_URI = os.environ.get('BRIKKS_BASE_URI', None)