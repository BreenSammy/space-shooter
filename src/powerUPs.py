import os.path as osp

import pygame
from random import randint
from random import choice

power_up_assets_folder = osp.join('assets', 'powerUPAssets')


powerUPImages = {}
powerUPImages["shield"] = pygame.image.load(osp.join(power_up_assets_folder, "ShieldPowerUP.png"))
powerUPImages["life"] = pygame.image.load(osp.join(power_up_assets_folder, "LifePowerUP.png"))
powerUPImages["gun"] = pygame.image.load(osp.join(power_up_assets_folder, "GunPowerUP.png"))



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
        
        


