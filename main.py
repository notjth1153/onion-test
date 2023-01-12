import pygame
from pygame.locals import *

def run():
    pygame.init()
    display = (pygame.display.set_mode(size=(640, 480)))
    onion = (pygame.image.load("images/onion.jpg"))
    displayinfo = pygame.display.Info()
    print(displayinfo)
    display.blit(onion, (0, 0))
    pygame.display.set_caption("onion")
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == quit:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
        display.blit(onion, (0, 0))
        pygame.display.flip()

run()