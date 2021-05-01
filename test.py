#! /usr/bin/python3

"""
    Ce script permet aux participants de vérifier que leur soumission 
    est conforme aux consignes.

    Pour lancer la vérification, désarchivez votre soumission dans le dossier
    courant et tapez la commande "./test" ou "python3 test".

    Si la commande de test affiche OK, votre soumission est correcte est résout avec
    succès la grille de sudoku "grid.txt". Sinon, la commande test signale une erreure.
"""

from os import system, path, access, X_OK
from glob import glob


def digit(x):
    return None if x == "?" else int(x)


def load_grid(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(map(digit, line.split(sep=" "))))
    return grid


def print_grid(grid):
    def vline(): print('-'*21, end='\n')
    def pp(x): return "?" if x is None else str(x)
    def triple(i, k): return " ".join([pp(grid[i][k + j]) for j in range(3)])

    for i in range(9):
        if (i % 3 == 0):
            vline()
        print(" | ".join([triple(i, k) for k in range(0, 9, 3)]))
    vline()


def for_all(test, iter):
    for e in iter:
        if not test(e):
            return False
    return True


def check_from(grid, base):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != grid[i][j] and grid[i][j] != None:
                return False
    return True


def check_row_shape(row):
    return len(row) == 9 and for_all(lambda x: type(x) == int and 1 <= x <= 9, row)


def check_shape(grid):
    return len(grid) == 9 and for_all(check_row_shape, grid)


def check_constraints(line):
    return for_all(lambda x: x in line, range(1, 10))


def cols(grid):
    return [[grid[i][j] for i in range(9)] for j in range(9)]


def blocks(grid):
    blocks = []
    for i in range(0, 3):
        for j in range(0, 3):
            blocks.append([grid[m][n] for n in range(j*3, j*3 + 3)
                           for m in range(i*3, i*3 + 3)])
    return blocks


def check_grid(grid, base):
    if not check_shape(grid):
        return False
    if not check_from(grid, base):
        return False
    if not for_all(check_constraints, grid):
        return False
    if not for_all(check_constraints, cols(grid)):
        return False
    if not for_all(check_constraints, blocks(grid)):
        return False
    return True


def test():
    print('Looking for makefile')
    if path.exists("./Makefile"):
        print('[OK] -> executing the makefile')
        if 0 != system("make solver &> make_log"):
            print('[KO] -> error during the execution (see make_log for details)')
            exit(1)
    print('[OK] -> no make file found')
    print('Looking for the solver')
    if path.exists("./solver"):
        print('[OK] -> solver found')
        if not access("./solver", X_OK):
            print('[KO] -> solver is not executable')
            exit(1)
    else:
        print('[KO] -> solver not found')
        exit(1)
    print('Testing the solver')
    print('[OK] -> executing the solver')
    if 0 != system("./solver 2> solver_log < grid.txt > tmp.txt"):
        print('[KO] -> error during the execution (see solver_log for details)')
        exit(1)
    A = load_grid("./grid.txt")
    T = load_grid("./tmp.txt")
    if check_grid(T, A):
        print('[OK] -> the solver successfully solved grid_sol.txt')
    else:
        print('[K0] -> the solver failed at solving grid_sol.txt')
        exit(1)


if __name__ == "__main__":
    test()
