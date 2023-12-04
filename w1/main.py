from PIL import Image, ImageDraw, ImageFont
import time
import random, os
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick

result = 0
#왼 위 오 아래
joystick = Joystick()
# my_image = Image.new("RGB", (joystick.width, joystick.height)) #도화지!
# my_draw = ImageDraw.Draw(my_image) #그리는 도구!

#reSiz = back.crop((0,0,240,240))
#joystick.disp.image(reSiz)

# 이미지 파일 경로
image_path = 'image/background.png' 
back = Image.open(image_path)

# 이미지 크기
image_width, image_height = back.size
screen_width, screen_height = 240, 240

# 초기 상태 설정
scroll_speed = 50
current_position = 0

# 조각내고 초기 화면 표시
cropped_image = back.crop((0, current_position, screen_width, screen_height + current_position))
joystick.disp.image(cropped_image)
    
while True:
# 이미지를 이동시킬 위치 계산
    current_position += scroll_speed

    # 이미지가 끝까지 스크롤되면 처음으로 돌아가도록 설정 -> 멈추기
    if current_position > image_height - screen_height:
        #current_position = 0
        result = 1
        break

    # 이미지 조각내기 및 화면에 표시
    cropped_image = back.crop((0, current_position, screen_width, screen_height + current_position))
    joystick.disp.image(cropped_image)

    # 일정한 간격으로 스크롤을 표시하기 위해 지연 시간 설정
    #time.sleep(0.1)  # 원하는 딜레이 설정
        

if result == 1:
    # 이미지 크기 설정
    image_width, image_height = 240, 240
    background_color = (0, 0, 0, 100)  # 배경색을 검정색으로 설정하거나 필요한 색상으로 변경

    # 새 이미지 생성
    image = Image.new("RGBA", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # 텍스트 설정
    text = "GAME CLEAR!!"
    text_color = (255, 255, 255)  # 텍스트 색상을 흰색으로 설정하거나 필요한 색상으로 변경
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)  # 폰트와 크기 설정

    # 텍스트 크기 계산
    #text_width, text_height = draw.textsize(text, font=font)
    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 텍스트를 이미지 중앙에 배치하기 위한 위치 계산
    text_x = (image_width - text_width) // 2
    text_y = (image_height - text_height) // 2

    # 텍스트를 이미지에 그리기
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # 현재 화면 이미지와 합성
    composed_image = Image.alpha_composite(cropped_image.convert("RGBA"), image)

    # 이미지를 화면에 표시
    joystick.disp.image(composed_image)


"""def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)

    my_circle = Character(joystick.width, joystick.height)
    while True:
        command = None
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'

        elif not joystick.button_D.value:  # down pressed
            command = 'down_pressed'

        elif not joystick.button_L.value:  # left pressed
            command = 'left_pressed'

        elif not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
            
        else:
            command = None

        my_circle.move(command)

        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0, 255, 255, 100))
        my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
    #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)


if __name__ == '__main__':
    main()"""