import check_ping
import time
import datetime
import csv

print("========")
print("========================")
print("======================================================================")
print("========================")
print("========\n")
print("Start Connection Test \n")
print("========================")
print("========================")
print("========================")

ts = time.time()

msg1 = "WAN is running"
msg2 = "WAN is down"
msg3 = "LAN is running"
msg4 = "LAN is down"
NW_ID_1 = "google.com"
NW_ID_2 = "192.168.1.1"

run_time_in_hours = 24
run_time_in_seconds = run_time_in_hours * 3600
start_time = int (ts)
end_time = start_time + run_time_in_seconds

print('start time is: {}'.format(start_time))
print('end time is: {}'.format(end_time))

status = ""
counter = 0
while(int(time.time()) <= end_time):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
   
    print("\n<<<----------------------->>>")
    print("             {}".format(counter))
    print("<<<----------------------->>>\n")
    counter+=1
    
    status = check_ping.check_ping(NW_ID_1)
    if status == "Network Active":

        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([counter]+[st]+[NW_ID_1]+[msg1])

        print(msg1)   

    else:
        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([counter]+[st]+[NW_ID_1]+[msg2])

        print(msg2)


    status = check_ping.check_ping(NW_ID_2)
    if status == "Network Active":

        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([counter]+[st]+[NW_ID_2]+[msg3])

        print(msg3)    

    else:
        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([counter]+[st]+[NW_ID_2]+[msg4])

        print(msg4)
        
    
    time.sleep(10)
        

print("real status" + status)
