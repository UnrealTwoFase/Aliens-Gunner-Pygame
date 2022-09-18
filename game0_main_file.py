import pygame, sys, pickle, random

from game0_gun import Gun
from pygame.sprite import Group
from game0_bullet import Bullet
from my_game_buttons import Button
from drop_boosters import Drop_Boosters
from my_game_game_controls import Control
from game0_opponents import Opponents_Alien
from gamewhile0 import Gamewhile0

class Aliens_and_Gunner():
    def start(screen):
 
        # 0 - deafult, 1 - winter, 2 - fire, 3 - alien, 4 - lose, 5 - bg window, 6 - bg lose
        
        # Head
        main_menu_while = True
        startrenderithm = True
        oned = True
        inventory_while = False
        game_while = False
        gameover_while = False
        pause_w = False
        shop_w = False
        inv_start = False
        skinbuttons = False
        silent_case_w = False
        neverlose_case_w = False
        boosters_w = False
        boosters_c = False
        boosters_sh = False
        
        # deafult strings
        game_levels = 0     # Levels
        score = 0           # Score
        bestscore = 0       # Bestscore
        skins = 0           # 0, 1, 2, 3 - Skin
        background_skin = 2 # 0, 1, 2 - bg skin
        speed_gun = 1    # Speed gun deafult
        double_score = 1    # Active double score
        money = 0           # Money
        shield = 0          # Active shield
        price = 100
        start = 0

        #/deafult strings
   
        # Download stats
        with open('bestscore.unrealcfg', 'rb') as f:
            bestscore = pickle.load(f)
        with open('skinpack.inv', 'rb') as f:
            skins_l = pickle.load(f)
        #/Download stats
        skins = skins_l
        # Methods
        aliens = Group()                # Создание группы aliens
        bullets = Group()               # Bullets
        boxes = Group()                 # Boxes
        boomboxes = Group()                 # Boxes
        dooms = Group()                 # Boxes
        control = Control()             # Control
        gun = Gun(screen, skins)
        
        
        white = 255, 255, 255
        black = 0, 0, 0
        #/Methods
        #/Head
        
        
        # Body  
        # Images
        main_menu_bg = pygame.image.load('games-caches\game0_cache\menu_player\menu.png')
        inventory_bg = pygame.image.load('games-caches\game0_cache\menu_player\inventory.png')
        
        pause_img = pygame.image.load('games-caches\game0_cache\pausemenu\pausebutton.png')
        pause_img_b1 = pygame.image.load('games-caches\game0_cache\pausemenu\pausebutton1.png')
        pause_img_b2 = pygame.image.load('games-caches\game0_cache\pausemenu\pausebutton2.png')
        
        #bg
        background_lose_img = pygame.image.load('games-caches\game0_cache\inventory_shop/background_skin/neverlose.png')
        background_window_img = pygame.image.load('games-caches\game0_cache\inventory_shop/background_skin\window.png')
        #/bg
        
        
        pause_bg = pygame.image.load('games-caches\game0_cache\pausemenu\pause_menu.png')
        pause_button = pygame.image.load('games-caches\game0_cache\pausemenu\pausebutton.png')
        
        gameover_img = pygame.image.load('games-caches\game0_cache\gameover.png')
        shield_img = pygame.image.load('games-caches\game0_cache\shield.png')
        
        exit_img = pygame.image.load('games-caches\game0_cache\exit.png')
        play_game_img = pygame.image.load('games-caches\game0_cache\menu_player\playgame.png')
        inventory_img = pygame.image.load('games-caches\game0_cache\menu_player\inventory_b.png')
        
        skin_pack_d_img = pygame.image.load('games-caches\game0_cache\case\skin_pack_d.png')
        skin_pack_f_img = pygame.image.load('games-caches\game0_cache\case\skin_pack_f.png')
        skin_pack_w_img = pygame.image.load('games-caches\game0_cache\case\skin_pack_w.png')
        skin_pack_a_img = pygame.image.load('games-caches\game0_cache\case\skin_pack_a.png')
        skin_pack_l_img = pygame.image.load('games-caches\game0_cache\case\skin_pack_l.png')
        
        shop_img = pygame.image.load('games-caches\game0_cache\shop_b.png')
        box_img = pygame.image.load('games-caches/game0_cache/box_random.png')
        block_img = pygame.image.load('games-caches/game0_cache/block.png')
        
        boom_img = pygame.image.load('games-caches\game0_cache/boom\granade.png')
        boom_bom_img = pygame.image.load('games-caches\game0_cache/boom/boom.png')
        #/Images
        
        
        # Buttons
        background_neverlose = Button(510, 147, background_lose_img, 1)
        background_window = Button(590, 147, background_window_img, 1)
        
        gameover_b = Button(120, 190, gameover_img, 1)
        
        
        play_game_b = Button(65, 250, play_game_img, 0.7) 
        inventory_b = Button(500, 250, inventory_img, 0.7) 
        exit_b = Button(730, 50, exit_img, 2) 
        
        shield_block = Button(0, 550, shield_img, 1)
        shop_b = Button(30, 80, shop_img, 1)
        
        
        skin_pack_d_but = Button(80, 260, skin_pack_d_img, 1)
        skin_pack_f_but = Button(200, 260, skin_pack_f_img, 1)
        skin_pack_w_but = Button(320, 260, skin_pack_w_img, 1)
        skin_pack_a_but = Button(440, 260, skin_pack_a_img, 1)
        skin_pack_l_but = Button(560, 260, skin_pack_l_img, 1)
        
        pause_b = Button(10, 30,pause_img, 0.3)
        pause_b1 = Button(37, 245,pause_img_b1, 1)
        pause_b2 = Button(37, 310,pause_img_b2, 1)
        block = Button(9, 600, block_img, 1)
        #/Buttons
        #/Body
        # deafult_score = 0
        ithems_inv = [0, 1, 2, 3, 4, 6, 5]
        # with open('bestscore.unrealcfg', 'wb') as f:
            # pickle.dump(deafult_score, f)
            
        ithems = ithems_inv
        while True:
            control.game_events(gun, bullets, screen, speed_gun)       # Контроль нажатия кнопок
            chanse_booster = random.randint(1, 900)
            
            if main_menu_while:     # Main Menu
                control.image_draw(screen, main_menu_bg, 0, 0, 1)
                play_game_b.draw_button(screen)
                inventory_b.draw_button(screen)
                if play_game_b.is_clicked():
                    print('Play')
                    game_while = True
                    start_w = True
                    main_menu_while = False
                if inventory_b.is_clicked():
                    print('invent')
                    main_menu_while = False
                    inventory_while = True
            
            if inventory_while:
                if oned:
                    oned = False
                    inventory_while = False
                    control.image_draw(screen, inventory_bg, 0, 0, 1)
                    exit_b.draw_button(screen)

                if startrenderithm:
                    startrenderithm = False
                    skinbuttons = True
                    
                    skin_pack_d_but.draw_button(screen)
                    skin_pack_w_but.draw_button(screen)
                    skin_pack_f_but.draw_button(screen)
                    skin_pack_a_but.draw_button(screen)
                    skin_pack_l_but.draw_button(screen)

            if skinbuttons:
                if skin_pack_d_but.is_clicked():
                    skins = 0
                    print('Deafult Skin Pack Activeted')
                if skin_pack_w_but.is_clicked():
                    skins = 1
                    print('Winter Skin Pack Activeted')
                if skin_pack_f_but.is_clicked():
                    skins = 2
                    print('Fire Skin Pack Activeted')
                if skin_pack_a_but.is_clicked():
                    skins = 3
                    print('Aliens Skin Pack Activeted')
                if skin_pack_l_but.is_clicked():
                    skins = 4
                    print('Lose Skin Pack Activeted')
                    
                if skins != skins_l:
                    with open('skinpack.inv', 'wb') as f:
                        pickle.dump(skins, f )
                 
            if exit_b.is_clicked():
                return True
                       
            if pause_w:
                game_while = False
                control.image_draw(screen, pause_bg, 0, 0, 1) 
                pause_b1.draw_button(screen)
                pause_b2.draw_button(screen)
                
                if pause_b1.is_clicked():
                    game_while = True
                    pause_w = False
                if pause_b2.is_clicked():
                    main_menu_while = True
                    pause_w = False
                    
            
            if game_while:   # Цикл игры
                screen.fill((0, 0, 0))   
                
                gun.update_position(speed_gun)                                   # Обновляем перемещения предмета gun
                bullets.update()                                        # Обновляем позицию
                aliens.update()                                         # Обновляем позицию
                boxes.update()
                boomboxes.update()
                dooms.update()
                
                pause_b.draw_button(screen)
                control.update_display(screen, gun, bullets, aliens, score, game_levels, dooms, boomboxes, speed_gun, double_score, shield, shield_block, bestscore)    # Обновление экрана
                
                if pause_b.is_clicked():
                    pause_w = True
                
                if control.update_collision(bullets, aliens, gun, block, boxes, shield):   # Цикл смерти игрока
                    game_levels = -1
                    for doom in dooms.copy():
                        dooms.remove(doom)
                    for alien in aliens.copy():
                        sliens.remove(alien)
                    gameover_while = True
                    game_while = False
                
                
                collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)   # Aliens Killes
                if collisions:
                    score += 1 * double_score
                    if chanse_booster >= 0 and  chanse_booster <= 1000:
                        x = random.randint(0, 740)
                        y = random.randint(-40, -20)
                        randomboom = random.randint(1, 1000)
                        if randomboom >100  and randomboom < 150:
                            x = random.randint(50, 550)
                            boxboom = Drop_Boosters(screen, boom_img, 1, 0.3, x, -20)
                            boomboxes.add(boxboom)
                
                for boomb in boomboxes.copy():
                    collisions = pygame.sprite.groupcollide(bullets, boomboxes, True, True)   # Aliens Killes
                    if collisions:
                        
                        xbomb = boomb.rect.x
                        ybomb = boomb.rect.y
                        boomsdoom = Drop_Boosters(screen, boom_bom_img, 0, 0.09, xbomb, ybomb)
                        dooms.add(boomsdoom)
                        boomboxes.remove(boomb)
                        
                if pygame.sprite.spritecollideany(gun, boomboxes):
                    for boomb in boomboxes.copy():
                        boomboxes.remove(boomb)
                    gameover_while = True
                    game_while = False
                    
                if pygame.sprite.spritecollideany(gun, dooms):
                    gameover_while = True
                    game_while = False
                    for do in dooms.copy():
                        dooms.remove(do)
                for alien in aliens.copy():
                    if pygame.sprite.spritecollideany(alien, dooms):
                        for do in dooms.copy():
                            dooms.remove(do)
                        aliens.remove(alien)
      
                # Создание группы пришельцев и вывод очков
                
                if len(aliens) == 0:
                    game_levels += 1
                    Opponents_Alien.aliens_creature(screen, aliens, game_levels)
                    for doom in dooms.copy():
                        dooms.remove(doom)
                    
                #/Создание группы пришельцев и вывод очков

         
            if gameover_while:
                screen.fill((0, 0, 0))
                gameover_b.draw_button(screen)
                control.draw_text(screen, 'Your score: ' + str(score), white, 20, 380, 400)
                if score > bestscore:
                    bestscore = score
                    with open('bestscore.unrealcfg', 'wb') as f:
                        pickle.dump(bestscore, f)
                        
                control.draw_text(screen, 'Best Score: ' + str(bestscore), white, 18, 380, 430)  # Отрисовка лучшего счёта
                    
                if gameover_b.is_clicked():
                    gameover_while = False
                    game_while = True
            
            pygame.display.update()          # Обновление экрана








  