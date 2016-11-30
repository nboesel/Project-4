
import random, math, pygame
from pygame.locals import *

counter = 0

def main():

    showstartscreen = 1
    
    while 1:
        ######## CONSTANTS

        WINSIZE = [800,600]
        WHITE = [255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN = [0,255,0]
        BLUE = [0,0,255]
        BLOCKSIZE = [20,20]
        UP = 1
        DOWN = 3
        RIGHT = 2
        LEFT = 4
        MAXX = 760
        MINX = 20
        MAXY = 560
        MINY = 80
        SNAKESTEP = 20
        TRUE = 1
        FALSE = 0
        

        ######## VARIABLES

        direction = RIGHT 
        snakexy = [300,400]
        snakelist = [[300,400],[280,400],[260,400]]
        counter = 0
        score = 0
        appleonscreen = 0
        #applexy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE
        gameregulator = 6
        gamepaused = 0
        growsnake = 0   
        snakegrowunit = 2 
        
        
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('SNAKER')
        screen.fill(BLACK)

        #### show initial start screen
        
        if showstartscreen == TRUE:
            showstartscreen = FALSE

            s = [[180,120],[180,100],[160,100],[140,100],[120,100],[100,100],[100,120],[100,140],[100,160],[120,160],[140,160],[160,160],[180,160],[180,180],[180,200],[180,220],[160,220],[140,220],[120,220],[100,220],[100,200]]
            apple = [100,200]
            
            pygame.draw.rect(screen,GREEN,Rect(apple,BLOCKSIZE))
            pygame.display.flip()
            clock.tick(8)
            
            for e in s:
                pygame.draw.rect(screen,BLUE,Rect(e,BLOCKSIZE))
                pygame.display.flip()
                clock.tick(8)
                
            font = pygame.font.SysFont("arial", 64)
            text_surface = font.render("NAKER", True, BLUE)
            screen.blit(text_surface, (220,180))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Move the snake with the arrow keys to eat the apples", True, BLUE)
            screen.blit(text_surface, (50,300))
            text_surface = font.render("Avoid the walls and yourself !", True, BLUE)
            screen.blit(text_surface, (50,350))
            text_surface = font.render("Press s to start a new game - Press q to quit at any time", True, BLUE)
            screen.blit(text_surface, (50,400))
            text_surface = font.render("Press p to pause r to resume at any time", True, BLUE)
            screen.blit(text_surface, (50,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_s]: break

                clock.tick(10)


        while not snakedead:

            

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[K_LEFT]: newdirection = LEFT
            if pressed_keys[K_RIGHT]: newdirection = RIGHT
            if pressed_keys[K_UP]: newdirection = UP
            if pressed_keys[K_DOWN]: newdirection = DOWN
            if pressed_keys[K_q]: snakedead = TRUE
            if pressed_keys[K_p]: gamepaused = 1

            
            
            while gamepaused == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_r]:
                    gamepaused = 0 
                clock.tick(10)


         

            
            if gameregulator == 6:

               

                if newdirection == LEFT and not direction == RIGHT:
                    direction = newdirection

                elif newdirection == RIGHT and not direction == LEFT:
                    direction = newdirection

                elif newdirection == UP and not direction == DOWN:
                    direction = newdirection

                elif newdirection == DOWN and not direction == UP:
                    direction = newdirection
                    
     
                    

                if direction == RIGHT:
                    snakexy[0] = snakexy[0] + SNAKESTEP
                    if snakexy[0] > MAXX:
                        snakedead = TRUE
                    
                elif direction == LEFT:
                    snakexy[0] = snakexy[0] - SNAKESTEP
                    if snakexy[0] < MINX:
                        snakedead = TRUE
                        
                elif direction == UP:
                    snakexy[1] = snakexy[1] - SNAKESTEP
                    if snakexy[1] < MINY:
                        snakedead = TRUE
                        
                elif direction == DOWN:
                    snakexy[1] = snakexy[1] + SNAKESTEP
                    if snakexy[1] > MAXY:
                        snakedead = TRUE

           
                        
                if len(snakelist) > 3 and snakelist.count(snakexy) > 0: 
                    snakedead = TRUE
                

            
                    
                if appleonscreen == 0:
                    good = FALSE
                    while good == FALSE:
                        x = random.randrange(1,39)
                        y = random.randrange(5,29)
                        applexy = [int(x*SNAKESTEP),int(y*SNAKESTEP)]
                        if snakelist.count(applexy) == 0:
                            good = TRUE
                    appleonscreen = 1

             

                snakelist.insert(0,list(snakexy))
                if snakexy[0] == applexy[0] and snakexy[1] == applexy[1]:
                    appleonscreen = 0
                    score = score + 1
                    growsnake = growsnake + 1
                elif growsnake > 0:
                    growsnake = growsnake + 1
                    if growsnake == snakegrowunit:
                        growsnake = 0
                else:
                    snakelist.pop()
                    
                

                gameregulator = 0


            ###### RENDER THE SCREEN ###############
            
            
            screen.fill(BLACK)
            
           
            pygame.draw.line(screen,BLUE,(0,9),(799,9),20)
            pygame.draw.line(screen,BLUE,(0,590),(799,590),20)
            pygame.draw.line(screen,BLUE,(0,69),(799,69),20)
            
            pygame.draw.line(screen,BLUE,(9,0),(9,599),20)
            pygame.draw.line(screen,BLUE,(789,0),(789,599),20)
            
           
            font = pygame.font.SysFont("arial", 38)
            text_surface = font.render("SNAKER!          Score: " + str(score), True, BLUE)
            screen.blit(text_surface, (50,18))

            
            for element in snakelist:
                pygame.draw.rect(screen,RED,Rect(element,BLOCKSIZE))

            
            pygame.draw.rect(screen,GREEN,Rect(applexy,BLOCKSIZE))

            
            pygame.display.flip()



            gameregulator = gameregulator + 1
            
            clock.tick(25)


        
            
        if snakedead == TRUE:
            screen.fill(BLACK)
            font = pygame.font.SysFont("arial", 48)
            text_surface = font.render("GAME OVER", True, BLUE)
            screen.blit(text_surface, (250,200))
            text_surface = font.render("Your Score: " + str (score), True, BLUE)
            screen.blit(text_surface, (250,300))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Press q to quit", True, BLUE)
            screen.blit(text_surface, (300,400))
            text_surface = font.render("Press n to play again", True, BLUE)
            screen.blit(text_surface, (275,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_n]: break

                clock.tick(10)
    
if __name__ == '__main__':
    main()



