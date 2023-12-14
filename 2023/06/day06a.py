# GLOBAL CONSTANTS
# ----------------
SPEED_INCREASE_PER_TIME_PRESSED = 1


# GLOBAL VARIABLES
# ----------------
raceList = list()


# CLASSES
# -------
class Race:
    def __init__(self, p_id: int, p_raceTime : int, p_recordDistance : int):
        self.id = p_id
        self.raceTime = p_raceTime
        self.recordDistance = p_recordDistance
        self.minTimePressedToWin = self.CalcMinTimePressedToWin()
        self.maxTimePressedToWin = self.raceTime - self.minTimePressedToWin
        self.numWaysToWin = self.CalcNumWaysToWin()

    def CalcMinTimePressedToWin(self):
        timePress = self.raceTime // 2
        # Simulating a do-while loop
        while (True):
            travelTime = self.raceTime - timePress
            travelSpeed = timePress * SPEED_INCREASE_PER_TIME_PRESSED
            distanceTraveled = travelTime * travelSpeed
            if (distanceTraveled <= self.recordDistance):
                break
            minTimePress = timePress
            timePress -= 1
        return minTimePress

    def CalcNumWaysToWin(self):
        waysToWin = range(self.minTimePressedToWin, self.maxTimePressedToWin + 1)
        return len(waysToWin)


# MAIN PROGRAM
# ------------
# FIXME: Change below code to automatically extract data from input file

'''
# Populate race list (using demo input)
raceList.append(Race(0, 7, 9))
raceList.append(Race(1, 15, 40))
raceList.append(Race(2, 30, 200))
'''
# Populate race list
raceList.append(Race(0, 62, 553))
raceList.append(Race(1, 64, 1010))
raceList.append(Race(2, 91, 1473))
raceList.append(Race(3, 90, 1074))
# Calculate margin of error
marginOfError = 1
for race in raceList:
    print('Race', race.id + 1)
    print('------------------')
    print('Minimum time press:', race.minTimePressedToWin)
    print('Maximum time press:', race.maxTimePressedToWin)
    print('Number of ways to win: {}'.format(race.numWaysToWin))
    print()
    marginOfError *= race.numWaysToWin
print('MARGIN OF ERROR:', marginOfError)