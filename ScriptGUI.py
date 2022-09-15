from netmiko import ConnectHandler
from pprint import pprint
import inquirer
import json
import sys

print("Welcome to ScriptSwitch!\nSwitch the way you script.\n")

ipOfSwitch = input("Enter target switch ip address: ")
usernameOfSwitch = input("Enter target switch username: ")
passwordOfSwitch = input("Enter target switch password: ")

print("\nConnecting to switch...")

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   ipOfSwitch,
    'username': usernameOfSwitch,
    'password': passwordOfSwitch
}
net_connect = ConnectHandler(**cisco_881)
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
                choices=["Set as trunk port", "Set as access port",
                         "Set IP address", "Set port shutdown", "Set port no shutdown"],
            ),
        ]
        configureAnswer = inquirer.prompt(questions)

        # Add configure port functionality here

        restartOption()

    if answers["initialChoice"] == "Use a template script":
        questions = [
            inquirer.List(
                "templateChoice",
                message="Select a template script to use",
                choices=["copy running-config startup-config", "show cdp neighbors", "show interface status",
                         "show interface summary", "show interfaces switchport", "show mac address-table", "show running-config"],
            ),
        ]
        answers = inquirer.prompt(questions)

        print("# SWITCH OUTPUT BELOW \/ ----------------------------------")
        output = net_connect.send_command(answers["templateChoice"])
        print(output)
        print("\n# SWITCH OUTPUT ABOVE /\\ ----------------------------------\n")

        restartOption()


optionsMenu()
