# GLOBAL VARIABLES
# ----------------
valueHistories = list()
valuePredictions = list()


# FUNCTIONS
# ---------
def PredictNextValue(p_valueHistory : list):
    differences = list()
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
    valuePredictions.append(PredictNextValue(history))
print('Value predictions:', valuePredictions)