import json, requests, ast

dataURL = "http://challenge.code2040.org/api/prefix"
validateURL = "http://challenge.code2040.org/api/prefix/validate"

query = {'token' : '71e6c159c2ae38103a613a57b1fb7a06'}

recieving_payload = requests.post(dataURL, data=query)

convertedData = recieving_payload.content

convertedData = ast.literal_eval(convertedData)

print "Prefix: " , convertedData['prefix'] , "\n"
print "Before: " , convertedData['array'] , "\n"

convertedData['array'] = [v for v in convertedData['array'] if(v[0:4] != convertedData['prefix'])]

print "After: " , convertedData['array'] , "\n"

sending_payload = {'token' : '71e6c159c2ae38103a613a57b1fb7a06',
                   'array' : convertedData['array']}

print requests.post(validateURL, data=sending_payload).text
