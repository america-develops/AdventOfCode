# GLOBAL VARIABLES
# ----------------
cardsMapping = dict()
cardCopiesCount = dict()
cardMatchesCount = dict()

# CLASSES
# -------
class Card:
    def __init__(self, p_id):
        self.id = p_id
        self.winningNums = set()
        self.handNums = list()
        self.foundWinningNums = list()
        self.numMatchesCounted = False
        self.numMatches = 0

    def setWinningNums(self, p_numListString: str):
        numList = set(p_numListString.strip().split(' '))
        if '' in numList: numList.remove('')
        self.winningNums = numList

    def setHandNums(self, p_numListString: str):
        numList = p_numListString.strip().split(' ')
        while '' in numList:
            numList.remove('')
        self.handNums = numList

    def calculateNumMatches(self):
        # Verify winning numbers and hand numbers have been set
        if self.winningNums and self.handNums:
            # Only run once
            if not self.numMatchesCounted:
                matchCount = 0
                for num in self.handNums:
                    if num.isdigit() and num in self.winningNums:
                        matchCount += 1
                self.numMatches = matchCount
                # Update match dictionary
                cardMatchesCount[self.id] = self.numMatches
                # Update flag
                self.numMatchesCounted = True

    def printInfo(self):
        print('Card ' + str(self.id))
        print('---------------------')
        print('Winning nums: ' + str(self.winningNums))
        print('Hand nums: ' + str(self.handNums))
        print('Matching number count: ' + str(self.numMatches))
        print()


# FUNCTION DEFINITIONS
# --------------------
def CalculateReturnedCards(p_Card : Card):
    id = p_Card.id
    if p_Card.numMatches > 0:
        totalReturnedCards = p_Card.numMatches
        for idOffset in range (1, p_Card.numMatches + 1):
            currentReturnedCards = CalculateReturnedCards(cardsMapping[id + idOffset])
            totalReturnedCards += currentReturnedCards
        return totalReturnedCards
    else:
        return 0
    pass


# MAIN PROGRAM
# ------------
# Extract file contents
filePath = "demo.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
# Parse file contents to extract cards
cardIdMax = -1
for line in lines:
    colonIndex = line.find(':')
    separatorIndex = line.find('|')
    # Extract card ID
    cardId = int(line[slice(5, colonIndex)].strip())
    # Update max card ID (if necessary)
    if cardId > cardIdMax: cardIdMax = cardId
    # Add card to collection
    cardsMapping[cardId] = Card(cardId)
    cardCopiesCount[cardId] = 1
    # Extract winning numbers
    winningNumString = line[slice(colonIndex + 1, separatorIndex)]
    cardsMapping[cardId].setWinningNums(winningNumString.strip())
    # Extract numbers in hand
    handNumString = line[slice(separatorIndex + 1, len(line))]
    cardsMapping[cardId].setHandNums(handNumString.strip())
    # Count winning numbers
    cardsMapping[cardId].calculateNumMatches()
# Calculate total calibration value
totalCalibrationValue = len(cardsMapping)
for id in cardsMapping:
    #cardsMapping[id].printInfo()
    totalCalibrationValue += CalculateReturnedCards(cardsMapping[id])


print('-------------------------------------------------------')
print('Total calibration value: ' + str(totalCalibrationValue))
print('Maximum card ID:', cardIdMax)
