#!/usr/bin/env python

import web

from pulses import pulses
from pulses import pulse

from relays import relays
from relays import relay

from sensors import sensors

urls = (
    '/pulses', 'pulses',
    '/pulse/(\d)', 'pulse',
    '/relays', 'relays',
    '/relay/(\d)', 'relay',
    '/sensors', 'sensors'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

