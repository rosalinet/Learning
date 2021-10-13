#Exercise 2

#Ask the user for a number, and save it as a variable "num"
num = int(input("Enter a number: "))
#if statement to compare the remainder/modulo and print the result
#(If the remainder is 0, the number is even, if it is 1, it is an odd number)
if num%2 == 0:
  print("This number is even.")
else:
  print("This number is odd.")

#Exercise 2 Extra
#Calculate modulo with 4 and print it as well
if num%4 == 0:
    print("This number is also a multiple of 4!")

#Exercise 2 Extra pt 2
#Take two integers to be calculated
numExtra = int(input("Enter a number to check: "))
numCheck = int(input("Enter a number to divide it by: "))
#if statement to check if the numExtra can be divided by numCheck and prints off the corresponding message
if numExtra%numCheck == 0:
    print(f"{numExtra} divides evenly into {numCheck}!")
else:
    print(f"{numExtra} DOES NOT divides evenly into {numCheck}.")

