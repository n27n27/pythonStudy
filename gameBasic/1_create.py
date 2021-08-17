
import pygame

# 초기화
pygame.init()

## 화면 크기 설정
# 가로 크기
screen_width = 480
# 세로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 이벤트 루프
# 게임 진행 여부 확인
running = True 

while running:
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생하였는가 (x 표시)
        if event.type == pygame.QUIT:
            running = False






# pygame 종료
pygame.quit()

