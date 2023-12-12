# GLOBAL VARIABLES
# ----------------
seeds = list()
seedToSoilMap = dict()
soilToFertilizerMap = dict()
fertilizerToWaterMap = dict()
waterToLightMap = dict()
lightToTempMap = dict()
tempToHumidityMap = dict()
humidityToLocMap = dict()
almanacMapNames = (
    'seed-to-soil map',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
)
almanacMaps = (
    seedToSoilMap,
    soilToFertilizerMap,
    fertilizerToWaterMap,
    waterToLightMap,
    lightToTempMap,
    tempToHumidityMap,
    humidityToLocMap
)


# MAIN PROGRAM
# ------------
# Extract file contents
filePath = "input.txt"
inputFile = open(filePath, 'r')
lines = inputFile.readlines()
inputFile.close()
# Populate seeds (always on first line)
seedLine = lines[0]
colonIndex = seedLine.find(':')
seedListString = seedLine[slice(colonIndex + 1, len(seedLine))]
seeds = seedListString.strip().split(' ')
del seedListString
del colonIndex
del seedLine
# Populate almanac maps from file contents
lineIndex = 1
mapIndex = -1
while mapIndex < len(almanacMaps) and lineIndex < len(lines):
    line = lines[lineIndex].strip()
    # Add almananc entry to map
    if line:
        nextSpace = line.find(' ')
        secondSpace = line.rfind(' ')
        destinationStart = int(line[slice(nextSpace)])
        sourceStart = int(line[slice(nextSpace+1, secondSpace)])
        intervalRange = int(line[slice(secondSpace + 1, len(line))])
        del nextSpace
        del secondSpace
        currentMap[sourceStart] = dict(dest = destinationStart, range = intervalRange)
        #print('Destination start:', destinationStart)
        #print('Source start:', sourceStart)
        #print('Range:', intervalRange)
        #print(lines[lineIndex])
        lineIndex += 1
    # Switch to next map after empty lines
    else:
        # Update current map
        mapIndex += 1
        currentMap = almanacMaps[mapIndex]
        # Jump ahead by two lines
        lineIndex += 2
del mapIndex
del lineIndex

def GetDestinationValue(p_sourceValue : int, p_almanacMap : dict):
    # Initialize destination value
    destValue = p_sourceValue
    # Iterate through map
    for sourceStart in p_almanacMap:
        sourceEnd = sourceStart + p_almanacMap[sourceStart]['range']
        if p_sourceValue == sourceStart:
            destValue = p_almanacMap[sourceStart]['dest']
            break
        elif sourceStart < p_sourceValue < sourceEnd:
            sourceStartDifference = p_sourceValue - sourceStart
            destValue = p_almanacMap[sourceStart]['dest'] + sourceStartDifference
            break
    return destValue

# Determine locations
minLocation = -1
for index in range(0, len(seeds)):
    seed = int(seeds[index])
    # Get soil
    seedSoil = GetDestinationValue(int(seed), seedToSoilMap)
    seedFertilizer = GetDestinationValue(seedSoil, soilToFertilizerMap)
    seedWater = GetDestinationValue(seedFertilizer, fertilizerToWaterMap)
    seedLight = GetDestinationValue(seedWater, waterToLightMap)
    seedTemp = GetDestinationValue(seedLight, lightToTempMap)
    seedHumidity = GetDestinationValue(seedTemp, tempToHumidityMap)
    seedLocation = GetDestinationValue(seedHumidity, humidityToLocMap)
    # Determine minimum location
    if index < 1:
        minLocation = seedLocation
    else:
        if seedLocation < minLocation:
            minLocation = seedLocation
    # Output associated values
    print('Seed {}, soil {}, fertilizer {}, ...'.format(seed, seedSoil, seedFertilizer))
    print('\t location {}'.format(seedLocation))
print('MINIMUM LOCATION:', minLocation)