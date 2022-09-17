# Script Switch

_Switching up ways to script._

## Introduction

ScriptSwitch is a project developed by Adam Spera at Arcadia University, computer science department as an original independent study capstone. ScriptSwitch is a CLI script injection software for Cisco switches. 

- Connect into Cisco switches securely using SSH
- Select from a variety of template scripts
- Craft custom scripts in the CLI for deployment
- Configure port interfaces with template scirpts
- Ease of use through any Anaconda PowerShell terminal
- Save output with formatting to an external file

Utilizing the functionality of NetMiko and ConnectHandler over SSH, ScriptSwitch provides the user a simple and easy platform for script injection and creation. Users are given flexibility to create their own scripts form scratch or use a template script.

## Usage

### Establishing a SSH connection

1. Run the following commands in an Anaconda PowerShell (in Cisco env: ```conda activate cisco```) for ScriptSwitch:
```
python ScriptGUI.py
```
2. When prompted, enter the target switch's IP address (no subnet)
3. When prompted, enter the intended user's SSH username
4. When prompted, enter the intended user's SSH password
 
5. Select one of the choices:
   - Create a new script
   - Use a template script
   - Configure an interface

### New Script Mode

1. When prompted, input the code to be deployed to the switch
2. The program will display the switch output after the response
3. When confirmation is received, select one of the following options:
   - Send another script
   - Exit the program 

### Template Script Mode

1. When prompted, select any of the presented template scripts to deploy it
2. The program will display the switch output after the response
3. When confirmation is received, select one of the following options:
   - Send another script
   - Exit the program
   
### Configure Interface Mode

1. When prompted, select an interface from the list of front facing ports
2. Select a script template you want to send (this will use the secret key for enable and configure terminal)
   - Some of the templates will request further information like ip addresses or subnets
3. When confirmation is received, select one of the following options:
   - Send another script!
   - Exit the program.

### Output File

The results are automatically saved to a file in the root directory named Output.txt

## Installation 

### Git and Cloning

1. Clone ScriptSwitch to your desired directory and folder.
   - The MSI installer for Git can be found at https://git-scm.com/download/win
2. Clone NTC-Templates inside the scriptswitch directory folder.
   - Clone NTC-Templates from https://github.com/networktocode/ntc-templates.git 
   
### Git Bash Variables

1. Open a Git Bash terminal in the scirptswitch directory and enter the following line of code:
```
export NET_TEXTFSM="C:\…….\scriptswitch\ntc-templates\ntc_templates\templates”
```
2. Test that the command was successful by entering the following code: ```echo $NET_TEXTFSM```
  
### Anaconda Enviorment and Libraries

1. Open an Anaconda PowerShell terminal and enter: ```conda create —name cisco python=3.9```
2. Enter the new enviorment by entering: ```conda activate cisco```
3. Install the following libraries:
```
pip install netmiko
pip install ntc_templates
pip install inquirer
```

## Contributions

Thank you to everybody who helped create the ScriptSwitch project possible!

Special mention and thanks to the following people:

- Guidance and Mentoring: Vitaly Ford
- Testing Equipment: Bobby Connel

_Made by: Adam T Spera_
