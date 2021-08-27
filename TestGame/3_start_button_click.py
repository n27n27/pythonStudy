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

# 게임 시작 여부
start = False

# 시작 화면 보여주기
def displayStartScreen():
    # 그릴위치, 색상, 시작점(원점), 반지름, 원의 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임 화면 보여주기
def displayGameScreen():
    print("Game Start")

# pos 에 해당하는 버튼 확인
def checkButtons(pos):
    global start
    # rect 안에 포인트가 포함되는지 확인
    if start_button.collidepoint(pos):
        start = True

# 게임 루프
running = True 
while running:

    clickPos = None
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            clickPos = pygame.mouse.get_pos()
            print(clickPos)
    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 시작 화면 표시
    if start:
        # 게임 화면 표시
        displayGameScreen()
    else:
        # 시작 화면 표시
        displayStartScreen()

    # 사용자가 클릭한 좌표 값이 있다면
    if clickPos:
        checkButtons(clickPos)
    # 화면 업데이트
    pygame.display.update()
# 게임 종료
pygame.quit()