import pygame
import pygame.freetype

displayFlags = pygame.DOUBLEBUF | pygame.HWSURFACE
speed = 500

def runGame():
    pygame.init()

    screen = pygame.display.set_mode(size = (640, 480), flags = displayFlags)
    clock = pygame.time.Clock()
    fps = 30
    font = pygame.freetype.SysFont("", 32)

    frameTime = 0.0

    running = True

    (x, y) = (320, 240)
    

    while running:
        screen.fill((0, 0, 0))
        font.render_to(screen, (32, 32), f"{clock.get_fps():.1f} fps", (255, 255, 255))
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_q]:
            running = False

        if keystate[pygame.K_UP]:
            y = y - (speed * frameTime)
        
        if keystate[pygame.K_DOWN]:
            y = y + (speed * frameTime)

        if keystate[pygame.K_LEFT]:
            x = x - (speed * frameTime)

        if keystate[pygame.K_RIGHT]:
            x = x + (speed * frameTime)

        if keystate[pygame.K_1]:
            fps = 30
        
        if keystate[pygame.K_2]:
            fps = 60

        if keystate[pygame.K_3]:
            fps = 120

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect((x, y), (128, 128)))
        pygame.display.flip()
        frameTime = (clock.tick(fps) / 1000.0)