""" Setup test fixtures
"""

import cookielib
import urllib
import urllib2
import os
from gabbi import fixture
import ConfigParser

setings = 'settings.ini'
name = __file__.split('.')[0]

config = ConfigParser.ConfigParser()
config.read('%s' % settings)

default = config.get('Server', 'default')

host_info = dict(config.items(default))
login_url = "http://%s/%s/login" % (host_info['host'], host_info['prefix'])

auth_info = dict(config.items('Auth'))
param = {'username': auth_info['username'], 'password':  auth_info['password']}

print "Setting Up Fixture"
print login_url

class NoRedirectHandler(urllib2.HTTPRedirectHandler):
    """ Disable redirect 
    """
    def http_error_302(self, req, fp, code, msg, headers):
        print "Redirect"
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
    http_error_301 = http_error_303 = http_error_307 = http_error_302

class AuthenticationFixture(fixture.GabbiFixture):
    """ Authenticte fixture
    """

    def start_fixture(self):
        """Create some sample data
        """
        p = urllib.urlencode(param)
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(NoRedirectHandler, urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen(login_url, p)
        cookies = {k.name: k.value for k in cj}
        os.environ['cookie'] = "ci_session=%s" % cookies['ci_session']
        cookie = "ci_session=%s" % cookies['ci_session']
        
    def stop_fixture(self):
    	pass