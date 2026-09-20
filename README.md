# C2-Remote-command-and-control

A barebones command and control script for simple educational use across VMs and Cybersecurity labs 

!This tool is designed to be used for educational purposes only!

This tool can send commands from the attacker's machine to the victim's machine running the corresponding script and receive the ouput back.

The tool is a barebones implementation, designed around the concept of the victim connecting to the attacker, to allow for reverse proxy implementation such as the ngrok service. The tool allows the following actions:
1) Send commands and receive output 
2) Send files or download them from the victim machine
3) Capture screenshots from the target machine

Available hard coded commands:
1) send (be prompted to send a file to the victim machine)
2) download (be prompted to receive a file from the victim machine)
3) screenshot (receive a screenshot from the victim's monitor)

Known issues to-be-fixed: directory navigation is not yet possible
