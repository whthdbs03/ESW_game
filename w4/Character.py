import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import random, os
from colorsys import hsv_to_rgb

class Character:
    def __init__(self, width, height):
        self.appearances = [Image.open('image/stone(1).png'),
                           Image.open('image/stone(2).png'),
                           Image.open('image/stone(3).png'),
                           Image.open('image/stone(4).png')]
        self.state = None
        #self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.position = [0,0,32,29] #초기위치
        self.outline = "#00FF00"
        self.image_index = 0

    def move(self, command = None):
        if command == None:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            # if command == 'up_pressed':
            #     self.position[1] -= 5
            #     self.position[3] -= 5

            # elif command == 'down_pressed':
            #     self.position[1] += 5
            #     self.position[3] += 5

            if command == 'left_pressed':
                self.position[0] -= 5
                self.image_index = (self.image_index - 1) % 4  # 3-2-1-0 순으로 반복
                self.appearance = self.appearances[self.image_index]
                #self.position[2] -= 5
                
            elif command == 'right_pressed':
                self.position[0] += 5
                self.image_index = (self.image_index + 1) % 4  # 0-1-2-3 순으로 반복
                #self.position[2] += 5
                self.appearance = self.appearances[self.image_index]
            #elif command == 'A_pressed':
                #