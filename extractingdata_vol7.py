import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:

    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    content = urllib.urlopen(url)
    data = content.read()
    print 'Retrieved',len(data),'characters'
    js = json.loads(data)

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)
    
    print 'Place id', js["results"][0]["place_id"]