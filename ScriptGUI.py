from netmiko import ConnectHandler
import inquirer
import json
import sys

print("Welcome to ScriptSwitch!\nSwitch the way you script.\n")

ipOfSwitch = input("Enter target switch ip address: ")
usernameOfSwitch = input("Enter target switch username: ")
passwordOfSwitch = input("Enter target switch password: ")
secretPasswordOfSwitch = input(
    "Enter target switch secret password (enable & configure terminal): ")

print("\nConnecting to switch...")

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   ipOfSwitch,
    'username': usernameOfSwitch,
    'password': passwordOfSwitch,
    "secret": secretPasswordOfSwitch,
}
net_connect = ConnectHandler(**cisco_881)
net_connect.enable()
print("Connection established!\n")


def restartOption():
    questions = [
        inquirer.List(
            "restartChoice",
            message="Script deployed successfully. Would you like to send another script?",
            choices=["Script more!", "Exit the program."],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["restartChoice"] == "Script more!":
        optionsMenu()
    if answers["restartChoice"] == "Exit the program.":
        sys.exit("Goodbye! Thanks for using ScriptSwitch!")


def optionsMenu():
    questions = [
        inquirer.List(
            "initialChoice",
            message="Would you like to select a script , create a new one, or configure an interface?",
            choices=["Create a new script",
                     "Use a template script", "Configure an interface"],
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers["initialChoice"] == "Create a new script":
        customCommand = input("Enter script commands: ")
        print("# SWITCH OUTPUT BELOW \/ ----------------------------------")
        output = net_connect.send_command(customCommand)
        print(output)
        print("\n# SWITCH OUTPUT ABOVE /\\ ----------------------------------\n")

        with open('Output.txt', 'w') as f:
            f.write(output)

        restartOption()

    if answers["initialChoice"] == "Configure an interface":
        output = net_connect.send_command(
            "show ip interface brief", use_textfsm=True)

        optionsList = []
        for i in output:
            optionsList.append(i["intf"])

        questions = [
            inquirer.List(
                "templateChoice",
                message="Select an interface to configure",
                choices=optionsList,
            ),
        ]
        interfaceAnswer = inquirer.prompt(questions)

        questions = [
            inquirer.List(
                "templateChoice",
                message="Select a configuration action for the interface",
                choices=["Set as access port", "Set IP address", "Set no IP address",
                         "Set port shutdown", "Set port no shutdown"],
            ),
        ]
        configureAnswer = inquirer.prompt(questions)

        if (configureAnswer["templateChoice"] == "Set as access port"):
            vlanNumber = input("Enter VLAN number: ")
            net_connect.config_mode()
            net_connect.send_config_set(
                ["interface " + interfaceAnswer["templateChoice"], "switchport mode access", "switchport access vlan " + vlanNumber, "exit"])
            print("# Successful configuration! #\n")
            restartOption()

        if (configureAnswer["templateChoice"] == "Set IP address"):
            ipNumber = input("Enter IP address: ")
            subnetNumber = input("Enter subnet: ")
            net_connect.config_mode()
            net_connect.send_config_set(
                ["interface " + interfaceAnswer["templateChoice"], "ip address " + ipNumber + "" + subnetNumber, "exit"])
            print("# Successful configuration! #\n")
            restartOption()

        if (configureAnswer["templateChoice"] == "Set no IP address"):
            net_connect.config_mode()
            net_connect.send_config_set(
                ["interface " + interfaceAnswer["templateChoice"], "no ip address", "exit"])
            print("# Successful configuration! #\n")
            restartOption()

        if (configureAnswer["templateChoice"] == "Set port shutdown"):
            net_connect.config_mode()
            net_connect.send_config_set(
                ["interface " + interfaceAnswer["templateChoice"], "shutdown", "exit"])
            print("# Successful configuration! #\n")
            restartOption()

        if (configureAnswer["templateChoice"] == "Set port no shutdown"):
            net_connect.config_mode()
            net_connect.send_config_set(
                ["interface " + interfaceAnswer["templateChoice"], "shutdown", "exit"])
            print("# Successful configuration! #\n")
            restartOption()

        restartOption()

    if answers["initialChoice"] == "Use a template script":
        questions = [
            inquirer.List(
                "templateChoice",
                message="Select a template script to use",
                choices=["copy running-config startup-config", "show cdp neighbors", "show interface status", "show interface summary",
                         "show interfaces switchport", "show ip interface", "show ip dhcp client interface", "show mac address-table", "show running-config"],
            ),
        ]
        answers = inquirer.prompt(questions)

        print("# SWITCH OUTPUT BELOW \/ ----------------------------------")
        output = net_connect.send_command(answers["templateChoice"])
        print(output)
        print("\n# SWITCH OUTPUT ABOVE /\\ ----------------------------------\n")

        restartOption()


optionsMenu()
