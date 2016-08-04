import web

from pulses import pulses
from relays import relays
from sensors import sensors

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

