# coding: utf-8

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

serveraddr = ('', 8888)

# 监听端口，添加处理器
httpd = HTTPServer(serveraddr, SimpleHTTPRequestHandler)
httpd.serve_forever()