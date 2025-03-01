import pygame, random

width, height = 1500, 800

def main():
    pygame.init()
    menu = pygame.display.set_mode((width, height))
    pygame.display.set_caption('2048')

    run = True

    while run:
        pygame.draw.rect(menu, (150, 150, 150), pygame.Rect(0, 0, width, height))
        menu.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 120), "2048", True, (255, 255, 255)), (width//2-120, height//20))
        for i in range(2):
            pygame.draw.rect(menu, (70,70,70),pygame.Rect(width//2-300,height//4 + 210*i,600,200))
            menu.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 120), ["PLAY","QUIT"][i], True, (255, 255, 255)), (width//2-150, height//4+210*i))
        for event in pygame.event.get():
            run = not event.type == pygame.QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if abs(mousePos[0]-width//2)<300 and abs(mousePos[1]-height//4)<200:
                    run =False
                    game()
                if abs(mousePos[0]-width//2)<300 and abs(mousePos[1]-height//4-210)<200:
                    run=False
        
        pygame.display.update()
    pygame.quit()

def sizemax(width, height):
    xmax=(width-200)//4
    ymax=(height*3/4-50)//4
    return(min(xmax,ymax))

def randomize(grid):
    if '' in grid[0] or '' in grid[1] or '' in grid[2] or '' in grid[3] :
        while 1:
            nb=(random.randint(0,3),random.randint(0,3))
            if grid[nb[0]][nb[1]] =='':
                grid[nb[0]][nb[1]] = [2,4][random.randint(0,1)]
                return(grid)
    else:return(grid)

def move(grid,direction):
    dep=True
    gridinit=grid
    if direction=='left':
        for _ in range(4):
            for i in range(1,4):
                for j in range(4):
                    if grid[i-1][j]=='':
                        grid[i-1][j]=grid[i][j]
                        grid[i][j]=''
                        
                    if grid[i-1][j]==grid[i][j]:
                        grid[i-1][j]=2*grid[i-1][j]
                        grid[i][j]=''
                        
    if direction=='right':
        for _ in range(4):
            for i in range(3):
                for j in range(4):
                    if grid[i+1][j]=='':
                        grid[i+1][j]=grid[i][j]
                        grid[i][j]=''
                        
                    if grid[i+1][j]==grid[i][j]:
                        grid[i+1][j]=2*grid[i+1][j]
                        grid[i][j]=''
                        
    if direction=='up':
        for _ in range(4):
            for i in range(4):
                for j in range(1,4):
                    if grid[i][j-1]=='':
                        grid[i][j-1]=grid[i][j]
                        grid[i][j]=''
                        
                    if grid[i][j-1]==grid[i][j]:
                        grid[i][j-1]=2*grid[i][j-1]
                        grid[i][j]=''
                        
    if direction=='down':
        for _ in range(4):
            for i in range(4):
                for j in range(3):
                    if grid[i][j+1]=='':
                        grid[i][j+1]=grid[i][j]
                        grid[i][j]=''
                        
                    if grid[i][j+1]==grid[i][j]:
                        grid[i][j+1]=2*grid[i][j+1]
                        grid[i][j]=''
                        
    if gridinit==grid:dep=True
    return(grid,dep)

def game():
    pygame.init()
    game = pygame.display.set_mode((width, height))
    pygame.display.set_caption('2048')
    size=sizemax(width,height)
    direction=''

    run = True

    grid=[[''for _ in range(4)]for _ in range(4)]
    for _ in range(2):
        grid=randomize(grid)
    
    while run:
        pygame.draw.rect(game, (150, 150, 150), pygame.Rect(0, 0, width, height))
        game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 120), "2048", True, (255, 255, 255)), (width//2-120, height//40))

        for i in range(4):
            for j in range(4):
                pygame.draw.rect(game, (70,70,70),pygame.Rect(width//2-(size+10)*(2-i),height//5 + (size+10)*j,size,size))
                game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 80), str(grid[i][j]), True, (255, 255, 255)), (width//2-(size+10)*(2-i),height//5 + (size+10)*j))
        if direction!='':
            grid,dep=move(grid,direction)
            if dep==True:
                grid=randomize(grid)
            direction=''
            

        for event in pygame.event.get():
            run = not event.type == pygame.QUIT
            if pygame.key.get_pressed()[pygame.K_z]:
                direction='up'
            if pygame.key.get_pressed()[pygame.K_s]:
                direction='down'
            if pygame.key.get_pressed()[pygame.K_q]:
                direction='left'
            if pygame.key.get_pressed()[pygame.K_d]:
                direction='right'

        pygame.display.update()
    pygame.quit()
    main()
main()
