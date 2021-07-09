import pygame
import random
pygame.init()

# Colours
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
black=(0,0,0)
blue=(0,0,255)

#Screen
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Himanshu Snake")
pygame.display.update()


clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,colour,x,y):
    screen_text=font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome",white,400,200)
        text_screen("Press Spacebar to play", white, 300, 250)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            pygame.display.update()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()


#GameLoop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 100
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    diff = 8
    score = 0
    fps = 60

    food_x = random.randint(50, screen_width / 1.2)
    food_y = random.randint(50, screen_height / 1.2)

    snk_list = []
    snk_length = 0

    while (not exit_game):
        f=open("highscore.txt","r")
        hscore=f.read()
        f.close()
        if game_over:
            gameWindow.fill(white)
            text_screen(f"Your Score is:{score}", red, 300,100)
            text_screen(f"High Score is:{hscore}",red,300,150)
            text_screen("Game is over.Press Enter to continue",red,110,200)

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        snake_x=snake_x+10
                        velocity_x=diff
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        snake_x=snake_x-10
                        velocity_x=-(diff)
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        snake_y=snake_y-10
                        velocity_y=-(diff)
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        snake_y=snake_y+10
                        velocity_y=(diff)
                        velocity_x=0


            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            gameWindow.fill(blue)

            if (abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15):
                score=score+10
                snk_length=snk_length+5
                food_x = random.randint(50, screen_width / 1.2)
                food_y = random.randint(50, screen_height / 1.2)
            if score>int(hscore):
                hscore=score
                f=open("highscore.txt","w")
                f.write(str(hscore))
                f.close()

            text_screen(f"Score is:{score }", white, 380, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if(len(snk_list)>snk_length):
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            if [snake_x,snake_y] in snk_list[:-1]:
                game_over=True

            plot_snake(gameWindow, black, snk_list, snake_size)

            pygame.draw.rect(gameWindow,red,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size,snake_size])
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    exit()

welcome()