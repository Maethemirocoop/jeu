import pygame 
pygame.init()

# générer une fênetre 
pygame.display.set_caption("Comet Fall game")
screen =pygame.display.set_mode((1080, 720))

# importation des images arrière plan
background = pygame.image.load("assets/bg.jpg")

running = True 

# boucle de condition 
while running : 

    # appliquer un arrière plan 
    screen.blit(background, (0, -200))
    pygame.display.flip()
    
    # si mon jouer ferme la fenêtre 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
