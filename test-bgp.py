from genie.testbed import load
from genie.utils import Dq
import os
import colorama
from colorama import Fore, Style
from tabulate import tabulate
import itertools as it

clear_commands = "clear"
testbed = load('testbed.yaml')
pass_list = []
fail_list = []
headers = ["PASSED", "FAILED"]
for i in range(1,8):
    device = testbed.devices['R' + str(i)]
    device.connect()
    output = device.parse('show ip bgp neighbors')
    tester = (Dq(output).contains('Established').get_values('neighbor'))
    if len(tester) == 6:
        pass_list.append(str(device))
        print("*" * 50)
        print(Fore.GREEN + str(device) + " HAS PASSED" + Style.RESET_ALL)
        print("*" * 50)
    else:
        fail_list.append(str(device))
        print("*" * 50)
        print(Fore.RED + str(device) + " HAS FAILED" + Style.RESET_ALL)
        print("*" * 50)
table = it.zip_longest(pass_list, fail_list)
os.system(clear_commands)
print(Fore.YELLOW + "*" * 60 + Style.RESET_ALL)
print("\n")
print(tabulate(table, headers=headers, tablefmt="psql"))
print("\n")
print(Fore.YELLOW + "*" * 60 + Style.RESET_ALL)
