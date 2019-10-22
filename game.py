
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



def text_objects(text):
        font = pygame.font.SysFont("comicsansms", 610)
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

        #GPIO logic
        if triggered:
                triggered = False
                IOS[triggeredIndex].wait_for_release()
                sleep(1)
        else:
                if IOS[0].is_pressed(): 
                      triggeredIndex = 0
                      triggered = True  
                      score = score + SCORES[0]
                if IOS[1].is_pressed(): 
                      triggeredIndex = 1
                      triggered = True 
                      score = score + SCORES[1] 
                if IOS[2].is_pressed(): 
                      triggeredIndex = 2
                      triggered = True  
                      score = score + SCORES[2]
                if IOS[3].is_pressed(): 
                      triggeredIndex = 3
                      triggered = True 
                      score = score + SCORES[3] 
                if IOS[4].is_pressed(): 
                      triggeredIndex = 4
                      triggered = True  
                      score = score + SCORES[4]
                if IOS[5].is_pressed(): 
                      triggeredIndex = 5
                      triggered = True  
                      score = score + SCORES[5]
                if IOS[6].is_pressed(): 
                      triggeredIndex = 6
                      triggered = True  
                      score = score + SCORES[6]
                if IOS[7].is_pressed(): 
                      triggeredIndex = 7
                      triggered = True  
                      score = score + SCORES[7]
                if IOS[8].is_pressed(): 
                      triggeredIndex = 8
                      triggered = True  
                      score = score + SCORES[8] 


        # redraw logic
        screen.fill(GREEN)
        screen.blit(*text_objects(str(score)))

        pygame.display.flip()

#End
pygame.quit()
