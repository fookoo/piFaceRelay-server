#!/usr/bin/env python
import pifacerelayplus

relaysCount = 12
devicesCount = 2
pfrs = []

for devBus in range(0, devicesCount):
    pfrs.append(pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY, devBus))
