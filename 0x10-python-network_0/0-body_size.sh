#!/bin/bash
# Getting size of the body of a response
curl -s -I $1 | grep -i "^Content-Length:" | awk '{print $2}'
