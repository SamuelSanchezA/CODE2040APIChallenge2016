import json, requests, ast

dataURL = "http://challenge.code2040.org/api/haystack"
validateURL = "http://challenge.code2040.org/api/haystack/validate"
query = {'token' : '71e6c159c2ae38103a613a57b1fb7a06'}

data = requests.post(dataURL, data=query)
index = 0

f = data.content

f = ast.literal_eval(f) # converts string to dictionary

for val in f['haystack']:
    if (f['needle'] == val):
        break;
    else:
        index += 1

payload = {'token' : '71e6c159c2ae38103a613a57b1fb7a06',
           'needle' : index}

print requests.post(validateURL, data=payload).text
