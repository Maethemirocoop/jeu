import pygame 
pygame.init()
from game import Game
from player import Player

# générer une fênetre
pygame.display.set_caption("Peace in our time")
screen =pygame.display.set_mode((1080, 720))

# importation des images arrière plan
background = pygame.image.load("assets/bg.jpg")

#charger le jeu
game = Game()

# chargement du joueur
player = Player()

running = True 

# boucle de condition 
while running : 

    # appliquer un arrière plan 
    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1080 - game.player.rect.width:
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    pygame.display.flip()
    
    # si mon jouer ferme la fenêtre 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # detection des touches lacher par le joueur 
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False