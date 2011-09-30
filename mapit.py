import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]).strip()
else:
    # get from clipboard
    import pyperclip
    address = pyperclip.getcb().strip()

googlemapsurl = 'http://maps.google.com/maps?q='
if sys.version.startswith('2.'): # for Python 2 version
    import urllib
    googlemapsurl += urllib.quote(address)
else:
    import urllib.parse
    googlemapsurl += urllib.parse.quote(address)

webbrowser.open(googlemapsurl)