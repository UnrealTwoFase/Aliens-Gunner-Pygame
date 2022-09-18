import pygame, sys
from my_game_buttons import Button
from game0_bullet import Bullet


class Control():
          

    def image_draw(self, screen, image, x, y, scale):
        self.screen = screen
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))  
        
        self.screen.blit(self.image, (x, y))
          
    def draw_text(self, screen, text, color, size, x, y):
        font_name = pygame.font.match_font('arial')
        
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (color))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
         
    def game_events(self, gun, bullets, screen, speed_gun):
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:             # Quit
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:           # right
                    gun.center += speed_gun
                    gun.mright = True
                    
                elif event.key == pygame.K_a:         # left
                    gun.center -= speed_gun
                    gun.mleft = True
                
                elif event.key == pygame.K_SPACE:     # Space
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
                    
            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_d:           # right
                    gun.mright = False
                    
                elif event.key == pygame.K_a:         # left
                    gun.mleft = False

   
    def update_display(self, screen, gun, bullets, aliens, score, game_levels, doom, boom, speed_boost, double_score, shield, shield_b, bestscore):
        
        white = 255, 255, 255
        if shield >= 1:
            shield_b.draw_button(screen)
            self.draw_text(screen, 'SHIELD', white, 20, 700, 280)  
            
        for bullet in bullets.sprites():
            bullet.draw_bullet()  
        gun.output()
        aliens.draw(screen)
        bullets.update() 
        doom.draw(screen)
        boom.draw(screen)

        
        self.draw_text(screen, 'Your Score: ' + str(score), white, 20, 720, 70)
        self.draw_text(screen, 'Opponents: ' + str(len(aliens)), white, 18, 730,100)
        self.draw_text(screen, 'Level: ' + str(game_levels), white, 15, 760,130)
        self.draw_text(screen, 'Your BEST Score: ' + str(bestscore), white, 14, 100, 5) 
  
                
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                
        
        pygame.display.update()
    
    
    def update_collision(self, bullets, aliens, gun, block, boxes, shield):
            
        if pygame.sprite.spritecollideany(gun, aliens):
            
            if shield == 1:
                ''''''
            if shield == 0:
                for alien in aliens.copy():
                    aliens.remove(alien)
                if len(bullets) != 0:
                    for bullet in bullets.copy():
                        bullets.remove(bullet)
                if len(boxes) != 0:
                    for box in boxes.copy():
                        boxes.remove(box)
            return True
            

        if pygame.sprite.spritecollideany(block, aliens):
            if shield == 1:
                ''''''
            if shield == 0:
                print('Game Over')
                for alien in aliens.copy():
                    aliens.remove(alien)
                for bullet in bullets.copy():
                    bullets.remove()
                for box in boxes.copy():
                    boxes.remove(box)
                return True
            
            
            
            
        