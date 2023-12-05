import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import random, os
from colorsys import hsv_to_rgb

class Character:
    def __init__(self, width, height):
        self.appearance = Image.open('image/돌(1).png') #.crop((100,100,200,200))
        self.state = None
        #self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.position = [int(width/2 - 20), int(height/2 - 20), int(width/2 + 20), int(height/2 + 20)]
        self.outline = "#00FF00"

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
                self.position[2] -= 5
                
            elif command == 'right_pressed':
                self.position[0] += 5
                self.position[2] += 5