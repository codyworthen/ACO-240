# A mapping of an arbitrary collection of objects indexed by values called keys, mutable and unordered

aStates = {
    "AZ": "Arizona",
    "AL": "Alabama",
    "AK": "Alaska",
    "AR": "Arkansas"
}

# 1) determine the number of key,value pairs in the dictionary
print("1) ", len(aStates))

# 2) write an expression to find Alaska's abbreviation from the states dictionary
key = list(filter(lambda value: aStates[value] == 'Alaska', aStates))
print("2) ", key[0])

# 3) write an expression that returns a sorted list of the 2-char state abbreviations in astates
sorted = sorted(aStates)
print(sorted)

# 4) write an expression that returns a list of (key, value) tuples from astates sorted by key
tuples = aStates.items()
print(tuples)