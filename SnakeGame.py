#############################################################################
##     _____                _____           _                _             ##
##    |  __ \              / ____|         | |              | |            ##
##    | |__) |___  _ __   | (___   __ _  __| | _____   _____| | ___   _    ##
##    |  _  // _ \| '_ \   \___ \ / _` |/ _` |/ _ \ \ / / __| |/ / | | |   ##
##    | | \ \ (_) | | | |  ____) | (_| | (_| | (_) \ V /\__ \   <| |_| |   ##
##    |_|  \_\___/|_| |_| |_____/ \__,_|\__,_|\___/ \_/ |___/_|\_\\__, |   ##
##                                                                __/ |    ##
##                                                               |___/     ##
## Description: Snake Game                                                 ##
## Due Date: Saturday, December 3, 2016                                    ##
##                                                                         ##
#############################################################################

import pygame
pygame.init()

from random import randint
from math import sqrt

HEIGHT = 600
WIDTH  = 800

screen=pygame.display.set_mode((WIDTH,HEIGHT))

#image declarations
snakeheadup = pygame.image.load("snakeheadup.png")
snakeheadup = pygame.transform.scale(snakeheadup,(30,30))

snakeheaddown = pygame.image.load("snakeheaddown.png")
snakeheaddown = pygame.transform.scale(snakeheaddown,(30,30))

snakeheadright = pygame.image.load("snakeheadright.png")
snakeheadright = pygame.transform.scale(snakeheadright,(30,30))

snakeheadleft = pygame.image.load("snakeheadleft.png")
snakeheadleft = pygame.transform.scale(snakeheadleft,(30,30))

snakevbody = pygame.image.load("snakevbody.png")
snakevbody = pygame.transform.scale(snakevbody,(30,30))

snakehbody = pygame.image.load("snakehbody.png")
snakehbody = pygame.transform.scale(snakehbody,(30,30))

snaketailup = pygame.image.load("snaketailup.png")
snaketailup = pygame.transform.scale(snaketailup,(30,30))

snaketaildown = pygame.image.load("snaketaildown.png")
snaketaildown = pygame.transform.scale(snaketaildown,(30,30))

snaketailright = pygame.image.load("snaketailright.png")
snaketailright = pygame.transform.scale(snaketailright,(30,30))

snaketailleft = pygame.image.load("snaketailleft.png")
snaketailleft = pygame.transform.scale(snaketailleft,(30,30))

snakeLTD = pygame.image.load("snakeLTD.png")
snakeLTD = pygame.transform.scale(snakeLTD,(28,28))

snakeLTU = pygame.image.load("snakeLTU.png")
snakeLTU = pygame.transform.scale(snakeLTU,(28,28))

snakeRTU = pygame.image.load("snakeRTU.png")
snakeRTU = pygame.transform.scale(snakeRTU,(28,28))

snakeRTD = pygame.image.load("snakeRTD.png")
snakeRTD = pygame.transform.scale(snakeRTD,(28,28))

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

background2 = pygame.image.load("background2.jpg")
background2 = pygame.transform.scale(background2,(WIDTH,HEIGHT))

background3 = pygame.image.load("background3.jpg")
background3 = pygame.transform.scale(background3,(WIDTH,HEIGHT))

apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple,(30,39))

greenapple = pygame.image.load("greenapple.png")
greenapple = pygame.transform.scale(greenapple,(30,39))

spikes = pygame.image.load("spikes.png")
spikes = pygame.transform.scale(spikes,(55,55))

startimage = pygame.image.load("startscreen.jpg")
startimage = pygame.transform.scale(startimage,(WIDTH,HEIGHT))

gameover = pygame.image.load("gameover.jpg")
gameover = pygame.transform.scale(gameover,(WIDTH,HEIGHT))

flames = [0]*100
currentFrame = 1

for i in range(len(flames)): #uploading all images in a sprite
    imageName = "frame_"+str(i)+"_delay-0.1s.gif"
    flames[i] = pygame.image.load(imageName)
    flames[i] = pygame.transform.scale(flames[i],(87,300))

font = pygame.font.SysFont("Default",45)
font2 = pygame.font.SysFont("Default",28)
font3 = pygame.font.SysFont("Default",33)

text1 = font.render("SNAKE GAME",2,(142,242,0))
text2 = font2.render("Use arrow keys to control your snake",1,(142,242,0))
text3 = font2.render("Eat red apples to gain points and grow in length",1,(142,242,0))
text4 = font2.render("There are 3 levels - you move up a level every 10 points",1,(142,242,0))
text5 = font2.render("Avoid green apples - they make your snake shorter",1,(142,242,0))
text6 = font2.render("Watch out for spikes and flames (level 3 only) - they kill your snake",1,(142,242,0))
text7 = font.render("Press SPACE to begin playing",1,(142,242,0))
text8 = font.render("GAME OVER",3,(255,0,0))

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
outline=0

#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 10
HSPEED = 20
VSPEED = 20

speedX = 0
speedY = -VSPEED
segx = [int(WIDTH/2.)]*3
segy = [HEIGHT, HEIGHT+VSPEED, HEIGHT+2*VSPEED]

