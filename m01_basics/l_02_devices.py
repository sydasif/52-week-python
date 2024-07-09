from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()  # CREATE EMPTY LIST

for index in range(1, 10):

    device = dict()

    device["name"] = (
            choice(["r2", "r3", "r4", "r6", "r10"])
            + choice(["L", "U"])
            + choice(string.ascii_letters)
    )

    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07x", "8.2(S).01", "20.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23", "8.4J", "6.4", "6.03"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.94.14", "3.14"])
    device["ip"] = "10.0.0." + str(index)

    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    devices.append(device)

# USE PPRINT TO PRINT DATA AS-IS
print("\n ------ DEVICES AS LIST OF DICTS -------")
pprint(devices)

print("\n------- SORTED DEVICES IN TABULAR FORMATE --------------")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))
