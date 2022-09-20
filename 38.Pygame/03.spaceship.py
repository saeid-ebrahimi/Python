
import pygame
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,255)
FPS = 60
VEL = 5
BULLET_VEL = 7
RED_HIT = pygame.USEREVENT + 1
NAVY_HIT = pygame.USEREVENT + 2
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 90, 70
BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
BULLET_HIT_SOUND = pygame.mixer.Sound("sounds/mixkit-shatter-shot-explosion-1693.wav")
#BULLET_FIRE_SOUND = pygame.mixer.Sound("sounds/mixkit-shatter-shot-explosion-1693.wav")
HEALTH_FONT = pygame.font.SysFont("comicsans",20)
WINNER_FONT = pygame.font.SysFont("comicsans",40)
SPACE = pygame.transform.scale(pygame.image.load("./images/space.jpg"),(WIDTH,HEIGHT))
NAVY_SPACESHIP_IMAGE = pygame.image.load("./images/navy.png")
NAVY_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(NAVY_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
PINK_SPACESHIP_IMAGE = pygame.image.load("./images/pink.png")
PINK_SPACESHIP_IMAGE = pygame.transform.scale(PINK_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load("./images/red.png")
RED_SPACESHIP_IMAGE = pygame.transform.rotate( pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
PURPLE_SPACESHIP_IMAGE = pygame.image.load("./images/purple.png")
PURPLE_SPACESHIP_IMAGE = pygame.transform.scale(PURPLE_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
pygame.display.set_caption("Spaceship Game")


def draw_window(red,navy,red_bullets, navy_bullets,red_health,navy_health):
    # WIN.fill(WHITE)
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("HEALTH: "+ str(red_health),False,WHITE)
    navy_health_text = HEALTH_FONT.render("HEALTH: " + str(navy_health),False,WHITE)
    WIN.blit(red_health_text,(10,10))
    WIN.blit(navy_health_text,(WIDTH-navy_health_text.get_width()-10,10))
    WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))
    WIN.blit(NAVY_SPACESHIP_IMAGE,(navy.x,navy.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in navy_bullets:
        pygame.draw.rect(WIN,BLUE,bullet)
    pygame.display.update()


def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_a]:  # left
        if red.x >= 0:
            red.x -= VEL
    if key_pressed[pygame.K_d]:  # right
        if red.x <= WIDTH / 2 - SPACESHIP_WIDTH:
            red.x += VEL
    if key_pressed[pygame.K_w]:  # up
        if red.y >= 20:
            red.y -= VEL
    if key_pressed[pygame.K_s]:  # south
        if red.y <= HEIGHT - SPACESHIP_HEIGHT:
            red.y += VEL


def navy_handle_movement(key_pressed, navy):
    if key_pressed[pygame.K_LEFT]:  # left
        if navy.x >= WIDTH/2 :
            navy.x -= VEL
    if key_pressed[pygame.K_RIGHT]:  # right
        if navy.x <= WIDTH - SPACESHIP_WIDTH:
            navy.x += VEL
    if key_pressed[pygame.K_UP]:  # up
        if navy.y >= 20:
            navy.y -= VEL
    if key_pressed[pygame.K_DOWN]:  # south
        if navy.y <= HEIGHT - SPACESHIP_HEIGHT:
            navy.y += VEL


def handle_bullets(red_bullets,navy_bullets,red,navy):
    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if navy.colliderect(bullet):
            pygame.event.post(pygame.event.Event(NAVY_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

    for bullet in navy_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            navy_bullets.remove(bullet)
        elif bullet.x < 0:
            navy_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
def main():
    red = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    navy = pygame.Rect(700,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    red_bullets = []
    navy_bullets = []
    red_health = 5
    navy_health = 5
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 -2,10,5)
                    red_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play(1,1,3)
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(navy.x , navy.y+navy.height//2 +2,10,5)
                    navy_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play(1,1,3)
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == NAVY_HIT:
                navy_health -= 1
                BULLET_HIT_SOUND.play()
        text = ""
        if red_health <= 0:
            text = "Right Hand Wins!"
        if navy_health <=0:
            text = "Left Hand Wins!"
        if text != "":
            draw_winner(text)
            break
        key_pressed = pygame.key.get_pressed()
        red_handle_movement(key_pressed,red)
        navy_handle_movement(key_pressed,navy)
        handle_bullets(red_bullets,navy_bullets,red,navy)
        draw_window(red,navy,red_bullets,navy_bullets,red_health,navy_health)

    main()
if __name__ == "__main__":
    main()