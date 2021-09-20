# print("Hello World")
# print("What is your name?:")
# myName = input()
# print("It is good to meet you", myName)
# print("What is your age?:")
# myAge = input()
# print("You will be " + str(int(myAge) + 5) + " in 5 years")
print("Perimeter of a rectangle Calculator")
print("""
---------------------------
l                         l
l                         l
l                         l
---------------------------
""")
length = int(input("What is the length of the rectangle?:"))
width = int(input("What is the witdh of the rectangle?:"))
print("The perimeter of the rectangle is: ", 2 * length + 2 * width)

print()
def Perimeterofrectangle(length, width):
    print(f"Perimeter of the rectangle is {int(2) * int(length) + int(2) * int(width)}")
print("Length is 5 cm")
print("Width is 10 cm")
Perimeterofrectangle(5, 10)
