# AWS Shadow Update using REST API
# Technix Cloud SDK

from aws_sign_post import sign_request
import requests,time

#------------ Configuration Data--------------
method = 'POST'
service = 'iotdata'  # Service Name. Donot Change for updating the Shadow
thingname = ''  # Thing Name
host = ''  # Hostname, identifier.iot.region.amazonaws.com
access_key = ''    # IAM Access key. Should have permission policy to update shadow
secret_key = ''
content_type = 'application/json'

region = host.split('.')[2]
canonical_uri = '/things/'+thingname+'/shadow'
endpoint = 'https://'+ host + canonical_uri
canonical_querystring = ''

property = 0
value = 0

while (True):
    property += 1
    value += 1

    # use the json format specified by aws to update the shadow data
    body = '{ "state": { "desired": { "property": '+ str(property) +', "Value": '+ str(value) + '},' \
                                    '"reported": {"property": '+ str(property) +',"Value":'+ str(value) +'}}}'
    headers = sign_request(method,service,host,region,content_type,access_key,secret_key,canonical_uri,canonical_querystring,body)
    r = requests.post(endpoint, data=body, headers=headers)
    print '\nRESPONSE++++++++++++++++++++++++++++++++++++'
    print 'Response code: %d\n' % r.status_code
	print r.data
    time.sleep(15)
