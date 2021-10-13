#Exercise 1

from datetime import date

#Create an instance of the date
today = date.today()
#Ask the user their name, and store it in a variable called 'name'.
name = input("What is your name?\n")
#Ask the user for their age, and store it in a variable called 'age'.
age = int(input("What is your age?\n"))
#Calculate the year it will be when the user turns 100.
finalYear = (today.year + (100-age))
#Print final calculation
print(f"You will be 100 when it is the year {finalYear}")

#Exercise 1 Part 2

toLoop = int(input("Enter the amount of times you want your message to be repeated:"))
for i in range(toLoop):
    print(f"You will be 100 when it is the year {finalYear}\n")
   
