import pygame
import random
import numpy as np
pygame.init()

# 視窗大小
window_width = 800
window_height = 600

# 創建視窗
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("十八仔")
bg = pygame.transform.scale(pygame.image.load('../game/骰子/view.png'),(800,600))
dice = []
for i in range(6):
    dice.append(pygame.transform.scale(pygame.image.load(f'../game/骰子/{i+1}.jpg'),(40,40)))

clock = pygame.time.Clock()
# 圖像參數
symbol_width = 100
symbol_height = 100

# 載入圖像
screw = pygame.transform.scale(pygame.image.load('../game/骰子/screw.png'),(38,38))

def cal(r1,r2,r3):
    number = [0 for i in range(6)]
    number[r1-1]+=1
    number[r2-1]+=1
    number[r3-1]+=1
    s = 0
    # 小
    if bit[0] and (r1+r2+r3)<=10:
        s+=power[0]
    # 大
    if bit[14] and (r1+r2+r3)>=11:
        s+=power[14]
    # 總和
    if bit[15] and r1+r2+r3==4:
        s+=power[15]
    if bit[16] and r1+r2+r3==5:
        s+=power[16]
    if bit[17] and r1+r2+r3==6:
        s+=power[17]
    if bit[18] and r1+r2+r3==7:
        s+=power[18]
    if bit[19] and r1+r2+r3==8:
        s+=power[19]
    if bit[20] and r1+r2+r3==9:
        s+=power[20]
    if bit[21] and r1+r2+r3==10:
        s+=power[21]
    if bit[22] and r1+r2+r3==11:
        s+=power[22]
    if bit[23] and r1+r2+r3==12:
        s+=power[23]
    if bit[24] and r1+r2+r3==13:
        s+=power[24]
    if bit[25] and r1+r2+r3==14:
        s+=power[25]
    if bit[26] and r1+r2+r3==15:
        s+=power[26]
    if bit[27] and r1+r2+r3==16:
        s+=power[27]
    if bit[28] and r1+r2+r3==17:
        s+=power[28]
    # 雙骰
    if bit[1] and number[0]>=2:
        s+=power[1]
    if bit[2] and number[1]>=2:
        s+=power[2]
    if bit[3] and number[2]>=2:
        s+=power[3]
    if bit[11] and number[3]>=2:
        s+=power[11]
    if bit[12] and number[4]>=2:
        s+=power[12]
    if bit[13] and number[5]>=2:
        s+=power[13]
    # 豹子
    if bit[4] and number[0]==3:
        s+=power[4]
    if bit[5] and number[1]==3:
        s+=power[5]
    if bit[6] and number[2]==3:
        s+=power[6]
    if bit[8] and number[3]==3:
        s+=power[8]
    if bit[9] and number[4]==3:
        s+=power[9]
    if bit[10] and number[5]==3:
        s+=power[10]
    # 任一豹子
    if bit[7] and (number[0]==3 or number[1]==3 or number[2]==3 or number[3]==3 or number[4]==3 or number[5]==3):
        s+=power[7]
    # 雙骰組合
    if bit[29] and number[0]>=1 and number[1]>=1:
        s+=power[29]
    if bit[30] and number[0]>=1 and number[2]>=1:
        s+=power[30]
    if bit[31] and number[0]>=1 and number[3]>=1:
        s+=power[31]
    if bit[32] and number[0]>=1 and number[4]>=1:
        s+=power[32]
    if bit[33] and number[0]>=1 and number[5]>=1:
        s+=power[33]
    if bit[34] and number[1]>=1 and number[2]>=1:
        s+=power[34]
    if bit[35] and number[1]>=1 and number[3]>=1:
        s+=power[35]
    if bit[36] and number[1]>=1 and number[4]>=1:
        s+=power[36]
    if bit[37] and number[1]>=1 and number[5]>=1:
        s+=power[37]
    if bit[38] and number[2]>=1 and number[3]>=1:
        s+=power[38]
    if bit[39] and number[2]>=1 and number[4]>=1:
        s+=power[39]
    if bit[40] and number[2]>=1 and number[5]>=1:
        s+=power[40]
    if bit[41] and number[3]>=1 and number[4]>=1:
        s+=power[41]
    if bit[42] and number[3]>=1 and number[5]>=1:
        s+=power[42]
    if bit[43] and number[4]>=1 and number[45]>=1:
        s+=power[43]
    # 單骰
    if bit[44] and number[0]==1:
        s+=1
    if bit[45] and number[1]==1:
        s+=1
    if bit[46] and number[2]==1:
        s+=1
    if bit[47] and number[3]==1:
        s+=1
    if bit[48] and number[4]==1:
        s+=1
    if bit[49] and number[5]==1:
        s+=1
    if bit[44] and number[0]==2:
        s+=2.4
    if bit[45] and number[1]==2:
        s+=2.4
    if bit[46] and number[2]==2:
        s+=2.4
    if bit[47] and number[3]==2:
        s+=2.4
    if bit[48] and number[4]==2:
        s+=2.4
    if bit[49] and number[5]==2:
        s+=2.4
    if bit[44] and number[0]==3:
        s+=12
    if bit[45] and number[1]==3:
        s+=12
    if bit[46] and number[2]==3:
        s+=12
    if bit[47] and number[3]==3:
        s+=12
    if bit[48] and number[4]==3:
        s+=12
    if bit[49] and number[5]==3:
        s+=12
    # print(number)
    # print(sum(bit))
    return s-sum(bit)

