#Exercise 4: Divisors
#Take in user input for a number they want to find the divisors of. 
userNum = int(input("Enter a number you'd like to find the divisors of: "))
#Create a list of numbers between 1 and the user-given number
x = range(1, userNum)
#print a list of the numbers in x that are divisors of the user's number.
#They are divisors if the userNumber can be divided by that number with NO REMAINDER
print([num for num in x if (userNum%num == 0)])
