from game.game import Game
from random import randint

if __name__ == '__main__':
    game = Game()
    moves = game.get_all_possible_moves()
    max_iter = 10
    while len(moves) > 0 and max_iter > 0:
        # print(moves)
        game.print_game()
        rand = randint(0, len(moves) - 1)
        game.apply_move(moves[rand])
        moves = game.get_all_possible_moves()
        max_iter -= 1
