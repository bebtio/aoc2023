import pdb

######################################################
#
######################################################
class Indexable():

    # Takes a (0 INDEXED!!) row and column value and computes which numbered element that element
    # is in a sequence.
    def twoDIndexToLinearIndex(self, row: int, col: int, numCols: int) -> int:

        index = (numCols * row) + col;
        return( index )

    # does the reverse. Returns row and col as a pair.
    def linearIndexToTwoDIndex(self, index: int, numCols: int, numRows: int) -> (int, int):

        row = index / numCols
        col = index % numCols

        return ( row, col )
######################################################
#
######################################################
class PartNumber(Indexable):

    # part numbers can have a range of positions depending on how many digits they are.
    def __init__(self, number: str, row: int, col: int, numCols: int):
        self.value = int(number)

        # We only get into this function at the last digit of the parsed number.
        # To get the correct start position we must subtract its length
        startPos = self.twoDIndexToLinearIndex(row, col, numCols)-len(number)

        # Compute the index of each character in this number.
        self.positions = [*range(startPos,startPos+len(number))]

        self.isPartNumber = False

######################################################
#
######################################################
class Gear(Indexable):

    def __init__(self, gear:str, row: int, col: int, numRows: int, numCols: int):

        self.gear   =gear 
        self.position = self.twoDIndexToLinearIndex(row,col,numCols)

        self.neighbors = list()

        # This is where part number adjacent to this Gear will go.
        self.partNumberRatios    = list()
        self.computeNeighbors( row, col, numRows, numCols) 

    def computeNeighbors(self, row: int, col:int , numRows: int, numCols: int):

        # Compute the 8 surronding neihbor indices
        # Neighbors directly above
        
        for r in range(-1,2,1):
            for c in range(-1,2,1):

                curRow = row + r
                curCol = col + c

                
                if not (curRow == row and curCol == col):
                    # only add them if thare within the bounds of 0 to numRows and 0 to numCols
                    
                    if( curRow < numRows and curRow >= 0):
                        if( curCol < numCols and curCol >= 0):
                            self.neighbors.append( self.twoDIndexToLinearIndex(curRow, curCol, numCols) )
        


######################################################
#
#######################################################
class Schematic():

    def __init__(self):
        
        # (Rows,Columns)
        self.numCols    = 0
        self.numRows    = 0

        self.partNumbers = list()
        self.gears       = list()


    ######################################################
    def initialize(self, fileName: str):
        
        with open( fileName, "r") as file:
            lines = file.readlines()
            lines = [l.strip() for l in lines]

            # The number of characters in each line is the number of columns.
            self.numCols = len(lines[0])
            
            # The number of lines is the number of rows.
            self.numRows = len(lines)

            for row, line in enumerate(lines):
                self.parseLineForPartNumbers(line, row, self.numCols)
                self.parseLineForGears(line, row, self.numRows, self.numCols)

        
    ######################################################
    # Pass the current line and the row its in.
    def parseLineForPartNumbers(self, line: str, row: int, numCols: int ):

        currDigit = list()
        
        for col, c in enumerate(line):

            if c.isdigit():
                currDigit.append(c)
            else:
                if len(currDigit) != 0:
                    digitStr = "".join(currDigit)
                    p = PartNumber(digitStr, row, col, numCols )

                    self.partNumbers.append(p)

                    # Empty the list once we have initialized the number.
                    currDigit = list()

        # Handle the last number in case there is one at the end of the file.
        if len(currDigit)!= 0:
            
            digitStr = "".join(currDigit)
            p = PartNumber(digitStr, row, col, numCols )

            self.partNumbers.append(p)
    
    ######################################################
    # Parse for gears "*" this time.
    def parseLineForGears(self, line: str, row: int, numRows: int, numCols: int ):

        for col, c in enumerate(line):
            if c == "*":
                
                g = Gear(c, row, col, numRows, numCols)

                self.gears.append(g) 


    def computeIntersections(self):

        partNumSum = 0
        for g in self.gears:
            for p in self.partNumbers:
                
                self.checkPartGearIntersection(p,g)



    def checkPartGearIntersection(self, p: PartNumber, g: Gear):

        # Loop through neighbors 
        for neighbor in g.neighbors:

            # Loop through the positions
            for position in p.positions:
                
                # Add all part numbers that are adjacent to the gear.
                if position == neighbor:
                    g.partNumberRatios.append(p.value) 
                    return

    def getSumOfGearRations(self) -> int:
        pdb.set_trace()
        sum = 0
        for g in self.gears:

            if len(g.partNumberRatios) == 2:
                sum += g.partNumberRatios[0] * g.partNumberRatios[1]
                

        return(sum)


    def getRealPartNumbers(self):

        realPartNumbers = [p for p in self.partNumbers if p.isPartNumber]

        return( realPartNumbers )

    def getFakePartNumbers(self):

        fakePartNumbers = [p for p in self.partNumbers if not p.isPartNumber]

        return( fakePartNumbers )

if __name__ == "__main__":
    s = Schematic()

    s.initialize("puzzle_input.txt")
    s.computeIntersections()

    print(s.getSumOfGearRations())