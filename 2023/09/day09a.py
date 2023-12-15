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
    print('Differences for', p_numList, 'is', differencesSequence)
    return differencesSequence

def predictNextValue(p_valueHistory : list):
    differences = list()
    differences.append(getDifferencesSequence(p_valueHistory))
    return -1


# MAIN PROGRAM
# ------------
# Extract file contents
# ---------------------
filePath = "demo.txt"
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
for history in valueHistories:
    valuePredictions.append(predictNextValue(history))
print('Value predictions:', valuePredictions)