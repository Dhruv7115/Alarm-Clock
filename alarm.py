import os
import datetime

def play_music():
    path = 'C:\\Users\\HP\\OneDrive\\Desktop\\Dhruv\\python\\alarm\\play.mp3'
    os.startfile(path)

hour = int(input("Enter hour: "))
minute = int(input("Enter minutes:"))
ampm = input("am/pm: ")

if (ampm == "pm"):
    hour = hour + 12

while( 1==1 ):
    if(hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute):
        play_music()
        exit()