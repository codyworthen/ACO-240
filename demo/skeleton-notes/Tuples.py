# tuple -- ordered and unchangeable, allows duplicate members

address = ("4701 W Thunderbird Rd", "Glendale", "AZ", "85306")
phone = ("602-543-5628", "work")

# using indexing of the phone variable, return the phone number as a string
print(str(phone[0]), "\n")

# Determine whether the address is in Arizona ("AZ") using sequence membership testing
print("AZ" in address, "\n")

# In what position of address does "AZ" appear? Use the index method.
print(address.index("AZ"), "\n")

# Using slicing of the address variable, return the zip code as a string
print(str(address[3]), "\n")

# Unpack the phone variable by binding 2 variables: phone_number and phone_type
(phone_number, phone_type) = phone
print("phone_number: " + str(phone_number))
print("phone_type: " + str(phone_type), "\n")

# Bind the variable scores to a tuple of scores. Find the maximum score in the tuple
scores = [75, 80, 93, 100, 65, 33]
max = scores[0]
for score in scores :
  if score > max:
    max = score
print("max score =", str(max), "\n")

# How many scores are in the scores variable?
print(len(scores))