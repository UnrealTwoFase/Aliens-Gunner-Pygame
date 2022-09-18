import pygame


#Color
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
bg_color = (0, 0, 0)
#/Color


class Gun():

    def __init__(self, screen, skins):
        #Skins
        # Deafult - 0
        deafult_gun = pygame.image.load('games-caches\game0_cache\gun\gun.png')

        # Winter - 1
        winter_gun = pygame.image.load('games-caches\game0_cache\gun\gun_w.png')

        # Fire - 2
        fire_gun = pygame.image.load('games-caches\game0_cache\gun\gun_f.png')

        # Aliens - 3
        alien_gun = pygame.image.load('games-caches\game0_cache\gun\gun_a.png')
        
        # Lose - 4
        lose_gun = pygame.image.load('games-caches\game0_cache\gun\gun_l.png')

        #/Skins
        
        #Check skin gun
        if skins == 0:                     # Deafult
            image = deafult_gun
        if skins == 1:                     # Winter
            image = winter_gun
        if skins == 2:                     # Fire
            image = fire_gun
        if skins == 3:                     # Alien
            image = alien_gun
        if skins == 4:
            image = lose_gun
        #/Check skin gun
        
        mright = False
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
    
    def output(self):
    
        self.screen.blit(self.image, self.rect)
        
    def update_position(self, speed_gun):
        speed_gun += 3
        
        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed_gun
        elif self.mleft == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= speed_gun
        
