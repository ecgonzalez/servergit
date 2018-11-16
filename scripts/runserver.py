from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
	cgi_directories = ["/scripts/"]

httpd = HTTPServer(("", 40), Handler)
httpd.serve_forever()
