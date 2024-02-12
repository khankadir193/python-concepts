import time;
import datetime;

#here getting the time as per timestamp.
print(time.time());

#get the local time
print('local time:----',time.localtime(time.time()));

#return the formatted time..
print('formated Time:=>',time.asctime(time.localtime(time.time())));

#sleep():-sleep method is used for stop the execution as a given time.
for i in range(1,5):
    print(i);
    time.sleep(1); #this is sleep the time for one seconds.

#return current date and time object.
print('date time object:-',datetime.datetime.now());

#creating date time object with construtor..
print('constructor...>',datetime.datetime(2023,4,10));