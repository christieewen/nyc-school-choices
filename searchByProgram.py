__author__ = 'Christie'
# http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
import urllib3
#import urllib2
from bs4 import BeautifulSoup
import json

#url = 'http://nycdoe.pediacities.com/api/action/datastore_search?limit=5&q=ELL%20Data:ELS'
#url = 'http://nycdoe.pediacities.com/api/action/datastore_search?resource_id=45f6a257-c13a-431b-acb9-b1468c3ff1e9&limit=5'
#url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22BUS%22,%22SUBWAY%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'
url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'


http = urllib3.PoolManager()

r = http.request('GET', url)

#Python 3 requires explicit Bytes to String conversions
# See http://www.rmi.net/~lutz/strings30.html
j = json.loads(r.data.decode())

print (j.keys())
#print (type(j))
print (j['result'])
#soup = BeautifulSoup(r.data)
#print (soup)


#print (soup.contents)
#print r.status
#print r.headers['server']
#print r.data
