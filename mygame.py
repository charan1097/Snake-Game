#packages 

import pygame
import random
#initialization
pygame.init()
#color variables
red =(255,0,0)
white = (255, 255, 255)
black=(0,0,0)
mode=pygame.display.set_mode((800,600))
mode_width = 800
mode_height = 600
pygame.display.set_caption('snake game')
snake_block = 10
snake_speed = 15
# for music
music =pygame.mixer.music.load('pirates.mp3')
pygame.mixer.music.play(-1)
#for score
def display_score(score):
    font = pygame.font.SysFont("comicsansms", 35)
    txt =font.render("score: "+str(score),True,white)
    mode.blit(txt,[0,0])
#for gameover image
def gameover():
    bg = pygame.image.load("gameover.png")
    mode.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.wait(2000)
#for snake body
def snake(snake_block, snake_list):
    for s in snake_list:
        pygame.draw.rect(mode, red, (s[0], s[1], snake_block, snake_block))
#for game running 
def runTime():
    
    run = True

    x=mode_width/2
    y=mode_height/2

    x_change = 0
    y_change = 0
    snake_List = []
    Length_of_snake = 1
    score =0
 
    foodx = int(round(random.randrange(0, mode_width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, mode_height - snake_block) / 10.0) * 10.0)
    


    while run:
        if score==0:
            pygame.time.delay(200)
        else:
            time = 200
            pygame.time.delay(time-50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0

        if x > mode_width or x < 0 or y >= mode_height or y < 0:
            run = False
            gameover()
            pygame.quit()
        x+=x_change
        y+=y_change
        mode.fill((0,0,0))
        pygame.draw.rect(mode, white, (foodx, foody, snake_block, snake_block))
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for z in snake_List[:-1]:
            if z == snake_Head:
                run = False 
        snake(snake_block, snake_List)
        display_score(Length_of_snake-1)
        pygame.display.update()
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, mode_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, mode_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
            
    gameover()
    pygame.display.update()
    pygame.time.wait(20000)
    pygame.quit()


runTime()


