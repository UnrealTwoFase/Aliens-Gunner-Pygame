import pygame, pickle, sys, random

from pygame.sprite import Group
from my_game_buttons import Button
from game0_opponents import Opponents_Alien

class Gamewhile0():
    def game(screen, control, gun, bullets, aliens, boxes, shield, game_levels, background_skin, score, start, money, block, speed_gun, double_score, bestscore): 
        if start == 0:
            game_while = True
            pause_w = False
            gameover_while = False
            
            shield_img = pygame.image.load('games-caches\game0_cache\images0\game_sprites\shield.png')
            background_lose_img = pygame.image.load('games-caches\game0_cache\inventory_shop/background_skin/neverlose.png')
            background_window_img = pygame.image.load('games-caches\game0_cache\inventory_shop/background_skin\window.png')
            gameover_img = pygame.image.load('games-caches\game0_cache\gameover.png')
            
            gameover_b = Button(120, 190, gameover_img, 1)
            shield_block = Button(0, 550, shield_img, 1)
            background_neverlose = Button(510, 147, background_lose_img, 1)
            background_window = Button(590, 147, background_window_img, 1)
        if game_while == True:

            #Bakground
            if background_skin == 0:
                screen.fill((0, 0, 0))
            if background_skin == 1:
                control.image_draw(screen, background_window, 0, 0, 1)
            if background_skin == 2:
                control.image_draw(screen, background_lose_img, 0, 0, 1)
            #/Bakground   
            
            gun.update_position(speed_gun)                                   # Обновляем перемещения предмета gun
            bullets.update()                                        # Обновляем позицию
            aliens.update()                                         # Обновляем позицию
            boxes.update()
            
            control.update_display(screen, gun, bullets, aliens, score, game_levels, boxes, speed_gun, double_score, shield, shield_block, bestscore)    # Обновление экрана
            
            
            if control.update_collision(bullets, aliens, gun, block, boxes, shield):   # Цикл смерти игрока
                game_levels = -1
                if speed_gun >= 2:
                    speed_gun = 1.6
                if double_score > 1:
                    double_score = 1
                if shield != 0:
                    shield = 0
                gameover_while = True
            
            
            collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)   # Aliens Killes
            if collisions:
                score += 1 * double_score
                if chanse_booster >= 100 and  chanse_booster <= 150:
                    x = random.randint(0, 740)
                    y = random.randint(-60, -40)
                    
                    box = Drop_Boosters(screen, box_img, 2, 1, x, y)
                    boxes.add(box)
            
             
            for box in boxes.copy():  # Boxesc Boosters  collisions
                if pygame.sprite.spritecollideany(gun, boxes):
                    chanse_boost = random.randint(1, 3)
                    boxes.remove(box)
                    if chanse_boost == 1:
                        double_score = 2
                        print('sc')
                    if chanse_boost == 2:
                        speed_gun * 2
                        print('sp')
                    if chanse_boost == 3:
                        "Shield"
                        shield = 1
                        print('sh')
     
            # Box speed boost time
            
            #/Box speed boost time
            
            # Создание группы пришельцев и вывод очков
            
            if len(aliens) == 0:
                game_levels += 1
                Opponents_Alien.aliens_creature(screen, aliens, game_levels)
                for alien in aliens.copy():
                    if alien.rect.y > 650:
                        score -= 5
                        aliens.remove(alien)
                
            #/Создание группы пришельцев и вывод очков

            
            
            if pause_w:
                control.image_draw(screen, pause_bg, 0, 0, 1) 

            
            
        if gameover_while:
            screen.fill((0, 0, 0))
            gameover_b.draw_button(screen)
            control.draw_text(screen, 'Your score: ' + str(score), white, 20, 380, 400)
            money += score // 2
            with open('money.inv', 'wb') as f:
                pickle.dump(money, f)
            if score > bestscore:
                bestscore = score
                with open('bestscore.unrealcfg', 'wb') as f:
                    pickle.dump(bestscore, f)
                    
            control.draw_text(screen, 'Best Score: ' + str(bestscore), white, 18, 380, 430)  # Отрисовка лучшего счёта
                
        if gameover_b.is_clicked():
            gameover_while = False
            game_while = True
    
        pygame.display.update()          # Обновление экрана