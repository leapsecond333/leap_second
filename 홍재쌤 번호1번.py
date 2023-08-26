import pygame

pygame.init()
screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Drawing Shapes")

clock = pygame.time.Clock()
run = True
key = None

pos = [300,0, 0,100]
check_direction = 0
value = [[-1,0,1,0], [0,1,0,-1]]
check = 0
# 게임 루프
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key = event.key

    # 2) 게임 상태 업데이트

    # 3) 게임 상태 그리기
    screen.fill(pygame.color.Color(255, 255, 255))

    if pos[0] == 0:
        check = 1
    if pos[1] == 100:
        pos = pos[2:] + pos[:2]
        check = 0
    for i in range(4):
        pos[i] += value[check][i]
        print(pos)
    
    pygame.draw.line(screen,
                         pygame.color.Color(0, 0, 0),
                         pos[:2],
                         pos[2:], 1)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
