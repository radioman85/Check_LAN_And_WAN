import check_ping
import time
import datetime
import csv

print("========================")
print("Start Connection Test \n")
print("========================")


ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

msg_success = "is running"
msg_fail = "is down"
inverval_seconds = 10

network_addresses = {"WAN":"www.google.com", "LAN":"192.168.1.1"}
total_down_time_seconds = {}
total_available_time_seconds = {}

for i in network_addresses:
    total_down_time_seconds.update({i:int(0)})
    total_available_time_seconds.update({i:int(0)})

print(total_down_time_seconds)
print(total_available_time_seconds)

    
#print("***********************************************************************")
#print("The following network addresses will be checked")
#for i in network_addresses:
#    print("{}: {}".format(i, network_addresses[i]))
#print("***********************************************************************")

run_time_in_hours = 24
run_time_in_seconds = run_time_in_hours * 3600
start_time = int (ts)
end_time = start_time + run_time_in_seconds

#print('start time is: {}'.format(start_time))
#print('end time is: {}'.format(end_time))

status = ""
counter = 0

title = "Networkprotokol"
company = " GGA-Maur"
star_line = "****************************************"

with open('eggs.csv', 'a') as csvfile:
    active_document = csv.writer(csvfile)
    active_document.writerow([star_line])
    active_document.writerow([title]+[company])
    active_document.writerow([star_line])
    active_document.writerow([])


    for i in network_addresses:
        string = str(i)+ ": " + str(network_addresses[i])
        active_document.writerow([string])
        
    
    active_document.writerow([])
        
latest_time_stamp = int(time.time())
        

while(int(time.time()) <= end_time):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
   
    print("\n<<<----------------------->>>")
    print("             {}".format(counter))
    print("<<<----------------------->>>\n")
    counter+=1
    
    
    for i in network_addresses:
    
        with open('eggs.csv', 'a') as csvfile:
            active_document = csv.writer(csvfile)
            
            status = check_ping.check_ping(network_addresses[i])
            if status == "Network Active":
                active_document.writerow([counter]+[st]+[i]+[msg_success])

                total_available_time_seconds[i] += int(ts - latest_time_stamp)
                

            else:
                active_document.writerow([counter]+[st]+[i]+[msg_fail])
                
                total_down_time_seconds[i] += int(ts - latest_time_stamp)             
                
                
    
    print(total_available_time_seconds)

    latest_time_stamp = ts
    
    
    output_string = "Total down time in seconds " + str(total_down_time_seconds) + " s\n"
    output_string += "Total available time in seconds " + str(total_available_time_seconds) + " s"
    statistic_file = open('statistics.txt', 'w')
    statistic_file.write(output_string)
        
        
    time.sleep(inverval_seconds)
