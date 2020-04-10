#######################################################
# 
# RequestCOTController.py
# Python implementation of the Class RequestCOTController
# Generated by Enterprise Architect
# Created on:      26-Mar-2020 6:32:34 PM
# Original author: Giu Platania
# 
#######################################################
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Model.Event import Event
from constant import vars as con
conn = con()

class RequestCOTController:
    """this controller manage all the different types of COTS, including the geochat
    """
# default constructor  
    def __init__(self):  
        a = 1
    def ping(self, lat, lon):
       event = Event(conn.PING, lat, lon) 
       return event

    def sendGeoChatToAllChatRooms(self, text, callsign):
        event = Event(conn.GEOTOALLROOMS, text, callsign)
        print(event)
        return event
    def sendGeoChatToGroup(self, text, callsign):
        event = Event(conn.GEOTOGROUP, text, callsign)
        return event
        print(event)
    def sendGeoChatToTeam(self, text, callsign):
        """
        this will send the geochat to team
        """
        event = Event(conn.GEOTOTEAM, text, callsign)
        return event
    def default(self):
        event = Event(conn.DEFAULT)
        return event
aEvent = RequestCOTController().ping(lat = 123, lon = 123)
print('over')