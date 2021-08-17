
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

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/rollingstone/Desktop/Study/Python/PythonApplication1/PythonApplication1/background.png")

# 이벤트 루프
# 게임 진행 여부 확인
running = True 

while running:
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생하였는가 (x 표시)
        if event.type == pygame.QUIT:
            running = False

    # 스크린 좌표        
    screen.blit(background, (0, 0))
#    screen.fill((0, 0, 255))

    # 게임화면을 다시 그리기!
    pygame.display.update()





# pygame 종료
pygame.quit()

