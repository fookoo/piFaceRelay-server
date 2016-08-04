import web
import json
import time
import server

class relays:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')
        output = "["

        for i in range(0, server.relaysCount):
            dev = i // 8
            relayId = i - (8 * dev) - 1
            output += "{ \"id\": \"" + str(i) + "\", \"state\": \"" + str(server.pfrs[dev].relays[int(relayId)].value) + "\" },"

        return output[:-1] + "]"

    def POST(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        values = json.loads(web.data())

        for item in values:
            dev = int(item['id']) // 8
            relayId = int(item['id']) - (8 * dev)

            if item['type'] == 'switch':
                server.pfrs[dev].relays[relayId].value = int(item['state'])
            elif item['type'] == 'pulse':
                if int(item['state']) == 1:
                    server.pfrs[dev].relays[relayId].value = 1
                    time.sleep(.1);
                    server.pfrs[dev].relays[relayId].value = 0

        return 200

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200


class relay:
    def GET(self, relay):

        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        dev = int(relay) // 8
        relayId = int(relay) - (8 * dev) - 1

        print "GET dev: " + str(dev) + ", relayId: " + str(relayId)

        output = "{ \"id\": \"" + str(relay) + "\", \"state\": \"" + str(server.pfrs[dev].relays[relayId].value) + "\" }"

        return output

    def POST(self, relay):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        i = web.input()

        dev = int(relay) // 8
        relayId = int(relay) - (8 * dev) - 1

        print "POST dev: " + str(dev) + ", relayId: " + str(relayId)
        server.pfrs[dev].relays[relayId].value = int(i.value)

        return 200

    def OPTIONS(self, relay):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200