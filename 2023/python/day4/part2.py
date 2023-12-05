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

        # Make this card's index its number minus for easier indexing later.
        self.index = self.number -1

        self.winningNumbers = list()
        self.cardNumbers    = list()

        splitText = cardText.split("|")
        self.createWinningNumbers(splitText[0])
        self.createCardNumbers(splitText[1])

        self.intersections = list()

        self.computeIntersections()

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

    # Compute the intersection between the card numebrs and the winning numbers.
    def computeIntersections(self):
        self.intersections = list(set(set(self.winningNumbers) & set(self.cardNumbers)))


# Create a class to count the combinations
class CardCounter():

    def __init__(self, inputFile: str):
        
        self.initialCards = list()
        
        self.generateInitialCardList(inputFile)
        pass
        
    # First read in all the cards and store them in a list.
    def generateInitialCardList(self,inputFile: str):

        cards = list() 

        with open(inputFile, "r") as file:

            lines = file.readlines()

            for line in lines:
                line = line.rstrip()
                c = Card(line)
                self.initialCards.append(c)

    # Loop over all the cards and count all the cards each of them win.
    def countClones(self):

        sum = 0 

        for card in self.initialCards:
            
            sum+= self.generateClones(card, self.initialCards)

        return(sum) 

    # Recursively search the cards the winning cards.
    def generateClones(self, card: Card, cardList: list()) -> int:
        
        # Count the initial card itself.
        sum = 1 

        # If the current card has no intersections we are done.
        if len(card.intersections) == 0:
            return sum
        
        # Iterate over all the intersections, which are the winning cards
        # recursively go to the next card in the sequence for each winning card.
        for idx, intersection in enumerate(card.intersections):


            sum += self.generateClones(cardList[card.number+idx], cardList)

        # Return the total number of cards this card won, including itself.
        return(sum)

if __name__ == "__main__":


    # Initialize the card counter with the input file text.
    c = CardCounter("puzzle_input.txt")

    # Count the winning cards and print it out.
    print(c.countClones())
