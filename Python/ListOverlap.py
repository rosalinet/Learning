#Exercise 5: List Overlap\
#Two given lists by the question
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes

#Print statement to find the similarities
print(list(set(a)&set(b)))

#Extra: Generate two random lists
import random as rand
#Making this a function to run it twice easier
def generate_random_list():
  newList = []
  for i in range(rand.randint(1,10)):
    newList.append(rand.randint(1,20))
  return newList

#Making a function to return a list of the similar values.
def compare_lists(list1, list2):
  return list(set(list1)&set(list2))


print(compare_lists(a,b))
#Making a main to practice list comprehension and method creation.
def main():
  print("Generating random lists")
  list1 = generate_random_list()
  list2 = generate_random_list()
  print(list1)
  print(list2)
  print(list(set(list1)&set(list2)))


main()
