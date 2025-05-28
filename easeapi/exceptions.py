# -*- coding: utf-8 -*-
"""
    exceptions.py

    Exceptions raised by the EaseApi client.

    :copyright: (c) 2025 by Ventura Securities Ltd.
    :license: see LICENSE for details.
"""


class EaseApiException(Exception):
    """
    Base exception class representing a EaseApi client exception.

    Every specific EaseApi client exception is a subclass of this
    and  exposes two instance variables `.code` (HTTP error code)
    and `.message` (error text).
    """

    def __init__(self, message, code=500):
        """Initialize the exception."""
        super(EaseApiException, self).__init__(message)
        self.code = code


class GeneralException(EaseApiException):
    """An unclassified, general error. Default code is 500."""

    def __init__(self, message, code=500):
        """Initialize the exception."""
        super(GeneralException, self).__init__(message, code)


class AuthTokenException(EaseApiException):
    """Represents all token and authentication related errors. Default code is 401."""

    def __init__(self, message, code=401):
        """Initialize the exception."""
        super(AuthTokenException, self).__init__(message, code)

class DataException(EaseApiException):
    """Represents a bad response from the backend Order Management System (OMS). Default code is 502."""

    def __init__(self, message, code=502):
        """Initialize the exception."""
        super(DataException, self).__init__(message, code)


class ParameterException(EaseApiException):
    """Represents a missing parameters exception. Default code is 503."""

    def __init__(self, message, code=503):
        """Initialize the exception."""
        super(ParameterException, self).__init__(message, code)
