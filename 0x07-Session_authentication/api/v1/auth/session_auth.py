#!/usr/bin/env python3
"""First step for creating a new authentication mechanism"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Inherits from Auth """
