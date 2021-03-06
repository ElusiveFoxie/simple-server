#!/usr/bin/python3

import sys
import http.server
import socketserver
import ssl

# generate server.pem with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes


help = '''
simple-server 1.0 by ElusiveFox

usage: simple-server.py [-m] [-p]

-m, --mode 	http or https (default: http)
-p, --port  	port number (default: 8080)

example: simple-server.py https 8443

'''

PORT = 8080
MODE = 'http'


if __name__ == '__main__':
	try:
		if (len(sys.argv) == 3):
			PORT = int(sys.argv[2])
			MODE = sys.argv[1]
		if (len(sys.argv) == 2):
			PORT = int(sys.argv[1])

		Handler = http.server.SimpleHTTPRequestHandler

		with socketserver.TCPServer(("", PORT), Handler) as httpd:
			if(MODE=="https"):
				httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
			print("serving "+MODE+" at port", PORT)
			httpd.serve_forever()
	except IndexError:
	    print(help)
