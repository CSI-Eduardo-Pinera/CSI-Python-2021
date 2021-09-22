print("Welcome to Cangrejeros de Santurce - BSN 2021")
print("The cost of each seat is as follow: Court Side = $183, Nivel Principal = $35, Club Seat = $45")
Court_Side = int(input("How many tickets for Court Side "))
Nivel_Principal = int(input("How many tickets for Nivel Principal "))
Club_Seat = int(input("How many tickets for Club Seat "))
def SectionSales(Court_Side, Nivel_Principal, Club_Seat):
    print(f"The cost for Court Side is : {int(Court_Side) * 183}")
    print(f"The cost for Nivel Principal is : {int(Nivel_Principal) * 35}")
    print(f"The cost for Club Seat is : {int(Club_Seat) * 45}")
print()
SectionSales(Court_Side, Nivel_Principal, Club_Seat)
Sales_CS = Court_Side * 183
Sales_NL = Nivel_Principal * 35
Sales_CS2 = Club_Seat * 45
def TicketsTotals(Sales_CS, Sales_NL, Sales_CS2):
    print(f"The total of tickets sales is: $ {int(Sales_CS) + int(Sales_NL) + int(Sales_CS2)}")
print()
TicketsTotals(Sales_CS, Sales_NL, Sales_CS2)