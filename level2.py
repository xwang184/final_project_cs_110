import pygame
import jy
from tkinter import *

import os


key = jy.key()
laptop = jy.laptop(key)
remote = jy.remote(laptop)
laptop.update()

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("window")


image1 = pygame.image.load("1.jpg")
image2 = pygame.image.load("2.jpg")
image3 = pygame.image.load("3.jpg")
image4 = pygame.image.load("4.jpg")
image = []
image.append(image1)
image.append(image2)
image.append(image3)
image.append(image4)
window.blit(image1,(0,0))

remote_image = pygame.image.load("remote.png")
image_length = len(image)
index = 0


remote_found = False



font_title = pygame.font.SysFont("monospace", 20)
title = font_title.render("You must collect all the images to open \
the door!", 1, (0,0,0))
key_number = str(key.sum) + "/3 collected."
image_info = font_title.render(key_number, 1, (0,0,0))
window.blit(title, (0, 0))
window.blit(image_info, (0, 30))


gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index += 1
                if index == image_length:
                    index = 0
        
        
            if event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = image_length - 1

window.blit(image[index],(0,0))
    window.blit(title, (0, 0))
        window.blit(image_info, (0, 30))
            if remote_found:
                window.blit(remote_image, (0, 500))

    if event.type == pygame.MOUSEBUTTONDOWN:
        x1, y1 = pygame.mouse.get_pos()
            if index == 3:
                if x1>= 568 and x1 <= 596 and y1 >= 395 and y1 <= 399:
                    remote_found = True
                if x1>= 264 and x1 <= 344 and y1 >= 230 and y1 <= 308:
                    print("key got")
                    key.key_got()

        if remote_found and x1>=42 and x1 <= 50 and y1>=522 and y1 <= 533:
            remote.click()
                laptop.mainloop()
            if remote_found and x1>=64 and x1 <= 74 and y1>=541 and y1 <= 553:
                remote.close()
                laptop.mainloop()

if index == 1:
    if x1>= 274 and x1<= 526 and y1>= 150 and y1<=297:
        print("key got")
            key.key_got()
            
            if index == 0:
                if x1>= 191 and x1<= 213 and y1>= 325 and y1<=337:
                    if key.finish():
                        gameLoop = False
                    else:
                        print("You must collect all the images to open the door!")
    
        key_number = str(key.sum) + "/3 collected."
            image_info = font_title.render(key_number, 1, (0,0,0))
            window.blit(image[index],(0,0))
            window.blit(title, (0, 0))
            window.blit(image_info, (0, 30))
            if remote_found:
                window.blit(remote_image, (0, 500))
                
            
            
pygame.display.flip()



pygame.quit()

