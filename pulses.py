class pulses:
    def POST(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials', 'true')

        values = json.loads(web.data())

        for item in values:
            pfr.relays[int(item['id'])].value = 1;

        time.sleep(5);

        for item in values:
            pfr.relays[int(item['id'])].value = 0;

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
        pfr.relays[int(relay)].value = 1
        time.sleep(.1);
        pfr.relays[int(relay)].value = 0

        return 200

    def OPTIONS(self, relay):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Headers', 'Content-Type')

        return 200

