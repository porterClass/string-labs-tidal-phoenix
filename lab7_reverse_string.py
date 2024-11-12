"""

7. Reverse String
Write a function reverse_string() that takes a string as a parameter and returns the string reversed.

reverse_string("hello")  # returns "olleh"
reverse_string("world")  # returns "dlrow"
reverse_string("Python")  # returns "nohtyP"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def reverse_string(x):
  a = 1
  s = ""
  for current_letter in x:
    current_letter = int((len(x)) - (1 * a))
    s = s + x[current_letter]
    a += 1
  return s



  
















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string to reverse: \n")
  print(reverse_string(x))