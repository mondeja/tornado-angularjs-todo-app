#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.printers import verboser, success
verboser("Starting server...")

from tornado.httpserver import HTTPServer
import tornado.options

from app import App


if __name__ == "__main__":
    app = App()

    http_server = HTTPServer(app)
    http_server.listen(app.port, address=app.host)

    success("Server listening at %s:%d" % (app.host, app.port))

    try:
        app.start()
    except KeyboardInterrupt:
        verboser("\nStopping server...")
        app.loop.stop()
