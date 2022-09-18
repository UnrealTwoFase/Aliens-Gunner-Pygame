import pygame, pickle


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        with open('skinpack.inv', 'rb') as f:
            skins = pickle.load(f)
                
        if skins == 0:                     # Deafult
            self.color = 255, 255, 0
        if skins == 1:                     # Winter
            self.color = 63, 243, 210
        if skins == 2:                     # Fire
            self.color = 255, 0, 0
        if skins == 3:                     # Alien
            self.color = 255, 255, 0
        if skins == 4:                     # Alien
            self.color = 230, 230, 230
 
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.speed = 2
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)