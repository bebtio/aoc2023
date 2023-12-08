import pdb

class NodeTraveler():

    def __init__(self, inFile: str):

        self.directions = ""
        self.nodes      = {}
        self.startNode  = ""

        self.parseFile(inFile)
        self.stepsToZZZ()
    
    def parseFile(self, inFile:str):

        with open( inFile, "r") as file:
            lines = file.readlines()
            lines = [l.strip() for l in lines]

            self.directions = lines.pop(0)
            lines.pop(0)
            self.startNode = lines[0].split(" = ")[0]

            for line in lines:
                n = Node(line)

                self.nodes[n.name] = n

    def stepsToZZZ(self):

        steps  = 0
        curNode = self.nodes["AAA"]

        while curNode.name != "ZZZ":

            for i in self.directions:
                
                if i == "L":
                    curNode = self.nodes[curNode.left]
                else:
                    curNode = self.nodes[curNode.right]

                
                steps += 1

                if curNode.name == "ZZZ":
                    break

        print(steps)

class Node():

    def __init__(self, inStr: str):

        parser     = inStr.split(" = ")
        self.name  = parser[0]

        parser     = parser[1].split(", ")
    
        self.left  = parser[0].replace("(","") 
        self.right = parser[1].replace(")","")


if __name__ == "__main__":

    n = NodeTraveler("puzzle_input.txt")