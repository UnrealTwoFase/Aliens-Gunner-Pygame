import pygame, sys
from my_game_buttons import Button
from game0_start import Start_Game0
from my_game_game_controls import Control
from game0_main_file import Aliens_and_Gunner

# Game Info
name = "Aliens & Gunner"
version = "1.0.0"
build = "1"
gameinfo = name + ' v' + version + ' build ' + build
#/Game Info


#Head
pygame.init()
first_running = True
game_Play_start = False
game_Play_one_start = False
first_running_button_game = False
first_running_button_start = True
clock = pygame.time.Clock()
pygame.display.set_caption(gameinfo)
pygame.display.set_icon(pygame.image.load('icongame.png'))
speed_gun = 0
#/Head


#Display   1024x768, 800x600, 640x480
W = 800
H = 600
screen = pygame.display.set_mode((W, H))
background = pygame.image.load('games-caches\my_game_cache/bg\style1/bg_main-menu.jpg')
background_select_game = pygame.image.load('games-caches\my_game_cache/bg\style1/bg_select-menu.jpg')
#/Display


#Color
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
white_blue = (63, 243, 210)
#/Color


#Button image
start_img = pygame.image.load('games-caches/my_game_cache/images1/start_button.png')                 # Start_img
exit_img = pygame.image.load('games-caches/my_game_cache/images1/exit_button.png')                   # Exit_img
setting_img = pygame.image.load('games-caches/my_game_cache/images1/setting_button.png')             # Setting_img

game_zero_img =  pygame.image.load('games-caches\select_game_cache\images\game0_button_play.png')    # Game0_img
game_zero_img2 =  pygame.image.load('games-caches\select_game_cache\images\game0_button1.png')       # Game0_img2
#/Button image
 

#StartButton
start_button = Button(298, 168, start_img, 1)                             # Start_Button
exit_button = Button(298, 265, exit_img, 1)                               # Exit_Button
setting_button = Button(650,485, setting_img, 0.5)                        # Setting_Button

game_zero_button = Button(515, 241, game_zero_img, 0.7)                   # Game0_Button
game_zero_button2 = Button(320, 250, game_zero_img2, 1.2)                 # Game0_Button2
#/StartButton


#Methods
control = Control()                  # Control
gun = 0
bullets = 0
#/Methods

print('  ')
print('      "Game1" Start')

#Game
while True: 
    clock.tick(60)                       # Устоновка значения FPS

    if first_running:                    # Проверка на первый запуск
        screen.blit(background,(0,0))    # Устоновка Фона
        start_button.draw_button(screen) # Button start
        exit_button.draw_button(screen)  # Button exit
        first_running = False            # Устоновка флага False у первого запуска

    control.game_events(gun, bullets, screen, speed_gun)   # Обработка events


    # Кнопки
    if first_running_button_start:             # Проверка на первый запуск
    
        # Menu Buttons
        if start_button.is_clicked():          # Проверка на клик start
            first_running_button_start = False # Flag false
            
            # Debug Prints
            print('         _____                      _____  ')
            print('        |  | |||||||||||||||||||||||| |  |')
            print('        |----||Нажата нопка "START"||----|')
            print('        |  | |||||||||||||||||||||||| |  |')
            print(' ')
            #/debug Prints

            # Подготовка к запуску игры
            screen.blit(background_select_game,(0,0))          # Load Backgrounds
            
            game_zero_button2.draw_button(screen)              # Game Buttons load2
            #game_one_button2.draw_button(screen)              # Game Buttons load2
            
            first_running_button_game = True                  # Flag True
            #/Подготовка к запуску игры  
            
        if exit_button.is_clicked():                           # Проверка на клик exit
            sys.exit()                                         # Выход из игры
        #/Menu Buttons    
 
    # Select Game 
    if first_running_button_game:                             # Проверка на первый запуск
        # Game0
        if game_zero_button2.is_clicked():  
            game_Play_start = True
            print("Выбрана игра №1, ожидание подтверждения...")
            game_zero_button.draw_button(screen)                                   # Game Buttons load
            Aliens_and_Gunner.start(screen)
            first_running_button_game = False

            first_running = True
            first_running_button_start = True
           
        #/Game0
    #/Select Game   
    #/Кнопки

    pygame.display.flip()       # Обновление экрана
#/Game
