import pygame, sys, pickle, random
from pygame.sprite import Group
from my_game_buttons import Button
from my_game_game_controls import Control

class Inventory():
    def system_case():
        chanse_itm = random.randint(300, 600)
        if chanse_itm < 400:
            print('Your prize: gun winter')
        if chanse_itm > 500 and chanse_itm < 600:
            print('Your prize: gun fire')
        if chanse_itm > 600:
            print('Your prize: gun alien')
            
    def shop(screen, money):
        cases = []
        control = Control()
        
        #img

        
        #/img
        # Button
        buy_b = Button(346, 402, buy_img, 1)
        #/Button
        
        control.image_draw(screen, shop_bg, 0, 0, 1)
        
        pygame.display.update()