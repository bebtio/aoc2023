import pdb

class Almanac():
    

    def __init__(self, fileName: str ):
        
        self.seedList                = list()
        self.seed_to_soil            = list()
        self.soil_to_fertilizer      = list()
        self.fertilizer_to_water     = list()
        self.water_to_light          = list()
        self.light_to_temperature    = list()
        self.temperature_to_humidity = list()
        self.humidity_to_location    = list()

        with open( fileName, "r" ) as file:

            lines = file.readlines()

            lines = [l.rstrip() for l in lines] 
            lines = [l.lstrip() for l in lines]

            for lineIndex,line in enumerate(lines):
        
                if "seeds:" in line:
                    self.createSeedList(line)

                elif "seed-to-soil map:" in line:
                    self.seed_to_soil = self.createMap(lines[lineIndex+1:])
                
                elif "soil-to-fertilizer map:" in line:
                    self.soil_to_fertilizer = self.createMap(lines[lineIndex+1:])

                elif "fertilizer-to-water map:" in line:
                    self.fertilizer_to_water = self.createMap(lines[lineIndex+1:])

                elif "water-to-light map:" in line:
                    self.water_to_light = self.createMap(lines[lineIndex+1:])
                
                elif "light-to-temperature map:" in line:
                    self.light_to_temperature = self.createMap(lines[lineIndex+1:])

                elif "temperature-to-humidity map:" in line:
                    self.temperature_to_humidity = self.createMap(lines[lineIndex+1:])

                elif "humidity-to-location map:" in line:
                    self.humidity_to_location = self.createMap(lines[lineIndex+1:])

    def createSeedList(self, inStr: str):

        seedList = inStr.split(": ")[1]
        seedList = seedList.split(" ")

        seedList = [int(s) for s in seedList]
        for i in range(0,len(seedList),2):


            startSeedList = seedList[i]
            rangeSeedList = seedList[i+1]

            # Change this to a list of ranges since the amount of data is huge.
            self.seedList.append(range(startSeedList,startSeedList+rangeSeedList))



    def createMap(self, lines: list()) -> list():
        
        mapList = list() 

        for line in lines:
            
            lineDict = {}

            lineArr = line.strip()
            lineArr = lineArr.split(" ")
            
            if line == "":
                break

            lineArr = [l for l in lineArr if l != ""]

            lineDict["dest"]  = int(lineArr[0])
            lineDict["src"]   = int(lineArr[1])
            lineDict["range"] = int(lineArr[2])

            mapList.append(lineDict)

        return mapList

    def findMinTraversal(self) -> int:

        minTraversal = self.traverseMaps( [*self.seedList[0]][0] )

        print(self.seedList)
        for ridx, seedRange in enumerate(self.seedList):

            print(f" Computing seedRange = {seedRange}")
            for idx,seed in enumerate(seedRange):
                print(f"SeedRange: {ridx}/{len(self.seedList)}: Percent Completion: {float(idx)/float(len(seedRange))}")
                tmp = self.traverseMaps( seed )

                if tmp < minTraversal:
                    minTraversal = tmp


        return minTraversal

    def traverseMaps(self, seed: int) -> int:

        nextDestination = seed

        nextDestination = self.traverseMap(nextDestination,self.seed_to_soil           ) 
        nextDestination = self.traverseMap(nextDestination,self.soil_to_fertilizer     ) 
        nextDestination = self.traverseMap(nextDestination,self.fertilizer_to_water    ) 
        nextDestination = self.traverseMap(nextDestination,self.water_to_light         ) 
        nextDestination = self.traverseMap(nextDestination,self.light_to_temperature   ) 
        nextDestination = self.traverseMap(nextDestination,self.temperature_to_humidity) 
        nextDestination = self.traverseMap(nextDestination,self.humidity_to_location   ) 
        
        return nextDestination 
    
    def traverseMap(self, seed: int, map: list() ) -> int:

        # Iterate over the maps
        for m in map:

            # If our seed lies in the source range of one of our maps.
            if ( m["src"] + m["range"] - 1 ) >= seed and ( seed >= m["src"] ):
                # Compute the seed's position relative to the map source start.
                seedPos = seed - m["src"]

                # Then compute its corresponding position relative to the map destination start.
                destPos = m["dest"] + seedPos

                return destPos
                 
        
        return seed

if __name__ == "__main__":

    a = Almanac("puzzle_input.txt")

    print(a.findMinTraversal())
