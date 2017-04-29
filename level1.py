import pygame
import gameclass1
import tkinter as tk

import os

key = gameclass1.key()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("window")

image1 = pygame.image.load("BalconyDoortoBdR.gif")
image2 = pygame.image.load("BalconyWall.gif")
image3 = pygame.image.load("BRTV.gif")
image4 = pygame.image.load("BalconyChairs.gif")
image = []
image.append(image1)
image.append(image2)
image.append(image3)
image.append(image4)
window.blit(image1,(0,0))


pygame.init()

font_title = pygame.font.SysFont("monospace", 15)
title = font_title.render("You need to find three keys to open the door", 1, (0,0,0))
key_number = str(key.sum) + "/3 collected."
image_info = font_title.render(key_number, 1, (0,0,0))
window.blit(title, (0, 0))
window.blit(image_info, (0, 30))

image_length = len(image)
index = 0

time = 0
time1 = 0
time2 = 0
time3 = 0


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

        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            if index == 2:
                if time == 0 and time1 ==0:
                    if x1>=457 and x1<=501 and y1>=418 and y1<=454:
                        print("key got")
                        key.key_got()
                        time1 += 1
                    
                if time == 0 and time2 ==0:
                    if x1>=83 and x1<= 119 and y1 >= 545 and y1 <= 560:
                        print("key got")
                        key.key_got()
                        time2 += 1


            if index == 1:
                if time ==0 and time3 == 0:
                    if x1>= 430 and x1<= 463 and y1>= 449 and y1<=513:
                        print("key got")
                        key.key_got()
                        time3 += 1

            if index == 0:
                if x1>= 40 and x1<= 179 and y1>= 146 and y1<=535:
                    if key.finish():
                        gameLoop = False
                    else:
                        print("You must collect all the stuff needed to open the door!")

            key_number = str(key.sum) + "/3 collected."
            image_info = font_title.render(key_number, 1, (0,0,0))
            window.blit(image[index],(0,0))
            window.blit(title, (0, 0))
            window.blit(image_info, (0, 30))



    pygame.display.flip()



pygame.quit()
