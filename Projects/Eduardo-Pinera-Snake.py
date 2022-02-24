import time
import pygame
pygame.init()
red = (245, 0, 0) #Game Over
green = (13, 255, 69) #Snake
redll = (245, 30, 9) #Food
blue = (22, 2, 222) #Score
yellow = (222, 185, 2) #Background
dis_width = 400
dis_height = 300
dis=pygame.dysplay.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.dysplay.set_caption("Snake Game by 6P")
game_over=False
clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10
font_style = pygame.font.SysFont(None, 50)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    while not game_over:
        while game_close == True:
            dis.fill(yellow)
            message("¡YOU LOST! Press Q - QUIT or P - PLAY AGAIN", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)
    pygame.draw.rect(dis, green,[x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)
# time.sleep(5)
pygame.quit()
quit() 