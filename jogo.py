# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

import os
import cmd
import sys
import textwrap
import time
import random

screen_width = 100

###Player Setup###
class player:
    def __init__(self):
        self.name = (int(input))
        self.hp = 0
        self.mp = 0
        self.status_effects = ()
        self.location = 'start'
myPlayer = player ()

###Title screen###
def title_screen_selections():
    option = input(">")
    if option.lower == ("play"):
        start_game () # placeholder until written
    elif option.lower () == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        system.exit()
    while option.lower () not in ('play', 'help','quit'):
        print ("Please enter a valid command")
        option = input(">")
        if option.lower == ("play"):
        start_game () # placeholder until written
        elif option.lower () == ("help"):
        help_menu()
        elif option.lower() == ("quit"):
        system.exit()
def title_screen():
    os.system('clear')
    print ('######################')
    print ('#Welcome to our game!#')
    print ('######################')
    print ('       -Play-         ')
    print ('       -Help-         ')
    print ('       -Quit-         ')
    title_screen_selections ()

def help_menu():
        print ('######################')
        print ('#Welcome to our game!#')
        print ('######################')
        print ('- Use up (w), down (s), left(a) and right(d) to move!')
        print (' Type your commands to use them')
        print ('Good luck and have fun!')
        #print ('       -Quit-         ')
        title_screen_selections ()


###GAME FUNCTIONALLITY####
def start_game (): 



######MAP#######
