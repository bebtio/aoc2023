import math
import pdb

class Card():

    # Initialize with a line from the input file.
    def __init__(self, cardText: str):

        # Get this cards number.
        self.number         = cardText.split("|")[0]
        self.number         = self.number.split(":")[0]
        self.number         = self.number.split(" ")
        self.number         = [n for n in self.number if n != ""]
        self.number         = int(self.number[1])

        self.winningNumbers = list()
        self.cardNumbers    = list()

        self.cardPointTotal = 0


        splitText = cardText.split("|")
        self.createWinningNumbers(splitText[0])
        self.createCardNumbers(splitText[1])

        self.computeCardPointTotal()

    # Populate the list of winning numbers.
    def createWinningNumbers(self, winningNumberText: str):

        numbers = winningNumberText.split(":")[1]
        
        # Remove any leading or trailing white space.
        numbers = numbers.lstrip()
        numbers = numbers.rstrip()

        # Get each number as its own element.
        numbers = numbers.split(" ")
        numbers = [n for n in numbers if len(n) != 0]
        
        # Cast each of the numbers to ints.
        self.winningNumbers = [int(n) for n in numbers]
        
    # Populate the list of numbers on the card.
    def createCardNumbers(self, cardNumbertext: str):
        
        # remove any leading or trailing white space.
        numbers = cardNumbertext.lstrip()
        numbers = numbers.rstrip()
        numbers = numbers.split(" ")
        numbers = [n for n in numbers if len(n) != 0]
        self.cardNumbers = [int(n) for n in numbers]

    def computeCardPointTotal(self):

        # Find the elements that both lists share.
        intersection = list(set(set(self.winningNumbers) & set(self.cardNumbers)))

        numWinningNumbers = len(intersection)

        if numWinningNumbers > 0:
            # Compute the point total.
            self.cardPointTotal = math.pow(2,numWinningNumbers-1)

    def getCardPointTotal(self) -> int:

        return(self.cardPointTotal)
    
def run(inputFile: str) -> int:

    cards = list() 

    sum = 0
    with open(inputFile, "r") as file:

        lines = file.readlines()

        for line in lines:
            print(line)
            line = line.rstrip()
            c = Card(line)

            sum += c.getCardPointTotal()

            cards.append(c)

    return sum



if __name__ == "__main__":



    print(run("puzzle_input.txt"))
