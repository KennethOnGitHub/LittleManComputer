import pygame
import settings

def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)

    ALU = ArithmeticLogicUnit()
    CU = ControlUnit()
    RAM = RandomAccessMemory()
    

    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(settings.BACKGROUND_COLOUR)
        pygame.display.flip()

class ArithmeticLogicUnit:
    def __init__(self) -> None:
        pass

    def add(num1, num2) -> int:
        return num1 + num2
    
    def sub(num1, num2) -> int:
        return num1 - num2

class ControlUnit:
    def __init__(self) -> None:
        self.PC:int = 0
        self.MAR:int
        self.MDR:int

class RandomAccessMemory:
    def __init__(self) -> None:
        self.mem:int = []

    def getVal(address: int):
        pass

    def setVal(address: int):
        pass

def cycle():
    pass
        


if __name__ == '__main__':
    main()