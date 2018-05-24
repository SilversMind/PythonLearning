#! /usr/bin/python
# -*- coding: utf-8 -*-


class Player():
    number_in_a_row = 4

    def __init__(self, symbol):
        self.list_token = []
        self.symbol = symbol

    def check_condition(self, primary_token, other_token, win_direction):
        win_pack = ((1, 0), (0, 1), (1, 1), (-1, 1))
        '''Win direction corresponds to the way of winning the game by connecting
         n token horizontally (win direction =0), vertically (win direction =1),
          and as per the left (win direction =2) and right (win direction =3) diagonals. '''
        for item in range(- Player.number_in_a_row, Player.number_in_a_row):
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
                    return out
        return None


class Token():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def return_position(self):
        return self.pos_x, self.pos_y


def quadrillage(list_token,lenght=8):
    for index_y in range(lenght, 0, -1):
        for index_x in range(1, lenght+2):
            if existing_token(list_token, index_x, index_y):
                print('|x', end="")
            else:
                print('| ', end="")
            if index_x == lenght + 1:
                print('')


def existing_token(list_token, pos_x, pos_y):
    if list_token:
        for token in list_token:
            if (pos_x, pos_y) == (token.pos_x, token.pos_y):
                return True
    return False


def ask_coordinate(item):
    pos_lambda = input("Please enter the {} coordinate\n".format(item))
    while pos_lambda not in list(map(str, range(1, 9))):
        pos_lambda = input('Enter a number between 1 and 8\n')
    return int(pos_lambda)


def ask_coordinates(list_token):
    pos_x, pos_y = ask_coordinate('column'), ask_coordinate('line')
    while existing_token(list_token, pos_x, pos_y)\
            or not(pos_y == 1 or existing_token(list_token, pos_x, pos_y -1)):

        print('This position is unavailable, please select a new one')
        pos_x, pos_y = ask_coordinate('line'), ask_coordinate('column')
    return pos_x, pos_y


def main():
    player_1 = Player('y')
    quadrillage(None)
    list_token = []
    while not player_1.check_connect():
        pos_x, pos_y = ask_coordinates(player_1.list_token)
        player_1.list_token.append(Token(int(pos_x), int(pos_y)))
        quadrillage(player_1.list_token)
    print(player_1.check_connect(list_token))


if __name__ == '__main__': main()
