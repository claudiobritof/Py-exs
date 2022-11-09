import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.globoesporte.com')
except urllib.error.URLError:
    print('The website is not accessible at the moment.')
else:
    print('The website is OK and functioning.')
    print(site.read())