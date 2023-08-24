#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Write a method that determines if a given data set represents a valid
    UTF-8 encoding.
        Prototype: def validUTF8(data)
        Return: True if data is a valid UTF-8 encoding, else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only need to
        handle the 8 least significant bits of each integer
    """
    num_of_bytes = 0
    for num in data:
        mask = 1 << 7
        if num_of_bytes == 0:
            while mask & num:
                num_of_bytes += 1
                mask >>= 1
            if num_of_bytes == 0:
                continue
            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            if not (num & mask and not (num & mask >> 1)):
                return False
        num_of_bytes -= 1
    return num_of_bytes == 0
