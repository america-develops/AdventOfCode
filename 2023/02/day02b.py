# GLOBAL VARIABLES
# ----------------
gameMapping = dict()

# CLASSES
# -------
class Game:
    def __init__(self, p_id):
        self.id = int(p_id)
        self.subsetList = list()
        self.isPossible = True
        self.minRed = 0
        self.minGreen = 0
        self.minBlue = 0

    def getMinimumPower(self):
        return self.minRed * self.minGreen * self.minBlue

    class GameSubset:
        def __init__(self, p_numRed, p_numGreen, p_numBlue):
            self.numRed = p_numRed
            self.numGreen = p_numGreen
            self.numBlue = p_numBlue

    def addSubset(self, p_numRed, p_numGreen, p_numBlue):
        self.subsetList.append(self.GameSubset(p_numRed, p_numGreen, p_numBlue))
        # Update minimum color counts if necessary
        self.minRed = p_numRed if p_numRed > self.minRed else self.minRed
        self.minGreen = p_numGreen if p_numGreen > self.minGreen else self.minGreen
        self.minBlue = p_numBlue if p_numBlue > self.minBlue else self.minBlue

# MAIN PROGRAM
# ------------
# Extract file contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()

# Initialize calibration value for file
totalCalibrationValue = 0

for line in lines:
    print(line.strip())
    # Extract game ID
    colonIndex = line.find(':')
    gameIdSlice = line[slice(colonIndex)]
    gameId = int(gameIdSlice[slice(5, colonIndex)])
    # Add game to dictionary
    gameMapping[gameId] = Game(gameId)
    # Extract subsets
    subsetsString = line[slice(colonIndex + 1, len(line))].strip()
    subsetsStringList = subsetsString.split("; ")
    print(subsetsStringList)
    for subset in subsetsStringList:
        # Initialize color counts
        numRed = 0
        numGreen = 0
        numBlue = 0
        # Extract subset's values
        subsetValues = subset.split(', ')
        print(subsetValues)
        for value in subsetValues:
            if value.find('red') > -1:
                numRed = int(value[slice(0, value.find('red'))].strip())
                print(numRed)
            elif value.find('green') > -1:
                numGreen = int(value[slice(0, value.find('green'))].strip())
                print(numGreen)
            elif value.find('blue') > -1:
                numBlue = int(value[slice(0, value.find('blue'))].strip())
                print(numBlue)
        # Add subset to current game
        gameMapping[gameId].addSubset(numRed, numGreen, numBlue)

    print()

inputFile.close()

# Calculate total calibration value
for id in gameMapping:
    totalCalibrationValue += gameMapping[id].getMinimumPower()
print("Total calibration value: " + str(totalCalibrationValue))