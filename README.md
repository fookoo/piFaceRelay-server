# piFaceRelay WWW Server

Simple web server that allow you to control your piFaceRelay board over the internet 

## What do you need?

    $ sudo apt-get install python{,3}-pifacecommon
    $ sudo apt-get install python{,3}-pifacerelayplus

You will also need to set up automatic loading of the SPI kernel module which can be done with the lastest version of raspi-config. Run:

    $ sudo raspi-config

Then navigate to Advanced Options, SPI and select yes.

You may need to reboot.

## How to use it

    chmod +x server.py
    ./server.py <IP-ADDRESS>

Then you can query server for:

    GET http://<IP-ADDRESS>:8080/relays

So you got in return, application/json representing state of first 8 relays

    [
        { "id": "0", "state": "0" },
        { "id": "1", "state": "0" }, 
        { "id": "2", "state": "0" },
        { "id": "3", "state": "0" },
        { "id": "4", "state": "0" },
        { "id": "5", "state": "0" },
        { "id": "6", "state": "0" },
        { "id": "7", "state": "0" }
    ]

If you do a POST request you can set relays 

    POST http://<IP-ADDRESS>:8080/relays
    [
        { "id": "0", "state": "0" },
        { "id": "2", "state": "1" },
        { "id": "3", "state": "0" },
        { "id": "7", "state": "1" }
    ]


## What should be done in near future?

Any contributions are welcome

- Error handling
- Support for more then just one piFaceRelay


## Author
Piotr Pliszczyński <fookoo@gmail.com>