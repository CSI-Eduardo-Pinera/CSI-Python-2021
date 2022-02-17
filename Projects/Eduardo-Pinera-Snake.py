import pygame
pygame.init()
red = (245, 0, 0) #Game Over
green = (13, 255, 69) #Snake
red_two = (245, 30, 9) #Food
blue = (22, 2, 222) #Score
yellow = (222, 185, 2) #Background
dis=pygame.dysplay.set_mode((400,300))
pygame.display.update()
pygame.dysplay.set_caption("Snake Game by 6P")
game_over=False
x1 = 150
y1 = 150
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)
    pygame.draw.rect(dis, green,[x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit() 