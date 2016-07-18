import os
import web
import json
import time
import pifacerelayplus

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

class sensors:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        directories = os.listdir('/sys/bus/w1/devices')

        return directories

class sensor:
    def GET(self, sensorId):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        return "{}"
