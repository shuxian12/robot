import pygame
import numpy as np
import random

if __name__ == "__main__":
    pygame.init()
    window_width = 800
    window_height = 600

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("資安中藥事件")

    clock = pygame.time.Clock()

    number = random.randint(1,500000)
    number = np.round(number/100,2)

    def setup():
        window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/background.jpg'),(800,600)),(0,0))
        window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/scale.png'),(300,300)),(140,250))
        window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/pull.png'),(176,71)),(500,500))
        window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/clear.png'),(176,71)),(100,500))
        pygame.draw.rect(window,(255,255,255),pygame.Rect(465,463,244,40))
        window.blit(pygame.font.Font('../pull_medicine/fonts/corbel.ttf',24).render(f'Need number: {number}',True,(0,0,0)),(475,470))

    num_medicine = [200,350,450,1000]
    num_posi = [(325,393),(310,393),(285,393),(270,393),(255,393),(240,393)]
    flow = [0,0,0,0,0,0,0,0,0,0.03,0.178,0.355,0.726,1.42,3.87]
    size = [(282,156),(253.8,140.4),(253.8,140.4),(253.8,140.4),(253.8,140.4),(275,145),(253.8,140.4),(260,145),\
            (274,150),(280,160),(275,160),(280,160),(270,166),(265,164),(278,170)]
    posi = [(380,100),(395,120),(395,120),(395,120),(395,120),(380,127),(395,130),(395,127),(380,130),(380,127),\
            (380,130),(380,130),(380,130),(380,135),(376,135)]
    weight = 0
    while True:
        stop = False
        setup()
        window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/1.png'),(282,156)),(380,100))
        
        # 磅秤上放藥
        if int(weight) >= num_medicine[0]:
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,320))
        if int(weight) >= num_medicine[1]:
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,310))
        if int(weight) >= num_medicine[2]:
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,300))
        if int(weight) >= num_medicine[3]:
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,290))
        

        pygame.draw.rect(window,(240,240,240),pygame.Rect(270,391,70,28))
        pygame.draw.rect(window,(0,0,0),pygame.Rect(305,412,3,3))
        if weight <= 0.01:
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(285,393))
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(310,393))
            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(325,393))
        else:
            tmp = weight*100
            index = 0
            while int(tmp) != 0:
                window.blit(pygame.transform.scale(pygame.image.load(f'../pull_medicine/medicine/num{int(tmp%10)}.png'),(14,23)),num_posi[index])
                index += 1
                tmp//=10
            if weight < 0.01:
                window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(325,393))
            if weight < 0.1:
                window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(310,393))
            if weight < 1:
                window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(285,393))

        for event in pygame.event.get():
            # print(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                exit()
            i = 0
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=505 and x<=669 and y>=503 and y<=564:
                    while not stop:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                stop = True
                        setup()
                        window.blit(pygame.transform.scale(pygame.image.load(f'../pull_medicine/medicine/{i+1}.png'),size[i]),posi[i])
                        pygame.draw.rect(window,(240,240,240),pygame.Rect(270,391,70,28))
                        pygame.draw.rect(window,(0,0,0),pygame.Rect(305,412,3,3))

                        if int(weight) >= num_medicine[0]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,320))
                        if int(weight) >= num_medicine[1]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,310))
                        if int(weight) >= num_medicine[2]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,300))
                        if int(weight) >= num_medicine[3]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,290))

                        weight += flow[i]
                        weight = np.round(weight,2)
                        weight = 9999.99 if weight>=9999.99 else weight
                        tmp = weight*100
                        index = 0
                        while int(tmp) != 0:
                            window.blit(pygame.transform.scale(pygame.image.load(f'../pull_medicine/medicine/num{int(tmp%10)}.png'),(14,23)),num_posi[index])
                            index += 1
                            tmp//=10
                        if weight < 0.01:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(325,393))
                        if weight < 0.1:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(310,393))
                        if weight < 1:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(285,393))
                        clock.tick(20)
                        pygame.display.flip()
                        i = i+1 if i<14 else 14
                    while i >= 0:
                        setup()
                        window.blit(pygame.transform.scale(pygame.image.load(f'../pull_medicine/medicine/{i+1}.png'),size[i]),posi[i])
                        pygame.draw.rect(window,(240,240,240),pygame.Rect(270,391,70,28))
                        pygame.draw.rect(window,(0,0,0),pygame.Rect(305,412,3,3))

                        if int(weight) >= num_medicine[0]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,320))
                        if int(weight) >= num_medicine[1]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,310))
                        if int(weight) >= num_medicine[2]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,300))
                        if int(weight) >= num_medicine[3]:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/medicine.png'),(250,30)),(170,290))

                        weight += flow[i]
                        weight = np.round(weight,2)
                        weight = 9999.99 if weight>=9999.99 else weight
                        tmp = weight*100
                        index = 0
                        while int(tmp) != 0:
                            window.blit(pygame.transform.scale(pygame.image.load(f'../pull_medicine/medicine/num{int(tmp%10)}.png'),(14,23)),num_posi[index])
                            index += 1
                            tmp//=10
                        if weight < 0.01:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(325,393))
                        if weight < 0.1:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(310,393))
                        if weight < 1:
                            window.blit(pygame.transform.scale(pygame.image.load('../pull_medicine/medicine/num0.png'),(14,23)),(285,393))
                        clock.tick(20)
                        pygame.display.flip()
                        i-=1
                    if abs(weight-number) <= 10:
                        print("success")
                        exit()

                if x>=107 and x<=270 and y>=503 and y<=564:
                    weight = 0
            
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()