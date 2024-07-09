from random import choice
import string
from tabulate import tabulate


def create_devices(num_devices=1, num_subnets=1):
    # CREATE A LIST OF DEVICES
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets.")
        return created_devices

    for subnet_index in range(1, num_subnets + 1):
        for device_index in range(1, num_devices + 1):

            device = dict()

            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r10"])
                    + choice(["L", "U"])
                    + choice(string.ascii_letters)
            )

            device["vendor"] = choice(["cisco", "juniper", "arista"])

            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(
                    ["12.1(T).04", "14.07x", "8.2(S).01", "20.45"]
                )
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["J6.23", "8.4J", "6.4", "6.03"])
            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(["2.45", "2.55", "2.94.14", "3.14"])

            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)
        return created_devices


if __name__ == "__main__":
    devices = create_devices(num_devices=10, num_subnets=1)
    print(tabulate(devices, headers="keys"))
