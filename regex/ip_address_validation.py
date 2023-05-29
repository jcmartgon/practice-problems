# Jesus Carlos Martinez Gonzalez
# 29/05/2023
# IP Address Validation (https://www.hackerrank.com/challenges/ip-address-validation/problem)

"""
You will be provided with N lines of what are possibly IP addresses. 
You need to detect if the text contained in each of the lines represents an (a)IPv4 address (b)IPv6 address or (c)None of these.
"""

import re

ip_pattern = r"(?:(?P<ipv4>(?:\d{1,3}\.){3}\d{1,3})|(?P<ipv6>(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}))"


def main():
    ip_types = []
    N = int(input())
    for _ in range(N):
        address = input()
        ip_types.append(validate_ip(address))

    for address in ip_types:
        print(address)


def validate_ip(string):
    """Returns type of IP address or 'Neither' if it isn't one"""
    if match := re.fullmatch(ip_pattern, string):
        if match := match.group("ipv4"):
            b1, b2, b3, b4 = map(int, match.split("."))
            if (
                b1 in range(256)
                and b2 in range(256)
                and b3 in range(256)
                and b4 in range(256)
            ):
                return "IPv4"
            else:
                return "Neither"
        else:
            return "IPv6"
    else:
        return "Neither"


if __name__ == "__main__":
    main()
