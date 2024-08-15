#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Run with the following command line parameters:
python3 client_browser.py <hostname> <port> <file>

Examples:
$ python3 client_browser.py info.cern.ch 80 "" # defaults to index.html
$ python3 client_browser.py localhost 6789 "hello_world.html"
"""

import sys
import socket

length = len(sys.argv)

if len(sys.argv) != 4:
    server_hostname = "localhost"
    server_ip = "127.0.0.1"
    server_port = 6789
    file_name = "web_files/hello_world.html"

else:
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    file_name = sys.argv[3]

    server_ip = socket.gethostbyname(server_hostname)

try:
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    get_request = (
        f"GET /{file_name} HTTP/1.1\r\nHost: {server_hostname}:{server_port}\r\n\r\n"
    )
    client_socket.connect((server_ip, server_port))
    client_socket.send(get_request.encode())

    # Just print what's returned from the server.
    response = ""

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data.decode()
    print(response)

except Exception as e:
    print("Exception was: ", e)

finally:
    client_socket.close()
