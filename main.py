import life
import time
import pygame
import sys


def main():
    # Screen stuff
    resolution = 20
    S_WIDTH, S_HEIGHT = 600, 600

    # Board state stuff
    width, height = round(S_WIDTH / resolution), round(S_HEIGHT / resolution)
    weight = 0.7

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

    board_state = life.random_state(width, height, weight)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # pygame.draw.rect(screen, pygame.Color(
        #     255, 255, 255), (0, 0, S_WIDTH, S_HEIGHT))
        life.render(board_state, screen, resolution)
        pygame.display.flip()
        board_state = life.next_board_state(board_state)
        time.sleep(.1)


if __name__ == '__main__':
    main()
