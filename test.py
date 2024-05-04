list = []
for i in range(50):
    list.append(i)
print(list)






'''import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1000, 800))

screen.fill(THECOLORS['green'])
font = pygame.font.SysFont('couriernew', 25, True)
text = font.render(str('Счет:'), True, THECOLORS['white'])
screen.blit(text, (25, 10))
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    screen.fill(THECOLORS['green'])
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)'''