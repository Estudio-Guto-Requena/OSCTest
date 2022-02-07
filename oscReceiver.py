#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from pythonosc import osc_server
from pythonosc import dispatcher

PORT = 5005
IP = "Put Sender IP address here"

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/BPM", print)
server = osc_server.ThreadingOSCUDPServer((IP, PORT), dispatcher)
server.serve_forever()
