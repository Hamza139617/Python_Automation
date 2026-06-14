#!/usr/bin/env python3

import email
import yagmail
import imaplib
import os
import sys


"""
Scenario: need to send some txt files every single day to multiple people

automation:
email automation for sending attachements every single day to multiple people by taking the number of people as argument , three different 
types of people
"""

def sendData(argv):
    
    times = []
    prev = 1
    
    for char in argv :
        if char.isdigit():
            times.append(int(char)  + prev)
            prev = int(char) + prev

    bot = yagmail.SMTP("hamza139617@gmail.com", os.environ.get("API_KEY"))

    i = 0 
   

    try:
        for i in range(1 , times[0]):
            bot.send(
                to=argv[i],
                subject="something",
                contents="something",
                attachments="one.txt"
            )
            
    except Exception as e:
        print(e)
     

    try:
        for i in range(times[0], times[1]):
            bot.send(
                to=argv[i],
                subject="something",
                contents="something",
                attachments="two.txt"
            )
            print("ran  2")
    except Exception as e:
        print(e)
      

    try:
        for i in range(times[1], times[2]):
            bot.send(
                to=argv[i],
                subject="something",
                contents="something",
                attachments="three.txt"
            )
         
    except Exception as e:
        print(e)
      

    bot.close()


if __name__ == "__main__":
    sendData(sys.argv)

