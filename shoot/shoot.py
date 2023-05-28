from time import sleep
import pygame
import random
import math

def shoot(return_list):
    color = ['clubs','diamonds','hearts','spades']
    number = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    left_symbol_posi_x = 80
    left_symbol_posi_y = 80
    right_symbol_posi_x = 650
    right_symbol_posi_y = 80
    my_symbol_posi_x = 365
    my_symbol_posi_y = 200
    card_images = []
    for n in number:
        for c in color:
            image = pygame.transform.scale(pygame.image.load(f'../shoot/cards/{n}_of_{c}.png'),(150,219))
            card_images.append(image)


    pygame.init()
    window_width = 800
    window_height = 600

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("射龍門")

    clock = pygame.time.Clock()

    def create_rand():
        rand1 = random.randint(0,51)
        rand2 = random.randint(0,51)
        my_rand = random.randint(0,51)
        while rand1 == rand2 or rand2 == my_rand or my_rand == rand1:
            rand2 = random.randint(0,51)
            my_rand = random.randint(0,51)
        if(rand1 > rand2):
            rand1, rand2 = rand2, rand1
        return rand1, my_rand, rand2

    def judge(rand1, my_rand, rand2):
        if my_rand//4 < rand1//4 or my_rand//4 > rand2//4:
            return 'Lose'
        elif my_rand//4 == rand1//4 or my_rand//4 == rand2//4:
            return "Hit"
        else:
            return "Win"

    start = False
    show_my_card = False
    bid = 0
    q = False
    while True:    
        for event in pygame.event.get():
            # print(pygame.mouse.get_pos())
            if q:
                sleep(5)
                exit()
            if event.type == pygame.QUIT:
                exit()
            window.blit(pygame.transform.scale(pygame.image.load('../shoot/cards/background.png'),(800,600)),(0,0))
            pygame.draw.rect(window,(36,132,58),pygame.Rect(16,6,112,151))
            pygame.draw.rect(window,(40,149,66),pygame.Rect(16,157,760,230))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/back.jpg'),(150,219)),(60,60))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/back.jpg'),(150,219)),(320,60))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/back.jpg'),(150,219)),(580,60))
            pygame.draw.rect(window,(200,20,20),pygame.Rect(320,500,150,50))
            window.blit(pygame.font.Font('../shoot/fonts/corbel.ttf',35).render('Start',True,(20,20,20)),(358,510))
            window.blit(pygame.font.Font('../shoot/fonts/corbel.ttf',35).render(f'{bid}',True,(255,255,255)),(320,400))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/minus.png'),(40,40)),(260,400))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/plus.png'),(40,40)),(500,400))
            window.blit(pygame.transform.scale(pygame.image.load(f'../shoot/cards/screw.png'),(60,60)),(560,395))
            # 按下start
            if not start and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                posi = pygame.mouse.get_pos()
                if posi[0]<=470 and posi[0]>=320 and posi[1]<=550 and posi[1]>=500:
                    start = True
                    rand1, my_rand, rand2 = create_rand()
            # 按下restart
            if start and show_my_card and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                posi = pygame.mouse.get_pos()
                if posi[0]<=470 and posi[0]>=320 and posi[1]<=550 and posi[1]>=500:
                    start = False
                    show_my_card = False
            # 按下住
            if not start and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                posi = pygame.mouse.get_pos()
                if math.sqrt(math.pow(posi[0]-280,2)+math.pow(posi[1]-420,2)) <= 19:
                    bid = 0 if bid == 0 else bid-1
                if math.sqrt(math.pow(posi[0]-520,2)+math.pow(posi[1]-420,2)) <= 19:
                    bid = 1000000 if bid == 1000000 else bid+1
            # 按我的牌
            if start and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                posi = pygame.mouse.get_pos()
                if posi[0]<=470 and posi[0]>=320 and posi[1]<=279 and posi[1]>=60:
                    show_my_card = True
                    if judge(rand1, my_rand, rand2) == 'Win':
                        return_list.append(bid*2)
                        print(bid*2)
                    elif judge(rand1, my_rand, rand2) == 'Lose':
                        return_list.append(-bid)
                        print(-bid)
                    else:
                        return_list.append(-bid*2)
                        print(-bid*2)
                    q = True

            if start:
                window.blit(card_images[rand1],(60,60))
                window.blit(card_images[rand2],(580,60))
            if show_my_card:
                window.blit(card_images[my_rand],(320,60))
                pygame.draw.rect(window,(200,20,20),pygame.Rect(320,500,150,50))
                window.blit(pygame.font.Font('../shoot/fonts/corbel.ttf',35).render('Restart',True,(20,20,20)),(340,510))
            clock.tick(60)
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    shoot([])