
class GameInfo:

    def __init__(self):
        self.gameId: int = -1
        self.boxSets = []
        self.isValid = False
        self.power   = 0
    
    # Parse the string represent the outcome of this game.
    def parseGame(self, gameFile: str):    

        # Get the gameID
        gameId = gameFile.split(':')[0]
        gameId = gameId.split()[1]
        self.gameId = int(gameId)


        # Get the sets for this game.
        gameSets = gameFile.split(":")[1]
        gameSets = gameSets.split(";")

        # Parse the portion containing game outcomes.
        self.parseGameSets(gameSets)

    # Parse the portion of the game string that contains the sets of
    # randomly selected colored boxes.
    def parseGameSets(self, sets: str ):

        for set in sets:
            
            # Get each of the colors in the current set.
            colorSets = set.split(",")
            colorSets = [s.lstrip() for s in colorSets]
            colorSets = [s.rstrip() for s in colorSets]

            colorDict = {}
            for colorSet in colorSets:
                number   = colorSet.split(" ")[0]
                color    = colorSet.split(" ")[1]

                colorDict[color] = int(number)

            self.boxSets.append( colorDict )


    # Brute force check the sets to see if they invalidate this game.
    # If any of the *Count input variables are smaller than any sets, number of colored
    # boxes, this game is invalid.
    # We could break after this occurs but that's extra logic I don't feel like implementing.            
    def checkIfGameValid(self, redCount:int, greenCount:int, blueCount:int ) -> bool:

        valid = False
        invalidCount = 0

        for set in self.boxSets:
            
            for color in set:
                if color == "red":
                   if set[color] > redCount:
                       invalidCount += 1 
                elif color == "green":
                    if set[color] > greenCount:
                        invalidCount += 1
                elif color == "blue":
                    if set[color] > blueCount:
                        invalidCount += 1
                else:
                    print(f' {color} is not a valid color')

        if invalidCount == 0:
            valid = True
            self.isValid = True

        return( valid )

    # Get the game points that are stored at self.gameId.
    def getGamePoints(self):

        if( self.isValid ):
            return( self.gameId )
        else:
            return(0)

    # Compute the power of the currenct game.        
    def computeGamePower(self) -> int:

        minRed   = -1
        minGreen = -1
        minBlue  = -1

        # Loop through the sets and update each color if the currently stored value
        # is smaller than the one we are looking at.
        for set in self.boxSets:
            for color in set:
                if color == "red":
                   if set[color] > minRed or minRed == -1:
                       minRed = set[color] 
                elif color == "green":
                    if set[color] > minGreen or minGreen == -1:
                        minGreen = set[color]
                elif color == "blue":
                    if set[color] > minBlue or minBlue == -1:
                        minBlue = set[color]
                else:
                    print(f' {color} is not a valid color')

        # compute the power and store it.
        self.power = minRed * minGreen * minBlue

        return(self.power)
    
# Parse the input file and compute the power of each game.
def parseFile( fileName: str ) -> int:

    gameSum = 0

    # Opent the file.
    with open(fileName, "r") as f:

        # Get all the lines in the file.
        lines = f.readlines()

        for line in lines:

            # Parse each line and create a GameInfo object.
            g = GameInfo()
            g.parseGame(line)

            # Compute the power based on the what was read in.
            gameSum += g.computeGamePower()            

            print(f'game {g.gameId}\'s power is {g.power}')

    return(gameSum)

if __name__ == "__main__":

    power = parseFile("./puzzle_input.txt")
    print( f'game power = {power}')

