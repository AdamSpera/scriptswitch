START cd %userprofile%
git clone https://github.com/AdamSpera/scriptswitch.git
cd scriptswitch
git clone https://github.com/networktocode/ntc-templates.git
pip install netmiko
pip install ntc_templates
pip install inquirer
start "" "%ProgramFiles%\Git\git-bash.exe" -c "cd %userprofile% && cd scriptswitch && export NET_TEXTFSM="%userprofile%\scriptswitch\ntc-templates\ntc_templates\templates" && echo $NET_TEXTFSM && /usr/bin/bash --login -i"
