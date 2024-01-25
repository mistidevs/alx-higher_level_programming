#!/bin/bash
# All methods accepted by sever
curl -sX OPTIONS -i $1 | grep -i "^Allow:" | cut -d' ' -f2-
