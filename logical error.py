# This code demonstrates a logical error. Logical Errors can be the toughest to fix as the program doesnt crash!

print(
    """
            Trust Fund Buddy
    Totals your monthly spending so that your fund doesnt run out. 

    Please enter the requested, monthly costs. Since you are loaded, ignore pennies and just use £ amounts. 
    
    """
)

car = input("Tesla Tune-Ups: ")
rent = input("London Penthouse: ")
maid = input("Maid cost: " )
food = input("Salt Bae dining: " )
staff = input("Staff: ")
guru = input("Self Help Guru: ")
games = input("Video Games: ")

total = car + rent + maid + food + staff + guru + games

print("\nGrand Monthly Total:", total)

input("\n\nPress the enter key to exit.")