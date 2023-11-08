#!/usr/bin/python3
""" Log parser for Server Logs """
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size

        status_codes[status_code] += 1
        line_count += 1

        if line_count % 10:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
