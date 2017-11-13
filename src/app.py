#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from datetime import datetime

from tornado.web import Application
from tornado.ioloop import IOLoop
import tornado.options
import tornado.autoreload
import tornado.log

exec('from config import %s as config' % os.environ['APP_SETTINGS'])

from utils.loggers import createLogger
from utils.dates import time_until_end_of_day


class App(Application):

    SCENES_DIR = os.path.join(config.BASE_DIR, "scenes")
    SERVICES_DIR = os.path.join(config.BASE_DIR, "services")

    def __init__(self):
        self.directories_included = [self.SCENES_DIR, self.SERVICES_DIR]      
        self._initialize_settings()

        self.loop = IOLoop.current()

        #self.db = config.DB   # Database global access
        self.host = config.HOST
        self.port = config.PORT
        self.web_url = config.WEB_URL

        # =============   SETTINGS   ==============

        #if tornado.options.options.debug:
        #    app_path = "build"
        #else:
        #    app_path = "dist"

        #static_path = os.path.join(app_location, "client", app_path, "static")
        #template_path = os.path.join(app_location, "client", app_path, "templates")

        settings =  {
            "debug": config.DEBUG,
            "cookie_secret": config.SECRET_KEY,
            "xsrf_cookies": True,
            "web_url": config.WEB_URL,
        }

        if config.SSL:
            ssl_options = {"certfile": "cetificado.crt", 
                           "keyfile": "clave.key"}
        else:
            ssl_options = None

        # ========================================
        # Show configuration in logger when debug mode
        show_config = {}
        for key, value in config.__dict__.items():
            if "__" not in key:
                show_config[key] = value
        
        self.logger.debug("App started with configuration: %s" % str(show_config))
        # ========================================

        super(App, self).__init__(self.router, 
                                  **settings,
                                  ssl_options=ssl_options)


    # ========================   ROUTER   ============================
    @property
    def router(self):
        from tornado.web import StaticFileHandler

        from scenes.Home import HomeHandler    


        routes = [

            # =================   WEB RENDER   ==================

            ("/", HomeHandler),

            # =================   STATIC FILES   ==================
            (r"/css/(.*)", StaticFileHandler, 
                {"path": os.path.join(config.STATIC_PATH, "css")} ),
            (r"/js/(.*)", StaticFileHandler, 
                {"path": os.path.join(config.STATIC_PATH, "js")} ),

            
            # =====================================================
        ]
        # FileHandlers for component based structure
        for folder in self.directories_included:
            for subdir, dirs, files in os.walk(folder):
                for d in dirs:
                    scene = (r"/%s/(.*)" % d, StaticFileHandler,
                        {"path": os.path.join(folder, d)})
                    routes.append(scene)
                break

        return routes
    
    # ===============================================================


    def start(self):
        self._startime = self.loop.time()
        self._schedule_next_logger_filename_update()        
        return self.loop.start()


    def _initialize_settings(self):
        # ================   RUNTIME CONFIGURATION   ====================

        # -----     Parse options     -----
        self._parse_options()

        # -----     Logging     -----
        self._config_logger()

        # -----     Watch files for autoreload     -----
        self._watch_files()
        
        # ===============================================================
        
    def _parse_options(self):
        tornado.options.define("port", default=int(config.PORT), 
                               help="Run on the given port", type=int)
        tornado.options.define("debug", default=config.DEBUG, 
                               help="Debug mode", type=bool)
        tornado.options.define("ssl", default=config.SSL,
                               help="On/off SSL", type=bool)

        config.PORT = tornado.options.options.port
        config.DEBUG = tornado.options.options.debug
        config.SSL = tornado.options.options.ssl

        tornado.options.parse_command_line()

    def _config_logger(self):
        now = datetime.now()
        date = "{}-{}-{}".format(now.year, now.month, now.day)
        log_filename = os.path.join(config.LOGS_DIR, date + ".log")
        logger_handler = logging.FileHandler(log_filename)
        logger_level = logging.DEBUG if config.DEBUG else logging.INFO
        # Global logger access
        self.logger = createLogger("main", logger_handler, level=logger_level)

    def _watch_files(self):
        # Configure html, css and js files for watching in debug mode (dev)
        if config.DEBUG:
            exts = ["html", "css", "js"]
            for folder in self.directories_included:
                for subdir, dirs, files in os.walk(folder):
                    for f in files:
                        if f.split(".")[1] in exts:
                            f = os.path.join(folder, os.path.basename(subdir), f)
                            tornado.autoreload.watch(f)

    def _schedule_next_logger_filename_update(self):
        # Calculates next update for change logger filename
        next_day = datetime.fromtimestamp(self._startime) + time_until_end_of_day()
        self.loop.call_at(next_day.timestamp(), self._update_logger_filename)

    def _update_logger_filename(self):
        now = datetime.now()
        date = "{}-{}-{}".format(now.year, now.month, now.day)
        log_filename = os.path.join(config.LOGS_DIR, date + ".log")
        self.logger.handler = logging.FileHandler(log_filename)
        self._schedule_next_logger_filename_update()

