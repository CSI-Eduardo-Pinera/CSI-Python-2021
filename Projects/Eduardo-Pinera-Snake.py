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
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, blue,[200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()