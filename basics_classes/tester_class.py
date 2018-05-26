#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from random import randint
from player_class import Player
from token_class import Token

class Tester:

    def __init__(self):
        self.dico_sum_position = {key: 0 for key in list(map(str, range(1, 8)))}
        self.current_serie = ''
        self.player_list = [Player('René Caravel', 'x'), Player('Miroslav O\'matic ', 'o')]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def play_possible_position():
        return str(randint(1, 7))

    def current_player(self):
        return sum(self.dico_sum_position.values()) % len(self.player_list)

    def check_playable_position(self, number):
        if self.dico_sum_position[number] < 8:
            self.dico_sum_position[number] += 1
            self.player_list[self.current_player()].list_token.append(Token(int(number),
                                                                            self.dico_sum_position[number]))
            Player.total_token.append((Token(int(number),
                                            self.dico_sum_position[number]),
                                      self.player_list[self.current_player()]))
            return True
        return False

    def play_position(self):
        position = self.play_possible_position()
        while not self.check_playable_position(position):
            position = self.play_possible_position()
        return position

    def construct_serie(self):
        self.current_serie = self.play_position()
        last_player = self.player_list[self.current_player()]
        while not last_player.check_connect():
            last_player = self.player_list[self.current_player()]
            if '-gt' in sys.argv:
                self.player_list[0].quadrillage()
                print('----------------------')
            self.current_serie += self.play_position()

        if '-g' in sys.argv:
            self.player_list[0].quadrillage()
        print(self.current_serie, last_player.name, last_player.check_connect(), last_player.list_token.__len__())

    def construct_token_from_existing_serie(self, existing_serie):
        for indx, value in enumerate(existing_serie):
            self.dico_sum_position[value] += 1
            Player.total_token.append((Token(int(value), self.dico_sum_position[value]), self.player_list[indx % 2]))
        self.player_list[0].quadrillage()


def main():
    tester = Tester()
    serie = '2252576253462244111563365343671351441'
    tester.construct_token_from_existing_serie(serie)
    possible_position = tester.player_list[len(serie) % 2].playable_position()
    print(possible_position)
    print('----------------------')
    for x in possible_position:
        print('Playing on the {} position'.format(x))
        new_serie = serie + str(x[0])
        with Tester() as new_tester:
            new_tester.construct_token_from_existing_serie(new_serie)
            print(new_tester.player_list[len(new_serie) % 2].playable_position())
            print('----------------------')


if __name__ == '__main__': main()