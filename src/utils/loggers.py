#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

DEFAULT_FORMAT = "\n%(asctime)s - %(levelname)-8s  %(name)s:%(lineno)d -> %(message)s\n"
DEFAULT_FORMATTER = logging.Formatter(DEFAULT_FORMAT)

def createLogger(name, handler, level=logging.DEBUG, propagate=True):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler.setFormatter(DEFAULT_FORMATTER)
    logger.addHandler(handler)
    logger.propagate = propagate
    return logger