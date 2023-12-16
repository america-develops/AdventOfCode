# GLOBAL CONSTANTS
# ----------------
# Cards in ascending order of relative strength
CARD_LABELS = (
    '2', '3', '4', '5', '6',
    '7', '8', '9', 'T', 'J',
    'Q', 'K', 'A'
)
# Types of hands in ascending order of relative strength
HAND_TYPES = (
    'High card',
    'One pair',
    'Two pair',
    'Three of a kind',
    'Full house',
    'Four of a kind',
    'Five of a kind'
)


# GLOBAL VARIABLES
# ----------------
handsMap = dict()


# CLASSES
# -------
class Hand:
    def __init__(self, p_handString, p_bid):
        self.cards = p_handString
        self.bid = p_bid
        self.type = self.determineHandType()

    def determineHandType(self):
        uniqueCardCounts = dict()
        for card in self.cards:
            # Valid card label
            if card in CARD_LABELS:
                if card in uniqueCardCounts:
                    uniqueCardCounts[card] += 1
                else:
                    uniqueCardCounts[card] = 1
            # Invalid card label
            else:
                return None
        numUniqueCards = len(uniqueCardCounts)
        # Check if five of a kind
        if numUniqueCards == 1:
            return HAND_TYPES[6]
        # Check if only 2 unique cards
        elif numUniqueCards == 2:
            cardCounts = uniqueCardCounts.values()
            # Check if four of a kind
            if 4 in cardCounts:
                return HAND_TYPES[5]
            # Check if full house
            elif 3 in cardCounts:
                return HAND_TYPES[4]
            # Invalid hand
            else:
                return None
        # Check if only 3 unique cards
        elif len(uniqueCardCounts) == 3:
            cardCounts = uniqueCardCounts.values()
            # Check if three of a kind
            if 3 in cardCounts:
                return HAND_TYPES[3]
            # Check if two pair
            elif 2 in cardCounts and sum(cardCounts) == 5:
                return HAND_TYPES[2]
            # Invalid hand
            else:
                return None
        # Check if one pair
        elif numUniqueCards == 4:
            return HAND_TYPES[1]
        # Check if high card (all cards unique)
        elif numUniqueCards == 5:
            return HAND_TYPES[0]
        # Invalid hand
        else:
            return None


# MAIN PROGRAM
# ------------
# Extract file contents
# ---------------------
filePath = "demo.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
del inputFile
del filePath
# Parse file for hands and bids
# -----------------------------
for line in lines:
    # Extract hand
    handString = line[0:4]
    

'''hands.append('AAAAA')
hands.append('AA8AA')
hands.append('AAAA8')
hands.append('8AAAA')
hands.append('23332')
hands.append('22333')
hands.append('33322')
hands.append('32323')
hands.append('TTT98')
hands.append('98TTT')
hands.append('9TTT8')
hands.append('T9T8T')
hands.append('23432')
hands.append('22433')
hands.append('42233')
hands.append('22334')
hands.append('A23A4')
hands.append('AA234')
hands.append('234AA')
hands.append('23AA4')
hands.append('23456')

for hand in hands:
    print(hand, determineHandType(hand))'''