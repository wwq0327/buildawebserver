#!/usr/bin/env python
# coding: utf-8

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import time, threading

starttime = time.time()

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self, doc):
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header('Content-Type', 'text/html')

    def _getdoc(self, filename):
        global starttime
        if filename == '/':
            return """<html><head><title>Sample Page</title></head>
            <body>This is a Sample page.<a href="stats.html">server statistics</a>.
            </body></html>"""
        elif filename == '/stats.html':
            return """<html><head><title>Statistics</title></head>
            <body>This server has been running for %d seconds.
            </body></html>""" % int(time.time() - starttime)
        else:
            return None


    def do_HEAD(self):
        doc = self._getdoc(self.path)
        self._writeheaders(doc)

    def do_GET(self):
        print "Hadling with thread", threading.currentThread().getName()
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
        if doc is None:
            self.wfile.write("""The requested document '%s' was not found.""" \
                % self.path)
        else:
            self.wfile.write(doc)


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


serveraddr = ('', 8888)
httpd = ThreadingHTTPServer(serveraddr, RequestHandler)
httpd.serve_forever()