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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/rollingstone/Desktop/Study/Python/PythonApplication1/PythonApplication1/character.png")
# 이미지의 크기를 구해옴
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
# 화면 가로의 절반 크기에 해당하는 곳에 위치
character_x_pos = (screen_width - character_width) / 2
# 화면 세로 크기 가장 아래
character_y_pos = screen_height - character_height

# 이동좌표
to_x = 0
to_y = 0

# 이벤트 루프
# 게임 진행 여부 확인
running = True 

while running:
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생하였는가 (x 표시)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=1
            elif event.key == pygame.K_RIGHT:
                to_x +=1
            elif event.key == pygame.K_UP:
                to_y -=1
            elif event.key == pygame.K_DOWN:
                to_y +=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 스크린 좌표        
    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))

    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임화면을 다시 그리기!
    pygame.display.update()





# pygame 종료
pygame.quit()

