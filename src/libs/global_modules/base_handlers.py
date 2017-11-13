#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

class ApplicationAccess:
    """Base class to access application properties
    (such db, host, port) trough syntax self.<attr>"""
    
    @property
    def logger(self):
        return self.application.logger

    @property
    def db(self):
        return self.application.db

    @property
    def host(self):
        return self.application.host

    @property
    def port(self):
        return self.application.port

    @property
    def web_url(self):
        return self.application.web_url

class BaseRequestHandler(RequestHandler, ApplicationAccess):
    pass
