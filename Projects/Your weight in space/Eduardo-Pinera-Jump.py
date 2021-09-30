planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]
print("Jumping on other planets")
myJump = float(input("What is your jump's length (meters)? "))
myPlanet = input(f"Select a planet from the list: {planets} ")
print(("Your jump length on Earth is: ") + str(myJump))
planet_index = planets.index(myPlanet)
print(f"The length of your jump in {planets[planet_index]} is {((myJump) * (rel_gravity[planet_index]))} meters ")