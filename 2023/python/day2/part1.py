import pdb

class GameInfo:

    def __init__(self):
        self.gameId: int = -1
        self.boxSets = []
        self.isValid = False

    def parseGame(self, gameFile: str):
        

        # Get the gameID
        gameId = gameFile.split(':')[0]
        gameId = gameId.split()[1]
        self.gameId = int(gameId)


        # Get the sets for this game.
        gameSets = gameFile.split(":")[1]
        gameSets = gameSets.split(";")


        self.parseGameSets(gameSets)

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

    def getGamePoints(self):

        if( self.isValid ):
            return( self.gameId )
        else:
            return(0)
        
def parseFile( fileName: str ) -> int:

    gameArray = list()
    rCount = 12
    gCount = 13
    bCount = 14

    gameSum = 0

    with open(fileName, "r") as f:

        lines = f.readlines()

        for line in lines:
            g = GameInfo()
            g.parseGame(line)
            g.checkIfGameValid(rCount,gCount,bCount)
            
            print(f'Game {g.gameId} validity is {str(g.isValid)}')
            gameSum += g.getGamePoints()            


    return(gameSum)

if __name__ == "__main__":

    sum = parseFile("./puzzle_input.txt")
    print( f'sum = {sum}')

