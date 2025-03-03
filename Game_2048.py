import pygame, random, copy

def sizemax(width, height):
    xmax = (width - 200) // 4
    ymax = (height * 3/4 - 50) // 4
    return min(xmax, ymax)

def randomize(grid):
    if '' in grid[0] or '' in grid[1] or '' in grid[2] or '' in grid[3] :
        while 1:
            nb = (random.randint(0, 3), random.randint(0, 3))
            if grid[nb[0]][nb[1]] == '':
                grid[nb[0]][nb[1]] = [2, 4][random.randint(0, 1)]
                return grid
    else:
        return grid

def move(gridinit, direction):
    can_move = False
    grid = copy.deepcopy(gridinit)

    if direction == 'left':
        for _ in range(3):  #A number can at most go 3 tiles on his left
            for i in range(1,4):
                for j in range(4):
                    if grid[i-1][j] == '':  #Nothing on his left => swap
                        grid[i-1][j] = grid[i][j]
                        grid[i][j] = ''

        #Multiply by two every number that have the same number on his left
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j] == grid[i][j]:
                    grid[i-1][j] *= 2
                    grid[i][j] = ''

        for _ in range(2):  #After the fusion a number can at most go 2 times on his left
            for i in range(1,4):
                for j in range(4):
                    if grid[i-1][j] == '':  #Nothing on his left => swap
                        grid[i-1][j] = grid[i][j]
                        grid[i][j] = ''
                        
    if direction == 'right':
        for _ in range(3):
            for i in range(3):
                for j in range(4):
                    if grid[3-i][j] == '':
                        grid[3-i][j] = grid[2-i][j]
                        grid[3-i-1][j] = ''

        for i in range(3):
            for j in range(4):                
                if grid[3-i][j] == grid[2-i][j]:
                    grid[3-i][j] *= 2
                    grid[2-i][j] = ''
                        
        for _ in range(2):
            for i in range(3):
                for j in range(4):
                    if grid[i+1][j] == '':
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = ''

    if direction == 'up':
        for _ in range(3):
            for i in range(4):
                for j in range(1,4):
                    if grid[i][j-1] == '':
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = ''

        for i in range(4):
            for j in range(1,4):
                if grid[i][j-1] == grid[i][j]:
                    grid[i][j-1] *= 2
                    grid[i][j] = ''

        for _ in range(2):
            for i in range(4):
                for j in range(1,4):
                    if grid[i][j-1] == '':
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = ''

                        
    if direction == 'down':
        for _ in range(3):
            for i in range(4):
                for j in range(3):
                    if grid[i][j+1] == '':
                        grid[i][j+1] = grid[i][j]
                        grid[i][j] = ''
                        
        for i in range(4):
            for j in range(3):
                if grid[i][3-j] == grid[i][2-j]:
                    grid[i][3-j] *= 2
                    grid[i][2-j] = ''

        for _ in range(2):
            for i in range(4):
                for j in range(3):
                    if grid[i][j+1] == '':
                        grid[i][j+1] = grid[i][j]
                        grid[i][j] = ''
                        
    if gridinit != grid:
        can_move = True
    return grid, can_move

def lose_detector(grid):
    game_over = True
    for direction in ["up", "down", "left", "right"]:
        if move(grid, direction)[1] == True:
            game_over = False
    return game_over

def game(width, height):
    pygame.init()
    game = pygame.display.set_mode((width, height))
    pygame.display.set_caption('2048')
    size = sizemax(width, height)
    direction = ''

    run = True

    grid = [['' for _ in range(4)] for _ in range(4)]
    for _ in range(2):
        grid = randomize(grid)

    pygame.draw.rect(game, (150, 150, 150), pygame.Rect(0, 0, width, height))
    game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 120), "2048", True, (255, 255, 255)), (width//2-120, height//40))

    for i in range(4):
        for j in range(4):
            pygame.draw.rect(game, (69,69,69),pygame.Rect(width//2-(size+10)*(2-i),height//5 + (size+10)*j,size,size))
            game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 80), str(grid[i][j]), True, (255, 255, 255)), (width//2-(size+10)*(2-i),height//5 + (size+10)*j))
    
    while run:
        if direction != '':
            grid, can_move = move(grid, direction)
            if can_move == True:
                grid = randomize(grid)
            direction = ''
            for i in range(4):
                for j in range(4):
                    pygame.draw.rect(game, (69,69,69),pygame.Rect(width//2-(size+10)*(2-i),height//5 + (size+10)*j,size,size))
                    game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 80), str(grid[i][j]), True, (255, 255, 255)), (width//2-(size+10)*(2-i),height//5 + (size+10)*j))
            if lose_detector(grid):
                game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 256), "Game over", True, (255, 0, 0)), (256, height//2 - 128))

        for event in pygame.event.get():
            run = not event.type == pygame.QUIT
            if pygame.key.get_pressed()[pygame.K_z]:
                direction = 'up'
            if pygame.key.get_pressed()[pygame.K_s]:
                direction = 'down'
            if pygame.key.get_pressed()[pygame.K_q]:
                direction = 'left'
            if pygame.key.get_pressed()[pygame.K_d]:
                direction = 'right'
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                run = False

        pygame.display.update()
    pygame.quit()

