import pygame
import settings

def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    
    program_counter: int = 0
    accumulator:int = 0
    instruction_register: int = 0


    memory:int = []

    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(settings.BACKGROUND_COLOUR)
        pygame.display.flip()


def cycle():
    
        


if __name__ == '__main__':
    main()