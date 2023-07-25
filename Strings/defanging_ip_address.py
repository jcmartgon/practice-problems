# Jesus Carlos Martinez Gonzalez
# 24/07/2023
# Defanging an IP address (https://leetcode.com/problems/defanging-an-ip-address)

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        # No built-ins

        defanged_address = ""
        for c in address:
            if c == ".":
                defanged_address += "[.]"
            else:
                defanged_address += c

        return defanged_address
        """

        return address.replace(".", "[.]")
