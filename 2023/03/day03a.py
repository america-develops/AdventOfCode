# GLOBAL VARIABLES
# ----------------
partsMapping = dict()
symbolMapping = dict()
# Extract file contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()


# FUNCTION DEFINITIONS
# --------------------
# Check if a string is only symbols
def isSymbol(p_char):
    if p_char.isalnum() or p_char == '.' or p_char.isspace():
        return False
    else:
        return True


# Find the start of a number
def extractFullNumberString(p_lineString, p_currIndex):
    MIN_INDEX = 0
    MAX_INDEX = len(p_lineString) - 1
    # Initialize variables
    numberString = p_lineString[p_currIndex]
    leftIndex = p_currIndex - 1
    rightIndex = p_currIndex + 1
    startIndex = p_currIndex
    leftChar = p_lineString[leftIndex] if leftIndex >= MIN_INDEX else '.'
    rightChar = p_lineString[rightIndex] if rightIndex <= MAX_INDEX else '.'
    # Search to the left
    while leftChar.isdigit():
        startIndex -= 1
        numberString = leftChar + numberString
        leftIndex -= 1
        leftChar = p_lineString[leftIndex] if leftIndex >= MIN_INDEX else '.'
    # Search to the right
    while rightChar.isdigit():
        numberString = numberString + rightChar
        rightIndex += 1
        rightChar = p_lineString[rightIndex] if rightIndex <= MAX_INDEX else '.'
    numberAndLoc = (numberString, startIndex)
    return numberAndLoc

# Check adjacent cells for numbers
def checkAdjacentCells(p_currRow, p_currCol):
    MIN_INDEX = 0
    MAX_ROW_INDEX = len(lines) - 1
    # Assumes all rows have the same length
    MAX_COL_INDEX = len(lines[0]) - 1
    prevRow = p_currRow - 1 if p_currRow > MIN_INDEX else MIN_INDEX
    nextRow = p_currRow + 1 if p_currRow < MAX_ROW_INDEX else MAX_ROW_INDEX
    prevCol = p_currCol - 1 if p_currCol > MIN_INDEX else MIN_INDEX
    nextCol = p_currCol + 1 if p_currCol < MAX_COL_INDEX else MAX_COL_INDEX
    # Iterate through adjacent and current rows
    for row in range(prevRow, nextRow + 1, 1):
        # Iterate through adjacent and current columns
        for col in range(prevCol, nextCol + 1, 1):
            # Do not check center cell
            if (row != p_currRow) or (col != p_currCol):
                # Ensure cell is not already mapped
                if (row, col) not in partsMapping:
                    adjacentCell = lines[row][col]
                    if adjacentCell.isdigit():
                        extractedNumAndIndex = extractFullNumberString(lines[row], col)
                        numberFullString = extractedNumAndIndex[0]
                        numberStartCol = extractedNumAndIndex[1]
                        partsMapping[(row, numberStartCol)] = numberFullString
                        if len(numberFullString) > 1:
                            secondIndex = numberStartCol + 1
                            endCutoff = numberStartCol + len(numberFullString)
                            for index in range(secondIndex, endCutoff, 1):
                                partsMapping[(row, index)] = 0

# MAIN PROGRAM
# ------------
for row in range(0, len(lines), 1):
    for col in range(0, len(lines[row]), 1):
        currentChar = lines[row][col]
        if isSymbol(currentChar):
            symbolMapping[(row, col)] = currentChar
            checkAdjacentCells(row, col)
print(symbolMapping)
print(partsMapping)
print()

# Calculate total calibration value
totalCalibrationValue = 0

for coords in partsMapping:
    partNumber = int(partsMapping[coords])
    totalCalibrationValue += partNumber


print("Total calibration value: " + str(totalCalibrationValue))