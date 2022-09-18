import pygame, sys, pickle, random
from game0_bullet import Bullet
from my_game_buttons import Button
from my_game_game_controls import Control
from pygame.sprite import Group
from game0_gun import Gun
from game0_opponents import Opponents_Alien
from drop_boosters import Drop_Boosters




class Start_Game0():
    def start_game(screen):
        
        
        # Head
        bg_load = pygame.image.load('games-caches/game0_cache/images0/LOAD_screen2.png')   # Bakground
        last = pygame.time.get_ticks()
        
        # False and True
        load_screen = True              # Flag True
        aliens_and_scores_while = True  # Flag True
        while_run = True                # Flag True
        setting_menu_while = False      # Flag False
        update_display_while = False    # Flag False
        game_while = False              # Flag False
        pause_while_menu = False        # Flag False
        pause_while = False             # Flag False
        game_over_screen_w = False        # Flag False
        box_text_draw = False
        load_screen_setting = True
        shuield_draw = False
        
        time_w_sp = False
        time_w_sc = False
        time_w_sh = False
        #/False and True
        
        # deafult strings
        game_levels = 0
        shield = 0
        score = 0
        bestscore = 0
        skins = 0               # 0, 1, 2, 3
        speed_gun = 1.45
        double_score = 1
        # point = 0
        cooldown_sp = 17000
        cooldown_sc = 30000
        cooldown_sh = 25000
        #/deafult strings
  
   
        # Download stats
        with open('bestscore.unrealcfg', 'rb') as f:
            bestscore = pickle.load(f)
        with open('skins.unrealcfg', 'rb') as f:
            skins = pickle.load(f)
        #/Download stats
        
        #Skins
        # Deafult - 0
        deafult_gun = pygame.image.load('games-caches/game0_cache\images0\game_sprites\gun.png')
        #/Deafult
        # Winter - 1
        winter_gun = pygame.image.load('games-caches/game0_cache\images0\game_sprites\gun_w.png')
        #/Winter
        # Fire - 2
        fire_gun = pygame.image.load('games-caches/game0_cache\images0\game_sprites\gun_f.png')
        #/Fire
        # Aliens - 3
        alien_gun = pygame.image.load('games-caches/game0_cache\images0\game_sprites\gun_a.png')
        #/Aliens
        #/Skins
        
        #Check stats
        if skins == 0:                     # Deafult
            gun = Gun(screen, deafult_gun)
        if skins == 1:                     # Winter
            gun = Gun(screen, winter_gun)
        if skins == 2:                     # Fire
            gun = Gun(screen, fire_gun)
        if skins == 3:                     # Alien
            gun = Gun(screen, alien_gun)
        #/Check stats
        
        # Methods
        aliens = Group()                # Создание группы aliens
        bullets = Group()               # Bullets
        boxes = Group()                 # Boxes
        control = Control()             # Control
        #/Methods
        #/Head
        
        # Body  
        # Images
        box_random_img = pygame.image.load('games-caches\game0_cache\images0\game_sprites/box_random.png')
        shield_img = pygame.image.load('games-caches\game0_cache\images0\game_sprites\shield.png')
        # Screens
        game_over_screen = pygame.image.load('games-caches/game0_cache/images0/game_overbutton.png')   
        load_screen_img = pygame.image.load('games-caches/game0_cache/images0/LOAD_screen2.png')
        block_img = pygame.image.load('games-caches/game0_cache/images0/game_sprites/block.png')
        #/Screens
        # Screen button
        load_screen_button_img = pygame.image.load('games-caches/game0_cache/images0/LOAD_screen_button.png')
        pause_bg_img = pygame.image.load('games-caches/game0_cache/images0/game_sprites/pause.png')
        #/Screen button
        # Setting button
        setting_menu_img = pygame.image.load('games-caches/game0_cache/images0/setting_sprite/setting_menu.png')
        setting_select_img = pygame.image.load('games-caches/game0_cache/images0/setting_sprite/setting_menu_buttons_select.png')
        setting_img = pygame.image.load('games-caches/my_game_cache/images1/setting_button.png')           
        #/Setting button
        
        exit_button_img_g = pygame.image.load('games-caches/game0_cache/images0/exitbuttongame.png')        
        intro_button1_img = pygame.image.load('games-caches/game0_cache/images0/intro_button1.png')
        intro_button2_img = pygame.image.load('games-caches/game0_cache/images0/intro_button2.png')
        game_stop_button_img = pygame.image.load('games-caches/game0_cache/images0/game_sprites/stop_button.png')
        #/Images
        
        # Buttons
        load_screen_b = Button(49, 287, load_screen_button_img, 1)
        gameoverbutton = Button(230, 230, game_over_screen, 1.4)
        block = Button(9, 600, block_img, 1)
        
        # Setting Menu
        pause_b = Button(250, 100, pause_bg_img, 1) 
        setting_select = Button(80, 450, setting_select_img, 0.4)
        setting_select1 = Button(255, 450, setting_select_img, 0.4)
        setting_select2 = Button(422, 450, setting_select_img, 0.4)
        setting_select3 = Button(600, 450, setting_select_img, 0.4)
        setting_button = Button(665,365, setting_img, 0.5)                    
        exit_button_menu = Button(730, 90, exit_button_img_g, 0.3) 
        #/Setting Menu
        
        shield_block = Button(0, 510, shield_img, 1)
        exit_button_g = Button(526, 114, exit_button_img_g, 0.3)
        intro_button = Button(395, 236, intro_button2_img, 1)
        skill_button = Button(400, 300, intro_button1_img, 1)
        game_stop_button = Button(5, 540, game_stop_button_img, 0.5)
        #/Buttons
        #/Body
        
        # Отрисовка для игры
        block.draw_button(screen)
        #/Отрисовка для игры

        # Game
        while while_run:
            control.game_events(gun, bullets, screen, speed_gun)       # Контроль нажатия кнопок

            # Load screen
            if load_screen:                         # Load screen цикл
                # game_over_screen = False
                screen.fill((0, 0, 0))
                control.image_draw(screen, load_screen_img, 5, 0, 1)                  # Устоновка обоев загрузки
                load_screen_b.draw_button(screen)           # Устоновка кнопки в бг
                setting_button.draw_button(screen)
                
                # Узнаём какой скин ставить
                if skins == 0:                   # Deafult
                    gun = Gun(screen, deafult_gun)
                if skins == 1:                   # Winter
                    gun = Gun(screen, winter_gun)
                if skins == 2:                   # Fire
                    gun = Gun(screen, fire_gun)
                if skins == 3:                   # Alien
                    gun = Gun(screen, alien_gun)
                #/Узнаём какой скин ставить
                
                if load_screen_b.is_clicked():              # Проверка на клик
                    load_screen = False                     # Флаг False
                    update_display_while = True             # Флаг True
                    game_while = True                       # Флаг True
                    aliens_and_scores_while = True          # Флаг True
                    
                if setting_button.is_clicked():   # Setting Button
                    setting_menu_while = True     # Флаг False
                    load_screen = False           # Флаг True
                     
            # SeTTing Menu        
            if setting_menu_while:
                               # Background load 
                    # Load menu
                if load_screen_setting:
                    load_screen_setting = False
                    screen.fill((0, 0, 0))
                    control.image_draw(screen, setting_menu_img, 5, 40, 1.4)
                    setting_select.draw_button(screen)    # select skin button deafult
                    setting_select1.draw_button(screen)   # select skin button winter
                    setting_select2.draw_button(screen)   # select skin button Fire
                    setting_select3.draw_button(screen)   # select skin button alien
                    exit_button_menu.draw_button(screen)  # Отрисовка кнопки
                    
                
                # Установка номeра скина
                if setting_select.is_clicked(): # Deafult
                    skins = 0
                    print('deafult skin')
                if setting_select1.is_clicked(): # Winter
                    skins = 1
                    print('winter skin')
                if setting_select2.is_clicked(): # Fire
                    skins = 2
                    print('fire skin')
                if setting_select3.is_clicked(): # Alien
                    skins = 3
                    print('aliens skin')
                #/Установка номра скина
                    
                # Выход из меню и запись выбранного скина
                if exit_button_menu.is_clicked():
                    setting_menu_while = False
                    load_screen = True
                        
                    with open('skins.unrealcfg', 'wb') as f:
                        pickle.dump(skins, f )
                #/Выход из меню и запись выбранного скина
            #/SeTTing Menu
            #/Load screen     

            # Game Over screen
            if game_over_screen_w:
                screen.fill((0, 0, 0))                           # Заполнение экрана цветом BLACK           
                gameoverbutton.draw_button(screen)               # Отрисовка кнопки
                control.draw_text(screen, 'Your final Score: ' + str(score), 18, 360, 289)  # Отрисовка финального счёта
                control.draw_text(screen, 'Your BEST Score: ' + str(bestscore), 18, 380, 310)  # Отрисовка лучшего счёта
                if score > bestscore:
                    bestscore = score
                    with open('bestscore.unrealcfg', 'wb') as f:
                        pickle.dump(bestscore, f )

                if gameoverbutton.is_clicked():
                    load_screen = True                       # Флаг True
                    game_over_screen_w = False
                    update_display_while = False             # Флаг False
                    game_while = False                       # Флаг False
                    aliens_and_scores_while = False          # Флаг False
                    speed_gun = 1.45
                    score = 0
            #/Game Over screen


            # Drawing Display
            if update_display_while:                  # Цикл обновления экрана
                screen.fill((0, 0, 0))                # Заполнение чёрным цвеотм экрана
            #/Drawing Display

            time_w = False
            # Game While
            if game_while:                                          # Цикл игры
                gun.update_position(speed_gun)                                   # Обновляем перемещения предмета gun
                bullets.update()                                        # Обновляем позицию
                aliens.update()                                         # Обновляем позицию
                boxes.update()
                control.update_display(screen, gun, bullets, aliens, score, game_levels, boxes, speed_gun, double_score, shield, shield_block, game_stop_button, bestscore)    # Обновление экрана
                

                
                # Цикл смерти игрока
                if control.update_collision(bullets, aliens, gun, block, boxes, shield):   # Если игрок умер
                    game_levels = -1                                        # Сбрасываем уровень
                    double_score = 1
                    
                    game_over_screen_w = True
                    update_display_while = False             # Флаг True
                    game_while = False                       # Флаг True
                    aliens_and_scores_while = False          # Флаг False
                    

                #/Цикл смерти игрока
                
                # Aliens Killes
                
                collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)   # Проверка коллизии пуль и пришельцев
                if collisions:    
                    score += 1 * double_score                                   # Прибовляем очки
                    chanse = random.randint(1, 700)
                    if chanse >= 335 and chanse <= 350:    
                            x = random.randint(1, 700)
                            box_random = Drop_box(screen, box_random_img, 2, 1, x, -50)
                            boxes.add(box_random)
                #/Aliens Killes
                
                # Boxesc Boosters  collisions
                chanse_booster = random.randint(1, 3)
                for box in boxes.copy():
                    if pygame.sprite.spritecollideany(gun, boxes):
                        box_text_draw = True
                        boxes.remove(box)
                        
                        print(chanse_booster)
                        if chanse_booster == 1:
                            time_w_sp = True
                            speed_gun_boost = speed_gun * 2.5
                            if speed_gun >= 8:
                                speed_gun = 8
                            else:
                                speed_gun = speed_gun_boost
                        if chanse_booster == 2:
                            time_w_sc = True
                            double_score = 2
                            
                        if chanse_booster == 3:
                            time_w_sh = True
                            shield = 1
                            
                            
                        
                #/Boxesc Boosters  collisions          
                # Box speed boost time
                now = pygame.time.get_ticks() 
                if time_w_sc:                  
                    if now - last >= cooldown_sc:
                        last = now
                        double_score = 1
                        time_w_sc = False
                if time_w_sp:
                    if now - last >= cooldown_sp:
                        last = now
                        speed_gun = 1.2
                        time_w_sp = False
                        
                if time_w_sh:
                    if now - last >= cooldown_sh:
                        last = now
                        shield = 0
                        time_w_sh = False
                #/Box speed boost time
                
                # Создание группы пришельцев и вывод очков
                if aliens_and_scores_while:                                          # Цикл
                    if len(aliens) == 0:                                             # Проверка количества пришельцев
                        game_levels += 1                                             # Увелечение уровня
                        while_true = True                                            # Флаг True
                        Opponents_Alien.aliens_creature(screen, aliens, game_levels) # Создание толпы пришельцев
                    for alien in aliens.copy():
                        if alien.rect.y > 650:
                            score -= 10
                            aliens.remove(alien)
                         
                #/Создание группы пришельцев и вывод очков
                
                if game_stop_button.is_clicked():
                    pause_while = True                       # Флаг True
                    game_over_screen_w = False                 # Флаг False
                    update_display_while = False             # Флаг False
                    game_while = False                       # Флаг False
                    aliens_and_scores_while = False          # Флаг False
                    
                # Pause Button
                if pause_while:
                    pause_while_menu = True            # Флаг True
                    pause_b.draw_button(screen)        # Отрисовка кнопки
                    intro_button.draw_button(screen)   # Отрисовка кнопки
                    exit_button_g.draw_button(screen)  # Отрисовка кнопки
                #/Pause Button
            # Pause menu
            if pause_while_menu:        
                if intro_button.is_clicked():
                    return False                             
                if exit_button_g.is_clicked():
                    game_over_screen_w = False                 # Флаг False
                    pause_while = False                      # Флаг False
                    update_display_while = True              # Флаг True
                    game_while = True                        # Флаг True
                    aliens_and_scores_while = True           # Флаг True

                    
            #/Pause menu

            pygame.display.update()          # Обновление экрана
            #/Создание группы пришельцев и вывод очков
            #/Game While
        #/Game