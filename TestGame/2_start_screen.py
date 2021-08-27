import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔 # RGB
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

# 시작 화면 보여주기
def displayStartScreen():
    # 그릴위치, 색상, 시작점(원점), 반지름, 원의 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임 루프
running = True 
while running:
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 시작 화면 표시
    displayStartScreen()

    # 화면 업데이트
    pygame.display.update()
# 게임 종료
pygame.quit()