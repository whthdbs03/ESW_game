import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import random, os
from colorsys import hsv_to_rgb
class attack:
    def __init__(self, position, command):
        '''
        position : 돌멩이 발사한 Character의 중앙 위치
        command : 조이스틱 입력 값
        '''
        self.appearance = Image.open('image/공격돌멩이.png')
        self.speed = 20
        self.damage = 10
        self.position = np.array([position[0]-3, position[1]-3, position[0]+3, position[1]+3])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.state = None
        self.outline = "#0000FF"
        
        if command['right_pressed']:
            self.direction['right'] = True
        if command['left_pressed']:
            self.direction['left'] = True

    def move(self):
        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed