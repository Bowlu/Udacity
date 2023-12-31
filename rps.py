#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, round_number):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Round {round_number} --")
        print(f"Rock, paper, scissors? > {move1}")
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        if beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1_score += 1
        elif beats(move2, move1):
            print("** PLAYER TWO WINS **")
            self.p2_score += 1
        else:
            print("It's a tie!")
        print(f"Score: Player One {self.p1_score},"
              "Player Two {self.p2_score}\n")

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(3):
            self.play_round(round)
        print("Game over!")
        print(f"Final Scores - Player One: {self.p1_score},"
              "Player Two: {self.p2_score}")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
