#Exercise 3
import re

#Use list from question
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Loop program to print any value less than 10 & print it
for num in a:
  if num < 5:
    print(num)

#Exercise 2 Extra 
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Instantiate new empty list
newList = []
#Tweak for-loop a bit to take output and put into new list
for num in a:
  if num < 5:
    newList.append(num)
#Print new list
print(newList)

#Trying to condense
#print statement
#brackets make a new array out of the condition
#From practicepython:
#A list comprehension behaves like this: [output] for [item] in [list] if [filter]
# and since its encompassed by [] it creates a new array then prints the new list out.
print([num for num in a if num < 5])

#Another extra: Ask the user for a number and return a list that contains only elements from the original list that are smaller than the given number.
#This one also just requires a little tweaking
userNum = int(input("Enter a number to check: "))
print([num for num in a if num < userNum])