hpos = [False]*1000

turnRD = [False]*100 #checks which turn image should be used
turnRU = [False]*100
turnLU = [False]*100
turnLD = [False]*100

level = 1

appleX = randint(15,WIDTH-15)
appleY = randint(15,HEIGHT-15)

greenappleX = randint(15,WIDTH-15)
greenappleY = randint(15,HEIGHT-15)

spikesX = randint(15,WIDTH-15)
spikesY = randint(15,HEIGHT-15)

flamesX = randint(50,WIDTH-50)
flamesY = randint(50,WIDTH-50)

startgame = False

startScr = True

gameOver = False

score = 0

timer = 20

greenappleVis = False #checks whether obstacles are visible or not
gaTimer = 10 #amount of time that obstacles are visible if not collided with

spikesVis = False
sTimer = 10

flamesVis = False
fTimer = 10

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#

def distance(x1, y1, x2, y2): #calculates distance between two points
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def startscreen():
    screen.blit(startimage,(0,0))
    screen.blit(text1,(300,55))
    screen.blit(text2,(100,125))
    screen.blit(text3,(100,145))
    screen.blit(text4,(100,165))
    screen.blit(text5,(100,185))
    screen.blit(text6,(100,205))
    screen.blit(text7,(150,450))

def endscreen():
    screen.fill(BLACK)
    screen.blit(gameover,(0,0))
    text15 = font3.render("Your score was "+str(score),1,(255,0,0))
    screen.blit(text8,(325,250))
    screen.blit(text15,(325,400))
    
def redraw_screen():
    if level==1: #different backgrounds each level
        screen.blit(background,(0,0))
    if level==2:
        screen.blit(background2,(0,0))
    if level==3:
        screen.blit(background3,(0,0))

    text9 = font3.render("Score: "+str(score),1,(142,242,0))
    text10 = font3.render("Time: "+str(int(round(timer)))+" seconds",1,(142,242,0))
    text11 = font3.render("Level: "+str(level),1,(142,242,0))
    screen.blit(text9,(600,25))
    screen.blit(text10,(60,25))
    screen.blit(text11,(360,25))

    if speedY==-VSPEED:
        screen.blit(snakeheadup,(segx[0]-15,segy[0]-15))
    if speedY == VSPEED:
        screen.blit(snakeheaddown,(segx[0]-15,segy[0]-15))
    if speedX == -HSPEED:
        screen.blit(snakeheadleft,(segx[0]-15,segy[0]-15))
    if speedX == HSPEED:
        screen.blit(snakeheadright,(segx[0]-15,segy[0]-15))

    if segx[len(segx)-1]+20 == segx[len(segx)-2]:
        screen.blit(snaketailright,(segx[len(segx)-1]-15,segy[len(segy)-1]-15))
    if segx[len(segx)-1]-20 == segx[len(segx)-2]:
        screen.blit(snaketailleft,(segx[len(segx)-1]-15,segy[len(segy)-1]-15))
    if segy[len(segy)-1]+20 == segy[len(segy)-2]:
        screen.blit(snaketaildown,(segx[len(segx)-1]-15,segy[len(segy)-1]-15))
    if segy[len(segy)-1]-20 == segy[len(segy)-2]:
        screen.blit(snaketailup,(segx[len(segx)-1]-15,segy[len(segy)-1]-15))

    for i in range(1,len(segx)-1):
        
        segmentCLR = (randint(0,255),randint(0,255),randint(0,255))
        
        if turnRD[i]:
            screen.blit(snakeRTD,(segx[i]-15,segy[i]-15))
        elif turnRU[i]:
            screen.blit(snakeRTU,(segx[i]-15,segy[i]-15))
        elif turnLD[i]:
            screen.blit(snakeLTD,(segx[i]-15,segy[i]-15))
        elif turnLU[i]:
            screen.blit(snakeLTU,(segx[i]-15,segy[i]-15))
        elif hpos[i]:
            screen.blit(snakehbody,(segx[i]-15,segy[i]-15))
        else:
            screen.blit(snakevbody,(segx[i]-15,segy[i]-15))
                
    screen.blit(apple,(appleX-15,appleY-15))

    if greenappleVis:
        screen.blit(greenapple,(greenappleX-15,greenappleY-15))

    if spikesVis:
        screen.blit(spikes,(spikesX-20,spikesY-20))
    
    if flamesVis:
        screen.blit(flames[currentFrame],(flamesX-20,flamesY-150))
        

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#

inPlay = True

