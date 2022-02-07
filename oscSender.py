#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import time
from threading import Thread
from pythonosc import udp_client

send = True
PORT = 5005
IP = "Put Receiver IP address here"

client = udp_client.SimpleUDPClient(IP, PORT)

print("Press f + Enter to start the packages")
print("Press s + Enter to stop the packages")

def getkey():
    global send
    while (True):
        key = input()
        if(key == 'f' and not send):
            send = True
            print("[+] Sending... to {} in port {}".format(IP, PORT))
        elif(key == 's' and send):
            send = False
            print("[-] Stop!")
        time.sleep(0.5)

def sender():
    global send
    while (True):
        if(send):
            client.send_message("/BPM", 60)
        time.sleep(1)

Thread(target=getkey).start()
Thread(target=sender).start()
