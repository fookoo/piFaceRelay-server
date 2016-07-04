#!/usr/bin/env python
import web
import json
import pifacerelayplus

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

urls = (
    '/relays', 'relays',
    '/relay/([0-7])', 'relay'
)

app = web.application(urls, globals())

class relays:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')
        output = "["

        for i in range(0,8):
            output += "{ \"id\": \"" + str(i) + "\", \"state\": \"" + str(pfr.relays[int(i)].value) + "\" },"

        return output[:-1] + "]"

    def POST(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        values = json.loads(web.data())

        for item in values:
                pfr.relays[int(item['id'])].value = int(item['state'])

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
        pfr.relays[int(relay)].value = int(i.value)

        return 200

    def OPTIONS(self, relay):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200

if __name__ == "__main__":
    app.run()

