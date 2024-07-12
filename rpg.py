
# Example file showing a circle moving on screen
import pygame
from random import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1145, 720))
clock = pygame.time.Clock()
running = True
dt = 0

m1 = True
mission = False 
n_mission = 0
mcompleted = False
g_mission = True

done1 = False
done2 = False
done3 = False
done4 = False
done5 = False
done6 = False


pygame.display.set_caption("Scrolling Text")
 
font=pygame.font.SysFont('timesnewroman',  30)


###NPCS###

npc_image1 = pygame.image.load("NPC1.png")
npc1_rect = pygame.Rect(720, 120, npc_image1.get_width(), npc_image1.get_height())
npc_image2 = pygame.image.load("NPC2.png")
npc2_rect = pygame.Rect(335, 170, npc_image2.get_width(), npc_image2.get_height())
npc_image3 = pygame.image.load("NPC3.png")
npc3_rect = pygame.Rect(840, 290, npc_image3.get_width(), npc_image3.get_height())
npc_image4 = pygame.image.load("NPC4.png")
npc4_rect= pygame.Rect(310, 310, npc_image4.get_width(), npc_image4.get_height())
npc_image5 = pygame.image.load("lily.png")
npc_image5 = pygame.transform.scale(npc_image5, (100, 100))
npc5_rect = pygame.Rect(570, 550, npc_image5.get_width() ,npc_image5.get_height())
npc_image6 = pygame.image.load("lou.png")
npc_image6 = pygame.transform.scale(npc_image6, (100, 100))
npc6_rect = pygame.Rect(1000, 200, npc_image6.get_width(), npc_image6.get_height())

###CASAS###

casa4 = pygame.image.load("casa4.png")
casa4_rect = pygame.Rect(510, 3, casa4.get_width(), casa4.get_height())
casa1 = pygame.image.load("casa1.png")
casa1_rect = pygame.Rect(300, 2, casa1.get_width(), casa1.get_height())
casa2 = pygame.image.load("casa2.png")
casa2_rect = pygame.Rect(900, 300, casa2.get_width(), casa2.get_height())
casa3 = pygame.image.load("casa3.png")
casa3_rect = pygame.Rect(550, 350, casa3.get_width(), casa3.get_height())
mk = pygame.image.load("stall.png")
mk_rect = pygame.Rect(10, 300, mk.get_width(), mk.get_height())
gal = pygame.image.load("gal (1).png")
gal_rect = pygame.Rect(400, 400, gal.get_width(), gal.get_height())

###ITENS###

chk = pygame.image.load("chicken.png")
chk_rect = pygame.Rect(410, 620, chk.get_width(), chk.get_height())
dr = pygame.image.load("dress.png")
dr = pygame.transform.scale(dr, (50,50))
dr_rect = pygame.Rect(40, 600, dr.get_width(), dr.get_height())
wg = pygame.image.load("wg.png")
wg = pygame.transform.scale(wg, (120,80))
wg_rect = pygame.Rect (70, 200, wg.get_width(), wg.get_height())
fd = pygame.image.load("food.png")
fd_rect = pygame.Rect (775, 125, fd.get_width(), fd.get_height())
dk = pygame.image.load("drink.png")
dk = pygame.transform.scale(dk, (40,40))
dk_rect = pygame.Rect (820, 130, dk.get_width(), dk.get_height())
fb = pygame.image.load("football.png")
fb = pygame.transform.scale (fb, (40, 40))
fb_rect = pygame.Rect (900, 600, fb.get_width(), fb.get_height() )
bb = pygame.image.load("baseball.png")
bb = pygame.transform.scale (bb, (40, 40))
bb_rect = pygame.Rect (355, 200, bb.get_width(), bb.get_height())

obstaculos = [casa1_rect, casa2_rect, casa3_rect, casa4_rect, mk_rect, gal_rect] 

