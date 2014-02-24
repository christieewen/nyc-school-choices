__author__ = 'Christie'
# http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
import urllib3
import json
import sys

# Nick's techniques
#'{0} {1}'.format('fist', 'second')
#myjsondata = {'name': 'nick', 'school': 'Brooklyn High'}
#'{name} went to {school}'.format(**myjsondata)

def getSchoolsByProgramHighlights(queryContains):
    url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%20%22Program%20Highlights%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22%20where%20%22Program%20Highlights%22%20like%20%27{0}%%27'.format(queryContains)
    #print(url)

    http = urllib3.PoolManager()
    
    r = http.request('GET', url)

    #print(r.data)

    #Python 3 requires explicit Bytes to String conversions
    # See http://www.rmi.net/~lutz/strings30.html
    return json.loads(r.data.decode())



# Example to call this program: python33 programSearch.py "Sports"
def main(args):
    j = getSchoolsByProgramHighlights(args[1])
    
    for k in j['result']['records']:
        print(k['Printed_Name'] + " | " + k['Program Highlights'] + "\n")


if __name__ == '__main__':
    main(sys.argv)

# see http://stackoverflow.com/questions/17523219/how-to-pass-sys-argvn-into-a-function-in-python
#main(sys.argv[1])
