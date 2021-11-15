import math
import os
from ExperimentalData import ExperimentalData
from pathlib import Path
import json

#  pistol = "GLOCK17"
# caliber = "9x19mm"
# ammunition = "QuakeMaker"
# velocity = 290
# building = "Soleil"
# building_height = 288
# gravity = 9.81

# Convert your variable into parameters
def projectileFunction(experimentalData: ExperimentalData):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
    planet = planets.index(experimentalData.planet)
    time = math.sqrt((2 * experimentalData.building_height) / g_ms2[planet])
    
    # distance = (experimentalData[velocity] * time)
    distance = (experimentalData.velocity * time)
 
    print(f"The gun selected was {experimentalData.pistol}, the caliber used is {experimentalData.caliber}, the ammunition type is {experimentalData.ammunition}, and the velocity is {experimentalData.velocity}. The building chosen is {experimentalData.building} and it is {experimentalData.building_height} feet. The planet is {experimentalData.planet} and the gravity is {experimentalData.g_ms2}. The projectile will travel {distance} ft in {time} seconds.")

# Convert your script parameters into a single JSON Object

# experimentalData = {
#  "pistol" : "GLOCK17",
#  "caliber" : "9x19mm",
#  "ammunition" : "QuakeMaker",
#  "velocity" : 290
#  "building" : "Soleil",
#  "building_height" : 288,
#  "gravity" : 9.81
# }
# experimentalData = ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Soleil", 288, 9.81)

myDataset = [
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Soleil", 288, 3.7, "Mercury"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Caribbean Sea View", 334, 8.87, "Venus"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Aquablue 2", 278, 9.81, "Earth"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Aquablue 1", 278, 3.711, "Mars"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Coliseum Tower Residences", 259, 24.79, "Jupiter"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Nacional Plaza", 238, 10.44, "Saturn"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Oriental Plaza", 210, 8.69, "Uranus"),
ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Torre Norte", 243, 11.15, "Neptune")
]

for data in myDataset:
    print("\n-----------------------------------------\n")
    projectileFunction(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Projectile-Motion.json")

print(myOutputFilePath)

with open(myOutputPath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)
    
deserialize = open(myOutputFilePath)
experimentJSON = json.load(deserialize)
for e in experimentJSON:
    print("\n------------------------------------\n")
    projectileFunction(ExperimentalData(**e))
    
# projectileFunction(experimentalData)