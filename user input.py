# Obtains personal information from the user and then
# prints true (but useless) information. 

name = input("Hi. What's your name? ")
age = input("And what's your current age? ")
age = int(age)

weight = float(input("Okay, last question. What do you weigh in Stone and Pounds? "))

input("Press Enter to Exit! ")

# The code in the book weight as pounds only, but I wanted to add Stone and Pounds. 
# To do this, I changed weight = int to weight = float which allows for 16.1 in my case. 