# Demonstration of the while loop. 

print("\tThis is an example of a while loop\n")
print("This program simulates continuous questions until the response Because is entered.")

response = "Why"
while response != "Because.":
    response = input("Why\n")

print("Oh. Okay!!")

# In this instance you will be contstantly ask "why" until you answer with Because. 
# because will not work, and neither will Because. It has to be Because as per line 7. 
# while loops are often controlled by the sentry variable. In this instance, the sentry variable is response.I 