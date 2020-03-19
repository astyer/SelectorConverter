turnToText = False
turnTextToAccessIds = True
capitalizeText = False

fixNumbering = False
count = 1

listFile = open("objsJSON.txt", "r")
lines = listFile.readlines()
finalString = ""
for line in lines:
    if '_id' in line or '{' in line or '}' in line:
        continue
    if fixNumbering:
        split = line.split('\"')
        finalLine = split[0] + '\"' + str(count) + '\"' + split[2] + '\"' + split[3] + '\"' + split[4]
        count += 1
    if turnToText:
        if line[-2] != ',':
            obj = line.split(':')[1][1:-1]
            if turnToText:
                if capitalizeText:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1].upper() + '\']\"'
                else:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\"'
            else:
                finalLine = obj + ' : \"\"'
        else:
            obj = line.split(':')[1][1:-2]
            if turnToText:
                if capitalizeText:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1].upper() + '\']\",\n'
                else:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\",\n'
            else:
                finalLine = obj + ' : \"\",\n'
    elif turnTextToAccessIds:
        if line[-2] != ',':
            text = line.split('=')[1][2:-4]
            if turnToText:
                finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\"'
            else:
                finalLine = obj + ' : \"\"'
        else:
            obj = line.split(':')[1][1:-2]
            if turnToText:
                if capitalizeText:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1].upper() + '\']\",\n'
                else:
                    finalLine = obj + ' : \"//android.view.View[@text = \'' + obj[1:-1] + '\']\",\n'
            else:
                finalLine = obj + ' : \"\",\n'

    finalString += finalLine

print(finalString)
outputFile = open("output.txt", "w")
outputFile.write(finalString)

listFile.close()
outputFile.close()
