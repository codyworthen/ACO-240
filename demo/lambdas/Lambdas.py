employees = [('1', 'Satoshi', 'Nakamoto', 45), ('2', 'Hal', 'Finney', 60)]

employees.sort()  # by default, sorts by employee[0]
print(employees)

employees.sort(key=lambda employee: employee[1])
print(employees)

# returns a new sorted list
new_sorted_list = sorted(employees, key = lambda employee: employee[1])
print(new_sorted_list)