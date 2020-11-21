# Importing Python Libraries
import pygame
import random
import os
#Initialize Pygame
pygame.mixer.init()
pygame.init()
#Constants for screen size
screen_width = 900
screen_height = 600
#Set Game Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimg = pygame.image.load('back.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,128,0)
pink = (255,192,203)
orange = (255,165,0)
blue = (0, 0, 255)
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
with open("hiscore.txt", "r")as f:
    hiscore = f.read()
# Function for the screen text
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
# Function for plotting snake on the screen
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size,  snake_size])
# Display Welcome screen
def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWindow.fill(pink)
        text_screen("Welcome to snakes", green, 260, 250)
        text_screen("Press space bar to play", green, 240, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
# gameloop designed to play game muliple time after getting over
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(25, screen_width/2)
    food_y = random.randint(25, screen_height/2)
    food_size = 30
    snake_size = 30
    init_velocity = 10
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
         hiscore = f.read()
    fps = 30
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.fill(orange)
            text_screen("Game Over ! Press Enter To Continue", red, 100, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome_screen()
        else:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0 
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10
            snake_x += velocity_x
            snake_y +=velocity_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score  +=10
                food_x = random.randint(25, screen_width/2)
                food_y = random.randint(25, screen_height/2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
            gameWindow.blit(bgimg, (0, 0))   
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), blue, 5,5 )
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size ] )
        
            head = []   
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    game_over = True
                    pygame.mixer.music.load('hit.mp3')
                    pygame.mixer.music.play()

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('hit.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list,  snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome_screen()