"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Rest Interface
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
import bootsrap.common

class RestServer(BaseHTTPRequestHandler):
    def _get_endpoints(self, method, path):
        components = bootsrap.common.loadComponents('rest')
        for component in components:
            endpoints = components[component].define()
            for endpoint in endpoints:
                if endpoint['method'] == method and endpoint['path'] == path:
                    return endpoint['callback']

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        callback = self._get_endpoints('get', self.path)

        try:
            response = callback()
        except:
            response = {'message': 'not found', 'path': self.path}

        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers['content-length'])
        body = json.loads(self.rfile.read(length))

        # send the message back
        self._set_headers()
        callback = self._get_endpoints('post', self.path)

        try:
            response = callback(body)
        except:
            response = {'message': 'not found', 'path': self.path}

        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))


class rest_interface():

  def __init__(self):
    print('REST Interface loaded')

  def run(self):
      hostName = "localhost"
      serverPort = 8080
      webServer = HTTPServer((hostName, serverPort), RestServer)
      print("Server started http://%s:%s" % (hostName, serverPort))

      try:
          webServer.serve_forever()
      except KeyboardInterrupt:
          pass

      webServer.server_close()
      print("Server stopped.")
