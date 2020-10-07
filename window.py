
import pygame
from settings import Setting
from ship import Ship
from pygame.sprite import Group
import game_func as gf
from statics import Stat
from button import Button
from scoreboard import Scoreboard 

def run_game():
    pygame.init()
    setg =  Setting()
    #giving a tuple value for screen resolution
    screen = pygame.display.set_mode((setg.scr_width, setg.scr_height))
    pygame.display.set_caption('Alien Invasion')
    stats = Stat(setg)
    ship = Ship(screen, setg)
    bullets = Group()
    aliens = Group()
    gf.new_fleet(screen, setg, aliens, ship)
    play_button = Button(screen, 'START')
    sb = Scoreboard(screen, setg, stats)

    #game starts here
    while True:#main loop of the game
        gf.chk_events(sb, screen, ship,setg, bullets, stats, play_button, aliens)
        if stats.active_game:
            ship.update()
            gf.bullet_update(bullets, aliens, screen
                , setg, ship, stats, sb )
            gf.alien_update(sb, aliens, setg, ship, stats, screen, bullets)
   
        gf.scr_update(setg, screen, ship, aliens, bullets, stats, play_button, sb )


       
run_game()
