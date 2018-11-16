from http.server import HTTPServer, CGIHTTPRequestHandler
import socket
import sys
 
try:
 
	port = int(sys.argv[1])
 
	if port:
 
		ip_interna = socket.gethostbyname(socket.gethostname())
		print ("Panel de control: http://%s:%s/cgi-bin/index.py" % (ip_interna, port))
		server_address=('', port)
		httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
		httpd.serve_forever()
 
except:
 
	print ("-"*40)
	print ("Uso:")
	print (sys.argv[0], "PUERTO")
	print ("-"*40)
	print ("Ejemplo de uso:")
	print (sys.argv[0], "5050")
	print ("-"*40)