import os.path as osp

import pygame
import src.mysprites as sp



assets_folder = osp.join('assets', 'enemyAssets')

enemy1 = pygame.image.load(osp.join(assets_folder, "EnemyShip1.png"))
enemy2 = pygame.image.load(osp.join(assets_folder, "EnemyShip2.png"))
enemy3 = pygame.image.load(osp.join(assets_folder, "EnemyShip3.png"))
enemy4 = pygame.image.load(osp.join(assets_folder, "EnemyShip4.png"))
boss = pygame.image.load(osp.join(assets_folder, "Boss.png"))


killCount = 0

class EasyEnemy(pygame.sprite.Sprite):

    def __init__(self,stop, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy1
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = -30
        self.speed = 1
        self.velocity = [0,self.speed]
        self.shootDelay = 1000
        self.lastShot = pygame.time.get_ticks()
        self.stop = stop
        self.xdirection = 1
        self.bulletSpeed = 2
        

    def shoot(self):

        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:
            self.lastShot = now 
            bullet = sp.Bullet([self.rect.centerx - 4 , self.rect.bottom],sp.yellowbullet1,-1, self.bulletSpeed)
            sp.enemyBullets.add(bullet)
            sp.allSprites.add(bullet)

    def update(self):
        
        global killCount

        collision = pygame.sprite.spritecollideany(self, sp.playerBullets)
        if collision:
            self.kill()
            killCount += 1
            
            

        bulletsHitList = pygame.sprite.spritecollide(self, sp.playerBullets,True)
        


        self.rect.y += self.velocity [1]
        self.rect.x += self.velocity [0]
        self.shoot()

        if self.rect.y >= self.stop:
            self.velocity[1] = 0
            self.velocity[0] = self.speed*self.xdirection
            
        if self.rect.right >= 550:
            self.xdirection = -1        
  
        elif self.rect.x <= 50:
            self.xdirection = 1
       
            
        

        

class HarderEnemy(pygame.sprite.Sprite):

    
    

    def __init__(self, stop, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy2
        self.rect = self.image.get_rect()
        self.stop = stop
        self.rect.x = xpos
        self.rect.y = -30
        self.speed = 1
        self.velocity = [0,self.speed]
        self.shootDelay = 750
        self.lastShot = pygame.time.get_ticks()
        self.lives = 2
        self.xdirection = 1
        self.bulletSpeed = 2

    def shoot(self):

        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:

            self.lastShot = now 
            bullet = sp.Bullet([self.rect.centerx - 6, self.rect.bottom],sp.yellowbullet2,-1,self.bulletSpeed)
            sp.enemyBullets.add(bullet)
            sp.allSprites.add(bullet)

    def update(self):

        global killCount

        collision = pygame.sprite.spritecollideany(self, sp.playerBullets)

        if collision:
            self.lives -= 1

        if self.lives == 0:
            self.kill()
            killCount += 1
        
        self.rect.y += self.velocity [1]
        self.rect.x += self.velocity [0]
        self.shoot()

        if self.rect.y >= self.stop:
            self.velocity[1] = 0
            self.velocity[0] = self.speed*self.xdirection
            
        if self.rect.right >= 550:
            self.xdirection = -1        
  
        elif self.rect.x <= 50:
            self.xdirection = 1

                
        bulletsHitList = pygame.sprite.spritecollide(self, sp.playerBullets,True)


class FasterEnemy(pygame.sprite.Sprite):


    def __init__(self, stop, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy3
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = -20
        self.speed = 2
        self.stop = stop
        self.xdirection = 1
        self.bulletSpeed = 4
        self.velocity = [0,self.speed]
        self.shootDelay = 500
        self.lastShot = pygame.time.get_ticks()

    def shoot(self):

        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:

            self.lastShot = now 
            bullet = sp.Bullet([self.rect.centerx - 4 , self.rect.bottom],sp.yellowbullet1,-1, self.bulletSpeed)
            sp.enemyBullets.add(bullet)
            sp.allSprites.add(bullet)

    def update(self):

        global killCount

        collision = pygame.sprite.spritecollideany(self, sp.playerBullets)
        if collision:
            self.kill()
            killCount += 1

        bulletsHitList = pygame.sprite.spritecollide(self, sp.playerBullets,True)

        self.rect.y += self.velocity [1]
        self.rect.x += self.velocity [0]
        self.shoot()

        if self.rect.y >= self.stop:
            self.velocity[1] = 0
            self.velocity[0] = self.speed*self.xdirection
            
        if self.rect.right >= 550:
            self.xdirection = -1        
  
        elif self.rect.x <= 50:
            self.xdirection = 1

        
       


class HardEnemy(pygame.sprite.Sprite):
    

    def __init__(self, stop, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy4
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = -100
        self.stop = stop
        self.xdirection = -1
        self.bulletSpeed = 2
        self.speed = 1
        self.velocity = [0,self.speed]
        self.shootDelay = 750
        self.lastShot = pygame.time.get_ticks()
        self.lives = 20

    def shoot(self):

        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:

            self.lastShot = now 
            bullet1 = sp.Bullet([self.rect.centerx - 18 , self.rect.bottom],sp.yellowbullet3,-1,self.bulletSpeed)
            bullet2 = sp.Bullet([self.rect.centerx + 8 , self.rect.bottom],sp.yellowbullet3,-1,self.bulletSpeed)
            sp.enemyBullets.add(bullet1)
            sp.allSprites.add(bullet1)
            sp.enemyBullets.add(bullet2)
            sp.allSprites.add(bullet2)

    def update(self):

        global killCount

        collision = pygame.sprite.spritecollideany(self, sp.playerBullets)

        if collision:
            self.lives -= 1

        if self.lives == 0:
            self.kill()
            killCount += 1 

        bulletsHitList = pygame.sprite.spritecollide(self, sp.playerBullets,True)

        self.rect.y += self.velocity [1]
        self.rect.x += self.velocity [0]
        self.shoot()

        if self.rect.y >= self.stop:
            self.velocity[1] = 0
            self.velocity[0] = self.speed*self.xdirection
            
        if self.rect.right >= 600:
            self.xdirection = -1        
  
        elif self.rect.x <= 0:
            self.xdirection = 1

                
        

class Boss(pygame.sprite.Sprite):
    
    def __init__(self,stop, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = -250
        self.speed = 1
        self.velocity = [0,self.speed]
        self.shootDelay = 600
        self.lastShot = pygame.time.get_ticks()
        self.stop = stop
        self.xdirection = 1
        self.bulletSpeed = 3
        self.lives = 400
        

    def shoot1(self):

        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:
            self.lastShot = now 
            bullet1 = sp.Bullet([self.rect.left + 10, self.rect.bottom - 43],sp.yellowbullet2,-1, self.bulletSpeed)
            bullet2 = sp.Bullet([self.rect.right - 20 , self.rect.bottom - 43],sp.yellowbullet2,-1, self.bulletSpeed)
            bullet3 = sp.Bullet([self.rect.centerx - 4 , self.rect.bottom - 25],sp.yellowbullet3,-1, self.bulletSpeed)
            sp.enemyBullets.add(bullet1)
            sp.allSprites.add(bullet1)
            sp.enemyBullets.add(bullet2)
            sp.allSprites.add(bullet2)
            sp.enemyBullets.add(bullet3)
            sp.allSprites.add(bullet3)

    def shoot2(self):
        self.shootDelay = 400
        self.bulletSpeed = 4

        
        now = pygame.time.get_ticks()

        if now - self.lastShot > self.shootDelay:
            self.lastShot = now 
            bullet1 = sp.Bullet([self.rect.left + 10, self.rect.bottom - 43],sp.yellowbullet2,-1, self.bulletSpeed)
            bullet2 = sp.Bullet([self.rect.right - 20 , self.rect.bottom - 43],sp.yellowbullet2,-1, self.bulletSpeed)
            bullet3 = sp.Bullet([self.rect.centerx - 4 , self.rect.bottom - 25],sp.yellowbullet3,-1, self.bulletSpeed)
            sp.enemyBullets.add(bullet1)
            sp.allSprites.add(bullet1)
            sp.enemyBullets.add(bullet2)
            sp.allSprites.add(bullet2)
            sp.enemyBullets.add(bullet3)
            sp.allSprites.add(bullet3)
        

    def update(self):
        
        global killCount

        collision = pygame.sprite.spritecollideany(self, sp.playerBullets)

        if collision:
            self.lives -= 1

        if self.lives == 0:
            self.kill()
            killCount += 1      

        bulletsHitList = pygame.sprite.spritecollide(self, sp.playerBullets,True)
        
        
        if self.lives >= 200:
            
            self.rect.y += self.velocity [1]
            self.rect.x += self.velocity [0]
            self.shoot1()

            if self.rect.y >= self.stop:
                self.velocity[1] = 0
                self.velocity[0] = self.speed*self.xdirection
            
            if self.rect.right >= 550:
                self.xdirection = -1        
  
            elif self.rect.x <= 50:
                self.xdirection = 1
                self.velocity[0] = 2

        elif self.lives < 200:
            self.shoot2()

            if self.rect.x in range(50,400) and self.rect.y >= 150:
                self.rect.x += 2
            elif self.rect.x <= 50 and self.rect.y >= 150:
                self.rect.x += 2
            elif self.rect.x >= 50 and self.rect.y <= 50:
                self.rect.x -= 2
            elif self.rect.y >= 50 and self.rect.x <= 50:
                self.rect.y += 2
            elif self.rect.y <= 150 and self.rect.x >= 400:
                self.rect.y -= 2
            

            
    

       
        
  
        
