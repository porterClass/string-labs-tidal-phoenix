"""

6. Count Vowels
Write a function count_vowels() that takes a string as a parameter and returns the number of vowels (a, e, i, o, u) in the string.

count_vowels("hello")  # returns 2
count_vowels("world")  # returns 1
count_vowels("Python")  # returns 1
"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def count_vowels(x):
  count = 0
  for current_letter in x:
    if current_letter == "a":
      count += 1
    elif current_letter == "e":
      count += 1
    elif current_letter == "i":
      count += 1
    elif current_letter == "o":
      count += 1
    elif current_letter == "u":
      count += 1
  return count















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string to count the vowels of: \n")
  print(count_vowels(x))