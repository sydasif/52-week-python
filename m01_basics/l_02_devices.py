from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

# Create an empty list to hold device dictionaries
devices = list()

# Loop to create 9 devices
for index in range(1, 10):
    device = dict()  # Create an empty dictionary for each device

    # Generate a random name for the device
    device["name"] = (
            choice(["r2", "r3", "r4", "r6", "r10"]) +
            choice(["L", "U"]) +
            choice(string.ascii_letters)
    )

    # Assign a random vendor
    device["vendor"] = choice(["cisco", "juniper", "arista"])

    # Assign an OS and version based on the vendor
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07x", "8.2(S).01", "20.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23", "8.4J", "6.4", "6.03"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.94.14", "3.14"])

    # Assign a unique IP address based on the index
    device["ip"] = "10.0.0." + str(index)

    # Print each key-value pair of the device dictionary
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # Add the device dictionary to the list
    devices.append(device)

# Use pprint to print the list of device dictionaries as-is
print("\n ------ DEVICES AS LIST OF DICTS -------")
pprint(devices)

# Sort the devices by vendor, os, and version, and print them in a table format
print("\n------- SORTED DEVICES IN TABULAR FORMATE --------------")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))
