#!/usr/bin/python

import sys
import math

possible_moves = ["rock", "paper", "scissors"]

def rock_paper_scissors(n):
    all_moves = [[] for i in range(math.pow(3, n))]

    def play(number):
        count = 0
        while count < math.pow(3, n):
            for i in range(math.pow(3, number)):
                all_moves[count].append()
                count += 1
        play(number - 1)
    play(n)
    return all_moves


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
