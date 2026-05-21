import pygame
import random

def genereaza_culori():
    grila = []
    for _ in range(10):
        rand = []
        for _ in range(10):
            culoare = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rand.append(culoare)
        grila.append(rand)
    return grila

pygame.init()

ecran = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid - Auto Update")

matrice_culori = genereaza_culori()
ruleaza = True
ultimul_update = pygame.time.get_ticks()

while ruleaza:
    ecran.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            culoare_curenta = matrice_culori[y][x]
            dreptunghi = (x * 50, y * 50, 50, 50)
            pygame.draw.rect(ecran, culoare_curenta, dreptunghi)
            
    pygame.display.flip()
    
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza = False
            
    timp_curent = pygame.time.get_ticks()
    if timp_curent - ultimul_update >= 5000:
        matrice_culori = genereaza_culori()
        ultimul_update = timp_curent

pygame.quit()