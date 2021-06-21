import pygame

def show(*rects):
    screen = pygame.display.set_mode(size = (640, 480))
    running = True

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for rect in rects:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), rect, 1)
        pygame.display.flip()
 
