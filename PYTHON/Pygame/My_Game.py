#Initializing the pygame module to make the game
import pygame
import random
pygame.init()
SCREENWIDTH = 900
SCREENHEIGHT = 600
#Making the gamewindow for the game
gamewindow = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
#Initializing all the colors for the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 100, 0)
#Creating the main function from whre our game will start
def Gameloop():
    #Initializing the game specific variables
    exit_game = False
    game_ove = False
    snake_x = 44
    snake_y = 45
    food_x = random.randint(255, SCREENHEIGHT/2)
    food_y = random.randint(255, SCREENWIDTH/2)
    velocity_x = 0
    velocity_y = 0
    snake_size = 30
    food_size = 30
    score = 0
    FPS = 30
    FPSCLOCK = pygame.time.Clock()
    #Starting our mainloop
    while not exit_game:
        #Filling the gamewindow with colors and ploting the snake, food
        gamewindow.fill(white)
        pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, food_size])
        pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
        #Handling the events for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                if event.key == pygame.K_RIGHT:
                    velocity_x += 10
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y += 10
                    velocity_x = 0
        snake_x += velocity_x
        snake_y += velocity_y
        if abs(food_x - snake_x)<6 or abs(food_y - snake_y)<6:
                score += 10
                print(f"Your score is: {score}")
        pygame.display.update()
        #Updating the display of the game
        pygame.display.update()
        #setting the fps for the game
        FPSCLOCK.tick(FPS)
Gameloop()