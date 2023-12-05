from PIL import Image, ImageDraw, ImageFont
import time
import random, os
from colorsys import hsv_to_rgb

from Character import Character 
from Joystick import Joystick

# 왼 위 오 아래
joystick = Joystick()

# 게임 시작 출력--------------------------------------------------------------------------
# 이미지 크기 설정
image_width, image_height = 240, 240
background_color = (0, 0, 0, 0)  # 배경색을 검정색으로 설정하거나 필요한 색상으로 변경

# 새 이미지 생성
image = Image.new("RGBA", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# 텍스트 설정
text = "GAME START!!"
text_color = (255, 255, 255)  # 텍스트 색상을 흰색으로 설정하거나 필요한 색상으로 변경
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)  # 폰트와 크기 설정

# 텍스트 크기 계산
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# 텍스트를 이미지 중앙에 배치하기 위한 위치 계산
text_x = (image_width - text_width) // 2
text_y = (image_height - text_height) // 2

# 텍스트를 이미지에 그리기
draw.text((text_x, text_y), text, fill=text_color, font=font)

# 이미지를 화면에 표시
joystick.disp.image(image)
    
time.sleep(2)
 # 게임 시작 출력 완----------------------------------------------------------------------   



my_stone = Character(joystick.width, joystick.height)

# 이미지 파일 경로
image_path = 'image/background.png'
back = Image.open(image_path)

# 초기 상태 설정
scroll_speed = 50
current_position = 0

# 이미지의 높이 가져오기
image_height = back.height  # 이미지의 높이를 가져옵니다.

# 캐릭터 이미지의 크기 조정
#my_stone.appearance = my_stone.appearance.resize((joystick.width, joystick.height))
my_stone.appearances[my_stone.image_index] = my_stone.appearances[my_stone.image_index].resize((joystick.width, joystick.height))
mask = my_stone.appearances[my_stone.image_index].split()[3]

result = 0
while True:
    command = None
    if not joystick.button_L.value:  # left pressed
        command = 'left_pressed'
    elif not joystick.button_R.value:  # right pressed
        command = 'right_pressed'
    elif not joystick.button_A.value: # A pressed
        command = 'A_pressed'
    else:
        command = None

    my_stone.move(command)

    # 이미지를 이동시킬 위치 계산
    current_position += scroll_speed

    # 이미지가 끝까지 스크롤되면 멈추기
    if current_position > image_height - joystick.height:  # 이미지가 끝까지 스크롤되면 멈추기
        result = 1
        break

    # 이미지 조각내기 및 화면에 표시
    cropped_image = back.crop((0, current_position, joystick.width, joystick.height + current_position))
    display_image = cropped_image.copy()  # 배경 이미지 복사
    my_draw = ImageDraw.Draw(display_image)  # 이미지 위에 그리기 도구 생성

    #초기 위치 맨왼쪽위...
    box=(-100,-100)
    # 이미지 위에 캐릭터 그리기
    #display_image.paste(my_stone.appearance, tuple(my_stone.position))
    display_image.paste(my_stone.appearances[my_stone.image_index], tuple(my_stone.position), mask)

    # 디스플레이에 이미지 표시
    joystick.disp.image(display_image)






 
# 게임 실패 했다. --------------------------------------------------------------------------
if result == 0:
    time.sleep(2)
    
    # 이미지 크기 설정
    image_width, image_height = 240, 240
    background_color = (0, 0, 0, 100)  # 배경색을 검정색으로 설정하거나 필요한 색상으로 변경

    # 새 이미지 생성
    image = Image.new("RGBA", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # 텍스트 설정
    text = "GAME OVER!!"
    text_color = (255, 0, 0)  # 텍스트 색상을 흰색으로 설정하거나 필요한 색상으로 변경
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
        
# 게임 클리어 했다. -------------------------------------------------------------------------
if result == 1:
    time.sleep(2) # 딜레이 주기
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