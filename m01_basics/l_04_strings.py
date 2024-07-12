from pprint import pprint

device1_str = " r3-L-n7, cisco, catalyst 2960, ios "

# SPLIT
print("STRING:- SPLIT, STRIP, REPLACE")
device1 = device1_str.split(',')
print("Device using split:")
print("     ", device1)

# STRIP
device1 = device1_str.strip().split(',')
print("Device using strip and split:")
print("     ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("Device replaced blanks using split:\n    ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("Device replaced blanks, comma to colon:")
print("     ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(','):
    device1.append(item.strip())
print("Device using loop and split")
print("     ", device1)

# LIST COMPREHENSIONS
device1 = [item.strip() for item in device1_str.split(',')]
print("Device1 using list comprehension:")
print("     ", device1)
