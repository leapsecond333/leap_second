import pygame

pygame.init()
screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Drawing Shapes")

clock = pygame.time.Clock()
run = True
key = None
start_pos = [300, 0]
another_pos = [0, 100]
x_location = [start_pos

# 게임 루프
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key = event.key

    # 2) 게임 상태 업데이트
    # 1번째 움직임
    if start_pos[0] > 0 and start_pos[1] == 0 and another_pos[0] < 300 and another_pos[1] == 100:
        start_pos[0] -= 1
        another_pos[0] += 1
    # 2번째 움직임
    elif start_pos[1] < 100 and start_pos[0] == 0 and another_pos[1] > 0 and another_pos[0] == 300:
        start_pos[1] += 1
        another_pos[1] -= 1
    # 3번째 움직임
    elif start_pos[0] < 300 and start_pos[1] == 100 and another_pos[0] > 0 and another_pos[1] == 0:
        start_pos[0] += 1
        another_pos[0] -= 1
    # 4번째 움직임
    else:
        start_pos[1] -= 1
        another_pos[1] += 1

    # 3) 게임 상태 그리기
    screen.fill(pygame.color.Color(255, 255, 255))

    if key == pygame.K_1:
        pygame.draw.line(screen,
                         pygame.color.Color(0, 0, 0),
                         start_pos,
                         another_pos, 1)
    elif key == pygame.K_2:
        pygame.draw.ellipse(screen,
                            pygame.color.Color(255, 0, 0),
                            pygame.Rect(start_pos, (50, 50)))
    elif key == pygame.K_3:
        pygame.draw.polygon(screen,
                            pygame.color.Color(0, 255, 0),
                            [start_pos,
                             (0, screen.get_height()),
                             (screen.get_width(), screen.get_height())])
    elif key == pygame.K_4:
        pygame.draw.rect(screen,
                        pygame.color.Color(0, 0, 255),
                        pygame.Rect(start_pos, (50, 50)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
