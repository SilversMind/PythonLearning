#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from random import randint
from player_class import Player
from token_class import Token
from pickle import dump

class Tester:
    possible_outcome = []

    def __init__(self):
        self.dico_sum_position = {key: 0 for key in list(map(str, range(1, 8)))}
        self.current_serie = ''
        self.player_list = [Player('René Caravel', 'x'), Player('Miroslav O\'matic', 'o')]
        self.total_token = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def quadrillage(self, lenght=7, width=6):
        for index_y in range(width, 0, -1):
            for index_x in range(1, lenght + 2):
                present_token = self.existing_token(index_x, index_y)
                if present_token:
                    print('|{}'.format(present_token[1].symbol), end="")
                else:
                    print('| ', end="")
                if index_x == lenght + 1:
                    print('')

    def existing_token(self, pos_x, pos_y):
        if self.total_token:
            for token in self.total_token:
                if (pos_x, pos_y) == (token[0].pos_x, token[0].pos_y):
                    return token
        return False

    @staticmethod
    def play_possible_position():
        return str(randint(1, 7))

    def current_player(self):
        return sum(self.dico_sum_position.values()) % len(self.player_list)

    def check_if_playable_position(self, number):
        if self.dico_sum_position[number] < 8:
            self.dico_sum_position[number] += 1
            self.player_list[self.current_player()].list_token.append(Token(int(number),
                                                                            self.dico_sum_position[number]))
            self.total_token.append((Token(int(number),
                                            self.dico_sum_position[number]),
                                      self.player_list[self.current_player()]))
            return True
        return False

    def check_playables_positions(self):
        out = list([(int(key), value + 1) for key, value in self.dico_sum_position.items() if value < 6])
        return out

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
            self.player_list[indx % 2].list_token.append((Token(int(value), self.dico_sum_position[value])))
            self.total_token.append((Token(int(value), self.dico_sum_position[value]), self.player_list[indx % 2]))
        self.quadrillage()

    def check_future_position(self, serie, possible_position):
        for x in possible_position:
            print('Playing on the {} position'.format(x))
            new_serie = serie + str(x[0])
            with Tester() as new_tester:
                new_tester.construct_token_from_existing_serie(new_serie)
                print(new_tester.check_playables_positions())
                current_player = new_tester.player_list[(len(new_serie) + 1) % 2]
                if current_player.check_connect():
                    print('Win for {} by playing {}'.format(current_player.name, x))
                    Tester.possible_outcome.append((new_serie, 'Win'))
                    return new_serie
                else:
                    Tester.possible_outcome.append((new_serie, 'No'))
                print('----------------------')
                new_possible_position = new_tester.check_playables_positions()
                serie_to_return = new_tester.check_future_position(new_serie, new_possible_position)
                Tester.possible_outcome.append(serie_to_return)


def determining_score(serie, outcome):
    current_player = len(serie) % 2
    last_player = (len(outcome) - 1) % 2
    multiplier = 1
    if len(outcome) == 42:
        return 0
    if current_player != last_player:
        multiplier = -1
    score = (((42 - len(outcome)) // 2) +1)*multiplier
    return score



def main():
    with Tester() as tester:
        serie = '7422341735647741166133573473242566'
        tester.construct_token_from_existing_serie(serie)
        print('----------------------')
        possible_position = tester.check_playables_positions()
        print(possible_position)
        tester.check_future_position(serie, possible_position)
        possible_outcome = [x for x in Tester.possible_outcome if x is not None]
        dump(possible_outcome, open("../test_minmax/possible_outcome_test.p", "wb"))
        print(len(possible_outcome))
        print([determining_score(serie, x[0]) for x in possible_outcome if x[1] == 'Win'])



if __name__ == '__main__': main()