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
                if item['type'] == 'switch':
                    pfr.relays[int(item['id'])].value = int(item['state'])
                elif item['type'] == 'pulse':
                    if int(item['state']) == 1:
                        pfr.relays[int(item['id'])].value = 1
                        time.sleep(.1);
                        pfr.relays[int(item['id'])].value = 0

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