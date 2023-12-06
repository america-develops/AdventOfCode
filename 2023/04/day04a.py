# GLOBAL VARIABLES
# ----------------
cardsMapping = dict()

# CLASSES
# -------
class Card:
    def __init__(self, p_id):
        self.id = p_id
        self.winningNums = set()
        self.handNums = list()
        self.winningNumCount = 0
        self.points = 0

    def setWinningNums(self, p_numListString: str):
        numList = set(p_numListString.strip().split(' '))
        if '' in numList: numList.remove('')
        self.winningNums = numList

    def setHandNums(self, p_numListString: str):
        numList = p_numListString.strip().split(' ')
        self.handNums = numList

    def calculatePoints(self):
        self.points = 0
        self.winningNumCount = 0
        for num in self.handNums:
            if num.isdigit() and num in self.winningNums:
                self.winningNumCount += 1
                if self.winningNumCount > 1:
                    self.points *= 2
                else:
                    self.points += 1

    def printInfo(self):
        print('Card ' + str(self.id))
        print('----------------')
        print('Winning Nums: ' + str(self.winningNums))
        print('Hand Nums: ' + str(self.handNums))
        print('Winning number count: ' + str(self.winningNumCount))
        print('Points: ' + str(self.points))
        print()


# MAIN PROGRAM
# ------------
# Extract file contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
# Parse file contents
for line in lines:
    colonIndex = line.find(':')
    separatorIndex = line.find('|')
    # Extract card ID
    cardId = int(line[slice(5, colonIndex)].strip())
    # Add card to collection
    cardsMapping[cardId] = Card(cardId)
    # Extract winning numbers
    winningNumString = line[slice(colonIndex + 1, separatorIndex)]
    cardsMapping[cardId].setWinningNums(winningNumString.strip())
    # Extract numbers in hand
    handNumString = line[slice(separatorIndex + 1, len(line))]
    cardsMapping[cardId].setHandNums(handNumString.strip())
# Calculate total calibration value
totalCalibrationValue = 0
for id in cardsMapping:
    # Calculate points
    cardsMapping[id].calculatePoints()
    totalCalibrationValue += cardsMapping[id].points
    cardsMapping[id].printInfo()

print('Total calibration value: ' + str(totalCalibrationValue))
