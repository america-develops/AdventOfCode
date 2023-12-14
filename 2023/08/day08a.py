# CLASSES
# -------
class Node:
    def __init__(self, p_id : str, p_left : str, p_right : str):
        self.id = p_id
        self.left = p_left
        self.right = p_right


# GLOBAL VARIABLES
# ----------------
nodes = dict()
headNode = None


# MAIN PROGRAM
# ------------
# Extract file contents
# ---------------------
filePath = "demo2.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
# Extract directions
# ------------------
directions = lines[0].strip()
# Populate nodes
# --------------
for index in range(2, len(lines)):
    nodeLine = lines[index]
    # Extract node's id
    nodeId = nodeLine[0:3]
    print('node id:', nodeId)
    # Extract left node
    leftNode = nodeLine[7:10]
    print('left node:', leftNode)
    # Extract right node
    rightNode = nodeLine[12:15]
    print('right node:', rightNode)
    # Add node
    nodes[nodeId] = Node(nodeId, leftNode, rightNode)
    # Update head node (if necessary)
    if not headNode:
        headNode = nodes[nodeId]
        print("HEAD NODE:", headNode.id)
print('\n')
# Travel through nodes
# --------------------
currentNode = headNode
endNode = 'ZZZ'
numSteps = 0
index = 0
while currentNode.id != endNode:
    numSteps += 1
    # Output info
    print('Current node:', currentNode.id)
    print('Direction index:', index)
    print('Direction:', directions[index])
    currentDirection = directions[index]
    if currentDirection == 'R':
        nextNodeId = currentNode.right
    elif currentDirection == 'L':
        nextNodeId = currentNode.left
    else:
        print("ERROR: Invalid direction")
        break
    currentNode = nodes[nextNodeId]
    # Update index (restart count if necessary)
    index += 1
    # Restart indexing if necessary
    if index == len(directions): index = 0
    print()

print('--------------------------')
print('NUMBER OF STEPS:', numSteps)

