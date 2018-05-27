#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys


def check_args(arg):
    for x in sys.argv:
        if arg in x:
            return True
    return False


def ask_coordinate(item):
    pos_lambda = input("Please enter the {} coordinate\n".format(item))
    while pos_lambda not in list(map(str, range(1, 9))):
        pos_lambda = input('Enter a number between 1 and 8\n')
    return int(pos_lambda)