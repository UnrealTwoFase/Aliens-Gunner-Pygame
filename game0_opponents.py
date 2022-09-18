import pygame, pickle


class Opponents_Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, screen, scale, speed, image):
        super(Opponents_Alien, self).__init__()
        # image = pygame.image.load('games-caches\game0_cache\images0\game_sprites\opponents_new.png')
        self.screen = screen
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.y = self.rect.y
        
    def draw(self, screen):
        self.screen.blit(self.image, (self.rect.x, self.y))
        
    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        
    def aliens_creature(screen, aliens, game_levels):
    
            def level1(screen, aliens, scale, speed, image):
                
                alien1 = Opponents_Alien(200, 20, screen, scale, speed, image)
                alien2 = Opponents_Alien(400, 20, screen, scale, speed, image)
                aliens.add(alien1, alien2)            
                
            def level2(screen, aliens, scale, speed, image):
                alien1 = Opponents_Alien(0, 20, screen, scale, speed, image)
                alien2 = Opponents_Alien(150, 20, screen, scale, speed, image)
                alien3 = Opponents_Alien(300, 20, screen, scale, speed, image)
                alien4 = Opponents_Alien(450, 20, screen, scale, speed, image)
                alien5 = Opponents_Alien(600, 20, screen, scale, speed, image)
                aliens.add(alien1, alien2, alien3, alien4, alien5)
                
            def level3(screen, aliens, scale, speed, image):
                alien1 = Opponents_Alien(0, 20, screen, scale, speed, image)
                alien2 = Opponents_Alien(80, 20, screen, scale, speed, image)
                alien3 = Opponents_Alien(160, 20, screen, scale, speed, image)
                alien4 = Opponents_Alien(240, 20, screen, scale, speed, image)
                alien5 = Opponents_Alien(320, 20, screen, scale, speed, image)
                alien6 = Opponents_Alien(400, 20, screen, scale, speed, image)
                alien7 = Opponents_Alien(480, 20, screen, scale, speed, image)
                alien8 = Opponents_Alien(560, 20, screen, scale, speed, image)
                alien9 = Opponents_Alien(640, 20, screen, scale, speed, image)
                alien10 = Opponents_Alien(720, 20, screen, scale, speed, image)
                
                alien1y = Opponents_Alien(0, 80, screen, scale, speed, image)
                alien2y = Opponents_Alien(80, 80, screen, scale, speed, image)
                alien3y = Opponents_Alien(160, 80, screen, scale, speed, image)
                alien4y = Opponents_Alien(240, 80, screen, scale, speed, image)
                alien5y = Opponents_Alien(320, 80, screen, scale, speed, image)
                alien6y = Opponents_Alien(400, 80, screen, scale, speed, image)
                alien7y = Opponents_Alien(480, 80, screen, scale, speed, image)
                alien8y = Opponents_Alien(560, 80, screen, scale, speed, image)
                alien9y = Opponents_Alien(640, 80, screen, scale, speed, image)
                alien10y = Opponents_Alien(720, 80, screen, scale, speed, image)
                
                aliens.add(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10)
                aliens.add(alien1y, alien2y, alien3y, alien4y, alien5y, alien6y, alien7y, alien8y, alien9y, alien10y)
 
                
            def level4(screen, aliens, scale, speed, image):
                alien1 = Opponents_Alien(0, 20, screen, scale, speed, image)
                alien2 = Opponents_Alien(80, 20, screen, scale, speed, image)
                alien3 = Opponents_Alien(160, 20, screen, scale, speed, image)
                alien4 = Opponents_Alien(240, 20, screen, scale, speed, image)
                alien5 = Opponents_Alien(320, 20, screen, scale, speed, image)
                alien6 = Opponents_Alien(400, 20, screen, scale, speed, image)
                alien7 = Opponents_Alien(480, 20, screen, scale, speed, image)
                alien8 = Opponents_Alien(560, 20, screen, scale, speed, image)
                alien9 = Opponents_Alien(640, 20, screen, scale, speed, image)
                alien10 = Opponents_Alien(720, 20, screen, scale, speed, image)
                
                alien1y = Opponents_Alien(0, 80, screen, scale, speed, image)
                alien2y = Opponents_Alien(80, 80, screen, scale, speed, image)
                alien3y = Opponents_Alien(160, 80, screen, scale, speed, image)
                alien4y = Opponents_Alien(240, 80, screen, scale, speed, image)
                alien5y = Opponents_Alien(320, 80, screen, scale, speed, image)
                alien6y = Opponents_Alien(400, 80, screen, scale, speed, image)
                alien7y = Opponents_Alien(480, 80, screen, scale, speed, image)
                alien8y = Opponents_Alien(560, 80, screen, scale, speed, image)
                alien9y = Opponents_Alien(640, 80, screen, scale, speed, image)
                alien10y = Opponents_Alien(720, 80, screen, scale, speed, image)
 
                aliens.add(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10)
                aliens.add(alien1y, alien2y, alien3y, alien4y, alien5y, alien6y, alien7y, alien8y, alien9y, alien10y)

                
            def level5(screen, aliens, scale, speed, image):
                alien1 = Opponents_Alien(0, 20, screen, scale, speed, image)
                alien2 = Opponents_Alien(80, 20, screen, scale, speed, image)
                alien3 = Opponents_Alien(160, 20, screen, scale, speed, image)
                alien4 = Opponents_Alien(240, 20, screen, scale, speed, image)
                alien5 = Opponents_Alien(320, 20, screen, scale, speed, image)
                alien6 = Opponents_Alien(400, 20, screen, scale, speed, image)
                alien7 = Opponents_Alien(480, 20, screen, scale, speed, image)
                alien8 = Opponents_Alien(560, 20, screen, scale, speed, image)
                alien9 = Opponents_Alien(640, 20, screen, scale, speed, image)
                alien10 = Opponents_Alien(720, 20, screen, scale, speed, image)
                
                alien1y = Opponents_Alien(0, 80, screen, scale, speed, image)
                alien2y = Opponents_Alien(80, 80, screen, scale, speed, image)
                alien3y = Opponents_Alien(160, 80, screen, scale, speed, image)
                alien4y = Opponents_Alien(240, 80, screen, scale, speed, image)
                alien5y = Opponents_Alien(320, 80, screen, scale, speed, image)
                alien6y = Opponents_Alien(400, 80, screen, scale, speed, image)
                alien7y = Opponents_Alien(480, 80, screen, scale, speed, image)
                alien8y = Opponents_Alien(560, 80, screen, scale, speed, image)
                alien9y = Opponents_Alien(640, 80, screen, scale, speed, image)
                alien10y = Opponents_Alien(720, 80, screen, scale, speed, image)
                
                alien1y2 = Opponents_Alien(0, 140, screen, scale, speed, image)
                alien2y2 = Opponents_Alien(80, 140, screen, scale, speed, image)
                alien3y2 = Opponents_Alien(160, 140, screen, scale, speed, image)
                alien4y2 = Opponents_Alien(240, 140, screen, scale, speed, image)
                alien5y2 = Opponents_Alien(320, 140, screen, scale, speed, image)
                alien6y2 = Opponents_Alien(400, 140, screen, scale, speed, image)
                alien7y2 = Opponents_Alien(480, 140, screen, scale, speed, image)
                alien8y2 = Opponents_Alien(560, 140, screen, scale, speed, image)
                alien9y2 = Opponents_Alien(640, 140, screen, scale, speed, image)
                alien10y2 = Opponents_Alien(720, 140, screen, scale, speed, image)
                
                aliens.add(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10)
                aliens.add(alien1y, alien2y, alien3y, alien4y, alien5y, alien6y, alien7y, alien8y, alien9y, alien10y)
                aliens.add(alien1y2, alien2y2, alien3y2, alien4y2, alien5y2, alien6y2, alien7y2, alien8y2, alien9y2, alien10y2)
 
                
            def level_boss(screen, aliens, scale, speed, image):
                
                alien1y = Opponents_Alien(0, 80, screen, scale, speed, image)
                alien2y = Opponents_Alien(80, 80, screen, scale, speed, image)
                alien3y = Opponents_Alien(160, 80, screen, scale, speed, image)
                alien4y = Opponents_Alien(240, 80, screen, scale, speed, image)
                alien5y = Opponents_Alien(320, 80, screen, scale, speed, image)
                alien6y = Opponents_Alien(400, 80, screen, scale, speed, image)
                alien7y = Opponents_Alien(480, 80, screen, scale, speed, image)
                alien8y = Opponents_Alien(560, 80, screen, scale, speed, image)
                alien9y = Opponents_Alien(640, 80, screen, scale, speed, image)
                alien10y = Opponents_Alien(720, 80, screen, scale, speed, image)
                
                
                alien1y2 = Opponents_Alien(0, 140, screen, scale, speed, image)
                alien2y2 = Opponents_Alien(80, 140, screen, scale, speed, image)
                alien3y2 = Opponents_Alien(160, 140, screen, scale, speed, image)
                alien4y2 = Opponents_Alien(240, 140, screen, scale, speed, image)
                alien5y2 = Opponents_Alien(320, 140, screen, scale, speed, image)
                alien6y2 = Opponents_Alien(400, 140, screen, scale, speed, image)
                alien7y2 = Opponents_Alien(480, 140, screen, scale, speed, image)
                alien8y2 = Opponents_Alien(560, 140, screen, scale, speed, image)
                alien9y2 = Opponents_Alien(640, 140, screen, scale, speed, image)
                alien10y2 = Opponents_Alien(720, 140, screen, scale, speed, image)
                
                
                alien1y3 = Opponents_Alien(0, -80, screen, scale, speed, image)
                alien2y3 = Opponents_Alien(80, -80, screen, scale, speed, image)
                alien3y3 = Opponents_Alien(160, -80, screen, scale, speed, image)
                alien4y3 = Opponents_Alien(240, -80, screen, scale, speed, image)
                alien5y3 = Opponents_Alien(320, -80, screen, scale, speed, image)
                alien6y3 = Opponents_Alien(400, -80, screen, scale, speed, image)
                alien7y3 = Opponents_Alien(480, -80, screen, scale, speed, image)
                alien8y3 = Opponents_Alien(560, -80, screen, scale, speed, image)
                alien9y3 = Opponents_Alien(640, -80, screen, scale, speed, image)
                alien10y3 = Opponents_Alien(720, -80, screen, scale, speed, image)
                
                
                alien1y4 = Opponents_Alien(0, -140, screen, scale, speed, image)
                alien2y4 = Opponents_Alien(80, -140, screen, scale, speed, image)
                alien3y4 = Opponents_Alien(160, -140, screen, scale, speed, image)
                alien4y4 = Opponents_Alien(240, -140, screen, scale, speed, image)
                alien5y4 = Opponents_Alien(320, -140, screen, scale, speed, image)
                alien6y4 = Opponents_Alien(400, -140, screen, scale, speed, image)
                alien7y4 = Opponents_Alien(480, -140, screen, scale, speed, image)
                alien8y4 = Opponents_Alien(560, -140, screen, scale, speed, image)
                alien9y4 = Opponents_Alien(640, -140, screen, scale, speed, image)
                alien10y4 = Opponents_Alien(720, -140, screen, scale, speed, image)
                
                alien1y5 = Opponents_Alien(0, -300, screen, scale, speed, image)
                alien2y5 = Opponents_Alien(80, -300, screen, scale, speed, image)
                alien3y5 = Opponents_Alien(160, -300, screen, scale, speed, image)
                alien4y5 = Opponents_Alien(240, -300, screen, scale, speed, image)
                alien5y5 = Opponents_Alien(320, -300, screen, scale, speed, image)
                alien6y5 = Opponents_Alien(400, -300, screen, scale, speed, image)
                alien7y5 = Opponents_Alien(480, -300, screen, scale, speed, image)
                alien8y5 = Opponents_Alien(560, -300, screen, scale, speed, image)
                alien9y5 = Opponents_Alien(640, -300, screen, scale, speed, image)
                alien10y5 = Opponents_Alien(720, -300, screen, scale, speed, image)
                
                
                alien1y6 = Opponents_Alien(0, -220, screen, scale, speed, image)
                alien2y6 = Opponents_Alien(80, -220, screen, scale, speed, image)
                alien3y6 = Opponents_Alien(160, -220, screen, scale, speed, image)
                alien4y6 = Opponents_Alien(240, -220, screen, scale, speed, image)
                alien5y6 = Opponents_Alien(320, -220, screen, scale, speed, image)
                alien6y6 = Opponents_Alien(400, -220, screen, scale, speed, image)
                alien7y6 = Opponents_Alien(480, -220, screen, scale, speed, image)
                alien8y6 = Opponents_Alien(560, -220, screen, scale, speed, image)
                alien9y6 = Opponents_Alien(640, -220, screen, scale, speed, image)
                alien10y6 = Opponents_Alien(720, -220, screen, scale, speed, image)
                
                
                alien1y7 = Opponents_Alien(0, -380, screen, scale, speed, image)
                alien2y7 = Opponents_Alien(80, -380, screen, scale, speed, image)
                alien3y7 = Opponents_Alien(160, -380, screen, scale, speed, image)
                alien4y7 = Opponents_Alien(240, -380, screen, scale, speed, image)
                alien5y7 = Opponents_Alien(320, -380, screen, scale, speed, image)
                alien6y7 = Opponents_Alien(400, -380, screen, scale, speed, image)
                alien7y7 = Opponents_Alien(480, -380, screen, scale, speed, image)
                alien8y7 = Opponents_Alien(560, -380, screen, scale, speed, image)
                alien9y7 = Opponents_Alien(640, -380, screen, scale, speed, image)
                alien10y7 = Opponents_Alien(720, -380, screen, scale, speed, image)
                
                
                alien1y8 = Opponents_Alien(0, -460, screen, scale, speed, image)
                alien2y8 = Opponents_Alien(80, -460, screen, scale, speed, image)
                alien3y8 = Opponents_Alien(160, -460, screen, scale, speed, image)
                alien4y8 = Opponents_Alien(240, -460, screen, scale, speed, image)
                alien5y8 = Opponents_Alien(320, -460, screen, scale, speed, image)
                alien6y8 = Opponents_Alien(400, -460, screen, scale, speed, image)
                alien7y8 = Opponents_Alien(480, -460, screen, scale, speed, image)
                alien8y8 = Opponents_Alien(560, -460, screen, scale, speed, image)
                alien9y8 = Opponents_Alien(640, -460, screen, scale, speed, image)
                alien10y8 = Opponents_Alien(720, -460, screen, scale, speed, image)
                
                aliens.add(alien1y, alien2y, alien3y, alien4y, alien5y, alien6y, alien7y, alien8y, alien9y, alien10y)
                aliens.add(alien1y2, alien2y2, alien3y2, alien4y2, alien5y2, alien6y2, alien7y2, alien8y2, alien9y2, alien10y2)
                aliens.add(alien1y3, alien2y3, alien3y3, alien4y3, alien5y3, alien6y3, alien7y3, alien8y3, alien9y3, alien10y3)
                aliens.add(alien1y4, alien2y4, alien3y4, alien4y4, alien5y4, alien6y4, alien7y4, alien8y4, alien9y4, alien10y4)
                aliens.add(alien1y5, alien2y5, alien3y5, alien4y5, alien5y5, alien6y5, alien7y5, alien8y5, alien9y5, alien10y5)
                aliens.add(alien1y6, alien2y6, alien3y6, alien4y6, alien5y6, alien6y6, alien7y6, alien8y6, alien9y6, alien10y6)
                aliens.add(alien1y7, alien2y7, alien3y7, alien4y7, alien5y7, alien6y7, alien7y7, alien8y7, alien9y7, alien10y7)
                aliens.add(alien1y8, alien2y8, alien3y8, alien4y8, alien5y8, alien6y8, alien7y8, alien8y8, alien9y8, alien10y8)
 
                 
            def level_ultumait(screen, aliens, scale, speed, image):
                alien1y = Opponents_Alien(0, 80, screen, scale, speed, image)
                alien2y = Opponents_Alien(80, 80, screen, scale, speed, image)
                alien3y = Opponents_Alien(160, 80, screen, scale, speed, image)
                alien4y = Opponents_Alien(240, 80, screen, scale, speed, image)
                alien5y = Opponents_Alien(320, 80, screen, scale, speed, image)
                alien6y = Opponents_Alien(400, 80, screen, scale, speed, image)
                alien7y = Opponents_Alien(480, 80, screen, scale, speed, image)
                alien8y = Opponents_Alien(560, 80, screen, scale, speed, image)
                alien9y = Opponents_Alien(640, 80, screen, scale, speed, image)
                alien10y = Opponents_Alien(720, 80, screen, scale, speed, image)
                
                
                alien1y2 = Opponents_Alien(0, 140, screen, scale, speed, image)
                alien2y2 = Opponents_Alien(80, 140, screen, scale, speed, image)
                alien3y2 = Opponents_Alien(160, 140, screen, scale, speed, image)
                alien4y2 = Opponents_Alien(240, 140, screen, scale, speed, image)
                alien5y2 = Opponents_Alien(320, 140, screen, scale, speed, image)
                alien6y2 = Opponents_Alien(400, 140, screen, scale, speed, image)
                alien7y2 = Opponents_Alien(480, 140, screen, scale, speed, image)
                alien8y2 = Opponents_Alien(560, 140, screen, scale, speed, image)
                alien9y2 = Opponents_Alien(640, 140, screen, scale, speed, image)
                alien10y2 = Opponents_Alien(720, 140, screen, scale, speed, image)
                
                
                alien1y3 = Opponents_Alien(0, -80, screen, scale, speed, image)
                alien2y3 = Opponents_Alien(80, -80, screen, scale, speed, image)
                alien3y3 = Opponents_Alien(160, -80, screen, scale, speed, image)
                alien4y3 = Opponents_Alien(240, -80, screen, scale, speed, image)
                alien5y3 = Opponents_Alien(320, -80, screen, scale, speed, image)
                alien6y3 = Opponents_Alien(400, -80, screen, scale, speed, image)
                alien7y3 = Opponents_Alien(480, -80, screen, scale, speed, image)
                alien8y3 = Opponents_Alien(560, -80, screen, scale, speed, image)
                alien9y3 = Opponents_Alien(640, -80, screen, scale, speed, image)
                alien10y3 = Opponents_Alien(720, -80, screen, scale, speed, image)
                
                
                alien1y4 = Opponents_Alien(0, -140, screen, scale, speed, image)
                alien2y4 = Opponents_Alien(80, -140, screen, scale, speed, image)
                alien3y4 = Opponents_Alien(160, -140, screen, scale, speed, image)
                alien4y4 = Opponents_Alien(240, -140, screen, scale, speed, image)
                alien5y4 = Opponents_Alien(320, -140, screen, scale, speed, image)
                alien6y4 = Opponents_Alien(400, -140, screen, scale, speed, image)
                alien7y4 = Opponents_Alien(480, -140, screen, scale, speed, image)
                alien8y4 = Opponents_Alien(560, -140, screen, scale, speed, image)
                alien9y4 = Opponents_Alien(640, -140, screen, scale, speed, image)
                alien10y4 = Opponents_Alien(720, -140, screen, scale, speed, image)
                
                alien1y5 = Opponents_Alien(0, -300, screen, scale, speed, image)
                alien2y5 = Opponents_Alien(80, -300, screen, scale, speed, image)
                alien3y5 = Opponents_Alien(160, -300, screen, scale, speed, image)
                alien4y5 = Opponents_Alien(240, -300, screen, scale, speed, image)
                alien5y5 = Opponents_Alien(320, -300, screen, scale, speed, image)
                alien6y5 = Opponents_Alien(400, -300, screen, scale, speed, image)
                alien7y5 = Opponents_Alien(480, -300, screen, scale, speed, image)
                alien8y5 = Opponents_Alien(560, -300, screen, scale, speed, image)
                alien9y5 = Opponents_Alien(640, -300, screen, scale, speed, image)
                alien10y5 = Opponents_Alien(720, -300, screen, scale, speed, image)
                
                
                alien1y6 = Opponents_Alien(0, -220, screen, scale, speed, image)
                alien2y6 = Opponents_Alien(80, -220, screen, scale, speed, image)
                alien3y6 = Opponents_Alien(160, -220, screen, scale, speed, image)
                alien4y6 = Opponents_Alien(240, -220, screen, scale, speed, image)
                alien5y6 = Opponents_Alien(320, -220, screen, scale, speed, image)
                alien6y6 = Opponents_Alien(400, -220, screen, scale, speed, image)
                alien7y6 = Opponents_Alien(480, -220, screen, scale, speed, image)
                alien8y6 = Opponents_Alien(560, -220, screen, scale, speed, image)
                alien9y6 = Opponents_Alien(640, -220, screen, scale, speed, image)
                alien10y6 = Opponents_Alien(720, -220, screen, scale, speed, image)
                
                
                alien1y7 = Opponents_Alien(0, -380, screen, scale, speed, image)
                alien2y7 = Opponents_Alien(80, -380, screen, scale, speed, image)
                alien3y7 = Opponents_Alien(160, -380, screen, scale, speed, image)
                alien4y7 = Opponents_Alien(240, -380, screen, scale, speed, image)
                alien5y7 = Opponents_Alien(320, -380, screen, scale, speed, image)
                alien6y7 = Opponents_Alien(400, -380, screen, scale, speed, image)
                alien7y7 = Opponents_Alien(480, -380, screen, scale, speed, image)
                alien8y7 = Opponents_Alien(560, -380, screen, scale, speed, image)
                alien9y7 = Opponents_Alien(640, -380, screen, scale, speed, image)
                alien10y7 = Opponents_Alien(720, -380, screen, scale, speed, image)
                
                
                alien1y8 = Opponents_Alien(0, -460, screen, scale, speed, image)
                alien2y8 = Opponents_Alien(80, -460, screen, scale, speed, image)
                alien3y8 = Opponents_Alien(160, -460, screen, scale, speed, image)
                alien4y8 = Opponents_Alien(240, -460, screen, scale, speed, image)
                alien5y8 = Opponents_Alien(320, -460, screen, scale, speed, image)
                alien6y8 = Opponents_Alien(400, -460, screen, scale, speed, image)
                alien7y8 = Opponents_Alien(480, -460, screen, scale, speed, image)
                alien8y8 = Opponents_Alien(560, -460, screen, scale, speed, image)
                alien9y8 = Opponents_Alien(640, -460, screen, scale, speed, image)
                alien10y8 = Opponents_Alien(720, -460, screen, scale, speed, image)
                
                alien1y9 = Opponents_Alien(0, -800, screen, scale, speed, image)
                alien2y9 = Opponents_Alien(80, -800, screen, scale, speed, image)
                alien3y9 = Opponents_Alien(160, -800, screen, scale, speed, image)
                alien4y9 = Opponents_Alien(240, -800, screen, scale, speed, image)
                alien5y9 = Opponents_Alien(320, -800, screen, scale, speed, image)
                alien6y9 = Opponents_Alien(400, -800, screen, scale, speed, image)
                alien7y9 = Opponents_Alien(480, -800, screen, scale, speed, image)
                alien8y9 = Opponents_Alien(560, -800, screen, scale, speed, image)
                alien9y9 = Opponents_Alien(640, -800, screen, scale, speed, image)
                alien10y9 = Opponents_Alien(720, -800, screen, scale, speed, image)
                
                
                alien1y10 = Opponents_Alien(0, -720, screen, scale, speed, image)
                alien2y10 = Opponents_Alien(80, -720, screen, scale, speed, image)
                alien3y10 = Opponents_Alien(160, -720, screen, scale, speed, image)
                alien4y10 = Opponents_Alien(240, -720, screen, scale, speed, image)
                alien5y10 = Opponents_Alien(320, -720, screen, scale, speed, image)
                alien6y10 = Opponents_Alien(400, -720, screen, scale, speed, image)
                alien7y10 = Opponents_Alien(480, -720, screen, scale, speed, image)
                alien8y10 = Opponents_Alien(560, -720, screen, scale, speed, image)
                alien9y10 = Opponents_Alien(640, -720, screen, scale, speed, image)
                alien10y10 = Opponents_Alien(720, -720, screen, scale, speed, image)
                
                alien1y11 = Opponents_Alien(0, -880, screen, scale, speed, image)
                alien2y11 = Opponents_Alien(80, -880, screen, scale, speed, image)
                alien3y11 = Opponents_Alien(160, -880, screen, scale, speed, image)
                alien4y11 = Opponents_Alien(240, -880, screen, scale, speed, image)
                alien5y11 = Opponents_Alien(320, -880, screen, scale, speed, image)
                alien6y11 = Opponents_Alien(400, -880, screen, scale, speed, image)
                alien7y11 = Opponents_Alien(480, -880, screen, scale, speed, image)
                alien8y11 = Opponents_Alien(560, -880, screen, scale, speed, image)
                alien9y11 = Opponents_Alien(640, -880, screen, scale, speed, image)
                alien10y11 = Opponents_Alien(720, -880, screen, scale, speed, image)
                
                alien1y12 = Opponents_Alien(0, -960, screen, scale, speed, image)
                alien2y12 = Opponents_Alien(80, -960, screen, scale, speed, image)
                alien3y12 = Opponents_Alien(160, -960, screen, scale, speed, image)
                alien4y12 = Opponents_Alien(240, -960, screen, scale, speed, image)
                alien5y12 = Opponents_Alien(320, -960, screen, scale, speed, image)
                alien6y12 = Opponents_Alien(400, -960, screen, scale, speed, image)
                alien7y12 = Opponents_Alien(480, -960, screen, scale, speed, image)
                alien8y12 = Opponents_Alien(560, -960, screen, scale, speed, image)
                alien9y12 = Opponents_Alien(640, -960, screen, scale, speed, image)
                alien10y12 = Opponents_Alien(720, -960, screen, scale, speed, image)
                
                
                aliens.add(alien1y, alien2y, alien3y, alien4y, alien5y, alien6y, alien7y, alien8y, alien9y, alien10y)
                aliens.add(alien1y2, alien2y2, alien3y2, alien4y2, alien5y2, alien6y2, alien7y2, alien8y2, alien9y2, alien10y2)
                aliens.add(alien1y3, alien2y3, alien3y3, alien4y3, alien5y3, alien6y3, alien7y3, alien8y3, alien9y3, alien10y3)
                aliens.add(alien1y4, alien2y4, alien3y4, alien4y4, alien5y4, alien6y4, alien7y4, alien8y4, alien9y4, alien10y4)
                aliens.add(alien1y5, alien2y5, alien3y5, alien4y5, alien5y5, alien6y5, alien7y5, alien8y5, alien9y5, alien10y5)
                aliens.add(alien1y6, alien2y6, alien3y6, alien4y6, alien5y6, alien6y6, alien7y6, alien8y6, alien9y6, alien10y6)
                aliens.add(alien1y7, alien2y7, alien3y7, alien4y7, alien5y7, alien6y7, alien7y7, alien8y7, alien9y7, alien10y7)
                aliens.add(alien1y8, alien2y8, alien3y8, alien4y8, alien5y8, alien6y8, alien7y8, alien8y8, alien9y8, alien10y8)
                aliens.add(alien1y9, alien2y9, alien3y9, alien4y9, alien5y9, alien6y9, alien7y9, alien8y9, alien9y9, alien10y9)
                aliens.add(alien1y10, alien2y10, alien3y10, alien4y10, alien5y10, alien6y10, alien7y10, alien8y10, alien9y10, alien10y10)
                aliens.add(alien1y11, alien2y11, alien3y11, alien4y11, alien5y11, alien6y11, alien7y11, alien8y11, alien9y11, alien10y11)
                aliens.add(alien1y12, alien2y12, alien3y12, alien4y12, alien5y12, alien6y12, alien7y12, alien8y12, alien9y12, alien10y12)

                
            # Aliens
            with open('skinpack.inv', 'rb') as f:
                skins = pickle.load(f)
                
            if skins == 0:                     # Deafult
                image = pygame.image.load('games-caches\game0_cache/aliens\opponents_deafult.png')
            if skins == 1:                     # Winter
                image = pygame.image.load('games-caches\game0_cache/aliens\opponents_winter.png')
            if skins == 2:                     # Fire
                image = pygame.image.load('games-caches\game0_cache/aliens\opponents_fire.png')
            if skins == 3:                     # Alien
                image = pygame.image.load('games-caches\game0_cache/aliens\opponents_deafult.png')
            if skins == 4:                     # Lose
                image = pygame.image.load('games-caches\game0_cache/aliens\opponents_lose.png')
            
            if game_levels == 1:
                print('')
                print('Level 1')
                print('')
                level1(screen, aliens, 1.4, 0.15, image)                    
            if game_levels == 2:
                print('')
                print('Level 2')
                print('')
                level2(screen, aliens, 1.4, 0.25, image)
 
                    
            if game_levels == 3:
                print('')
                print('Level 3')
                print('')
                level3(screen, aliens, 1.4, 0.35, image)
 
                    
            if game_levels == 4:
                print('')
                print('Level 4')
                print('')
                level4(screen, aliens, 1.4, 0.40, image)
 
                    
            if game_levels == 5:
                print('')
                print('Level 5')
                print('')
                level5(screen, aliens, 1.4, 0.50, image)
 
                
            if game_levels == 6:
                print('')
                print('Level Boss')
                print('')
                level_boss(screen, aliens, 1.4, 0.61, image)
 
            
            
            if game_levels >= 7:

                print('')
                print('Level Ultimaite')
                print('')
                
                level_ultumait(screen, aliens, 1.4, 0.7, image)

                
                
            
            #/Aliens
        
          