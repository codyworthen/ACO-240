# list -- ordered and changeable, allows duplicate members

from datetime import datetime

aco_core = [
    "ACO 101", "ACO 102", "ACO 201", "ACO 240", "ACO 320", "ACO 330",
    "ACO 350", "MAT 210", "MAT 243", "STP 226"
]

days_of_the_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# 1) sing slicing of the days_of_the_week variable, return a list representing weekdays
print("1) ", days_of_the_week[1:6])

# 2) how many classes are in aco_core?
print("2) ", str(len(aco_core)))

# 3) reverse the order of the list aco_core in place
print("3 before) ", aco_core)
aco_core.reverse()
print("3 after) ", aco_core)

# 4) bind a variable primes_under10 with the prime numbers less than 10
primes = [1, 3, 5, 7]
print("4) ", str(sum(primes)))

# 5) use list concatenation and slicing to define the binding for a variable named weekend that is a list of strings representing the weekend days
weekend = days_of_the_week[0::6]
print("5) ", weekend)

# 6) what is the position of today's day in the days_of_the_week variable?
weekday_as_int = datetime.now().weekday()  # docs are wrong, monday == 1
print("6) ", days_of_the_week[weekday_as_int], "is at index", weekday_as_int)

# 7) list concatenation
firstNames = ["Joe", "Jim", "Betsy", "Shelly"]
lastNames = states = ["Jones", "Patel", "Hicks", "Fisher"]
fullNames = firstNames + lastNames
print("7) ", fullNames)

letters = list("abcdefg")
print(letters)