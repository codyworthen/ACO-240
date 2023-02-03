# accessing a character index
name = "cody"
print("name[0] is " + name[0])

# strings have negative indexes
print("name[-1] is " + name[-1])

# length of a string
print("len(name) is " + str(len(name)))

# convert string to uppercase
upper = name.upper()
print("name.upper() returns " + upper)

# convert string to lower case
lower = upper.lower()
print("name.lower() returns " + lower)

# convert numbers to string with str()
int = 3
print("integer to string " + str(int))

float = 3.14
print("float to string " + str(float))

# index of character
print("name.index('o') returns " + str(name.index("o")))

# replace
name.replace("o", "0")
print("name.replace('o', '0') returns " + name)

# converting chars to their int value
print("the letter c is stored internally as " + str(ord("c")))

# converting int to char representatiom
print("the int 99 represents the character " + chr(99))

# formatting
pi = 3.14159265359
print("price: %.2f" % pi)  # '%' is also the string format operator

my_string = "Hello World"

# find - returns the index where the first substring occurs
print(str(my_string.find("or")))

# string.count()
print(my_string.count("l"))

# substring
print(my_string[0:2])

# string.replace()
print(my_string.replace("l", "1"))

# string.islpha() --> true if tjr string only contains >= 1 letters
# isalnum(), isdigit(), islower(), isupper(), and isspace() also exist
print(my_string.isalpha())

# in operator
# 'not in' operator also exists
bitcoin = "bitcoin"
print("'it' is in bitcoin: " + str(("it" in bitcoin)))

# prevent a new line
print("00", end="")
print(3 + 4)

# multi-line string - each Line X is on it's own line, whitespace is included
multi_line = """ 
  Line 1 
  Line 2
  Line 3
"""
print(multi_line)

# strings are immutable
immutable = "Bitcoin"
print("str: " + str(id(immutable)))
immutable = immutable + " is sound money" # creating a new string object
print("str: " + str(id(immutable)))
# immutable[0] = "x" # TypeError: 'str' object does not support item assignment
