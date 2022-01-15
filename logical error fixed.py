# This code demonstrates a logical error. Logical Errors can be the toughest to fix as the program doesnt crash!
# This is the logical error with the Fix. Nesting the int and input in the same line. 
# float eg 10.0, int eg 10, str is string. 

print(
    """
            Trust Fund Buddy
    Totals your monthly spending so that your fund doesnt run out. 

    Please enter the requested, monthly costs. Since you are loaded, ignore pennies and just use £ amounts. 
    
    """
)

car = int(input("Tesla Tune-Ups: "))
rent = int(input("London Penthouse: "))
maid = int(input("Maid cost: " ))
food = int(input("Salt Bae dining: " ))
staff = int(input("Staff: "))
guru = int(input("Self Help Guru: "))
games = int(input("Video Games: "))

# food = food * 52 is the same as food *= 52

total = car + rent + maid + food + staff + guru + games

print("\nGrand Monthly Total:", total)

input("\n\nPress the enter key to exit.")