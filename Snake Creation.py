import pygame, random, time

pygame.init()

#Creation of window
window_size = 600
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake Creation")
button = pygame.image.load('assets/buttons/button1.png')
buttonFont = pygame.font.SysFont("comicsansms", 18, 1, 1)


class Snake():
    def __init__(self, initX, initY):
        #Snake
        self.initX = initX
        self.initY = initY
        self.snakeBlocksSize = 20
        self.snakeSpeed = 7
        self.snakeChainList = []
        self.snakeLength = 1
        self.changeX = 0
        self.changeY = 0
        self.hitbox = (self.initX, self.initY, self.snakeBlocksSize, self.snakeBlocksSize)
        self.hit = pygame.Rect(self.hitbox)
    def drawSnake(self, snakeBlocksSize, snakeChainList, color):
        self.hitbox = (self.initX, self.initY, self.snakeBlocksSize, self.snakeBlocksSize)
        self.hit = pygame.Rect(self.hitbox)
        #Move Snake
        for block in snakeChainList:
            pygame.draw.rect(screen, color, [block[0], block[1], snakeBlocksSize, snakeBlocksSize])

class Apple():
    def __init__(self, xpos = None, ypos = None):
        self.radius = 10
        self.xpos = xpos
        self.ypos = ypos
        self.hitbox = (-10, -10, 10, 10)
        self.hit = pygame.Rect(self.hitbox)
    def newApple(self, screen):
        self.xpos = round(random.randrange(0, window_size - self.radius) / 20) * 20 + 10
        self.ypos = round(random.randrange(0, window_size - self.radius) / 20) * 20 + 10
        self.hitbox = (self.xpos - self.radius, self.ypos - self.radius, self.radius * 2, self.radius *2)
        self.hit = pygame.Rect(self.hitbox)
        self.drawApple(screen)
    def drawApple(self, screen):
        pygame.draw.circle(screen, "blue", (self.xpos, self.ypos), self.radius)
    
def generateApples(screen, applecount):
    apples = []

    for _ in range(applecount):
        apple = Apple()
        apple.newApple(screen)
        apples.append(apple)
        
    return apples

def play(twoPlayer):
    gameEnd = 1
    drop = True
    apples = generateApples(screen, 1)
    twoPlayer = twoPlayer
    if twoPlayer:
        snake = Snake(window_size/2 + 25, window_size/2)
        snake2 = Snake(window_size/2 - 25, window_size/2)
    else:
        snake = Snake(window_size/2, window_size/2)
    while drop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drop = False
        screen.fill("green")
        if twoPlayer:
            #Update snake list
            snake2Head = []
            snake2Head.append(snake2.initX)
            snake2Head.append(snake2.initY)
            snake2.snakeChainList.append(snake2Head)
            if len(snake2.snakeChainList) > snake2.snakeLength:
                del snake2.snakeChainList[0]
            
            snake2.initX += snake2.changeX
            snake2.initY += snake2.changeY
            snake2.drawSnake(snake2.snakeBlocksSize, snake2.snakeChainList, "blue")
            
                
        
        
        #Update snake list
        snakeHead = []
        snakeHead.append(snake.initX)
        snakeHead.append(snake.initY)
        snake.snakeChainList.append(snakeHead)
        if len(snake.snakeChainList) > snake.snakeLength:
            del snake.snakeChainList[0]
        
        snake.initX += snake.changeX
        snake.initY += snake.changeY
        snake.drawSnake(snake.snakeBlocksSize, snake.snakeChainList, "red")

        
        for apple in apples:
            apple.drawApple(screen)    
            if snake.hit.colliderect(apple.hit):
                print("hit")
                apples.pop(apples.index(apple))
                snake.snakeLength += 1
                apples = generateApples(screen, 1)
            if twoPlayer:
                if snake2.hit.colliderect(apple.hit):
                    print("hit")
                    apples.pop(apples.index(apple))
                    snake2.snakeLength += 1
                    apples = generateApples(screen, 1)
        
        
        
        
        #Frames
        clock = pygame.time.Clock()
        clock.tick(snake.snakeSpeed)

        #Keyboard Event
        KEYS = pygame.key.get_pressed()
        if KEYS[pygame.K_LEFT]:
            snake.changeX = -snake.snakeBlocksSize
            snake.changeY = 0
        elif KEYS[pygame.K_RIGHT]:
            snake.changeX = snake.snakeBlocksSize
            snake.changeY = 0
        elif KEYS[pygame.K_UP]:
            snake.changeX = 0
            snake.changeY = -snake.snakeBlocksSize
        elif KEYS[pygame.K_DOWN]:
            snake.changeX = 0
            snake.changeY = snake.snakeBlocksSize
        if twoPlayer:
            if KEYS[pygame.K_a]:
                snake2.changeX = -snake2.snakeBlocksSize
                snake2.changeY = 0
            elif KEYS[pygame.K_d]:
                snake2.changeX = snake2.snakeBlocksSize
                snake2.changeY = 0
            elif KEYS[pygame.K_w]:
                snake2.changeX = 0
                snake2.changeY = -snake2.snakeBlocksSize
            elif KEYS[pygame.K_s]:
                snake2.changeX = 0
                snake2.changeY = snake2.snakeBlocksSize

        if twoPlayer:
            if -20 > snake2.initX or snake2.initX > window_size or -20 > snake2.initY or snake2.initY > window_size:
                gameEnd = 0
                break
            if -20 > snake.initX or snake.initX > window_size or -20 > snake.initY or snake.initY > window_size:
                gameEnd = 0
                break
        else:
            if -20 > snake.initX or snake.initX > window_size or -20 > snake.initY or snake.initY > window_size:
                gameEnd = 0
                break
        pygame.display.flip()
        
    if gameEnd == 0:
        DrawEMenu()

def DrawEMenu():
    endMenu = True
    while endMenu:
        #Will cause program to not respond if missing.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endMenu = False
                pygame.quit()
        screen.fill("black")
        pygame.display.flip()


def DrawMMenu():
    mainMenu = True
    while mainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseXPos, mouseYPos = pygame.mouse.get_pos()

                #Checks if mouse is on start button
                if (window_size/2 - 64) <= mouseXPos <= (window_size/2 - 64) + 128 and window_size/2 - 66 <= mouseYPos <= window_size/2 - 10:
                    twoPlayer = False
                    mainMenu = False
                    play(twoPlayer)

                elif (window_size/2 - 64) <= mouseXPos <= (window_size/2 - 64) + 128 and window_size/2 <= mouseYPos <= window_size/2 + 56:
                    twoPlayer = True
                    mainMenu = False
                    play(twoPlayer)
                elif (window_size/2 - 64) <= mouseXPos <= (window_size/2 - 64) + 128 and window_size/2 + 66 <= mouseYPos <= window_size/2 + 122:
                    mainMenu = False
                    pygame.quit()
                
        screen.fill("black")
        screen.blit(button, (window_size/2 - 64, window_size/2 - 66))
        buttonSingle = buttonFont.render("Singleplayer", 1, "black")
        screen.blit(buttonSingle, (window_size/2 - 52, window_size/2 - 56))
        screen.blit(button, (window_size/2 - 64, window_size/2))
        buttonDouble = buttonFont.render("Two player", 1, "black")
        screen.blit(buttonDouble, (window_size/2 - 48, window_size/2 + 16))
        screen.blit(button, (window_size/2 - 64, window_size/2 + 66))
        buttonExit = buttonFont.render("Exit", 1, "black")
        screen.blit(buttonExit, (window_size/2 - 24, window_size/2 + 80))
        pygame.display.flip()


def main():
    DrawMMenu()

main()