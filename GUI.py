import pygame
import settings
Vector2 = pygame.Vector2

GUI_objects = []

def init():
    global font 
    global screen 
    font = pygame.font.SysFont('Comic Sans', 20)
    screen = pygame.display.get_surface()

# def update(): #splitting these two into seperate funcs is a bit inefficient but I like to keep these separate
#     object: GUI_objects
#     for object in GUI_objects:
#         object.update()

def render():
    screen.fill(settings.BACKGROUND_COLOUR)

    object: GUI_objects
    for object in GUI_objects:
        object.render()

class GUIObject:
    def __init__(self, position, size) -> None:
        self.pos = position
        self.size = size
        GUI_objects.append(self)

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

class Box(GUIObject):
    def __init__(self, position: Vector2, size: Vector2, colour: str) -> None:
        super().__init__(position, size)
        self.colour = colour
        self.Rect = pygame.Rect(position, size)

    def render(self) -> None:
        super().render()
        pygame.draw.rect(screen, self.colour, self.Rect)

class TextBox(Box):
    def __init__(self, position: Vector2, size: Vector2, colour: pygame.Color, text:str, text_colour: pygame.Color) -> None:
        super().__init__(position, size, colour)
        self.text = text
        self.text_colour = text_colour

    def render(self) -> None:
        super().render()
        screen.blit(font.render(self.text, True, self.text_colour), self.pos)

