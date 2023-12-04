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
class Symbol(Indexable):

    def __init__(self, symbol:str, row: int, col: int, numRows: int, numCols: int):

        self.symbol   = symbol
        self.position = self.twoDIndexToLinearIndex(row,col,numCols)

        self.neighbors = list()

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
        self.symbols     = list()


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
                self.parseLineForSymbols(line, row, self.numRows, self.numCols)

        
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
    def parseLineForSymbols(self, line: str, row: int, numRows: int, numCols: int ):

        for col, c in enumerate(line):
            if not c.isalnum() and c != ".":
                
                s = Symbol(c, row, col, numRows, numCols)

                self.symbols.append(s) 


    def computeIntersections(self) -> int:

        partNumSum = 0
        for s in self.symbols:
            for p in self.partNumbers:
                
                partNumSum += self.checkPartSymbolIntersection(p,s)


        return(partNumSum)

    def checkPartSymbolIntersection(self, p: PartNumber, s: Symbol) -> bool:

        # Loop through neighbors 
        for neighbor in s.neighbors:

            # Loop through the positions
            for position in p.positions:
                # if any position matches up with a symbols neighbor, 
                # return the value of this part number.
                if position == neighbor:
                    p.isPartNumber = True
                    return( p.value )

        # If there is no intersection, this is not a part number and we return nothing.
        return(0)



    def getRealPartNumbers(self):

        realPartNumbers = [p for p in self.partNumbers if p.isPartNumber]

        return( realPartNumbers )

    def getFakePartNumbers(self):

        fakePartNumbers = [p for p in self.partNumbers if not p.isPartNumber]

        return( fakePartNumbers )

if __name__ == "__main__":
    s = Schematic()

    s.initialize("puzzle_input.txt")

    print(s.computeIntersections())
