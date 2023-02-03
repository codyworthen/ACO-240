# tuple -- ordered and unchangeable, allows duplicate members

address = ("4701 W Thunderbird Rd", "Glendale", "AZ", "85306")
phone = ("602-543-5628", "work")

# 1) using indexing of the phone variable, return the phone number as a string
print("1) ", str(phone[0]))

# 2) etermine whether the address is in Arizona ("AZ") using sequence membership testing
print("2) ", "AZ" in address)

# 3) in what position of address does "AZ" appear? Use the index method.
print("3) ", address.index("AZ"))

# 4) using slicing of the address variable, return the zip code as a string
print("4) ", str(address[3]))

# 5) unpack the phone variable by binding 2 variables: phone_number and phone_type
(phone_number, phone_type) = phone
print("5) ", "phone_number: " + str(phone_number))
print("5) ", "phone_type: " + str(phone_type))

# 6) bind the variable scores to a tuple of scores. Find the maximum score in the tuple
scores = [75, 80, 93, 100, 65, 33]
max = scores[0]
for score in scores :
  if score > max:
    max = score
print("6) ", "max score =", str(max))

# 7) how many scores are in the scores variable?
print("7) ", len(scores))