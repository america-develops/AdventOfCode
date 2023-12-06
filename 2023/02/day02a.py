# CONSTANTS
# ---------
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

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

    class GameSubset:
        def __init__(self, p_numRed, p_numGreen, p_numBlue):
            self.numRed = p_numRed
            self.numGreen = p_numGreen
            self.numBlue = p_numBlue

    def addSubset(self, p_numRed, p_numGreen, p_numBlue):
        self.subsetList.append(self.GameSubset(p_numRed, p_numGreen, p_numBlue))
        # Set game to impossible if subset exceeds max values
        if p_numRed > MAX_RED or p_numGreen > MAX_GREEN or p_numBlue > MAX_BLUE:
            self.isPossible = False

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

for id in gameMapping:
    print(str(id) + ": " + str(gameMapping[id].isPossible))
    # Add ID to total calibration if game is possible
    if gameMapping[id].isPossible:
        totalCalibrationValue += id

print("Total calibration value: " + str(totalCalibrationValue))