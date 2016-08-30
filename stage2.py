import json, requests

url1 = "http://challenge.code2040.org/api/reverse"
validatingURL = "http://challenge.code2040.org/api/reverse/validate"
payload = {
'token' : '71e6c159c2ae38103a613a57b1fb7a06'
}

data = requests.post(url1, data=payload)

originalString = data.text

print "Original: " , originalString
def reverseString(string):
    x = -1
    newString = []
    for y in string:
        newString.append(string[x])
        x = x - 1

    return newString


result = ''.join(reverseString(originalString))

print "Reverse: " , result

results = {
'token' : '71e6c159c2ae38103a613a57b1fb7a06',
'string' : result
}

print requests.post(validatingURL, data=results).text
