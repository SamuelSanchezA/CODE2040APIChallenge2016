import requests, ast

recievingURL = "http://challenge.code2040.org/api/dating"
validateURL = "http://challenge.code2040.org/api/dating/validate"
token = '71e6c159c2ae38103a613a57b1fb7a06'

query = {'token' : token}

recieving_payload = requests.post(recievingURL, data=query).text

recieving_payload = ast.literal_eval(recieving_payload) #Converts unicode string to a dictionary

print recieving_payload

def extractString(myDict):
    lst = []
    secondsToAdd = myDict['interval']
    timeString = myDict['datestamp'][myDict['datestamp'].find('T',0) + 1:myDict['datestamp'].find('Z',0)]
    lst.append(timeString)
    lst.append(secondsToAdd)

    return lst

def convertInterval(myList):
    interval = myList[1]
    seconds = interval % 60
    interval /=  60
    minutes = interval % 60
    interval /= 60
    hours = interval % 24

    result = []
    result.append(hours)
    result.append(minutes)
    result.append(seconds)
    print "Converted Interval: " , result
    return result

def addToOriginalTime(myList, timestamp):
    days = 0
    result = {}
    temp = [x for x in timestamp[0] if x != ':'] #Parsing out colon

    hour = ''.join(temp[0:2])
    minutes = ''.join(temp[2:4])
    seconds = ''.join(temp[4:6])

    #Converting strings into hours for proper calculating
    extractedHour = int(hour)
    extractedMinute = int(minutes)
    extractedSeconds = int(seconds)

    totalSeconds = extractedSeconds + myList[2]
    totalMinutes = extractedMinute + myList[1]
    totalHours = extractedHour + myList[0]

    if(totalSeconds > 59):
        totalMinutes += totalSeconds / 60
        totalSeconds %= 60

    if(totalMinutes > 59):
        totalHours += totalMinutes / 60
        totalMinutes %= 60

    if(totalHours > 23):
        print "Total hour check: ",totalHours
        days += totalHours / 24
        totalHours %= 24

    print days, totalHours, totalMinutes, totalSeconds
    result['dayToAdd'] = days
    result['hoursToAdd'] = totalHours
    result['minutesToAdd'] = totalMinutes
    result['secondsToAdd'] = totalSeconds

    return result

def insertToString(myDict, datestamp):
    print myDict
    newDatestamp = ""
    if(myDict['dayToAdd'] > 0):
        leftBound = datestamp['datestamp'].find('T',0) - 2
        rightBound = datestamp['datestamp'].find('T',0)
        originalDay = int(datestamp['datestamp'][leftBound:rightBound])
        modifiedDay = originalDay + myDict['dayToAdd']

        if(modifiedDay < 10):
            dayString = '0' + str(modifiedDay)
        else:
            dayString = str(modifiedDay)

    else:
        dayString = datestamp['datestamp'][8:10]

    if(myDict['hoursToAdd'] < 10):
        hourString = '0' + str(myDict['hoursToAdd'])
    else:
        hourString = str(myDict['hoursToAdd'])

    if(myDict['minutesToAdd'] < 10):
        minuteString = '0' + str(myDict['minutesToAdd'])
    else:
        minuteString = str(myDict['minutesToAdd'])

    if(myDict['secondsToAdd'] < 10):
        secondsString = '0' + str(myDict['secondsToAdd'])
    else:
        secondsString = str(myDict['secondsToAdd'])

    newTimeStamp = 'T' + hourString + ':' + minuteString + ':' + secondsString + 'Z'

    yearAndMonth = datestamp['datestamp'][0:8]

    newDatestamp = yearAndMonth + dayString + newTimeStamp
    return newDatestamp

data = extractString(recieving_payload)
timeToAdd = convertInterval(data)
modifiedTime = addToOriginalTime(timeToAdd, data)
modifiedDateStamp = insertToString(modifiedTime, recieving_payload)
print modifiedDateStamp
sending_payload = {
    'token' : token,
    'datestamp' : modifiedDateStamp
}

r = requests.post(validateURL, data=sending_payload)

print r.text
