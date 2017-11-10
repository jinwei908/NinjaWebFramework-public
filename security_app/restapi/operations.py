SALT1 = 'LM:TB:BB:WRU:+fwePO%&^*4$('
SALT2 = '_:/_77$1857(S%*(&0SeEW'

import base64
import json
from datetime import datetime

def Decrypt_B64(encryptedText):
    cacheString = encryptedText[0:7] + encryptedText[8:]
    encryptedText2 = Base64_Decode(cacheString)
    cacheString = encryptedText2[0:len(encryptedText2) - (len(SALT2) + len(SALT1))]
    encryptedText3 = Base64_Decode(cacheString)
    cacheString = encryptedText3[0:7] + encryptedText3[(7+len(SALT2)):]
    cacheString = Base64_Decode(cacheString)
    cacheString = cacheString.replace("[ENTER]", "\r\n")
    cacheString = cacheString.replace("[Enter]", "\r\n")
    cacheString = cacheString.replace("[ENT]", "\r\n")
    #cacheString = cacheString.replace("utf-8", "\r\n")
    return cacheString; 

def Base64_Decode(s):
    data = base64.b64decode(s)
    decodedString = data.decode('utf-8', 'ignore')
    return decodedString

def Convert_To_Packets_Data(username, com_name, logged_user, decodedString):
    allInstances = []
    
    rawInstances = decodedString.split('(--------)')
    returnObject = {}
    tagDictionary = {}
    
    for i in range(1, len(rawInstances)):
        #Converting Raw Instances to Analysis Instances
        currentIndex = 0
        workingString = rawInstances[i]
        pFrom = workingString.index("---*[") + 5
        pTo = workingString.index("]*---")
        allTags = workingString[pFrom:pTo]
        tagsArray = allTags.split(', ')
        currentIndex = pFrom + len(allTags) + 5 + 2
        
        pFrom = workingString.index("TIME=", currentIndex) + 5
        pTo = workingString.index("\r\n", currentIndex)
        time = workingString[pFrom:pTo]
        dTime = datetime.strptime(time, "%d.%m.%Y %H:%M:%S")

        currentIndex += len(time) + 5 + 2

        pFrom = workingString.index("[LMB]Current Window:", currentIndex) + 21
        pTo = workingString.index("\r\n", currentIndex)
        currentWindow = workingString[pFrom:pTo]
        currentIndex += len(currentWindow) + 5 + 2 + 16

        pFrom = currentIndex
        pTo = workingString.index("Click Count Detected", currentIndex)
        currentContent = workingString[pFrom:pTo - pFrom]
        currentIndex += len(currentContent)-2
        pFrom = workingString.index("Click Count Detected: ", currentIndex) + 22
        try:
            pTo = workingString.index("\r\n", pFrom)
            clickCount = ""
            if (pTo != -1):
                clickCount = workingString[pFrom:pTo]
            else:
                clickCount = workingString[pFrom:]
        except:
            clickCount = workingString[pFrom:]

        clickCountInt = int(clickCount) + 1
        
        for b in range(len(tagsArray)):
            if(tagsArray[b] in tagDictionary):
                tagDictionary[tagsArray[b]] = tagDictionary[tagsArray[b]] + 1
            else:
                tagDictionary[tagsArray[b]] = 1
        
        
        allInstances.append({
            "username": username,
            "computer_name": com_name,
            "logged_user": logged_user,
            "all_tags": tagsArray,
            "current_window":currentWindow,
            "string_content": currentContent,
            "click_count": clickCountInt,
            "log_time": dTime
        })
    returnObject["packets_data"] = allInstances
    returnObject["tags_data"] = json.dumps(tagDictionary)
    return returnObject;