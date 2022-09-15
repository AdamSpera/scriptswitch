from netmiko import ConnectHandler
from datetime import datetime

# ENTER SWITCH IP ADDRESS BELOW
ipOfSwitch = ''
# ENTER SWITCH USERNAME BELOW
usernameOfSwitch = ''
# ENTER SWITCH PASSWORD BELOW
passwordOfSwitch = ''

# ENTER NAME OF FILE TO SAVE OUTPUT TO
# LEAVE EMPTY TO NOT SAVE OUTPUT
nameOfFile = ''

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   ipOfSwitch,
    'username': usernameOfSwitch,
    'password': passwordOfSwitch
}

net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_command('show int summary')

print(output) 

if (nameOfFile == ''):
    print('\n# No file name entered, no output file saved.')
else:
    with open(nameOfFile + '.txt', 'w') as f:
        f.write(output)

