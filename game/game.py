import itertools
from random import shuffle
from typing import List
from colorama import Back, Style
from .flask import Flask


class Game:
    def __init__(self, initial_flasks: list = None, n_empty: int = 2, n_full: int = 4):
        self.__n = n_empty + n_full
        if initial_flasks is None:
            it = range(1, n_full + 1)
            whole = []
            for _ in it:
                whole += it
            whole += it
            shuffle(whole)
            self.flasks: List[Flask] = []
            for i in range(0, n_full * 4, 4):
                self.flasks.append(Flask(whole[i:i + 4]))
        else:
            self.flasks: List[Flask] = []
            for flask in initial_flasks:
                if len(flask) != 4:
                    raise ValueError('One or more of initial flasks is not 1x4 vector')
                self.flasks.append(Flask(flask))
        for i in range(n_empty):
            self.flasks.append(Flask([0, 0, 0, 0]))

    @property
    def flasks(self) -> List['Flask']:
        return self.__flasks

    @flasks.setter
    def flasks(self, val: List['Flask']):
        self.__flasks = val

    '''
    pour_from_to takes effect only if 
        - from flask is not empty
        - to flask is not full
        - from/to flask's last layers are eq
    '''

    @staticmethod
    def get_color(i: int):
        table = [
            Back.BLACK + '  ' + Style.RESET_ALL,
            Back.GREEN + '  ' + Style.RESET_ALL,
            Back.RED + '  ' + Style.RESET_ALL,
            Back.BLUE + '  ' + Style.RESET_ALL,
            Back.YELLOW + '  ' + Style.RESET_ALL,
            Back.MAGENTA + '  ' + Style.RESET_ALL,
            Back.LIGHTBLUE_EX + '  ' + Style.RESET_ALL,
            Back.CYAN + '  ' + Style.RESET_ALL,
        ]
        return table[i]

    def print_game(self):
        print()
        for flask in self.flasks:
            print(flask.id, end='  ')
        print('\n')
        for i in range(4)[::-1]:
            for flask in self.flasks:
                print(self.get_color(flask[i]), end=' ')
            print()

    '''
    Method returns List of from/to indexes of possible moves
    '''

    def get_all_possible_moves(self) -> List[tuple]:
        moves = []
        seq = range(self.__n)
        product = itertools.combinations(seq, r=2)
        for i in product:
            moves.append(self.__get_possible(i[0], i[1]))
        return [item for sublist in moves for item in sublist]

    def __get_possible(self, ind1: int, ind2: int) -> List[tuple]:
        operations = []
        is_empty1 = self.flasks[ind1].is_empty()
        is_empty2 = self.flasks[ind2].is_empty()
        if is_empty1 and is_empty2:
            return operations
        is_full1 = self.flasks[ind1].is_full()
        is_full2 = self.flasks[ind2].is_full()
        if is_full1 and is_full2:
            return operations
        index1 = self.flasks[ind1].get_last_index()
        index2 = self.flasks[ind2].get_last_index()
        match = self.flasks[ind1][index1] == self.flasks[ind2][index2]
        match1 = (match or (is_full1 and is_empty2)) and not is_full2
        match2 = (match or (is_full2 and is_empty1)) and not is_full1

        if match1:
            operations.append((ind1, ind2, index1, index2 + 1))
        if match2:
            operations.append((ind2, ind1, index2, index1 + 1))
        return operations

    def apply_move(self, coordinates: tuple) -> None:
        self.flasks[coordinates[0]].pour_to(self.flasks[coordinates[1]], self_last_index=coordinates[2],
                                            to_flask_last_index=coordinates[3])
