#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from base_handlers import BaseRequestHandler

class HomeHandler(BaseRequestHandler):
	def get(self):
		return self.render("index.html")
		