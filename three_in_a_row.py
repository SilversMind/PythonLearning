#! /usr/bin/python
# -*- coding: utf-8 -*-

from basics_classes.player_class import Player


def main():
    player_1 = Player('Barnabé', 'o')
    player_2 = Player('Mauricio', 'x')
    player_3 = Player('Marvin Serviette', '&')
    list_player = (player_1, player_2, player_3)
    Player.quadrillage()
    last_player = list_player[0]
    while not last_player.check_connect():
        i = 0
        while not last_player.check_connect() and i < len(list_player):
            last_player = list_player[i]
            last_player.ask_coordinates()
            Player.quadrillage()
            i += 1
    print('{} wins with the move {}'.format(last_player.name, last_player.check_connect()))


if __name__ == '__main__': main()
