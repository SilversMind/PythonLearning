#! /usr/bin/python
# -*- coding: utf-8 -*-

from basics_classes.token_class import Token
from utils_functions.basic_functions import ask_coordinate


class Player:
    number_in_a_row = 4
    total_token = []

    def __init__(self, name, symbol):
        self.list_token = []
        self.name = name
        self.symbol = symbol
    @classmethod
    def quadrillage(cls, lenght=7, width=6):
        for index_y in range(width, 0, -1):
            for index_x in range(1, lenght + 2):
                present_token = cls.existing_token(index_x, index_y)
                if present_token:
                    print('|{}'.format(present_token[1].symbol), end="")
                else:
                    print('| ', end="")
                if index_x == lenght + 1:
                    print('')

    @classmethod
    def existing_token(cls, pos_x, pos_y):
        if Player.total_token:
            for token in Player.total_token:
                if (pos_x, pos_y) == (token[0].pos_x, token[0].pos_y):
                    return token
        return False

    def ask_coordinates(self):
        pos_x, pos_y = ask_coordinate('column'), ask_coordinate('line')
        while Player.existing_token(pos_x, pos_y) \
                or not (pos_y == 1 or Player.existing_token(pos_x, pos_y - 1)):
            print('This position is unavailable, please select a new one')
            pos_x, pos_y = ask_coordinate('line'), ask_coordinate('column')
        self.list_token.append(Token(pos_x, pos_y))
        Player.total_token.append((Token(pos_x, pos_y),self))

    @staticmethod
    def check_condition(primary_token, other_token, win_direction):
        win_pack = ((1, 0), (0, 1), (1, 1), (-1, 1))
        '''Win direction corresponds to the way of winning the game by connecting
         n token horizontally (win direction =0), vertically (win direction =1),
          and as per the left (win direction =2) and right (win direction =3) diagonals. '''
        for item in range(0, Player.number_in_a_row):
            if primary_token.pos_x == other_token.pos_x + item * (win_pack[win_direction][0]) \
                    and primary_token.pos_y == other_token.pos_y + item * (win_pack[win_direction][1]):
                return True

    def check_connect(self):
        for x in self.list_token:
            out = [x.return_position()]
            other_token = self.list_token[:]
            other_token.remove(x)
            for item in range(4):
                corresponding_token = [y for y in other_token if self.check_condition(x, y, item)]
                if len(corresponding_token) == Player.number_in_a_row - 1:
                    for x in corresponding_token: out.append(x.return_position())
                    return sorted(out)
        return None
