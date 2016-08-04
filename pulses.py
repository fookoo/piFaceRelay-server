import web
import json
import time

class pulses:
    def POST(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        values = json.loads(web.data())

        for item in values:
            dev = int(item['id']) // 8
            relayId = int(item['id']) - (8 * dev)

            pfrs[dev].relays[relayId].value = 1;

        time.sleep(.1);

        for item in values:
            dev = int(item['id']) // 8
            relayId = int(item['id']) - (8 * dev)

            pfrs[dev].relays[relayId].value = 0;

        return 200

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200

class pulse:
    def POST(self, relay):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        i = web.input()

        dev = int(relay) // 8
        relayId = int(relay) - (8 * dev)

        pfrs[dev].relays[relayId].value = 1
        time.sleep(.1);
        pfrs[dev].relays[relayId].value = 0

        return 200

    def OPTIONS(self, relay):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200

