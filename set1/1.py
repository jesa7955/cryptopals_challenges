#!/bin/python3

import base64

get = input()
origin = bytes.fromhex(get)
print(base64.b64encode(origin).decode())
