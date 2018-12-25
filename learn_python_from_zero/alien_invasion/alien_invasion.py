#! /usr/local/bin/python3
import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_functions as gf 

def run_game() :
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    bg_color = (230,230,230)
    ship = Ship(ai_settings,screen)
    #Make a group to store bullets in.
    bullets = Group()

    while True :
        gf.check_events(ai_settings, screen, ship, bullets)
        #update the ship
        ship.update()

        #update the bullet
        gf.update_bullets(bullets)
        #Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()
