import pygame
from random import randint
from random import choice

powerUPImages = {}
powerUPImages["shield"] = pygame.image.load("PowerUPAssets/ShieldPowerUP.png")
powerUPImages["life"] = pygame.image.load("PowerUPAssets/LifePowerUP.png")
powerUPImages["gun"] = pygame.image.load("PowerUPAssets/GunPowerUP.png")



class PowerUP(pygame.sprite.Sprite):

    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.type = choice(["shield","life","gun","gun"])
        self.image = powerUPImages[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = randint(50,550)
        self.rect.y = -50

    def update(self):

        self.rect.y += 2

        if self.rect.y >= 800:
            self.kill()
        
        


