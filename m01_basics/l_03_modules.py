from tabulate import tabulate
from util.create_util import create_devices  # Import the create_devices function from the create_util module

if __name__ == "__main__":
    # Create a list of devices with the specified number of devices and subnets
    devices = create_devices(num_devices=10, num_subnets=1)

    # Print the list of devices in a tabular format
    print(tabulate(devices, headers="keys"))
