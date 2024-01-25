# Example file showing a circle moving on screen
import pygame
import random
from labyrinthe import Labyrinthe
# pygame setup
pygame.init()

#constantes
tilesize = 32 # taille d'une tuile IG
size = (20, 10) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement

# color
ground_color = "#EDDACF"
grid_color = "#7F513D"
player_color = "#9F715D"

laby = Labyrinthe(size[0], size[1])
laby.load_from_file("laby-01.csv")
screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
clock = pygame.time.Clock()
running = True
dt = 0
show_grid = True
show_pos = False

keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0 }

player_pos = pygame.Vector2(round(0), round(1))

#tour de boucle, pour chaque FPS
while running:
    screen.fill(ground_color)

    # lecture clavier / souris
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 1
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 0
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 0

            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_g:
                show_grid = not show_grid
            if event.key == pygame.K_p:
                show_pos = not show_pos
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouse_pos:", pos)
    


    next_move += dt
    # gestion des déplacements
    if next_move>0:
        new_x, new_y = int(player_pos.x),int(player_pos.y)
        if keys['UP'] == 1:
            new_y -=1
        elif keys['DOWN'] == 1:
            new_y += 1
        elif keys['LEFT'] == 1:
            new_x -=1
        elif keys['RIGHT'] == 1:
            new_x += 1



        # vérification du déplacement du joueur                                    
        if not laby.hitBox(new_x, new_y):
            player_pos.x, player_pos.y = new_x, new_y
            next_move -= player_speed

        if show_pos:
            print("pos: ",player_pos)

    laby.draw(screen, tilesize)

    # affichage des différents composants
    if show_grid:
        for i in range(1,size[0]):
            pygame.draw.line(screen,grid_color, (tilesize*i, 0), (tilesize*i, tilesize*size[0]) )
        for i in range(0,size[1]):
            pygame.draw.line(screen,grid_color, (0, tilesize*i), (tilesize*size[0], tilesize*i) )

    #affichage du joueur
    pygame.draw.rect(screen, player_color, pygame.Rect(player_pos.x*tilesize, player_pos.y*tilesize, tilesize, tilesize))

    pygame.display.flip()
    dt = clock.tick(fps)

pygame.quit()