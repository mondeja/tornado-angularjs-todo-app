#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, hashlib
from motor.motor_tornado import MotorClient

class Config:
    SECRET_KEY = hashlib.sha256(os.environ["COOKIE_SECRET"].encode("utf-8")).digest()

    #DB_NAME = "tornado-react-todo-app"
    #DB = MotorClient(os.environ["MONGODB_URI"] % (os.environ["MONGODB_USERNAME"],
    #                                               os.environ["MONGODB_PASSWORD"], 
    #                                               DB_NAME))[DB_NAME]
    # MONGODB_URI is something like: mongodb://%s:%s@ds253452.mlab.com:53452/%s
    BASE_DIR = os.path.dirname(__file__)
    LOGS_DIR = os.path.join(BASE_DIR, "log")
    STATIC_PATH = os.path.join(BASE_DIR, "assets", "static")

    GLOBAL_MODULES = [
        # Folders to append to system path for easy python imports
        os.path.join(BASE_DIR, "libs/global_modules")
    ]

class DevelopmentConfig(Config):
    DEBUG = True
    SSL = False
    HOST = "localhost"
    PORT = os.environ["PORT"]
    WEB_URL = "http://{}:{}".format(HOST, PORT)

class StagingConfig(Config):
    DEBUG = True
    SSL = True
    HOST = "0.0.0.0"
    PORT = os.environ["PORT"]
    WEB_URL = "http://{}:{}".format(HOST, PORT)

class ProductionConfig(Config):
    DEBUG = False
    SSL = True
    HOST = "0.0.0.0"
    PORT = os.environ["PORT"]
    WEB_URL = "http://{}:{}".format(HOST, PORT)


# Environments configs mapping
dev = DevelopmentConfig
stage = StagingConfig
pro = ProductionConfig


# ======    GLOBAL CONFIG   =======

for path in Config.GLOBAL_MODULES:
    sys.path.append(path)

# ==================================