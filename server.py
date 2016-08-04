#!/usr/bin/env python
import web
import pifacerelayplus


from pulses import pulses
from relays import relays
from sensors import sensors

relaysCount = 12
devicesCount = 2
pfrs = []

for devBus in range(0,devicesCount):
    pfrs.append(pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY, devBus))


urls = (
    '/pulses', 'pulses',
    '/pulse/([0-63])', 'pulse',
    '/relays', 'relays',
    '/relay/([0-63])', 'relay',
    '/sensors', 'sensors'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

