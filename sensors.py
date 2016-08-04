import os
import web
import json
import time
import pifacerelayplus
import commands

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

class sensors:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        directories = list(commands.getstatusoutput('ls -I w1_bus_master1 /sys/bus/w1/devices'))
	directories.pop(0)

        return json.dumps(directories)

class sensor:
    def GET(self, sensorType, sensorId):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

	sensorV = list(commands.getstatusoutput("scripts/" + sensorType + ".sh " + sensorId))
	sensorV.pop(0)

        return json.dumps(sensorV)
