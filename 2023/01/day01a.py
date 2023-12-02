# Open input file and extract contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
# Initialize calibration value for file
totalCalibrationValue = 0
# Iterate through each line in the file
for line in lines:
    # Initializations
    firstDigit = ""
    secondDigit = ""
    lineCalibrationValue = ""
    lastIndex = len(line) - 1
    # Search through current line from beginning
    for character in line:
        if character.isdigit():
            firstDigit += character
            break
    # Search through current line from end
    for index in range(lastIndex, -1, -1):
        character = line[index]
        if character.isdigit():
            secondDigit += character
            break
    lineCalibrationValue = str(firstDigit) + str(secondDigit)
    print(lineCalibrationValue)
    totalCalibrationValue += int(lineCalibrationValue)
print("Total Calibration Value: " + str(totalCalibrationValue))
inputFile.close()