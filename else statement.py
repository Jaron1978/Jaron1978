# Access or Denied. 
# We are not implementing the else clause. If the password is wrong, the user is denied access. 

name = "Ron"

print("Welcome to System Security Inc")
print("--Security is our middle name\n")

password = input("Enter your password: ")

if password == "secret":
    print("Access Granted")
    print("Welcome", name, "You must be very improtant"
    )
else:
    print("Access Denied")

input("\n\nPress the Enter Key to exit")

# If the condition is true (correct password) the first code block runs. 
# If the condition is false (incorrect password) the second code block runs. 