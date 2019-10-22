
from gpiozero import Button
from time import sleep
import pygame, sys

GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
SCORES = [100, 500, 1000, 0, 10000, 0, 1000, 500, 100]
IOS = [
        Button(10, pull_up=False),
        Button(9, pull_up=False),
        Button(11, pull_up=False),
        Button(0, pull_up=False),
        Button(5, pull_up=False),
        Button(6, pull_up=False),
        Button(13, pull_up=False),
        Button(19, pull_up=False),
        Button(26, pull_up=False),
]

running = True
triggered = False
triggeredIndex = 0
score = 0
count = 0


def text_objects(text):
        font = pygame.font.SysFont("comicsansms", 610)
        rendered = font.render(text, True, WHITE)
        return rendered, rendered.get_rect(center=screen.get_rect().center)

pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1500, 500))
pygame.display.update()

while running:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                running = False 
                        if event.key == pygame.K_1:
                                score = score + SCORES[0]
                        if event.key == pygame.K_2:
                                score = score + SCORES[1]
                        if event.key == pygame.K_3:
                                score = score + SCORES[2]                                                               
                        if event.key == pygame.K_4:
                                score = score + SCORES[3]
                        if event.key == pygame.K_5:
                                score = score + SCORES[4]
                        if event.key == pygame.K_6:
                                score = score + SCORES[5]
                        if event.key == pygame.K_7:
                                score = score + SCORES[6]     
                        if event.key == pygame.K_8:
                                score = score + SCORES[7]  
                        if event.key == pygame.K_9:
                                score = score + SCORES[8]  
                        if event.key == pygame.K_r:
                                score = 0
                                triggered = False
                                print("reset")
                                sleep(0.89)



        #GPIO logic
        if triggered:
                print("triggered: " + " " + str(triggeredIndex) + " " + str(IOS[triggeredIndex].is_pressed) + " " + str(count))
                if IOS[triggeredIndex].is_pressed:
                    triggered = False
                    print("Sleep")
                    sleep(0.89)
                    
        else:
                print("not triggered: " + str(count))
                if not IOS[7].is_pressed: 
                      triggeredIndex = 7
                      triggered = True
                      score = score + SCORES[7]


        # redraw logic
        screen.fill(GREEN)
        screen.blit(*text_objects(str(score)))

        pygame.display.flip()
        
        count = count + 1

#End
pygame.quit()