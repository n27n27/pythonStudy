

import pygame
import os
# 초기화
pygame.init()

## 화면 크기 설정
# 가로 크기
screen_width = 640
# 세로 크기
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Pang")

# FPS
clock = pygame.time.Clock()

##################################################################

## 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 현재 파일 위치 반환
current_path = os.path.dirname(__file__)
# images 폴더 위치 반환
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height - stage_height


# 이벤트 루프
# 게임 진행 여부 확인
running = True 

while running:

    #게임 화면의 초당 프레임 수
    dt = clock.tick(60)

    # 캐릭터가 1초 동안 100 만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼!
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼!
    

    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생하였는가 (x 표시)
        if event.type == pygame.QUIT:
            running = False
       
   
    # 스크린 좌표        
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    # 게임화면을 다시 그리기!
    pygame.display.update()


pygame.quit()


