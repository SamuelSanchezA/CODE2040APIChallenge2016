import json, requests

#***********************************************************************************
url = "http://challenge.code2040.org/api/register"
payload = {'token' : '71e6c159c2ae38103a613a57b1fb7a06',
           'github' : 'https://github.com/SamuelSanchezA/CODE2040APIChallenge2016'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=payload)

#***********************************************************************************

print r.text
