import pygame
import pygame.freetype

displayFlags = pygame.DOUBLEBUF | pygame.HWSURFACE
fps = 120

def runGame():
    pygame.init()

    screen = pygame.display.set_mode(size = (640, 480), flags = displayFlags)
    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont("", 32)


    running = True

    (x, y) = (320, 240)
    

    while running:
        screen.fill((0, 0, 0))
        font.render_to(screen, (32, 32), f"{clock.get_fps():.1f} fps", (255, 255, 255))
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_q]:
            running = False

        if keystate[pygame.K_UP]:
            y = y - 5
        
        if keystate[pygame.K_DOWN]:
            y = y + 5

        if keystate[pygame.K_LEFT]:
            x = x - 5

        if keystate[pygame.K_RIGHT]:
            x = x + 5


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect((x, y), (128, 128)))
        pygame.display.flip()
        clock.tick(fps)