import math
# pistol = "GLOCK17"
# caliber = "9x19mm"
# ammunition = "QuakeMaker"
# velocity = 290
# building = "Soleil"
# building_height = 288
# gravity = 9.81
def projectileFunction(pistol:str, caliber:str, ammunition:str, velocity:int, building:str, building_height:int, gravity:int):
    time = math.sqrt((2 * building_height) / gravity)
    distance = (velocity * gravity)
    print(f"The gun selected was {pistol}, the caliber used is {caliber}, the ammunition type is {ammunition}, and the velocity is {velocity}. The building chosen is {building} and it is {building_height} feet.")
projectileFunction("GLOCK17", "9x19mm", "QuakeMaker", 290, "Soleil", 288, 9.81)
