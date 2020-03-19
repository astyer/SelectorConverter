turnToText = False
turnTextToAccessIds = True
capitalizeText = False

fixNumbering = False
count = 1

listFile = open("objectsJSON.txt", "r")
lines = listFile.readlines()
totalLines = -1
firstDataLine = -1
lastDataLine = -1
finalString = ""
for line in lines:
    totalLines += 1
    if '_id' in line or '{' in line or '}' in line:
        continue
    if firstDataLine == -1:
        firstDataLine = totalLines
    else:
        lastDataLine = totalLines
    if fixNumbering:
        split = line.split('\"')
        finalLine = split[0] + '\"' + str(count) + '\"' + split[2] + '\"' + split[3] + '\"' + split[4]
        count += 1
    else:
        if line[-2] != ',':
            obj = line.split(':')[1][1:-1]
            if turnToText:
                if capitalizeText:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1].upper() + '\']\"'
                else:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\"'
            elif turnTextToAccessIds:
                text = obj.split('=')[1].strip()[1:-3]
                realObj = line.split(':')[0]
                finalLine = realObj + ': \"~' + text + '\"\n'
            else:
                finalLine = obj + ' : \"\"'
        else:
            obj = line.split(':')[1][1:-2]
            if turnToText:
                if capitalizeText:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1].upper() + '\']\",\n'
                else:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\",\n'
            elif turnTextToAccessIds:
                text = obj.split('=')[1].strip()[1:-3]
                realObj = line.split(':')[0]
                finalLine = realObj + ': \"~' + text + '\",\n'
            else:
                finalLine = obj + ' : \"\",\n'

    finalString += finalLine

lineCount = 0
appendBefore = ""
for line in lines:
    if lineCount < firstDataLine:
        appendBefore += line
    elif lastDataLine < lineCount < len(lines):
        finalString += line
    lineCount += 1
finalString = appendBefore + finalString

print(finalString)
outputFile = open("output.txt", "w")
outputFile.write(finalString)

listFile.close()
outputFile.close()
