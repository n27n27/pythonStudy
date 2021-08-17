import pygame
import os
### 기본초기화
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

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리


    # 5. 화면 그리기



    pygame.display.update()


pygame.quit()
