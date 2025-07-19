#!/usr/bin/python3
def print_last_digit(num):
    ld = abs(num) % 10
    print("{}".format(ld))
    return ld
