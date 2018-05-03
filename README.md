The Network Checker
==========================

This project is continuously checking the LAN and WAN connection and writes a protocol (.csv).
Currently "google.com" is pinged as well as the access point (AP) that is 192.168.1.1 in my case.
The checking rate is set to every 10 seconds.

Start application with
"python Check_Internet.py"

It will use the function check_ping in "check_ping".
