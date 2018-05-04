The Network Checker
==========================

This project is continuously checking the LAN and WAN connection and writes a protocol (.csv).
Currently "google.com" is pinged as well as the access point (AP) that is 192.168.1.1 in my case.
The checking rate is set to every 10 seconds.

Start application with
"python Check_Internet.py"

It will use the function check_ping in "check_ping".

Output:
This python script will output two files. The first, here called "eggs.csv" represents the entire record of the availability check. The second file "statistics.csv" simply outputs the times in which the WAN resp. the LAN are either available or absent. It is updated at every taken check.

This application runs 24h by default. This time can simply be modified, look up the variable "run_time_in_hours" 

To clone repo:

git clone https://github.com/radioman85/Check_LAN_And_WAN.git

To add new commits:
git add 
git commit -m "<your comment>"
git push origin master
user name: <user name>
user password: <*********>
