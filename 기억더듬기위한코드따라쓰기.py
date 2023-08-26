import pygame
group1 = Group()
group2 = Group()
group1_group = pygame.sprite.Group()
group1_group.add(group1)
group2_group = pygame.sprite.Group()
group2_group.add(group2)
while True:
    collided = pygame.sprite.groupcollide(group1, group2, False, True)
    for item in collided.items():
        print(item)
