from random import choice
import string


def create_devices(num_devices=1, num_subnets=1):
    """
    Create a list of devices with random attributes.

    Parameters:
    num_devices (int): Number of devices to create in each subnet.
    num_subnets (int): Number of subnets to create.

    Returns:
    list: A list of dictionaries, each representing a device.
    """
    # Create an empty list to hold the created devices
    created_devices = list()

    # Check if the number of devices or subnets exceeds the allowable limit
    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets.")
        return created_devices

    # Loop through each subnet
    for subnet_index in range(1, num_subnets + 1):
        # Loop through each device in the subnet
        for device_index in range(1, num_devices + 1):
            # Create a dictionary for each device
            device = dict()

            # Generate a random name for the device
            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r10"]) +
                    choice(["L", "U"]) +
                    choice(string.ascii_letters)
            )

            # Assign a random vendor to the device
            device["vendor"] = choice(["cisco", "juniper", "arista"])

            # Assign OS and version based on the vendor
            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07x", "8.2(S).01", "20.45"])
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["J6.23", "8.4J", "6.4", "6.03"])
            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(["2.45", "2.55", "2.94.14", "3.14"])

            # Assign a unique IP address based on the subnet and device index
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            # Add the device dictionary to the list of created devices
            created_devices.append(device)

    return created_devices
