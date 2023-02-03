from math import sqrt

pennies = 567
# '%' operator can be used as a string formatter or as the modulos operator
print("$%d.%d" % (pennies // 100, pennies % 100)) 

r = sqrt(2.0)
print(r * r) # 2.000000000004

EPSILON = 1E-14
if abs(r * r - 2.0) < EPSILON :
  print("sqrt(2.0) squared is approx. 2.0")

# sum of range
print(sum(range(1, 11))) # excludes 11

# the following 2 functions are equivalent
def count_evens(numbers) :
  count = 0
  for number in numbers :
    if (number % 2 == 0) :
      count += 1

def count_evens2(numbers) :
  return len([n for n in numbers if n % 2 == 0]) # list comprehension

print(count_evens2([1, 2, 3, 4, 5])) # 2 numbers are even