import os.path as osp

import pygame

allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()
playerBullets = pygame.sprite.Group()
enemyBullets =  pygame.sprite.Group()
powerUPList = pygame.sprite.Group()

player_assets_folder = osp.join('assets', 'playerAssets')
bluebullet = pygame.image.load(osp.join(player_assets_folder, "bulletPlayer.png"))
live = pygame.image.load(osp.join(player_assets_folder, "heartPixelArt2.png"))

enemy_assets_folder = osp.join('assets', 'enemyAssets')
yellowbullet1 = pygame.image.load(osp.join(enemy_assets_folder, "EnemyBullet1.png"))
yellowbullet2 = pygame.image.load(osp.join(enemy_assets_folder, "EnemyBullet2.png"))
yellowbullet3 = pygame.image.load(osp.join(enemy_assets_folder, "EnemyBullet3.png"))


# draws lives on screen
def drawLives(screen, lives, image):
    image_rect = image.get_rect()
    for i in range (lives):
        image_rect.x = 480 + 40 * i
        image_rect.y = 10
        screen.blit(image, image_rect)
        
    
class Bullet(pygame.sprite.Sprite):


    def __init__(self,startPos,bullettype,bulletDirection,bulletSpeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullettype
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        self.bulletDirection = bulletDirection
        self.bulletSpeed = bulletSpeed
        


    def update(self):
        # bullet moves
        self.rect.y -= self.bulletDirection*self.bulletSpeed

        #kill bullet after it leaves the screen
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.top > 800:
            self.kill()
            
class PowerUP(pygame.sprite.Sprite):

    def __init_(self,startPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = powerupImage1
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]


    def update(self):

        self.rect.y += 2

        if self.rect.top > 800:
            self.kill()
        
    



            
