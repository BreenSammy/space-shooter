import pygame
import sys
import mysprites as sp
import powerUPs as pUP
import time 


ship = pygame.image.load("PlayerAssets/ship.png")
shipWithShield = pygame.image.load("PlayerAssets/shipWithShield.png")


class Player(pygame.sprite.Sprite):

    movementSpeed = 3
    velocity = [0, 0]
    
    isDead = False

    def __init__(self, startPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship
        self.position = startPos
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        self.shootDelay = 1000
        self.lastShot = pygame.time.get_ticks()
        self.lives = 3
        self.shield = False
        self.weaponLevel = 1
        self.invincible = False
        self.invincibilityTimer = pygame.time.get_ticks()
    

    def move(self, moveDirection):
        if moveDirection == "Left":
            self.velocity[0] = -self.movementSpeed
            
        elif moveDirection == "Right":
            self.velocity[0] = self.movementSpeed

        elif moveDirection == "Up":
            self.velocity[1] = -self.movementSpeed

        elif moveDirection == "Down":
            self.velocity[1] = self.movementSpeed

            
    def stopMoveing(self,moveDirection):
        if moveDirection == "Left" and self.velocity[0] < 0 or moveDirection == "Right" and self.velocity[0] > 0:
            self.velocity[0] = 0
            
        elif moveDirection == "Up" and self.velocity [1] < 0 or moveDirection == "Down" and self.velocity[1] > 0:
            self.velocity[1] = 0

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def upgradeWeapon(self):
        if self.weaponLevel in range(1,5):
            self.shootDelay = self.shootDelay/2

        elif self.weaponLevel in range(6,11):
            self.shootDelay = self.shootDelay/1.25

    def downgradeWeapon(self):
        if self.weaponLevel in range (1,6):
            self.shootDelay = self.shootDelay*2

        elif self.weaponLevel in range (6,11):
            self.shootDelay = self.shootDelay*1.25
        

    def shoot(self):
        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:
            self.lastShot = now

            if self.weaponLevel in range(1,6):
                bullet = sp.Bullet([self.rect.centerx - 6, self.rect.top],sp.bluebullet,1,4)
                sp.playerBullets.add(bullet)
                sp.allSprites.add(bullet)

            if self.weaponLevel in [6,7]:
                bullet1 = sp.Bullet([self.rect.centerx - 28,self.rect.top],sp.bluebullet,1,4)
                bullet2 = sp.Bullet([self.rect.centerx + 15 , self.rect.top],sp.bluebullet,1,4)
                sp.playerBullets.add(bullet1)
                sp.allSprites.add(bullet1)
                sp.playerBullets.add(bullet2)
                sp.allSprites.add(bullet2)

            if self.weaponLevel >= 8:
                bullet1 = sp.Bullet([self.rect.centerx - 28,self.rect.top],sp.bluebullet,1,4)
                bullet2 = sp.Bullet([self.rect.centerx + 15 , self.rect.top],sp.bluebullet,1,4)
                bullet3 = sp.Bullet([self.rect.centerx - 6 , self.rect.top],sp.bluebullet,1,4)
                sp.playerBullets.add(bullet1)
                sp.allSprites.add(bullet1)
                sp.playerBullets.add(bullet2)
                sp.allSprites.add(bullet2)
                sp.playerBullets.add(bullet3)
                sp.allSprites.add(bullet3)
                

    def makeInvincible(self):
        self.invincible = True
        self.invincibilityTimer = pygame.time.get_ticks()

    def handleCollision(self):
        
        #handle collisions
            collisionWithBullet = pygame.sprite.spritecollideany(self, sp.enemyBullets)
            collisionWithEnemy = pygame.sprite.spritecollideany(self, sp.enemySprites)
            collisionWithPowerUP = pygame.sprite.spritecollideany(self, sp.powerUPList)
            PowerUPHitList = pygame.sprite.spritecollide(self, sp.powerUPList, True)

            if collisionWithBullet and not self.invincible or collisionWithEnemy and not self.invincible:
                self.makeInvincible()

                if self.shield:
                    currentPosition =  [self.rect.x, self.rect.y]
                    self.shield = False
                    self.image = ship
                    self.rect = self.image.get_rect()
                    self.rect.x = currentPosition[0]
                    self.rect.y = currentPosition[1]
                    
                else:
                    self.lives -= 1
                    if self.weaponLevel > 1:
                        self.weaponLevel -= 1
                        self.downgradeWeapon()
                      
                    

            if self.invincible and pygame.time.get_ticks() - self.invincibilityTimer > 2000:
                self.invincible = False

            if collisionWithPowerUP:
                for powerUP in PowerUPHitList:
                    if powerUP.type == "shield":
                        currentPosition =  [self.rect.x, self.rect.y]
                        self.image = shipWithShield
                        self.rect = self.image.get_rect()
                        self.rect.x = currentPosition[0]
                        self.rect.y = currentPosition[1]
                        self.shield = True

                    elif powerUP.type == "life":
                        if self.lives < 3:
                            self.lives += 1
                            
                    elif powerUP.type == "gun":
                        if self.weaponLevel <= 10:
                            self.weaponLevel += 1
                            self.upgradeWeapon()
                
            bulletHitList = pygame.sprite.spritecollide(self, sp.enemyBullets,True)
        
  


    def update(self):
       
        if not self.isDead:

            self.handleCollision()
            
      
            self.rect.y += self.velocity[1]
            self.rect.x += self.velocity[0]

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.shoot()
            
            
            # check for borders
            if self.rect.right > 600:
                self.rect.right = 600
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > 800:
                self.rect.bottom = 800

                

            if self.lives == 0:
                self.isDead = True

           
        elif self.isDead:
            self.kill()
            sp.allSprites.empty()

            pygame.quit()
            sys.exit()

            
            

        

        

        
        
        
