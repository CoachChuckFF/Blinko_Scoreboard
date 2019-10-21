import pygame, sys

GREEN = [0, 255, 0]
WHITE = [255, 255, 255]

running = True
score = 0;

def text_objects(text):
        font = pygame.font.SysFont("comicsansms", 889)
        rendered = font.render(text, True, WHITE)
        return rendered, rendered.get_rect(center=screen.get_rect().center)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.update()

while running:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                running = False 


        # score logic
        score = score + 1

        # redraw logic
        screen.fill(GREEN)
        screen.blit(*text_objects(str(score)))

        pygame.display.flip()

#End
pygame.quit()
