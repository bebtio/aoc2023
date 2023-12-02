import pdb
import re

# For part 2, we want to do the same thing as part 1, EXCEPT, we want to turn any fully spelled out number
# into its digit character first. That will let us keep the code we already wrote unchanged.

numIntMap = {'one'  :'1',
             'two'  :'2',
             'three':'3',
             'four' :'4',
             'five' :'5',
             'six'  :'6',
             'seven':'7',
             'eight':'8',
             'nine' :'9'}

# Get a map of all the string integers and their index.
def getAllStrNums( inStr: str ): 
    
    # Get text we are looking for.
    keys = numIntMap.keys()
    
    forwardDict  = {}
    listOfKeys = []

    # Loop through keys and find every instance they occur.
    for k in keys:
        indices = [m.start() for m in re.finditer(k, inStr)]

        # If we found any occurences, record them.
        if len(indices) != 0:
            for index in indices:
                
                forwardDict[index] = numIntMap[k]
                listOfKeys.append(index)

    return forwardDict

# Get a map of all the integer characters and their index.
def getAllIntNums( inStr: str ):

    retDict = {}
    for index,c in enumerate(inStr):
        if c.isdigit(): 
            retDict[index] = c


    return retDict

# Now we iterate through the lines in the file using the two previous functions.
def loopThroughFile( filePath: str ) -> int:

    calibrationSum = 0

    with open( filePath, 'r') as file:
        lines = file.readlines()

        for line in lines:

            line       = line.strip()
            numStrDict = getAllStrNums(line)
            intStrDict = getAllIntNums(line)

            # Combine the dictionaries.
            intStrDict.update(numStrDict)

            # Get the list of keys
            keyList = list(intStrDict.keys())

            # Get the min key and max key. This effectively gives us the
            # first and last number in the line, which is what we want.
            minKey = min(keyList)
            maxKey = max(keyList)
            
            # Combine them to make a single integer.
            value = int( intStrDict[minKey] + intStrDict[maxKey])

            # Keep track of the running total.
            calibrationSum += value

    return calibrationSum

if __name__ == "__main__":

    fileName = "puzzle_input.txt"

    result = loopThroughFile(fileName)

    print(f'result = {result}')