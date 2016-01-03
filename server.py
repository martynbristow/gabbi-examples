import BaseHTTPServer
import cgi, random, sys, json

MESSAGES = [
    "That's as maybe, it's still a frog.",
    "Albatross! Albatross! Albatross!",
    "It's Wolfgang Amadeus Mozart",
    "A pink form from Reading.",
    "Hello people, and welcome to 'It's a Tree'"
    "I simply stare at the brick and it goes to sleep.",
]
HTML = """<html>
<body>
<p>Today's quote: <i>%s</i></p>
</body>
</html>
"""
PORT = 8000

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
        	self.send_response(200)
        	self.send_header("Content-type", "text/html")
        	self.end_headers()
        	self.output = ""
        elif self.path == "/page":
        	self.send_response(200)
        	self.send_header("Content-type", "text/html")
        	self.end_headers()
        	self.output = ""
        if self.path == "/api":
        	self.send_response(200)
        	self.send_header("Content-type", "text/html")
        	self.end_headers()
        	self.output = json.dumps("")
        else:
            self.send_error(404, "File not found")
            return
        
        try:
            # redirect stdout to client
            stdout = sys.stdout
            sys.stdout = self.wfile
        	output = HTML % cgi.escape(self.output)
        	print output
        finally:
            sys.stdout = stdout # restore




httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
if __name__ == '__main__':
	run()