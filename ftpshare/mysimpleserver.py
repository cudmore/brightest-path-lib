#!/usr/bin/env python3

"""
Run a local http server

Fixes the dreaded CORS error "Access-Control-Allow-Origin"

See:
    https://stackoverflow.com/questions/21956683/enable-access-control-on-simple-http-server
    
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        
        # disable cache
        # print('QQQ DISABLE CACHE')
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

        self.send_header('Access-Control-Allow-Origin', '*')


        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8001)