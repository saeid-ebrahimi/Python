
import pygame
pygame.init()
white = (255, 255, 255)
surface = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("jiggle")
image = pygame.image.load("linux_logo.png")


while True:
    surface.fill(white)
    surface.blit(image, (0,0))
    # print(pygame.event.get())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #  Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any
    #  updates that you make on the game screen to make visible.
    #pygame.display.flip()

    pygame.display.update()


