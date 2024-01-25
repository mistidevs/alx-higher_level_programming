#!/bin/bash
# All methods accepted by sever
curl -sX OPTIONS -i 0.0.0.0:5000/route_4 | grep -i "^Allow:" | cut -d' ' -f2-
