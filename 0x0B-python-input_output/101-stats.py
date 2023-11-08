#!/usr/bin/python3
""" Log parser for Server Logs """
import sys

total_size = 0
status_codes = {str(code): 0 for code in [200,
                                          301, 400, 401, 403, 404, 405, 500]}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])
        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count % 10:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes[code] > 0):
                if status_codes[code] > 0:
                    print ("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
