# The losing battle! 
# This demonstrates the dreaded infinite loop!

print("Your lone hero is surrounded by a massive Army of Trolls, Orcs and Goblins.")
print("The battlefild is filled with the decaying green bodies of the enemy, the gound running green with blood")
print("The hero unsheaths his sword one last time for what he doesnt know, will be the final battle of his life.")

health = 10
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health -= damage

print("Your hero swings and slays an evil troll, " "but takes ", damage, "damage points. \n")

print("Your hero fought valiantley and bravely and defeated", trolls ,"trolls.")
print("But alas, your hero is no more.")

input("\n\nPress Enter to continue")

