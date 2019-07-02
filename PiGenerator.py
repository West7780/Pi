import math, time, socket, threading, ProgressBar
from queue import Queue
from decimal import *

### set up ###

#define thread function

def threader():
    global pi
    getcontext().prec = num_digits
    while True:
        k = q.get()
        pi+= (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        q.task_done()

#get user input for # threads and # digits

num_threads = int(input("How many threads would you like to use?"))
num_digits = int(input("How many digits would you like to generate?"))
if input("Would you like to save in pi.txt or print at the end?")[0] == 'p': mode = 1
else: mode = 0

#set number of digits of percision

getcontext().prec = num_digits

### CALCULATING ###

#save start time

start_time = time.time()

#create pi

pi = Decimal(0)

#create queue

q = Queue()

for k in range(0,num_digits):
    q.put(Decimal(k))

Queue_Time = time.time()-start_time
print('Finished creating Queue in '+str(Queue_Time)+'s')

#create threads

for x in range(0,num_threads):
    t = threading.Thread(target=threader)
    t.daemon = True
    try:
        t.start()
    except:
        input('Reached Maximum number of threads ('+str(x)+'), press enter to continue')
        break

Thread_Time = time.time()-start_time-Queue_Time
print('Finished creating Threads in '+str(time.time()-start_time-Queue_Time)+'s\n')

#progress bar

p = ProgressBar.ProgressBar(num_digits, 50, title='Generating Digits')

while q.qsize() > 0:
    p.setProgress(int(num_digits-q.qsize()))
    p.update()
    time.sleep(0.1)

#Ensure All threads are finished

q.join()

### DONE ###

#print results

Time_Time = time.time()-start_time-Thread_Time
print('Time:'+str(Time_Time)+'s')

#save pi
if mode:
    file = open('pi.txt','w')
    file.write(str(pi))
    file.close()
else:
    print(pi)
input('press enter to quit')
