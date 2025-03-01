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

def randomize(grille):
    if '' in grille[0] or '' in grille[1] or '' in grille[2] or '' in grille[3] :
        while 1:
            nb=(random.randint(0,3),random.randint(0,3))
            if grille[nb[0]][nb[1]] =='':
                grille[nb[0]][nb[1]] = [2,4][random.randint(0,1)]
                return(grille)
    else:return(grille)

def move(grille,direction):
    dep=True
    grilleinit=grille
    if direction=='left':
        for _ in range(4):
            for i in range(1,4):
                for j in range(4):
                    if grille[i-1][j]=='':
                        grille[i-1][j]=grille[i][j]
                        grille[i][j]=''
                        
                    if grille[i-1][j]==grille[i][j]:
                        grille[i-1][j]=2*grille[i-1][j]
                        grille[i][j]=''
                        
    if direction=='right':
        for _ in range(4):
            for i in range(3):
                for j in range(4):
                    if grille[i+1][j]=='':
                        grille[i+1][j]=grille[i][j]
                        grille[i][j]=''
                        
                    if grille[i+1][j]==grille[i][j]:
                        grille[i+1][j]=2*grille[i+1][j]
                        grille[i][j]=''
                        
    if direction=='up':
        for _ in range(4):
            for i in range(4):
                for j in range(1,4):
                    if grille[i][j-1]=='':
                        grille[i][j-1]=grille[i][j]
                        grille[i][j]=''
                        
                    if grille[i][j-1]==grille[i][j]:
                        grille[i][j-1]=2*grille[i][j-1]
                        grille[i][j]=''
                        
    if direction=='down':
        for _ in range(4):
            for i in range(4):
                for j in range(3):
                    if grille[i][j+1]=='':
                        grille[i][j+1]=grille[i][j]
                        grille[i][j]=''
                        
                    if grille[i][j+1]==grille[i][j]:
                        grille[i][j+1]=2*grille[i][j+1]
                        grille[i][j]=''
                        
    if grilleinit==grille:dep=True
    return(grille,dep)

def game():
    pygame.init()
    game = pygame.display.set_mode((width, height))
    pygame.display.set_caption('2048')
    size=sizemax(width,height)
    direction=''

    run = True

    grille=[[''for _ in range(4)]for _ in range(4)]
    for _ in range(2):
        grille=randomize(grille)
    
    while run:
        pygame.draw.rect(game, (150, 150, 150), pygame.Rect(0, 0, width, height))
        game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 120), "2048", True, (255, 255, 255)), (width//2-120, height//40))

        for i in range(4):
            for j in range(4):
                pygame.draw.rect(game, (70,70,70),pygame.Rect(width//2-(size+10)*(2-i),height//5 + (size+10)*j,size,size))
                game.blit(pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 80), str(grille[i][j]), True, (255, 255, 255)), (width//2-(size+10)*(2-i),height//5 + (size+10)*j))
        if direction!='':
            grille,dep=move(grille,direction)
            if dep==True:
                grille=randomize(grille)
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
