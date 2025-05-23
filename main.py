import asyncio
import pygame
import sys
import player as pl
import mysprites as sp
import Enemy as en
import powerUPs as pUP
from random import randint



gameRunning = True
gameWindowSize = [600, 800]
spawnCount = 0


#start game
pygame.init()
gameWindow = pygame.display.set_mode(gameWindowSize)
pygame.display.set_caption("Game")
background = pygame.image.load("background.png").convert()
backgroundY = 0
winScreen = pygame.image.load("winScreen.png")


#Frameratelimiter
clock = pygame.time.Clock()
FPS = 120

#create player
player = pl.Player([280, 600])
sp.allSprites.add(player)

#create first enemy and start spawntimer
enemy = en.EasyEnemy(350,300)
sp.allSprites.add(enemy)
sp.enemySprites.add(enemy)
spawnCount += 1
lastSpawn = 10000
lastPowerUPSpawn = - 5000


def drawGame():
    
    #Scrolling Background
    global backgroundY
    backgroundY += 1
    relBackgroundY = backgroundY % background.get_rect().height
    gameWindow.blit(background, (0,relBackgroundY - background.get_rect().height))
    if relBackgroundY < gameWindowSize[1]:
        gameWindow.blit(background,(0, relBackgroundY))

    #draw allSprites and interface
    sp.allSprites.draw(gameWindow)
    sp.drawLives(gameWindow, player.lives, sp.live)

    #display winner
    if en.killCount == 103:
        gameWindow.blit(winScreen,(100,100))

    pygame.display.update()

def handle_events():

     for event in pygame.event.get():
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.stopMoveing("Left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.stopMoveing("Right")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.stopMoveing("Up")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.stopMoveing("Down")
            

        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move("Left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move("Right")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move("Up")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move("Down")        

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def spawn():

    global killCount
    global spawnCount
    global lastSpawn
    global lastPowerUPSpawn
    now = pygame.time.get_ticks()

    #Spawn PowerUP 
    powerUPSpawnDelay = 10000
    if now - lastPowerUPSpawn > powerUPSpawnDelay:
        lastPowerUPSpawn = now
        powerUP = pUP.PowerUP()
        sp.allSprites.add(powerUP)
        sp.powerUPList.add(powerUP)

    #Spawn Enemys
    if en.killCount <= 9 and spawnCount <= 9:      
        spawnDelay = 3000
        
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint(150,400)
            enemy = en.EasyEnemy(stop, randint(50,550))
            sp.allSprites.add(enemy)
            sp.enemySprites.add(enemy)
            spawnCount += 1

    elif en.killCount <= 24 and spawnCount <= 24:

        spawnDelay = 4000
        
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint(150,400)
            enemy1 = en.EasyEnemy(stop,260)
            enemy2 = en.EasyEnemy(stop,300)
            enemy3 = en.EasyEnemy(stop,340)

            sp.allSprites.add(enemy1)
            sp.enemySprites.add(enemy1)
            sp.allSprites.add(enemy2)
            sp.enemySprites.add(enemy2)
            sp.allSprites.add(enemy3)
            sp.enemySprites.add(enemy3)
            spawnCount += 3

    elif en.killCount <= 30 and spawnCount <= 30:
        spawnDelay = 2000
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint (150,400)
            enemy = en.HarderEnemy(stop,randint(50,500))
            sp.allSprites.add(enemy)
            sp.enemySprites.add(enemy)
            spawnCount += 1

    elif en.killCount <= 50 and spawnCount <= 50:
        spawnDelay = 2000
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint (150,400)
            enemy = en.FasterEnemy(stop,randint(50,550))
            sp.allSprites.add(enemy)
            sp.enemySprites.add(enemy)
            spawnCount += 1

    elif en.killCount <= 55 and spawnCount <= 55:
        spawnDelay = 5000
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint (150,400)
            enemy = en.HardEnemy(stop,randint(50,450))
            sp.allSprites.add(enemy)
            sp.enemySprites.add(enemy)
            spawnCount += 1

    elif en.killCount <= 76 and spawnCount <= 76:
        spawnDelay = 2000
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint (150,400)
            spawn = randint(50,450)
            enemy1 = en.HarderEnemy(stop,spawn)
            enemy2 = en.HarderEnemy(stop,spawn+50)
            sp.allSprites.add(enemy1)
            sp.enemySprites.add(enemy1)
            sp.allSprites.add(enemy2)
            sp.enemySprites.add(enemy2)
            spawnCount += 2
            
    elif en.killCount <= 100 and spawnCount <= 100:

        spawnDelay = 1000
        
        if now - lastSpawn > spawnDelay:
            lastSpawn = now
            stop = randint(150,400)
            enemy1 = en.FasterEnemy(stop,260)
            enemy2 = en.FasterEnemy(stop,300)
            enemy3 = en.FasterEnemy(stop,340)

            sp.allSprites.add(enemy1)
            sp.enemySprites.add(enemy1)
            sp.allSprites.add(enemy2)
            sp.enemySprites.add(enemy2)
            sp.allSprites.add(enemy3)
            sp.enemySprites.add(enemy3)
            spawnCount += 3
            

    elif en.killCount == 102 and spawnCount == 102:

        boss = en.Boss(150,220)
        sp.allSprites.add(boss)
        sp.enemySprites.add(boss)
        spawnCount += 1      
    

async def main():


    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices


        spawn()
        sp.allSprites.update()
        drawGame()
        handle_events()
        clock.tick(FPS)

        # pygame.display.update() should go right next line

        await asyncio.sleep(0)  # Very important, and keep it 0

# This is the program entry point:
asyncio.run(main())





    

    

 
   
    
    
    
    
 
    
    
   

   

            
                
      

        
                
            

     
        
