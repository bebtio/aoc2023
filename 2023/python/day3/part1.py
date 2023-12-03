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

                #self.parseLineForPartNumbers(line,row)
                self.parseLineForSymbols(line,row, self.numCols)

    
    ######################################################
    # Pass the current line and the row its in.
    def parseLineForPartNumbers(self, line: str, row: int, numCols: int ):

        currDigit = list()
        startCol  = 0
        endCol    = 0
        for col, c in enumerate(line):

            if c.isdigit():
                currDigit.append(c)
            else:
                pass


    ######################################################
    def parseLineForSymbols(self, line: str, row: int, numCols: int ):

        for col, c in enumerate(line):
            if not c.isalnum() and c != ".":
                
                pdb.set_trace()
                s = Symbol(c, row, col, numCols)

                self.symbols.append(s) 


######################################################
#
######################################################
class PartNumber(Indexable):

    def __init__(self):
        self.value = 0
        self.positions = list()


######################################################
#
######################################################
class Symbol(Indexable):

    def __init__(self, symbol:str, row: int, col: int, numCols: int):

        self.symbol   = symbol
        self.position = self.twoDIndexToLinearIndex(row,col,numCols)

        self.neighbors = list()

        self.computeNeighbors( row, col, numCols) 

    def computeNeighbors(self, row: int, col:int , numCols: int):

        # Compute the 8 surronding neihbor indices
        # Neighbors directly above
        self.neighbors.append( self.twoDIndexToLinearIndex(row+1, col+1, numCols) )
        self.neighbors.append( self.twoDIndexToLinearIndex(row+1, col, numCols) )
        self.neighbors.append( self.twoDIndexToLinearIndex(row+1, col-1, numCols) )
        
        # Right and left neighbors.
        self.neighbors.append( self.twoDIndexToLinearIndex(row, col+1, numCols) )
        self.neighbors.append( self.twoDIndexToLinearIndex(row, col-1, numCols) )

        # Bottom neighbors.
        self.neighbors.append( self.twoDIndexToLinearIndex(row-1, col+1, numCols) )
        self.neighbors.append( self.twoDIndexToLinearIndex(row-1, col, numCols) )
        self.neighbors.append( self.twoDIndexToLinearIndex(row-1, col-1, numCols) )



if __name__ == "__main__":
    s = Schematic()

    pdb.set_trace()
    s.initialize("./test.txt")

    pdb.set_trace()