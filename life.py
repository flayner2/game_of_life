from typing import List
import random
import copy
import pygame


def random_state(width: int, height: int, weight: float = 0.5) -> List[List]:
    return [[0 if random.random() <= weight else 1 for _ in range(width)] for _ in range(height)]


def render(board_state: List[List], surface, resolution):
    for i, row in enumerate(board_state):
        for j, _ in enumerate(row):
            x, y = i * resolution, j * resolution
            if board_state[i][j] == 1:
                pygame.draw.rect(surface, pygame.Color(
                    0, 0, 0), (x, y, resolution, resolution))
            else:
                pygame.draw.rect(surface, pygame.Color(
                    255, 255, 255), (x, y, resolution, resolution))


def calc_corners(board_state: List[List], i: int, j: int) -> int:
    width = len(board_state[0])
    height = len(board_state)

    if i == 0:
        # Top-left corner
        if j == 0:
            new_cell_state = board_state[i][j+1] + \
                board_state[i+1][j] + board_state[i+1][j+1]
        # Top-right corner
        elif j == width - 1:
            new_cell_state = board_state[i][j-1] + \
                board_state[i+1][j] + board_state[i+1][j-1]
        # Top edge, but not corner
        else:
            new_cell_state = board_state[i][j-1] + board_state[i][j+1] + \
                board_state[i+1][j] + board_state[i+1][j-1] + \
                board_state[i+1][j+1]
    elif i == height - 1:
        # Bottom-left corner
        if j == 0:
            new_cell_state = board_state[i][j+1] + \
                board_state[i-1][j] + board_state[i-1][j+1]
        # Bottom-right corner
        elif j == width - 1:
            new_cell_state = board_state[i][j-1] + \
                board_state[i-1][j] + board_state[i-1][j-1]
        # Bottom edge, but not corner
        else:
            new_cell_state = board_state[i][j-1] + board_state[i][j+1] + \
                board_state[i-1][j] + board_state[i-1][j-1] + \
                board_state[i-1][j+1]

    return new_cell_state


def next_board_state(board_state: List[List]):
    width = len(board_state[0])
    height = len(board_state)
    new_board_state = copy.deepcopy(board_state)

    for i in range(height):
        for j in range(width):
            current_cell_state = board_state[i][j]
            if i == 0 or i == width - 1:
                new_cell_state = calc_corners(board_state, i, j)
            else:
                # Left edge, but not corner:
                if j == 0:
                    new_cell_state = board_state[i-1][j] + board_state[i-1][j+1] + \
                        board_state[i][j+1] + \
                        board_state[i+1][j] + board_state[i+1][j+1]
                # Right edge, but not corner
                elif j == width - 1:
                    new_cell_state = board_state[i-1][j] + board_state[i-1][j-1] + \
                        board_state[i][j-1] + \
                        board_state[i+1][j] + board_state[i+1][j-1]
                else:
                    new_cell_state = board_state[i-1][j] + board_state[i-1][j-1] + \
                        board_state[i-1][j+1] + board_state[i][j-1] + board_state[i][j+1] + \
                        board_state[i+1][j] + board_state[i+1][j-1] + \
                        board_state[i+1][j+1]

            if current_cell_state == 1:
                # Rule 1: live with 0 or 1 live neighbor, becomes dead
                if new_cell_state <= 1:
                    new_board_state[i][j] = 0
                # Rule 2: live with 2 or 3 live neighbors, stays alive
                # Rule 3: live with > 3 live neighbors, becomes dead
                elif new_cell_state > 3:
                    new_board_state[i][j] = 0
            else:
                # Rule 4: dead with exactly 3 neighbors, becomes alive
                if new_cell_state == 3:
                    new_board_state[i][j] = 1

    return new_board_state
