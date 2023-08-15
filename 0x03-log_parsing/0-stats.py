#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line must be
skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (see input
    format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear or is not an integer, don’t print
        anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""
import sys


if __name__ == "__main__":
    status = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}
    count = 1
    file_size = 0

    def status_size(line):
        """
        parses line, then increases the values in the status dictionary and
        returns file_size
        """
        try:
            parsed_line = line.split()
            file_size = parsed_line[-1]
            status_code = parsed_line[-2]
            if status_code in status.keys():
                status[status_code] += 1
            return int(file_size)
        except Exception:
            return 0

    def print_stats():
        """
        prints file size, status code and status code occurrence
        """
        print("File size: {}".format(file_size))
        for key in sorted(status.keys()):
            if status[key]:
                print("{}: {}".format(key, status[key]))

    try:
        for line in sys.stdin:
            file_size += status_size(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
