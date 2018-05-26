#! /usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from player_class import Player
from token_class import Token

class Tester:

    def __init__(self):
        self.dico_sum_position = {key: 0 for key in list(map(str, range(1, 8)))}
        self.current_serie = ''
        self.player_list = [Player('René Caravel', 'x'), Player('Miroslav O\'matic ', 'o')]

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
            self.player_list[0].quadrillage()
            print('----------------------')
            self.current_serie += self.play_position()

        self.player_list[0].quadrillage()
        print(last_player.name, last_player.check_connect())
        print(self.current_serie)
        print(len(self.current_serie))


def main():
    tester = Tester()
    tester.construct_serie()

if __name__ == '__main__': main()