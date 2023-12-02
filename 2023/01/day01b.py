# Initialize dictionaries mapping digits to first and last letters
spelledDigits = dict(zero='0', one='1', two='2', three='3',
                     four='4', five='5', six='6', seven='7',
                     eight='8', nine='9')
firstDigitLetters = dict()
lastDigitLetters = dict()
for digit in spelledDigits:
    firstLetter = digit[0]
    lastLetter = digit[len(digit) - 1]
    # check if first letter already exists
    if firstLetter not in firstDigitLetters:
        firstDigitLetters[firstLetter] = [digit]
    else:
        firstDigitLetters[firstLetter].append(digit)
    # check if last letter already exists
    if lastLetter not in lastDigitLetters:
        lastDigitLetters[lastLetter] = [digit]
    else:
        lastDigitLetters[lastLetter].append(digit)
# Open input file and extract contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
# Initialize calibration value for file
totalCalibrationValue = 0
# Iterate through each line in the file
for line in lines:
    # Initializations
    firstDigit = ''
    secondDigit = ''
    lineCalibrationValue = ''
    lastIndex = len(line) - 1
    # Search through current line from beginning
    for index in range(0, len(line), 1):
        foundDigit = False
        character = line[index]
        # found a digit
        if character.isdigit():
            firstDigit += character
            foundDigit = True
        elif character in firstDigitLetters:
            for digit in firstDigitLetters[character]:
                # check if following letters spell out the digit
                lineSlice = line[slice(index, index + len(digit))]
                # found a spelled-out digit
                if lineSlice == digit:
                    firstDigit += spelledDigits[digit]
                    foundDigit = True
        if foundDigit:
            break
    # Search through current line from end
    for index in range(lastIndex, -1, -1):
        foundDigit = False
        character = line[index]
        # found a digit
        if character.isdigit():
            secondDigit += character
            foundDigit = True
        elif character in lastDigitLetters:
            for digit in lastDigitLetters[character]:
                # check if preceding letters spell out the digit
                lineSlice = line[slice(index - len(digit) + 1, index + 1)]
                # found a spelled-out digit
                if lineSlice == digit:
                    secondDigit += spelledDigits[digit]
                    foundDigit = True
        if foundDigit:
            break
    lineCalibrationValue = str(firstDigit) + str(secondDigit)
    print(lineCalibrationValue)
    totalCalibrationValue += int(lineCalibrationValue)
print("Total Calibration Value: " + str(totalCalibrationValue))
inputFile.close()