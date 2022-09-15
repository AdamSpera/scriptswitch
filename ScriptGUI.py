from netmiko import ConnectHandler
from pprint import pprint
import inquirer
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
            choices=["Send another script", "Exit the program"],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["restartChoice"] == "Send another script":
        optionsMenu()
    if answers["restartChoice"] == "Exit the program":
        sys.exit("Goodbye! Thanks for using ScriptSwitch!")


def optionsMenu():
    questions = [
        inquirer.List(
            "initialChoice",
            message="Would you like to select a script or create a new one?",
            choices=["Create a new script", "Use a template script"],
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers["initialChoice"] == "Create a new script":
        customCommand = input("Enter script commands: ")
        print("# SWITCH OUTPUT BELOW \/ ----------------------------------")
        print(net_connect.send_command(customCommand))
        print("\n# SWITCH OUTPUT ABOVE /\\ ----------------------------------\n")
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
        print(net_connect.send_command(answers["templateChoice"]))
        print("\n# SWITCH OUTPUT ABOVE /\\ ----------------------------------\n")
        restartOption()


optionsMenu()