items = [chk_rect]
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2 - 100)
jogador = pygame.image.load("player.png")
player_rect = pygame.Rect(player_pos.x, player_pos.y, jogador.get_width(), jogador.get_height())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    pp = pygame.image.load("bg.jpg").convert()
    screen.blit(pp, (0,0))

    ##images loading##
    
    screen.blit(npc_image1, (720,120))
    screen.blit(npc_image2, (335,170))
    screen.blit(npc_image3, (840,290))
    screen.blit(npc_image4, (310,310))
    screen.blit(npc_image5, (570,550))
    screen.blit(npc_image6, (1000,200))
    screen.blit(casa4, (510,3))
    screen.blit(casa1, (300,2))
    screen.blit(casa2, (900,300))
    screen.blit(casa3, (550,350))
    screen.blit(mk, (10,300))
    screen.blit(gal, (400,400))
    screen.blit(chk,(410,620))
    screen.blit(wg, (70,200))
    screen.blit(dr, (50, 600))
    screen.blit(fd, (775,125))
    screen.blit(dk, (820, 130))
    screen.blit(fb, (900, 600))
    screen.blit(bb, (355, 200))

    screen.blit(jogador,player_pos )

    
    ##collision##

    keys = pygame.key.get_pressed()
   
    ##player speed##
    player_speed = 5

    ##collision###

    imp = pygame.image.load("casa4.png").get_width()
    imp = pygame.image.load("casa4.png").get_height()
    
    imp = pygame.image.load("casa1.png").get_height()
    imp = pygame.image.load("casa1.png").get_width()

    imp = pygame.image.load("casa2.png").get_width()
    imp = pygame.image.load("casa2.png").get_height()

    imp = pygame.image.load("casa3.png").get_width()
    imp = pygame.image.load("casa3.png").get_height()

    player_pos_old_x = player_pos.x
    player_pos_old_y = player_pos.y

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    player_rect = pygame.Rect(player_pos.x, player_pos.y, jogador.get_width(), jogador.get_height())

    for obs in obstaculos:
        if pygame.Rect.colliderect(player_rect, obs):
            player_pos.x = player_pos_old_x
            player_pos.y = player_pos_old_y

    ###NPC DAR MISSÃO###
    
    if pygame.Rect.colliderect(player_rect, npc1_rect) and mission == False and done1 == False:
        mission = True
        n_mission = 1
    if pygame.Rect.colliderect(player_rect, npc2_rect) and mission == False and done2 == False:
        mission = True
        n_mission = 2
        g_mission = 1
    if pygame.Rect.colliderect(player_rect, npc3_rect) and mission == False and done3 == False:
        mission = True
        n_mission = 3
    if pygame.Rect.colliderect(player_rect, npc4_rect) and mission == False and done4 == False:
        mission= True
        n_mission = 4
    if pygame.Rect.colliderect(player_rect, npc5_rect) and mission == False and done5 == False:
        mission = True
        n_mission = 5
    if pygame.Rect.colliderect(player_rect, npc6_rect) and mission == False and done6 == False:
        mission = True
        n_mission = 6
    
    ###MISSÕES###

    if m1 == True:
        text = font.render('Go to the girl with a hat to get mission one', True, 'white', 'purple')
        screen.blit(text, (10,10))

    if mission == True:
        if n_mission == 1:
            text = font.render('Alexia: Bring me a chicken', True, 'white', 'pink')
            m1 = False
        if n_mission == 2:
            text = font.render('Daisy: Go get me a new dress in the shop', True, 'white', 'pink')
        if n_mission == 3:
            text = font.render('Luke: Go get me a baseball ball', True, 'white', 'pink')    
        if n_mission == 4:
            text = font.render('Klaus: Bring me a football ball', True, 'white', 'pink')
        if n_mission == 5:
            text = font.render('Lily: Go to Alexia and bring me one of her drinks and a piece of cake', True, 'white', 'pink')
        if n_mission == 6:
            text = font.render('Louis: Bring me a fucking water gun', True, 'white', 'pink')

        screen.blit(text, (10,10))
    
    
        
    
    ###ITENS###

    if pygame.Rect.colliderect(player_rect, chk_rect) and n_mission == 1:
        done1 = True
        mission = False
        mcompleted = True
        miss = font.render('Mission one complete. You received a "Cookie Cat"!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    if pygame.Rect.colliderect(player_rect, dr_rect) and n_mission == 2:
        done2 = True
        mission = False
        mcompleted = True
        miss = font.render('mission two complete. You received a "Jornal 3"!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    if pygame.Rect.colliderect(player_rect, bb_rect) and n_mission == 3:
        done3 = True
        mission = False
        mcompleted = True
        miss = font.render('mission three complete. You received a "Totoro" plushie', True, 'red', 'black')
        screen.blit(miss, (20,20))
    if pygame.Rect.colliderect(player_rect, fb_rect) and n_mission == 4:
        done4 = True
        mission = False
        mcompleted = True
        miss = font.render('mission four complete. You received a "Camality Box"!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    if pygame.Rect.colliderect(player_rect, dk_rect) and n_mission == 5:
        done5 = True
        mission = False
        mcompleted = True
        miss = font.render('mission five complete. You received an "MEWO" plushie and "Fe3O4" album!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    if pygame.Rect.colliderect(player_rect, wg_rect) and n_mission ==6:
        done6 = True
        mission = False
        mcompleted = True
        miss = font.render ('Last mission complete! You received 28 smiley faces!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    
    ###FIM###

    if done1 == True and done2 == True and done3 == True and done4 == True and done5 == True and done6 == True:
        miss = font.render('You completed all of the missions!', True, 'red', 'black')
        screen.blit(miss, (20,20))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000






pygame.quit()