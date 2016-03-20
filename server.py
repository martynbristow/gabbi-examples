""" Simple HTTP Server
"""
import BaseHTTPServer
import cgi
import random
import sys
import json
import ConfigParser
import Cookie

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
 
def load_settings():
    """ Load Settings from settings.ini
    """
    config = ConfigParser.ConfigParser()
    config.read('settings.ini') # Load the settings.ini file
    settings = {}
    server = dict(config.items('Server'))
    auth = dict(config.items('Auth'))
    settings['port'] = int(server['port'])
    port = ":%s" % server['port'] if server['port'] else ""
    settings['login_url'] = "http://%s%s/%s/login" % (server['host'], port, server['prefix'])
    settings['param'] = {'username': auth['admin_username'], 'password':  auth['admin_password']}
    return settings

URLS = {"page": 'Page', "login":'Login', "api":'API'}
LIST_ITEM = "<li>%s</li>"
LINK = "<a href='{url}'>{text}</a>"
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    """ Server
    """
    def do_GET(self):
        """ GET
        """
        uri = self.path.split('/')
        print uri
        if len(uri) == 1:
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
            page = ""
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
            print "login"
            print "show form"
            self.output = HTML % LOGIN_FORM

        else:
            self.send_error(404, HTML % ("File not found: %s" % self.path))
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
        """ Collate HTTP POST
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
        """ curl -v --data "username=admin&password=password" http://localhost:8000/login
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

if __name__ == '__main__':
    settings = load_settings()
    httpd = BaseHTTPServer.HTTPServer(("", settings['port']), Handler)
    print "Serving content on port", settings['port']
    httpd.serve_forever()
    run()