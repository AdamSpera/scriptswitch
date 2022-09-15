# Script Switch

_Switching up ways to script._

## Introduction

ScriptSwicth is a project developed by Adam Spera at Arcadia University, computer science department as an original independent study capstone. ScriptSwitch is a CLI script injection software for Cisco switches. 

- Connect into Cisco switches securely using SSH
- Select from a variety of template scripts
- Craft custom scripts in the CLI for deployment
- Ease of use through any Anaconda PowerShell terminal
- Save output with formatting to an external file

Utilizing the functionality of NetMiko and ConnectHandler over SSH, ScriptSwitch provides the user a simple and easy platform for script injection and creation. Users are given flexibility to create their own scripts form scratch or use a template script.

## Usage

### Establishing a SSH connection

1. Run the following commands in a configured terminal for ScirptGUI:
```
conda activate cisco
python ScriptGUI.py
```
2. When promted, enter the target switch's IP address (no subnet)
3. When promted, enter the intended user's SSH username
4. When promted, enter the intended user's SSH password
 
5. Select one of the choices:
   - Create a new script
   - use a template Script

### New Script Mode

1. When prompted, input the code to be deployed to the switch
2. The program will display the switch output after the response
3. When confirmation is recieved, select oen of the following options:
   - Send another script
   - Exit the program 

### Template Script Mode

1. When prompted, select any of the presented template scripts to deploy it
2. The program will display the switch output after the response
3. When confirmation is recieved, select oen of the following options:
   - Send another script
   - Exit the program

### Output File

The results are automatically saved to a file in teh root directory named Output.txt

## Installation 

## Contributions

Thank you to everybody who helped create the ScriptSwitch project possible!

Special mention and thanks to the following people:

- Guidance and Mentoring: Vitaly Ford
- Testing Equipment: Bobby Connel
