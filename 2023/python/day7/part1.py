import pdb

cardTypes = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

valueMap  = {
             'A':12, 
             'K':11, 
             'Q':10, 
             'J':9, 
             'T':8, 
             '9':7,
             '8':6,
             '7':5,
             '6':4,
             '5':3,
             '4':2,
             '3':1,
             '2':0
             }


class Set():

    def __init__(self, inFile: str):

        self.strengthMap = { 0: list(), 1:list(), 2:list(), 3:list(), 4:list(), 5:list(),6:list() }

        with open(inFile, "r") as file:
            lines = file.readlines()

            for line in lines:
                c = Hand(line)

                self.strengthMap[c.typeStrength].append(c)


        self.sortStrengthMap()

        self.computeSetScore()

    def sortStrengthMap(self):

        for key,value in self.strengthMap.items():

            if len(value) != 0:
                x = sorted(value, key=lambda v: (v.rankedCards[0],v.rankedCards[1],v.rankedCards[2],v.rankedCards[3],v.rankedCards[4]),reverse=False)
                self.strengthMap[key] = x

    def computeSetScore(self):

        rank = 1
        sum  = 0
        for key,value in self.strengthMap.items():

            for v in value:
                sum += v.bid * rank
                print(f"cards={v.cards} bid={v.bid} rank={rank}")
                rank +=1



        print(sum)
class Hand():

    def __init__(self, inStr: str):

        self.cards = inStr.split()[0]
        self.bid   = int(inStr.split()[1])

        self.rankedCards = list()

        for c in self.cards:
            self.rankedCards.append(valueMap[c])

        # The strength level of the card Levels are in this order:
        # Five of a Kind  = 6
        # Four of a kind  = 5
        # Full house      = 4
        # Three of a kind = 3
        # two pair        = 2
        # one pair        = 1
        # high card       = 0
        self.typeStrength = 0

        self.computeTypeStrength(self.cards)
    
    def computeTypeStrength(self, cards:str):

        cMap = {}

        for c in cards:
            if c in cMap:
                cMap[c] += 1
            else:
                cMap[c] = 1

        mapLen = len(cMap)

        # You can determine what the hand is by the number of unique cards.
        # There is only overlap between 2 unique cards and 3 unique cards
        # so we have to deal with those cases specifically to determine what they are.
        if mapLen == 1:

            # Five of a kind
            self.typeStrength = 6
        
        elif mapLen == 2:

            values = sorted(cMap.values(),reverse=True)
        
            if values[0] == 4:
        
                # Four of a kind
                self.typeStrength = 5
            else:
        
                # Full house
                self.typeStrength = 4
        
        elif mapLen == 3:
        
            values = sorted(cMap.values(),reverse=True)
            
            if values[0] == 3:
        
                #  Three of a kind
                self.typeStrength = 3
        
            else:
        
                # Two Pair
                self.typeStrength = 2
        
        elif mapLen == 4:
        
            # One pair
            self.typeStrength = 1
        
        else:
            # High card
            self.typeStrength = 0


if __name__ == "__main__":


    s = Set("puzzle_input.txt")
