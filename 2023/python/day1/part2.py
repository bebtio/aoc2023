import pdb

# We want to loop forwards from the start of the string and return the first number we find.
def loopForwards( inStr: str ) -> str:

    for c in inStr:
        if c.isdigit():
            return(c)

# We want to loop backwards and return the first number we find.
def loopBackwards( inStr: str ) -> str:
    
    for c in reversed(inStr):
        if c.isdigit():
            return(c)

# Now we iterate through the lines in the file using the two previous functions.
def loopThroughFile( filePath: str ) -> int:

    calibrationSum = 0

    with open( filePath, 'r') as file:
        lines = file.readlines()

        for line in lines:

            line = line.strip()
            firstNum  = loopForwards(line)
            secondNum = loopBackwards(line)

            # concatenate the results and convert to integer.
            value = int(firstNum + secondNum )

            print(f"value = {value}")
            calibrationSum += value

    return calibrationSum

if __name__ == "__main__":

    fileName = "puzzle_input.txt"

    result = loopThroughFile(fileName)

    print(f'result = {result}')