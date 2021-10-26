pistol = "GLOCK17"
cartridge = "9x19mm"
roundtype = "Single"
velocity = 30
building = "Soleil"
building_height = 288
gravity = 9.81
import math
time = math.sqrt((2 * building_height) / gravity)
distance = (velocity * time)
print(f"The gun selected was {pistol}, the cartidge used is {cartridge}, the round type is {roundtype}, and the velocity is {velocity}. The building chosen is {building}and it is {building_height} feet.")