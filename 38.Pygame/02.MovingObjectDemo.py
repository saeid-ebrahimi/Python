
import pygame
pygame.init()
white = (255, 255, 255)
width = 1000
height = 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("jiggle")
image = pygame.image.load("linux_logo.png")

y = 100
x = 100
while True:
    surface.fill(white)
    surface.blit(image, (0,0))
    event = pygame.event.wait()
    # print(pygame.event.get())
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            y -= 20
            if y == 0:
                y = height
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            y += 20
            if y == height:
                y = 0
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            x -= 20
            if x == 0:
                x = width
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            x += 20
            if x == width:
                x = 0
    pygame.draw.rect(surface, (255,100,100),pygame.Rect(x,y,100,100))
    #  Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any
    #  updates that you make on the game screen to make visible.
    pygame.display.flip()



