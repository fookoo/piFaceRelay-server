#!/usr/bin/env python
import web
import json
import time
import pifacerelayplus

import pulses from pulses
import relays from relays
import sensors from sensors

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

urls = (
    '/pulses', 'pulses',
    '/pulse/([0-7])', 'pulse',
    '/relays', 'relays',
    '/relay/([0-7])', 'relay',
    '/sensors', 'sensors'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

