#! /usr/local/bin/python3
"""
   Settings data for Alien Invasion project 
"""

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self) :
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 3.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5


