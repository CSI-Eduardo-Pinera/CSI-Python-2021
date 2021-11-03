import math
from ExperimentalData import ExperimentalData
# pistol = "GLOCK17"
# caliber = "9x19mm"
# ammunition = "QuakeMaker"
# velocity = 290
# building = "Soleil"
# building_height = 288
# gravity = 9.81
def projectileFunction(experimentalData: ExperimentalData):
    time = math.sqrt((2 * building_height) / gravity)
    # distance = (experimentalData[velocity] * gravity)
    distance = (velocity * gravity)
    print(f"The gun selected was {pistol}, the caliber used is {caliber}, the ammunition type is {ammunition}, and the velocity is {velocity}. The building chosen is {building} and it is {building_height} feet.")

# experimentalData = {
 
#  "pistol" : "GLOCK17",
#  "caliber" : "9x19mm",
#  "ammunition" : "QuakeMaker",
#  "velocity" : 290,
#  "building" : "Soleil",
#  "building_height" : 288,
#  "gravity" : 9.81

# }
experimentalData = ExperimentalData("GLOCK17", "9x19mm", "QuakeMaker", 290, "Soleil", 288, 9.81)
projectileFunction(experimentalData)