#!/usr/bin/python3
import sys


def solve_nqueens(n):
    def can_place(pos, occupied_positions):
        for i in range(len(occupied_positions)):
            if occupied_positions[i] == pos or \
               occupied_positions[i] - i == pos - len(occupied_positions) or \
               occupied_positions[i] + i == pos + len(occupied_positions):
                return False
        return True

    def place_queens(n, index, occupied_positions,
                     all_occupied_positions):
        if index == n:
            all_occupied_positions.append(occupied_positions[:])
            return

        for i in range(n):
            if can_place(i, occupied_positions):
                occupied_positions.append(i)
                place_queens(n, index + 1, occupied_positions,
                             all_occupied_positions)
                occupied_positions.pop()

    all_occupied_positions = []
    place_queens(n, 0, [], all_occupied_positions)
    return all_occupied_positions


def print_solutions(solutions, n):
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions, n)


if __name__ == '__main__':
    main()
