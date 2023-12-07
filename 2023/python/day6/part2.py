import math
import numpy as np

def quadraticFormula( a:float, b:float, c:float ) -> list():

    roots = np.roots([a, b, c])

    return roots


if __name__ == "__main__":

    times = [53897698]
    distances = [313109012141202]

    timesToWin = list()

    multiple = 1

    for idx, t in enumerate(times):
        
        root = quadraticFormula(1,-times[idx],distances[idx])
        print(root)
        root[0] = math.floor(root[0])
        root[1] = math.ceil(root[1])
        
        print(root)

        multiple *= (root[0] - root[1] + 1)
        print(multiple)
        print("")

