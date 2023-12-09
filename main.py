import pygame
pygame.init() #messy :/
import settings
import GUI

Vector2 = pygame.Vector2

def main():
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    GUI.init()

    ALU = ArithmeticLogicUnit()
    CU = ControlUnit()
    RAM = RandomAccessMemory()

    # CU_rect = pygame.Rect(Vector2(10, 10), Vector2(400, 600))
    # PC_rect = pygame.Rect(Vector2(20, 20), Vector2(100, 50))
    # MAR_rect = pygame.Rect(Vector2(20, 80), Vector2(100, 50))

    run = True
    while (run):
        # PC_text = font.render(str(CU.PC), True, 'black')
        # MAR_text = font.render(str(CU.MAR), True, 'black')
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        CU.update()
        GUI.render()

        # pygame.draw.rect(screen, 'grey', CU_rect)
        # pygame.draw.rect(screen, 'darkgrey', PC_rect)
        # screen.blit(PC_text, PC_rect.topleft)
        # pygame.draw.rect(screen, 'darkgrey', MAR_rect)
        # screen.blit(MAR_text, MAR_rect.topleft)

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
        self.MAR:int = 0
        self.MDR:int = 0

        self.CU_rect = GUI.Box(Vector2(10, 10), Vector2(400, 600), 'grey') #i should've made it more like twonk, this is pretty bad :/
        self.PC_rect = GUI.TextBox(Vector2(20, 20), Vector2(100, 50), 'darkgrey', '-', 'black')
        self.MAR_rect = GUI.TextBox(Vector2(20, 80), Vector2(100, 50), 'darkgrey', '-', 'black')
        self.MDR_rect = GUI.TextBox(Vector2(20, 140), Vector2(100, 50), 'darkgrey', '-', 'black')

    def update(self):
        self.PC_rect.text = str(self.PC)
        self.MAR_rect.text = str(self.MAR)
        self.MDR_rect.text = str(self.MDR)
    
    def PC_inc(self) -> None:
        #self.PC = 
        pass

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