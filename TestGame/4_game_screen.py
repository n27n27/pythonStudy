import pygame
from random import *
# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    # 20 초과하면 20으로 초기화
    number_count = min(number_count, 20)

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 grid cell 별 가로, 세로 크기
    button_size = 110 # grid cell 내에 실제로 그려질 버튼 그기
    screen_left_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    grid = [[ 0 for col in range(columns)] for row in range(rows)]

    # 시작 숫자 부터 number_count 까지
    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) - (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) - (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)            
            button.center(center_x, center_y)
            number_buttons.append(button)
    
    print(grid)


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
GRAY = (50, 50, 50)
# 사용자가 눌러야 할 버튼 
number_buttons = [] 

# 게임 시작 여부
start = False

# 시작 화면 보여주기
def displayStartScreen():
    # 그릴위치, 색상, 시작점(원점), 반지름, 선 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임 화면 보여주기
def displayGameScreen():
    for idx, rect in enumerate(number_buttons, start = 1):
        pygame.draw.rect(screen, GRAY, rect)

# pos 에 해당하는 버튼 확인
def checkButtons(pos):
    global start
    # rect 안에 포인트가 포함되는지 확인
    if start_button.collidepoint(pos):
        start = True

# 게임 시작 전에 게임 설정 함수 실행
setup(5)

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