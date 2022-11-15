#--Imports (from standard library)
import http.server
import socketserver
import ssl
import socket

#--Specifying port and creating handler
PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

#--Serving
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

#--Section to wrap the socket for self signed certificate
'''
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLS)
    print("serving at port", PORT)
    httpd.serve_forever()
'''









