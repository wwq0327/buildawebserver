#!/usr/bin/env python
# coding: utf-8

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        self._writeheaders()
        self.wfile.write("""<html><body><h3>This is a sample HTML page. Every page this server provides will look like this.</h3></body></html>""")

serveraddr = ('', 8888)
httpd = HTTPServer(serveraddr, RequestHandler)
httpd.serve_forever()