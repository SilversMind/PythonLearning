#! /usr/bin/python
# -*- coding: utf-8 -*-


class Token:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def return_position(self):
        return self.pos_x, self.pos_y