power = [1.035,12.37,12.37,12.37,215,215,215,35,215,215,215,12.37,12.37,12.37,1.035,\
         70.3,34.65,20.4,13.25,9.17,7.56,6.92,6.92,7.56,9.17,13.25,20.4,34.65,70.3,\
            6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,6.13,\
                1,1,1,1,1,1]
bit = [False for i in range(50)]
show_dice = False
while True:
    if not show_dice:
        rand1, rand2, rand3 = 0, 0, 0
    window.blit(bg,(0,0))
    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/check.png'),(249,51)),(550,503))
    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/clear.png'),(198,51)),(351,503))
    pygame.draw.rect(window,(0,150,0),pygame.Rect(145,97,75,77))
    pygame.draw.rect(window,(0,75,0),pygame.Rect(0,496,347,70))
    if show_dice:
        window.blit(dice[rand1-1],(380,50))
        window.blit(dice[rand2-1],(340,110))
        window.blit(dice[rand3-1],(420,110))
        if (rand1+rand2+rand3)>=10:
            window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/1.png'),(35,50)),(147,110))
        window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/{(rand1+rand2+rand3)%10}.png'),(35,50)),(182,110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posi = pygame.mouse.get_pos()
            x = posi[0]
            y = posi[1]
            # 確認押注
            if x>=550 and x<=799 and y>=503 and y<=554:
                for i in range(16):
                    window.blit(bg,(0,0))
                    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/check.png'),(249,51)),(550,503))
                    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/clear.png'),(198,51)),(351,503))
                    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/row{i%4+1}.png'),(334,208)),(230,0))
                    pygame.draw.rect(window,(0,150,0),pygame.Rect(145,97,75,77))
                    pygame.draw.rect(window,(0,75,0),pygame.Rect(0,496,347,70))
                    pygame.display.update()
                    clock.tick(4)
                rand1, rand2, rand3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)
                window.blit(dice[rand1-1],(380,50))
                window.blit(dice[rand2-1],(340,110))
                window.blit(dice[rand3-1],(420,110))
                earn = cal(rand1,rand2,rand3)
                if (rand1+rand2+rand3)>=10:
                    window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/1.png'),(35,50)),(147,110))
                window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/{(rand1+rand2+rand3)%10}.png'),(35,50)),(182,110))
                print(int(np.floor(earn)))
                show_dice = True
            # 清除押注
            if x>=351 and x<=549 and y>=503 and y<=554:
                bit = [False for i in range(50)]
                bg = pygame.transform.scale(pygame.image.load('../game/骰子/view.png'),(800,600))
                window.blit(bg,(0,0))
                window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/check.png'),(249,51)),(550,503))
                window.blit(pygame.transform.scale(pygame.image.load(f'../game/骰子/clear.png'),(198,51)),(351,503))
                pygame.draw.rect(window,(0,150,0),pygame.Rect(145,97,75,77))
                pygame.draw.rect(window,(0,75,0),pygame.Rect(0,496,347,70))
                pygame.display.update()
            # 小
            if x>=22 and x<=129 and y>=210 and y<=310:
                bg.blit(screw,(40,246))
                bit[0] = True
            # 大
            if x>=677 and x<=783 and y>=210 and y<=309:
                bg.blit(screw,(695,246))
                bit[14] = True
            # 雙骰
            if x>=130 and x<=179 and y>=230 and y<=310:
                bg.blit(screw,(140,253))
                bit[1] = True
            if x>=181 and x<=228 and y>=230 and y<=310:
                bg.blit(screw,(190,253))
                bit[2] = True
            if x>=230 and x<=277 and y>=230 and y<=310:
                bg.blit(screw,(240,253))
                bit[3] = True
            if x>=529 and x<=575 and y>=230 and y<=309:
                bg.blit(screw,(539,253))
                bit[11] = True
            if x>=578 and x<=625 and y>=230 and y<=309:
                bg.blit(screw,(588,253))
                bit[12] = True
            if x>=628 and x<=675 and y>=230 and y<=309:
                bg.blit(screw,(638,253))
                bit[13] = True
            # 豹子
            if x>=280 and x<=355 and y>=230 and y<=255:
                bg.blit(screw,(283,229))
                bit[4] = True
            if x>=280 and x<=355 and y>=259 and y<=282:
                bg.blit(screw,(283,256))
                bit[5] = True
            if x>=280 and x<=355 and y>=285 and y<=309:
                bg.blit(screw,(283,283))
                bit[6] = True
            if x>=450 and x<=524 and y>=230 and y<=255:
                bg.blit(screw,(453,229))
                bit[8] = True
            if x>=450 and x<=524 and y>=259 and y<=282:
                bg.blit(screw,(453,256))
                bit[9] = True
            if x>=450 and x<=524 and y>=285 and y<=309:
                bg.blit(screw,(453,283))
                bit[10] = True
            # 任意豹子
            if x>=358 and x<=446 and y>=230 and y<=309:
                bg.blit(screw,(380,246))
                bit[7] = True
            # 總和
            if x>=22 and x<=73 and y>=312 and y<=357:
                bg.blit(screw,(32,321))
                bit[15] = True
            if x>=77 and x<=128 and y>=312 and y<=357:
                bg.blit(screw,(87,321))
                bit[16] = True
            if x>=132 and x<=183 and y>=312 and y<=357:
                bg.blit(screw,(142,321))
                bit[17] = True
            if x>=185 and x<=238 and y>=312 and y<=357:
                bg.blit(screw,(195,321))
                bit[18] = True
            if x>=240 and x<=292 and y>=312 and y<=357:
                bg.blit(screw,(250,321))
                bit[19] = True
            if x>=294 and x<=345 and y>=312 and y<=357:
                bg.blit(screw,(304,321))
                bit[20] = True
            if x>=350 and x<=401 and y>=312 and y<=357:
                bg.blit(screw,(360,321))
                bit[21] = True
            if x>=404 and x<=456 and y>=312 and y<=357:
                bg.blit(screw,(414,321))
                bit[22] = True
            if x>=458 and x<=510 and y>=312 and y<=357:
                bg.blit(screw,(468,321))
                bit[23] = True
            if x>=514 and x<=565 and y>=312 and y<=357:
                bg.blit(screw,(524,321))
                bit[24] = True
            if x>=567 and x<=619 and y>=312 and y<=357:
                bg.blit(screw,(577,321))
                bit[25] = True
            if x>=622 and x<=674 and y>=312 and y<=357:
                bg.blit(screw,(632,321))
                bit[26] = True
            if x>=677 and x<=729 and y>=312 and y<=357:
                bg.blit(screw,(687,321))
                bit[27] = True
            if x>=733 and x<=783 and y>=312 and y<=357:
                bg.blit(screw,(743,321))
                bit[28] = True
            # 雙骰組合
            if x>=92 and x<=135 and y>=358 and y<=435:
                bg.blit(screw,(99,379))
                bit[29] = True
            if x>=139 and x<=181 and y>=358 and y<=435:
                bg.blit(screw,(146,379))
                bit[30] = True
            if x>=184 and x<=227 and y>=358 and y<=435:
                bg.blit(screw,(191,379))
                bit[31] = True
            if x>=231 and x<=275 and y>=358 and y<=435:
                bg.blit(screw,(238,379))
                bit[32] = True
            if x>=276 and x<=321 and y>=358 and y<=435:
                bg.blit(screw,(283,379))
                bit[33] = True
            if x>=323 and x<=366 and y>=358 and y<=435:
                bg.blit(screw,(330,379))
                bit[34] = True
            if x>=370 and x<=413 and y>=358 and y<=435:
                bg.blit(screw,(377,379))
                bit[35] = True
            if x>=416 and x<=458 and y>=358 and y<=435:
                bg.blit(screw,(423,379))
                bit[36] = True
            if x>=462 and x<=506 and y>=358 and y<=435:
                bg.blit(screw,(469,379))
                bit[37] = True
            if x>=508 and x<=551 and y>=358 and y<=435:
                bg.blit(screw,(515,379))
                bit[38] = True
            if x>=555 and x<=599 and y>=358 and y<=435:
                bg.blit(screw,(562,379))
                bit[39] = True
            if x>=601 and x<=645 and y>=358 and y<=435:
                bg.blit(screw,(608,379))
                bit[40] = True
            if x>=648 and x<=690 and y>=358 and y<=435:
                bg.blit(screw,(655,379))
                bit[41] = True
            if x>=694 and x<=737 and y>=358 and y<=435:
                bg.blit(screw,(701,379))
                bit[42] = True
            if x>=741 and x<=784 and y>=358 and y<=435:
                bg.blit(screw,(748,379))
                bit[43] = True
            # 單骰
            if x>=22 and x<=145 and y>=438 and y<=471:
                bg.blit(screw,(64,440))
                bit[44] = True
            if x>=149 and x<=274 and y>=438 and y<=471:
                bg.blit(screw,(191,440))
                bit[45] = True
            if x>=276 and x<=400 and y>=438 and y<=471:
                bg.blit(screw,(318,440))
                bit[46] = True
            if x>=404 and x<=527 and y>=438 and y<=471:
                bg.blit(screw,(446,440))
                bit[47] = True
            if x>=531 and x<=656 and y>=438 and y<=471:
                bg.blit(screw,(573,440))
                bit[48] = True
            if x>=660 and x<=782 and y>=438 and y<=471:
                bg.blit(screw,(702,440))
                bit[49] = True

        # print(pygame.mouse.get_pos())
    
    # window.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)

pygame.quit()


