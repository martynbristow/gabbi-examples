""" A Simple HTTP Server in Python

This is a simple HTTP server designed to be used with gabbi-examples
It should only use the Python standard library to avoid needing to install dependancies
Its not designed to server real websites, only a demonstration for testing
"""

import BaseHTTPServer
import cgi
import random
import sys
import json
import ConfigParser
import Cookie
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG)

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
%s
</body>
</html>
"""
STATIC_TEXT = "<p>Today's quote: <i>%s</i></p>"
LOGIN_FORM = """
<form method="post" action="/login">
<div><label>Username</label><input name="username" type="text"/></div>
<div><label>Password</label><input name="password" type="password" /></div>
<div><input name="Submit" type="submit" /></div>
</form>
"""
URLS = {"page": 'Page', "login":'Login', "api":'API'}
LIST_ITEM = "<li>%s</li>"
LINK = "<a href='{url}'>{text}</a>"

def load_settings(filename="settings.ini"):
    """ Load the server settings from the file `filename`
    """

    config = ConfigParser.ConfigParser()
    config.read(filename) # Load the settings.ini file
    settings = {
        'server': dict(config.items('Server')),
        'auth': dict(config.items('Auth')),
    }
    settings['server']['port'] = int(settings['server']['port'])
    port = ":%s" % settings['server']['port'] if settings['server']['port'] else ""
    prefix = "/%s" % settings['server']['prefix'] if settings['server']['prefix'] else ""
    settings['login_url'] = "http://%s%s/%s/login" % (settings['server']['host'], port, prefix)
    settings['param'] = {'username': settings['auth']['admin_username'], 'password':  settings['auth']['admin_password']}
    return settings


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """ HTTP Request Handler
   Add session http://michelanders.blogspot.co.uk/2011/10/managing-session-id-with-cookies.html
    """

    '''
    def __init__(self, *args, **kwargs):
        self.sessionidmorsel = None 
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, *args,**kwargs)
    '''

    def do_GET(self):
        """ Process a HTTP Get Request
        """
        uri = self.path.split('/')
        logging.debug('Requested URI: %s', uri)
        if self.path == "" or self.path == "/" or len(uri) == 1:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            tmp = "".join([LIST_ITEM % LINK.format(url=url, text=URLS[url]) for url in URLS])
            content = "<nav><ul>%s</ul></nav>" % tmp
            self.output = HTML % "<h1>Welcome</h1>\n%s" % content

        elif uri[1] == "page":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            page = "PAGE"
            self.output = page

        elif uri[1] == "api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = ""
            self.output = json.dumps(data)

        elif uri[1] == "image":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.send_header("Content-Disposition", "attachment; filename=genome.jpeg;")
            self.end_headers()
            data = 0
            self.output = data
  
        elif uri[1] == "pdf":
            self.send_response(200)
            self.send_header("Content-type", "application/pdf")
            self.send_header("Content-Disposition", "Content-Disposition: attachment; filename=genome.jpeg;")
            self.end_headers()
            data = 0
            self.output = data

        elif uri[1] == "login":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.output = HTML % LOGIN_FORM

        elif uri[1] == "~":
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.output = "Goodbye"
            global shutdown
            shutdown = True

        else:
            #self.send_error(404, HTML % ("File not found: %s" % self.path))
            self.send_error(404, "%s" % ("File not found: %s" % self.path))
            #self.end_headers()
            return
        
        try:
            # redirect stdout to client
            stdout = sys.stdout
            sys.stdout = self.wfile
            #output = HTML % cgi.escape(self.output)
            output = HTML % self.output
            print output
        finally:
            sys.stdout = stdout # restore

    def parse_POST(self):
        """ Parse a HTTP POST request
        """

        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = cgi.parse_qs(
                    self.rfile.read(length), 
                    keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_POST(self):
        """ Recieve a post request
        curl -v --data "username=admin&password=password" http://localhost:8000/login
        """
        postvars = self.parse_POST()
        if self.path == "/login":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            #self.end_headers()
            c = Cookie.SimpleCookie()
            c['value'] = "random"
            self.send_header('Set-Cookie', c.output(header=''))
            self.end_headers()
            self.output = ""
            try:
                # redirect stdout to client
                stdout = sys.stdout
                sys.stdout = self.wfile
                #output = HTML % cgi.escape(self.output)
                output = HTML % self.output
                print output
            finally:
                sys.stdout = stdout # restore
    def send_error(self, *args):
        mimetype="text/html"
        self.send_response(404)
        self.send_header('Content-type',mimetype)
        self.end_headers()
        self.wfile.write("Sorry")

if __name__ == '__main__':
    server_settings = load_settings()
    httpd = BaseHTTPServer.HTTPServer(("127.0.0.1", server_settings['server']['port']), MyHandler)
    logging.info("Serving content on port %s", server_settings['server']['port'])
    shutdown=False
    run_server = lambda: shutdown==False
    while run_server():
        try:
            httpd.handle_request()
        except KeyboardInterrupt:
            print "\nGoodbye\n"
            shutdown=True
        #httpd.serve_forever()
    #run()