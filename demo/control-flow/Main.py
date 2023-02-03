# if-else
print("Enter an integer: 5")
number = 5
if (number % 2 == 0):
  print(str(number) + " is even")
else:
  print(str(number) + " is odd")

# like a tertiary
print(str(number) +
      " is even") if number % 2 == 0 else print(str(number) + " is odd")

# while loop
print("\nwhile loop:")
x = 0
while x < 3:
  x += 1
  print("x = " + str(x))

# do while loop
x = 0
print("\ndo while loop:")
while True:
  print("x = " + str(x))
  x += 1
  if (x >= 3):
    break

# for loop
colors = ["red", "white", "blue"]
print('\nfor loop:')
for color in colors:  # grabs elements
  print(str(color), end=", ")  # prevents new line

# for loop in range
print("\n\nfor loop (in range):")
for i in range(len(colors)):  # grabs numbers, iterates once for each element in colors
  print(colors[i], end=", ")  # prevents new line

# for loop in range
print("\n\nfor loop (in range): ")
for i in range(3):  # iterates 3 times (i goes from 0 to 2)
  print(i)

# sum of first (n) even integers
n = int(input("\nsum of the first (n) even integers: "))
sum = 0;
for i in range(1, n + 1) :
   sum = sum + i * 2

print("sum = " + str(sum))