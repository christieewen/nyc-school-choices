__author__ = 'Christie'
# http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
import urllib3
#import urllib2
from bs4 import BeautifulSoup
import json
import sys
#import requests

#url = 'http://nycdoe.pediacities.com/api/action/datastore_search?limit=5&q=ELL%20Data:ELS'
#url = 'http://nycdoe.pediacities.com/api/action/datastore_search?resource_id=45f6a257-c13a-431b-acb9-b1468c3ff1e9&limit=5'
#url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22BUS%22,%22SUBWAY%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'
#url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'

# Nick's techniques
#'{0} {1}'.format('fist', 'second')
#myjsondata = {'name': 'nick', 'school': 'Brooklyn High'}
#'{name} went to {school}'.format(**myjsondata)

def getSchoolsByProgramHighlights(queryContains):

    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22where%20%22Program%20Highlights%22%20like%20%22{0}%22'.format(queryContains)
    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22where%20%22Program%20Highlights%22%20like%20%22%25{0}%25%22'.format(queryContains)
    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22%20where%20%22Program%20Highlights%22%20like%20%22%25{0}%25%22'.format(queryContains)
    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22%20where%20%22Program%20Highlights%22%20in%20%22{0}%22'.format(queryContains)
    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?'
    #url += 'sql=SELECT "Printed_Name", "Program Highlights" from "45f6a257-c13a-431b-acb9-b1468c3ff1e9"'
    #url += ' where "Program Highlights" like '{0}''.format(queryContains)
    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%20%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22%20where%20%22Program%20Highlights%22%20like%20%27Core%%27'
    url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%20%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22%20where%20%22Program%20Highlights%22%20like%20%27{0}%%27'.format(queryContains)


#url = http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT "Printed_Name", "Program Highlights" from "45f6a257-c13a-431b-acb9-b1468c3ff1e9" where "Program Highlights" like "Core"'

    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?' \
    #      'sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'

    #querystring = "SELECT `Printed_Name`, `Program Highlights` from `45f6a257-c13a-431b-acb9-b1468c3ff1e9` where `Program_Highlights` like {0}".format(queryContains)
    #url = b'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql='+querystring.encode()
    print(url)


    #url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22where%20%22Program_Highlights%22%20like%20%22'+queryContains+ '%22'


    http = urllib3.PoolManager()

    r = http.request('GET', url)

    #print(r.data)

    #Python 3 requires explicit Bytes to String conversions
    # See http://www.rmi.net/~lutz/strings30.html
    j = json.loads(r.data.decode())


    for k in j['result']['records']:
        print(k['Printed_Name'] + " | " + k['Program Highlights'] + "\n")

    return j


#    print(k['Printed_Name'] + "\n")


#    print (j.keys())

#print (type(j))
#print (j['result'])
#soup = BeautifulSoup(r.data)
#print (soup)


#print (soup.contents)
#print r.status
#print r.headers['server']
#print r.data

# Example to call this program: python33 programSearch.py "Sports"
def main(args):
    j = getSchoolsByProgramHighlights(args[1])

if __name__ == '__main__':
    main(sys.argv)

# see http://stackoverflow.com/questions/17523219/how-to-pass-sys-argvn-into-a-function-in-python
#main(sys.argv[1])
