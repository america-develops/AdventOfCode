# GLOBAL VARIABLES
# ----------------
# Cards in ascending order of relative strength
cards = (
    '2', '3', '4', '5', '6',
    '7', '8', '9', 'T', 'J',
    'Q', 'K', 'A'
)
handTypes = (
    'High card',
    'One pair',
    'Two pair',
    'Three of a kind',
    'Full house',
    'Four of a kind',
    'Five of a kind'
)

# FUNCTION DEFINITIONS
# --------------------
def determineHandType(p_handString : str):
    uniqueCardCounts = dict()
    for card in p_handString:
        if card in uniqueCardCounts:
            uniqueCardCounts[card] += 1
        else:
            uniqueCardCounts[card] = 1
    numUniqueCards = len(uniqueCardCounts)
    # Check if five of a kind
    if numUniqueCards == 1: return handTypes[6]
    # Check if only 2 unique cards
    elif numUniqueCards == 2:
        cardCounts = uniqueCardCounts.values()
        # Check if four of a kind
        if 4 in cardCounts: return handTypes[5]
        # Check if full house
        elif 3 in cardCounts: return handTypes[4]
        # Invalid hand
        else: return None
    # Check if only 3 unique cards
    elif len(uniqueCardCounts) == 3:
        cardCounts = uniqueCardCounts.values()
        # Check if three of a kind
        if 3 in cardCounts: return handTypes[3]
        # Check if two pair
        elif 2 in cardCounts and sum(cardCounts) == 5:
            return handTypes[2]
        # Invalid hand
        else: return None
    # Check if one pair
    elif numUniqueCards == 4: return handTypes[1]
    # Check if high card (all cards unique)
    elif numUniqueCards == 5: return handTypes[0]
    # Invalid hand
    else: return None


# MAIN PROGRAM
# ------------
hands = list()
hands.append('AAAAA')
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
    print(hand, determineHandType(hand))