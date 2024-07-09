from pprint import pprint

device = {"name": "nox-9k", "vendor": "cisco", "os": "nex-9000", "ip": "10.1.1.1"}

print("\n_______ SIMPLE PRINT ___________")
print(device)
print("Device name: ", device["name"])

print("\n__________ PPRINT _____________")
pprint(device)

print("\n__________ F-STRING ___________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
