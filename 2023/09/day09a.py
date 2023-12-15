# GLOBAL VARIABLES
# ----------------
valueHistories = list()
valuePredictions = list()


# FUNCTIONS
# ---------
def isAllZeroes(p_numList : list):
    if len(p_numList) > 0:
        return all(num == 0 for num in p_numList)
    else:
        return False

def getDifferencesSequence(p_numList : list):
    differencesSequence = [None] * (len(p_numList) - 1)
    for index in range (0, len(differencesSequence)):
        difference = p_numList[index + 1] - p_numList[index]
        differencesSequence[index] = difference
    #print('Differences for', p_numList, 'is', differencesSequence)
    return differencesSequence

def getAllDifferenceSequences(p_valueHistory : list):
    differenceSequences = [p_valueHistory]
    currentDifferences = getDifferencesSequence(p_valueHistory)
    differenceSequences.append(currentDifferences)
    while not isAllZeroes(currentDifferences):
        currentDifferences = getDifferencesSequence(currentDifferences)
        differenceSequences.append(currentDifferences)
    return differenceSequences

def predictNextValue(p_valueHistory : list):
    recursiveDifferences = getAllDifferenceSequences(p_valueHistory)
    # First add an additional zero to last sequence
    lineIndex = len(recursiveDifferences) - 1
    recursiveDifferences[lineIndex].append(0)
    lineIndex -= 1
    while lineIndex >= 0:
        currentLine = recursiveDifferences[lineIndex]
        belowLine = recursiveDifferences[lineIndex + 1]
        belowLineLastValue = belowLine[len(belowLine) - 1]
        currentLineLastValue = currentLine[len(currentLine) - 1]
        currentLineNextValue = currentLineLastValue + belowLineLastValue
        recursiveDifferences[lineIndex].append(currentLineNextValue)
        lineIndex -=1
    return currentLineNextValue


# MAIN PROGRAM
# ------------
# Extract file contents
# ---------------------
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
del inputFile
# Extract number histories
# ------------------------
for line in lines:
    line = line.strip()
    line = line.split(' ')
    valueHistory = [int(num) for num in line]
    valueHistories.append(valueHistory)
del valueHistory
del line
del lines
# Predict next values
# -------------------
sumOfExtrapolatedValues = 0
for history in valueHistories:
    extrapolatedValue = predictNextValue(history)
    valuePredictions.append(extrapolatedValue)
    sumOfExtrapolatedValues += extrapolatedValue
print('Value predictions:', valuePredictions)
print('SUM OF EXTRAPOLATED VALUES:', sumOfExtrapolatedValues)