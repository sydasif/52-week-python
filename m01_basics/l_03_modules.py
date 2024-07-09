from tabulate import tabulate
from util.create_util import create_devices

if __name__ == "__main__":
    devices = create_devices(num_devices=10, num_subnets=1)
    print(tabulate(devices, headers="keys"))
