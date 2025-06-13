# -*- coding: utf-8 -*-
"""
EaseApi client for Python -- [EaseAPI](https://easeapi.venturasecurities.com).

Ventura Securities Ltd.

License
-------
EaseApi Python library is licensed under the MIT License

The library
-----------
EaseApi is a set of REST-like APIs that expose
many capabilities required to build a complete
investment and trading platform. Execute orders in
real time, manage user portfolio, and more, with the simple HTTP API collection

This module provides an easy to use abstraction over the HTTP APIs.
The HTTP calls have been converted to methods and their JSON responses
are returned as native Python structures, for example, dicts, lists, bools etc.
See the **[EaseApi API documentation](https://easeapi.venturasecurities.com/docs)**
for the complete list of APIs, supported parameters and values, and response formats.

"""

from __future__ import unicode_literals, absolute_import

from easeapi import exceptions
from easeapi.easeapigateway import EaseApiGateway
from easeapi.easeapiticker import EaseApiTicker

__all__ = ["EaseApiGateway", "EaseApiTicker", "exceptions"]
