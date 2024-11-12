"""
8. Count Words
Write a function count_words() that takes a string as a parameter and returns the number of words in the string. Words are separated by spaces.

count_words("hello world")  # returns 2
count_words("Python is fun")  # returns 3
count_words("Count the number of words in this sentence.")  # returns 7

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def count_words(x):
  count = 0
  for current_letter in x:
    if current_letter == " ":
      count += 1
  if x == "":
    count = 0
  else:
    count += 1
  return count
    
  
    
  
  
  
  
  

  

















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a sentence to count the words of: \n")
  print(count_words(x))