# sets - a mutable collection of unique values, which must be immutable; unordered and thus, not accessible by position

primes_under10 = {2, 3, 5, 7}
my_classes = {"ACO 240", "ACO 350", "ACO 361", "ACO 430"}
rainbow_colors = { "red", "orange", "yellow", "green", "blue", "indigo", "violet"}
aco_majors = {1, 2, 3, 4}
mat_majors = {2, 4, 6}

# 1) write an expression to sort the colors of the rainbow alphabetically
new_set = sorted(rainbow_colors)
print("1) ", new_set)

# 2) update aco_majors to include student 5
aco_majors.add(5)
print("2) ", aco_majors)

# 3) write an expression to find the students who are double majoring in aco and mat
aco_and_mat_majors_intersection = aco_majors.intersection(mat_majors)
print("3) ", aco_and_mat_majors_intersection)

# 4) Write an expression to find mat majors who are NOT double majoring in aco
mat_only_majors = mat_majors.difference(aco_majors)
print("4) ", mat_only_majors)

# 5) Write an expression to find all students who are majoring in aco or mat 
aco_and_mat_majors_union = aco_majors.union(mat_majors)
print("5) ", aco_and_mat_majors_union)

# 6) Determine the size of the set of prime numbers under 10
size = len(primes_under10)
print("6) ", str(size))