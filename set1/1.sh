#!/bin/bash

# xrr: -r -> perform reverse operation of hexdump, which get original string 
#            from hex 
#      -p -> print result 
# base64: convert string into base64
echo $1 | xxd -r -p | base64
