from pprint import pprint

# Dictionary containing device information
device = {"name": "nox-9k", "vendor": "cisco", "os": "nex-9000", "ip": "10.1.1.1"}

print("\n_______ SIMPLE PRINT ___________")
# Simple print of the entire dictionary
print(device)
# Print the value associated with the "name" key
print("Device name: ", device["name"])

print("\n__________ PPRINT _____________")
# Pretty-print the dictionary for easier readability
pprint(device)

print("\n__________ F-STRING ___________")
# Loop through each key-value pair in the dictionary and print them with formatted output
for key, value in device.items():
    print(f"{key:>16s} : {value}")
