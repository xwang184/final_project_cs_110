import tkinter as tk
from tkinter import *
import gameclass1
import pygame
import jy
import random


class gameGUI:

    def __init__(self):
        self.main_window = tk.Tk()

        self.main_window.title('Escape Room')

        frame = tk.Canvas(bg = "white", height = 700, width = 1300)

        frame.pack(side = TOP)

        background = tk.PhotoImage(file = "/Users/apple/Desktop/final project/StartMenu.gif")

        image = frame.create_image(1300, 0, anchor = NE, image = background)

        frame.pack()

        self.button1 = tk.Button(self.main_window, text = 'Easy', command = self.game1)

        self.button1.grid(row=3, column=5)

        self.button1.pack()

        self.button2 = tk.Button(self.main_window, text = 'Difficult', command = self.game2)

        self.button2.grid(row=4, column=5)

        self.button2.pack()

        tk.mainloop()

    def game1(self):
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
        title = font_title.render("You need to find two keys to open the door", 1, (0,0,0))
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


    def game2(self):

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

        time = 0
        time1 = 0
        time2 = 0



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
                        if time == 0 and time1 ==0:
                            if x1>= 264 and x1 <= 344 and y1 >= 230 and y1 <= 308:
                                print("key got")
                                key.key_got()
                                time1 +=1

                    if remote_found and x1>=42 and x1 <= 50 and y1>=522 and y1 <= 533:
                        remote.click()
                        laptop.mainloop()

                    if index == 1:
                        if time ==0 and time2 == 0:
                            if x1>= 274 and x1<= 526 and y1>= 150 and y1<=297:
                                print("key got")
                                key.key_got()
                                time2 += 1

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

def main():

    gameGUI()

main()
