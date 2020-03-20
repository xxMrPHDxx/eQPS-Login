from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver

handler = HTTPServer(('127.0.0.1', 8888), SimpleHTTPRequestHandler)
handler.serve_forever()