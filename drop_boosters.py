import pygame

class Drop_Boosters(pygame.sprite.Sprite):

    def __init__(self, screen, image, speed, scale, x, y):
    
        super(Drop_Boosters, self).__init__()
        width = image.get_width()
        height = image.get_height()
        self.screen = screen
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = self.rect.y
        self.x = self.rect.x

        
    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        