while inPlay:

    # check for events

    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            inPlay = False               # Flag that we are done so we exit this loop

    keys = pygame.key.get_pressed()
    
    if startgame==False and startScr:
        startscreen()

    if keys[pygame.K_SPACE] and gameOver==False: #start game is space is pressed
        startgame = True
        startScr = False
        
    if startgame:
        
    # act upon key events

        if timer>0:
            timer-=0.1
            
        if keys[pygame.K_LEFT] and speedX!=HSPEED:
            speedX = -HSPEED
            speedY = 0
        if keys[pygame.K_RIGHT] and speedX!=-HSPEED:
            speedX = HSPEED
            speedY = 0
        if keys[pygame.K_UP] and speedY!=VSPEED:
            speedX = 0
            speedY = -VSPEED
        if keys[pygame.K_DOWN] and speedY!=-VSPEED:
            speedX = 0
            speedY = VSPEED
            
        if distance(segx[0],segy[0],appleX+10,appleY+10) <= 10+BODY_SIZE:#if segx[0]<appleX+10 and segx[0]>appleX-10 and segy[0]<appleY+10 and segy[0]>appleY-20: #or keys[pygame.K_SPACE]: # if space bar is pressed, add a segment:
            segx.append(segx[-1])           # assign the same x and y coordinates
            segy.append(segy[-1])           # as those of the last segment
            appleX = randint(20,WIDTH-20)
            appleY = randint(20,HEIGHT-20)
            timer = 20
            score+=1

        if score>=10 and score<=19:
            level = 2

        if score>=20:
            level = 3
    
        # move all segments
        for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
            segx[i]=segx[i-1]               # every segment takes the coordinates
            segy[i]=segy[i-1]               # of the previous one

    # move the head
        segx[0] = segx[0] + speedX
        segy[0] = segy[0] + speedY

    #determines the positions of each snake segment
        
        for i in range(1,len(segx)-1):
            if segy[i] == segy[i+1] and segy[i] == segy[i-1]:
                hpos[i] = True
            else:
                hpos[i] = False
     
            if segy[i] == segy[i+1]-20 and segx[i] == segx[i-1]+20: #left, up
                turnLU[i] = True
            elif segy[i] == segy[i-1]-20 and segx[i] == segx[i+1]+20: #left, up
                turnLU[i] = True
            else:
                turnLU[i] = False
                
            if segx[i] == segx[i+1]-20 and segy[i] == segy[i-1]-20:
                turnRU[i] = True
            elif segx[i] == segx[i-1]-20 and segy[i] == segy[i+1]-20:
                turnRU[i] = True
            else:
                turnRU[i] = False
                
            if segx[i] == segx[i-1]-20 and segy[i] == segy[i+1]+20:
                turnRD[i] = True
            elif segx[i] == segx[i+1]-20 and segy[i] == segy[i-1]+20:
                turnRD[i] = True
            else:
                turnRD[i] = False
                
            if segx[i] == segx[i+1]+20 and segy[i] == segy[i-1]+20:
                turnLD[i] = True
            elif segx[i] == segx[i-1]+20 and segy[i] == segy[i+1]+20:
                turnLD[i] = True
            else:
                turnLD[i] = False

    #code for all the pop-up obstacles in the game
                
        if greenappleVis==False:
            paChance = randint(0,100)
            greenappleX = randint(15,WIDTH-15)
            greenappleY = randint(15,HEIGHT-15)
            gaTimer = 10

        if paChance==1 and len(segx)>3:
            greenappleVis = True

        if greenappleVis:
            gaTimer = gaTimer - 0.1
        if gaTimer<0:
            greenappleVis = False

        if distance(segx[0],segy[0],greenappleX+10,greenappleY+10) <= 10+BODY_SIZE and greenappleVis:
            greenappleVis = False
            segx.remove(segx[len(segx)-1])
            segy.remove(segy[len(segy)-1])
            score-=1
        
        if spikesVis==False:
            sChance = randint(0,150)
            spikesX = randint(15,WIDTH-15)
            spikesY = randint(15,HEIGHT-15)
            sTimer = 10
            
        if sChance==1:
            spikesVis = True

        if spikesVis:
            sTimer = sTimer - 0.1
        if sTimer<0:
            spikesVis = False

        if distance(segx[0],segy[0],spikesX+20,spikesY+20) <= 20+BODY_SIZE and spikesVis:
            gameOver = True

        if level==3:
            
            if flamesVis==False:
                fChance = randint(0,50)
                flamesX = randint(100,WIDTH-100)
                flamesY = randint(100,WIDTH-100)
                fTimer = 10

            if fChance==1:
                flamesVis = True
            if flamesVis:
                fTimer = fTimer - 0.1
                currentFrame+=1
                if currentFrame >= len(flames):
                    currentFrame = 1
            if fTimer<0:
                flamesVis = False

            if segx[0] < flamesX + 10 and segx[0] > flamesX-10 and segy[0] < flamesY+150 and segy[0] > flamesY-150 and flamesVis:#if distance(segx[0],segy[0],flamesX+10,flamesY+100) <= 20+BODY_SIZE and flamesVis:
                gameOver = True
            
            
        if (segx[0]==WIDTH or segx[0]==0):
            gameOver=True
        if (segy[0]==HEIGHT or segy[0]==0):
            gameOver=True

        for i in range(1,len(segx)):
            if (segx[0]==segx[i] and segy[0]==segy[i]):
                gameOver=True
                
        if timer<0:
            gameOver=True
    
        redraw_screen()

    if gameOver:
        startgame = False
        endscreen()

    pygame.display.update()
    pygame.time.delay(90)
    
pygame.quit()                           # always quit pygame when done!
