import pygame
from random import *
# 레벨에 맞게 설정
def setup(level):
    global display_time
    # 얼마 동안 숫자를 보여줄지
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

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
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)        
            button.center = (center_x, center_y)
            number_buttons.append(button)
    
    print(grid)


# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔 # RGB
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
# 사용자가 눌러야 할 버튼 
number_buttons = []
curr_level = 1
display_time = None
start_ticks = None 

# 게임 시작 여부
start = False
# 숫자 숨김 여부(사용자가 1을 클릭했거나, 보여주는 시간 초과했을 때)
hidden = False

# 시작 화면 보여주기
def displayStartScreen():
    # 그릴위치, 색상, 시작점(원점), 반지름, 선 두께
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center = start_button.center)
    
    screen.blit(msg, msg_rect)


# 게임 화면 보여주기
def displayGameScreen():
    global hidden

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start = 1):
        if hidden:
                # 버튼 사각형 그리기
                pygame.draw.rect(screen, WHITE, rect)
        else:
            # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)        

# pos 에 해당하는 버튼 확인
def checkButtons(pos):
    global start, start_ticks
    # 게임이 시작했으면
    if start:
        check_number_buttons(pos)

    # rect 안에 포인트가 포함되는지 확인
    elif start_button.collidepoint(pos):
        start = True
        # 타이머 시작(현재 시간을 저장)
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global hidden, start, curr_level
    for button in number_buttons:
        if button.collidepoint(pos):
            # 올바른 숫자 클릭
            if button == number_buttons[0]:
                print("Corrent")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
                # game_over()                
            break
    # 모든 숫자를 맞췄으면 레벨 높혀서 다음 스테이지
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

# 게임 종료 처리
def game_over():
    global running
    running = False
    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center = (screen_width / 2, screen_height / 2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)


# 게임 시작 전에 게임 설정 함수 실행
setup(curr_level)

# 게임 루프
running = True 
while running:

    clickPos = None
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
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

pygame.time.delay(5000)    
# 게임 종료
pygame.quit()