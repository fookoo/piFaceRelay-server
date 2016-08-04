import web
import json
import time
import pifacerelayplus

class relays:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')
        output = "["

        for i in range(0,relaysCount):
            dev = i // 8
            relayId = i;
            if relayId >= 8:
                relayId = i - 8

            print "dev: " + str(dev) + " , relay: " + str(relayId) + "\n"

            output += "{ \"id\": \"" + str(i) + "\", \"state\": \"" + str(pfrs[dev].relays[int(relayId)].value) + "\" },"

        return output[:-1] + "]"

    def POST(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        values = json.loads(web.data())

        for item in values:
            dev = int(item['id']) // 8
            relayId = int(item['id']) - (8 * dev)

            if item['type'] == 'switch':
                pfrs[dev].relays[relayId].value = int(item['state'])
            elif item['type'] == 'pulse':
                if int(item['state']) == 1:
                    pfrs[dev].relays[relayId].value = 1
                    time.sleep(.1);
                    pfrs[dev].relays[relayId].value = 0

        return 200

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200


class relay:
    def GET(self, relay):
        output = "{ \"id\": \"" + str(relay) + "\", \"state\": \"" + str(pfr.relays[int(relay)].value) + "\" }"
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        return output

    def POST(self, relay):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        i = web.input()

        dev = int(relay) // 8
        relayId = int(relay) - (8 * dev)

        pfrs[dev].relays[relayId].value = int(i.value)

        return 200

    def OPTIONS(self, relay):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200