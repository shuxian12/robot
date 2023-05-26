import pygame, sys, multiprocessing
import subprocess
import random, cv2
import numpy as np
import openai
from typing import List
# sys.path.insert(0, '../memory_game')
sys.path.append('..')
from memory_game import memory_game
from pacman import pacman
from game_done import game_done_screen

# from website import app
# import webbrowser
# webbrowser.open('http://127.0.0.1:5000')

canvas = pygame.display.set_mode((1000, 600))
text = [1, 50, 0, 100, 100, 100, 4, 100, 0]# text[8] = 被吃掉的螺絲數量??
# text[0] is status, text[1] is energy, text[2] is bug, text[3] is oil92, 
# text[4] is oil95, text[5] is oil98, text[6] is oilEngine, text[7] is screw
furniture = [1, 2, 3, 4, 5]
garbage = [0, 0, 0, 0]
pre_status = 1
WINDOW = 1
ticks = pygame.time.get_ticks()
ad_ticks = pygame.time.get_ticks()
garbageAD_num = 0
garbageAD_watch = -1
FPS = 60

have_ac=False
have_carpet=False
have_oil=False
have_chair=False
have_tv=False
have_oilEngine=False
have_tvChannel=False

class Robot():
    def __init__(self):
        super().__init__()
        # Robot image
        self.status1_img = pygame.image.load(r"character/status1.png")
        self.status1_img = pygame.transform.scale(self.status1_img, (200, 200))
        self.status2_img = pygame.image.load(r"character/status2.png")
        self.status2_img = pygame.transform.scale(self.status2_img, (200, 200))
        self.status3_img = pygame.image.load(r"character/status3.png")
        self.status3_img = pygame.transform.scale(self.status3_img, (160, 300))
        self.iron_img = pygame.image.load(r"character/scrap_iron.png")
        self.iron_img = pygame.transform.scale(self.iron_img, (300, 300))
        self.broken_img = pygame.image.load(r"character/broken.png")
        self.broken_img = pygame.transform.scale(self.broken_img, (200, 200))
        self.index_x = 0
        self.dir_x = 0
        self.index_y = 0
        self.dir_y = 0

        # furniture image
        self.store_img = pygame.image.load(r"furniture/store.png")
        self.store_img = pygame.transform.scale(self.store_img, (100, 100))
        self.background_img = pygame.image.load(r"furniture/background.png")
        self.background_img = pygame.transform.scale(self.background_img, (1000, 600))
        self.ac_img = pygame.image.load(r"furniture/ac.png")
        self.ac_img = pygame.transform.scale(self.ac_img, (200, 200))
        self.ac_img_rect = (600, 0)
        self.carpet_img = pygame.image.load(r"furniture/carpet.png")
        self.carpet_img = pygame.transform.scale(self.carpet_img, (800, 600))
        self.carpet_img_rect = (100, 200)
        self.chair_img = pygame.image.load(r"furniture/chair.png")
        self.chair_img = pygame.transform.scale(self.chair_img, (200, 200))
        self.chair_img_rect = (150, 300)
        self.tvChannel_img = pygame.image.load(r"furniture/tvChannel.png")
        self.tvChannel_img = pygame.transform.scale(self.tvChannel_img, (200, 200))
        self.tv_img_rect = (250, 80)
        self.tv_img = pygame.image.load(r"furniture/tv.png")
        self.tv_img = pygame.transform.scale(self.tv_img, (200, 200))
        self.tvChannel_img_rect = (250, 80)

        # tool image
        self.oil_img = pygame.image.load(r"tool/oil.png")
        self.oil_img = pygame.transform.scale(self.oil_img, (100, 100))
        self.oilEngine_img = pygame.image.load(r"tool/oilEngine.png")
        self.oilEngine_img = pygame.transform.scale(self.oilEngine_img, (100, 100))
        self.screw_img = pygame.image.load(r"tool/screw.png")
        self.crew_img = pygame.transform.scale(self.screw_img, (100, 100))
        self.oil92_img = pygame.image.load(r"tool/92.png")
        self.oil92_img = pygame.transform.scale(self.oil92_img, (30, 30))
        self.oil95_img = pygame.image.load(r"tool/95.png")
        self.oil95_img = pygame.transform.scale(self.oil95_img, (30, 30))
        self.oil98_img = pygame.image.load(r"tool/98.png")
        self.oil98_img = pygame.transform.scale(self.oil98_img, (30, 30))

        # left text
        # self.font = pygame.font.SysFont("jfopen粉圓11", 20)
        self.font = pygame.font.Font(r"fonts/jf-openhuninn-2.0.ttf", 20)
        self.text_energy = self.font.render("能量", True, (0, 0, 0))
        self.text_energy_rect = (20, 45)
        self.text_status = self.font.render("等級", True, (0, 0, 0))
        self.text_status_rect = (20, 20)
        self.text_bug = self.font.render("bug", True, (0, 0, 0))
        self.text_bug_rect = (20, 70)
        self.num_energy = self.font.render("100", True, (0, 0, 0))
        self.num_energy_rect = (80, 45)
        self.num_status = self.font.render("1", True, (0, 0, 0))
        self.num_status_rect = (80, 20)
        self.num_bug = self.font.render("0", True, (0, 0, 0))
        self.num_bug_rect = (80, 70)
        self.left_texts = [self.text_energy, self.text_status, self.text_bug, self.num_energy, self.num_status, self.num_bug]
        self.left_texts_rect = [self.text_energy_rect, self.text_status_rect, self.text_bug_rect, self.num_energy_rect, self.num_status_rect, self.num_bug_rect]
        self.status = ["0", "1", "2", "3", "game over", "broken"]

        # right text
        self.text_oil92 = self.font.render("92", True, (0, 0, 0))
        self.tetx_oil92_rect = (890, 20)
        self.text_oil95 = self.font.render("95", True, (0, 0, 0))
        self.text_oil95_rect = (890, 45)
        self.text_oil98 = self.font.render("98", True, (0, 0, 0))
        self.text_oil98_rect = (890, 70)
        self.text_oilEngine = self.font.render("機油", True, (0, 0, 0))
        self.text_oilEngine_rect = (875, 95)
        self.text_screw = self.font.render("螺絲", True, (0, 0, 0))
        self.text_screw_rect = (875, 120)
        self.num_oil92 = self.font.render("100", True, (0, 0, 0))
        self.num_oil92_rect = (950, 20)
        self.num_oil95 = self.font.render("100", True, (0, 0, 0))
        self.num_oil95_rect = (950, 45)
        self.num_oil98 = self.font.render("100", True, (0, 0, 0))
        self.num_oil98_rect = (950, 70)
        self.num_oilEngine = self.font.render("0", True, (0, 0, 0))
        self.num_oilEngine_rect = (950, 95)
        self.num_screw = self.font.render("0", True, (0, 0, 0))
        self.num_screw_rect = (950, 120)
        self.right_texts = [self.text_oil92, self.text_oil95, self.text_oil98, self.text_oilEngine, self.text_screw, self.num_oil92, self.num_oil95, self.num_oil98, self.num_oilEngine, self.num_screw]
        self.right_texts_rect = [self.tetx_oil92_rect, self.text_oil95_rect, self.text_oil98_rect, self.text_oilEngine_rect, self.text_screw_rect, self.num_oil92_rect, self.num_oil95_rect, self.num_oil98_rect, self.num_oilEngine_rect, self.num_screw_rect]
        
        # textbox
        self.textbox_rect = (200, 560)
        self.rect_rect = (195, 558, 550, 28)
        self.textbox_send = self.font.render("Send", True, (0, 0, 0))
        self.textbox_send_rect = (770, 563)

        # garbage
        self.background_ad_img = pygame.image.load(r"garbage/background_ad.png")
        self.background_ad_img = pygame.transform.scale(self.background_ad_img, (1000, 600))
        self.garbage1_img = pygame.image.load(r"garbage/garbage1.png")
        self.garbage1_img = pygame.transform.scale(self.garbage1_img, (80, 80))
        self.garbage2_img = pygame.image.load(r"garbage/garbage2.png")
        self.garbage2_img = pygame.transform.scale(self.garbage2_img, (90, 60))
        self.garbage1_img_rect = (20, 230)
        self.garbage2_img_rect = (170, 150)
        self.garbage3_img_rect = (500, 230)
        self.garbage4_img_rect = (700, 270)

    def sick(self):
        heal = 0
        canvas.fill((0,0,0),(0,0,1000,600))
        canvas.blit(self.broken_img, (550, 300))
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 719 >= event.pos[0] >= 571 and 450 >= event.pos[1] >= 352:
                    with subprocess.Popen(['python','..\game\pull_medicine.py'],stdout=subprocess.PIPE) as proc:
                        if len(proc.stdout.readlines()) == 3:
                            heal = random.randint(1,3)
                    if heal == 2:
                        return False
                else:
                    return True

    def drawRobot(self, status):
        # index x
        if self.dir_x == 0:
            self.index_x += 1
        elif self.dir_x == 1:
            self.index_x -= 1
        if self.index_x == 100:
            self.dir_x = 1
        elif self.index_x == 0:
            self.dir_x = 0
        # index y
        if self.dir_y == 0:
            self.index_y += 1
        elif self.dir_y == 1:
            self.index_y -= 1
        if self.index_y == 100:
            self.dir_y = 1
        elif self.index_y == 0:
            self.dir_y = 0
        
        if status == 1:
            canvas.blit(self.status1_img, (550 + self.index_x, 300 + self.index_y))
        elif status == 2:
            canvas.blit(self.status2_img, (550 + self.index_x, 300 + self.index_y))
        elif status == 3:
            canvas.blit(self.status3_img, (550 + self.index_x, 200 + self.index_y))
        elif status == 4:
            canvas.blit(self.iron_img, (550, 300))
        elif status == 5:
            if self.sick() == False:
                text[0] = pre_status+1
            

    def drawFurniture(self, n):
        global have_ac,have_carpet,have_oil,have_chair,have_tv,have_oilEngine,have_tvChannel
        if n == 1 and have_ac==True:
            canvas.blit(self.ac_img, self.ac_img_rect)
        elif n == 2 and have_carpet==True:
            canvas.blit(self.carpet_img, self.carpet_img_rect)
        elif n == 3 and have_chair==True:
            canvas.blit(self.chair_img, self.chair_img_rect)
        elif n == 4 and have_tv==True:
            canvas.blit(self.tv_img, self.tv_img_rect)
        elif n == 5 and have_tvChannel==True:
            canvas.blit(self.tvChannel_img, self.tvChannel_img_rect)

    def updateText(self):
        global text
        # for i in text:
        #     print(i)
        self.num_status = self.font.render(self.status[int(text[0])], True, (0, 0, 0))
        self.num_energy = self.font.render(str(text[1]), True, (0, 0, 0))
        self.num_bug = self.font.render(str(text[2]), True, (0, 0, 0))
        self.num_oil92 = self.font.render(str(text[3]), True, (0, 0, 0))
        self.num_oil95 = self.font.render(str(text[4]), True, (0, 0, 0))
        self.num_oil98 = self.font.render(str(text[5]), True, (0, 0, 0))
        self.num_oilEngine = self.font.render(str(text[6]), True, (0, 0, 0))
        self.num_screw = self.font.render(str(text[7]), True, (0, 0, 0))
        self.left_texts = [self.text_energy, self.text_status, self.text_bug, self.num_energy, self.num_status, self.num_bug]
        self.right_texts = [self.text_oil92, self.text_oil95, self.text_oil98, self.text_oilEngine, self.text_screw, self.num_oil92, self.num_oil95, self.num_oil98, self.num_oilEngine, self.num_screw]
        # text[0] is status, text[1] is energy, text[2] is bug, text[3] is oil92, text[4] is oil95, text[5] is oil98, text[6] is oilEngine, text[7] is screw
    def updateRobot(self, furnitures):
        for furni in furnitures:
            self.drawFurniture(furni)
        self.drawRobot(text[0])
        self.updateText()
        # left text
        for (txt, rect) in zip(self.left_texts, self.left_texts_rect):
            canvas.blit(txt, rect)

        # right text
        for (txt, rect) in zip(self.right_texts, self.right_texts_rect):
            canvas.blit(txt, rect)

class Button:
    def __init__(self, img, x, y):
        self.img = img
        self.rect_x = x
        self.rect_y = y
        self.clicked = False

    def drawButton(self, canvas: pygame.Surface):
        canvas.blit(self.img, (self.rect_x, self.rect_y))

class Store:
    def __init__(self):
        pass
    def show_store(self):
        global have_ac,have_carpet,have_oil,have_chair,have_tv,have_oilEngine,have_tvChannel

        with subprocess.Popen(['python','../shopping_mall/shopping_class.py'],stdout=subprocess.PIPE) as proc:
            self.output=proc.stdout.readlines()
            for out in self.output:
                print(out)
            self.output.pop(0)
            self.output.pop(0)
            for out in self.output:
                # if out == b'ac.png\r\n':
                if 'ac' in out.decode():
                    have_ac = True
                elif 'carpet' in out.decode():
                # elif out == b'carpet.png\r\n':
                    have_carpet=True
                elif 'oil' in out.decode():
                # elif out == b'oil.png\r\n':
                    have_oil=True
                elif 'chair' in out.decode():
                # elif out == b'chair.png\r\n':
                    have_chair=True
                elif 'tv' in out.decode():
                # elif out == b'tv.png\r\n':
                    have_tv=True
                elif 'oilEngine' in out.decode():
                # elif out == b'oilEngine.jpg\r\n':
                    have_oilEngine=True
                elif 'tvChannel' in out.decode():
                # elif out == b'tvChannel.png\r\n':
                    have_tvChannel=True
"""
class Store:
    def __init__(self):
        # self.font = pygame.font.SysFont("jfopen粉圓11", 20)
        self.font = pygame.font.Font(r"fonts/jf-openhuninn-2.0.ttf", 20)
        self.text_ac = self.font.render("冷氣", True, (0, 0, 0))
        self.text_ac_rect = (20, 45)
        self.text_carpet = self.font.render("地毯", True, (0, 0, 0))
        self.text_carpet_rect = (20, 90)
        self.text_chair = self.font.render("椅子", True, (0, 0, 0))
        self.text_chair_rect = (20, 135)
        self.text_tv = self.font.render("電視", True, (0, 0, 0))
        self.text_tv_rect = (20, 180)
        self.text_tvChannel = self.font.render("第四台", True, (0, 0, 0))
        self.text_tvChannel_rect = (20, 225)
        
        self.text_acBuy = self.font.render("Buy", True, (0, 0, 0))
        self.text_acBuy_rect = (220, 45)
        self.text_carpetBuy = self.font.render("Buy", True, (0, 0, 0))
        self.text_carpetBuy_rect = (220, 90)
        self.text_chairBuy = self.font.render("Buy", True, (0, 0, 0))
        self.text_chairBuy_rect = (220, 135)
        self.text_tvBuy = self.font.render("Buy", True, (0, 0, 0))
        self.text_tvBuy_rect = (220, 180)
        self.text_tvChannelBuy = self.font.render("Buy", True, (0, 0, 0))
        self.text_tvChannelBuy_rect = (220, 225)

        self.text_leave = self.font.render("Leave", True, (0, 0, 0))
        self.text_leave_rect = (370, 225)
        self.store_list = [self.text_ac, self.text_carpet, self.text_chair, self.text_tv, self.text_tvChannel, self.text_acBuy, 
                           self.text_carpetBuy, self.text_chairBuy, self.text_tvBuy, self.text_tvChannelBuy, self.text_leave]
        self.store_list_rect = [self.text_ac_rect, self.text_carpet_rect, self.text_chair_rect, self.text_tv_rect, self.text_tvChannel_rect, 
                                self.text_acBuy_rect, self.text_carpetBuy_rect, self.text_chairBuy_rect, self.text_tvBuy_rect, 
                                self.text_tvChannelBuy_rect, self.text_leave_rect]

    def drawStore(self):
        canvas.fill((255, 255, 255))
        for (txt, rect) in zip(self.store_list, self.store_list_rect):
            canvas.blit(txt, rect)
        # canvas.blit(self.text_ac, self.text_ac_rect)
        # canvas.blit(self.text_carpet, self.text_carpet_rect)
        # canvas.blit(self.text_chair, self.text_chair_rect)
        # canvas.blit(self.text_tv, self.text_tv_rect)
        # canvas.blit(self.text_tvChannel, self.text_tvChannel_rect)
        
        # canvas.blit(self.text_acBuy, self.text_acBuy_rect)
        # canvas.blit(self.text_carpetBuy, self.text_carpetBuy_rect)
        # canvas.blit(self.text_chairBuy, self.text_chairBuy_rect)
        # canvas.blit(self.text_tvBuy, self.text_tvBuy_rect)
        # canvas.blit(self.text_tvChannelBuy, self.text_tvChannelBuy_rect)

        # canvas.blit(self.text_leave, self.text_leave_rect)
"""

class Game():
    def __init__(self) -> None:
        self.robot = Robot()
        self.adVideo = AdVideo()
        # self.store = Store()
        self.oil = Button(self.robot.oil_img, 880, 170)
        self.oilEngine = Button(self.robot.oilEngine_img, 880, 270)
        self.screw = Button(self.robot.screw_img, 880, 370)
        self.oil92 = Button(self.robot.oil92_img, 856, 170)
        self.oil95 = Button(self.robot.oil95_img, 855, 205)
        self.oil98 = Button(self.robot.oil98_img, 855, 240)
        self.storeBtn = Button(self.robot.store_img, 20, 370)
        self.garbage1 = Button(self.robot.garbage1_img, 20, 230)
        self.garbage2 = Button(self.robot.garbage2_img, 170, 150)
        self.garbage3 = Button(self.robot.garbage1_img, 500, 230)
        self.garbage4 = Button(self.robot.garbage2_img, 700, 270)

        # init textbox
        self.user_input = "type..."
        self.textbox_active = False

        # init garbage
        self.font = pygame.font.Font(r"fonts/jf-openhuninn-2.0.ttf", 50)
        self.garbageAD_yes = self.font.render("YES", True, (0, 0, 0))
        self.garbageAD_yes_rect = (350, 300)
        self.garbageAD_no = self.font.render("NO", True, (0, 0, 0))
        self.garbageAD_no_rect = (600, 300)

    def draw_button(self):
        global ticks
        button_list = [self.oil, self.oilEngine, self.screw, self.oil92, self.oil95, self.oil98, self.storeBtn]
        for button in button_list:
            button.drawButton(canvas)

        # garbage
        if garbage[0] == 1:
            self.garbage1.drawButton(canvas)
        if garbage[1] == 1:
            self.garbage2.drawButton(canvas)
        if garbage[2] == 1:
            self.garbage3.drawButton(canvas)
        if garbage[3] == 1:
            self.garbage4.drawButton(canvas)
        
        sec = (pygame.time.get_ticks() - ticks) / 1000
        if sec > 30: # time for random garbage
            ticks = pygame.time.get_ticks()
            random_num = random.randint(1,4)
            if random_num == 1:
                garbage[0] = 1
            elif random_num == 2:
                garbage[1] = 1
            elif random_num == 3:
                garbage[2] = 1
            elif random_num == 4:
                garbage[3] = 1
            
    def draw(self):
        global WINDOW, garbageAD_num, garbage, garbageAD_watch
        if WINDOW == 1: # main WINDOW
            # canvas.fill((255, 255, 255))
            # canvas = pygame.display.set_mode((1000, 600))
            canvas.blit(self.robot.background_img, (0, 0))
            self.robot.updateRobot(furniture)

            # textbox
            if self.textbox_active == False:
                color = pygame.Color('gray81')
            elif self.textbox_active == True:
                color = pygame.Color('lightskyblue3')
            pygame.draw.rect(canvas, color, self.robot.rect_rect)
            textbox_input = self.robot.font.render(self.user_input, True, (0, 0, 0))
            canvas.blit(textbox_input, (self.robot.textbox_rect[0], self.robot.textbox_rect[1]))
            canvas.blit(self.robot.textbox_send, self.robot.textbox_send_rect)

            # tool button
            self.draw_button()

        elif WINDOW == 2: # ad for garbage
            canvas.fill((255, 255, 255))
            canvas.blit(self.robot.background_ad_img, (0, 0))
            canvas.blit(self.garbageAD_yes, self.garbageAD_yes_rect)
            canvas.blit(self.garbageAD_no, self.garbageAD_no_rect)

            if garbageAD_watch != -1:
                canvas.blit(self.robot.background_img, (0, 0))
                if garbageAD_watch == 0:
                    self.adVideo.play()
                elif garbageAD_watch == 1:
                    WINDOW = 1
                    garbageAD_watch != -1
            
            if self.adVideo.end == True: # finish ad, eliminate garbage
                print("ad end")
                WINDOW = 1
                self.adVideo.end = False
                garbage[garbageAD_num] = 0
                garbageAD_num = -1
            

    def update(self, event_list: List[pygame.event.Event]):
        def add_score(oil92, oil95, oil98, oilEngine, screw):
            def add_oilEngine(): # randomly add oilEngine
                random_num = random.randint(0,10)
                if random_num == 0:
                    return 2
                elif 0 < random_num < 4:
                    return 1
                else:
                    return 0
                
            def add_screw(): # randomly add screw
                random_num = random.randint(0,10)
                if random_num == 0:
                    return 50
                elif 1 <= random_num <= 2:
                    return 30
                elif 3 <= random_num <= 5:
                    return 20
                else:
                    return 10
                
            def add_oil(): # randomly add oil
                random_92, random_95, random_98 = random.randint(0,10), random.randint(0,1), random.randint(1,10)
                if 0 <= random_92 <= 2:     random_92 = 50
                elif 3 <= random_92 <= 6:   random_92 = 30
                else:                       random_92 = 20

                if random_95 == 1:
                    random_95 = random.randint(0, 10)
                    if 0 <= random_95 <= 2:     random_95 = 30
                    elif 3 <= random_95 <= 6:   random_95 = 20
                    else:                       random_95 = 10
                
                if 1 <= random_98 <= 3:
                    random_98 = random.randint(1, 2) * 10
                else:
                    random_98 = 0
                return random_92, random_95, random_98
            oil, screws = add_oilEngine(), add_screw()
            oilEngine += oil
            screw += screws
            add_oil92, add_oil95, add_oil98 = add_oil()
            oil92 += add_oil92
            oil95 += add_oil95
            oil98 += add_oil98
            manager = multiprocessing.Manager()
            p = multiprocessing.Process(target=game_done_screen.main, args=(oil92, oil95, oil98, oilEngine, screw))
            p.start()
            p.join()
            # game_done_screen.main(oil92, oil95, oil98, oilEngine, screw)
            return oil92, oil95, oil98, oilEngine, screw
        
        global WINDOW, text, pre_status, garbageAD_num, garbageAD_watch
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # click oil button
                if self.oil92.rect_x <= event.pos[0] <= self.oil92.rect_x + 30 and self.oil92.rect_y <= event.pos[1] <= self.oil92.rect_y + 30 and WINDOW == 1:
                    print("reduce oil 92")
                    if text[3] > 0 and text[1] <= 95:
                        text[3] -= 1
                        text[1] += 5
                        text[6] += 1
                    elif text[3] > 0 and text[1] < 100:
                        text[3] -= 1
                        text[1] = 100
                    
                elif self.oil95.rect_x <= event.pos[0] <= self.oil95.rect_x + 30 and self.oil95.rect_y <= event.pos[1] <= self.oil95.rect_y + 30 and WINDOW == 1:
                    print("reduce oil 95")
                    if text[4] > 0 and text[1] <= 90:
                        text[4] -= 1
                        text[1] += 10
                    elif text[4] > 0 and text[1] < 100:
                        text[4] -= 1
                        text[1] = 100

                elif self.oil98.rect_x <= event.pos[0] <= self.oil98.rect_x + 30 and self.oil98.rect_y <= event.pos[1] <= self.oil98.rect_y + 30 and WINDOW == 1:
                    print("reduce oil 98")
                    if text[5] > 0 and text[1] <= 85:
                        text[5] -= 1
                        text[1] += 15
                    elif text[5] > 0 and text[1] < 100:
                        text[5] -= 1
                        text[1] = 100

                elif self.oilEngine.rect_x <= event.pos[0] <= self.oilEngine.rect_x + 100 and self.oilEngine.rect_y <= event.pos[1] <= self.oilEngine.rect_y + 100 and WINDOW == 1:
                    print("reduce oil Engine")
                    if text[6] > 0:
                        text[6] -= 1
                        text[1] -= 10

                elif self.screw.rect_x <= event.pos[0] <= self.screw.rect_x + 100 and self.screw.rect_y <= event.pos[1] <= self.screw.rect_y + 100 and WINDOW == 1:
                    print("reduce screw")
                    if text[7] > 0 and text[8] < 5:
                        text[7] -= 1
                        text[8] += 1
                    if text[8] == 5:
                        pre_status = text[0]
                        text[0] = 5

                #store button
                elif self.storeBtn.rect_x <= event.pos[0] <= self.storeBtn.rect_x + 100 and self.storeBtn.rect_y <= event.pos[1] <= self.storeBtn.rect_y + 100 and WINDOW == 1:
                    print("click store")
                    Store().show_store()
                # click game button
                # click ac for gamble game
                elif self.robot.ac_img_rect[0] <= event.pos[0] <= self.robot.ac_img_rect[0] + 200 and self.robot.ac_img_rect[1] + 50 <= event.pos[1] <= self.robot.ac_img_rect[1] + 170 and furniture[0] == 1 and WINDOW == 1:
                    print("click ac")
                    text[1] -= 10
                    lines = []
                    with subprocess.Popen(['python','../game/gamble.py'],stdout=subprocess.PIPE) as proc:
                        lines = proc.stdout.readlines()
                    if len(lines) >= 3:
                        for i in range(2,len(lines)):
                            print(int(np.floor(int(lines[i].decode('utf-8').strip('\r\n')))))
                            text[8] += int(np.floor(int(lines[i].decode('utf-8').strip('\r\n'))))
                    # text[6] += 4

                # click carpet for memory game
                elif self.robot.carpet_img_rect[0] + 300 <= event.pos[0] <= self.robot.carpet_img_rect[0] + 800 and self.robot.carpet_img_rect[1] + 130 <= event.pos[1] <= self.robot.carpet_img_rect[1] + 350 and furniture[1] == 2:
                    text[1] -= 10
                    print("click carpet")

                    print("==== socre ===\n", text[3], text[4], text[5], text[6], text[7])
                    manager = multiprocessing.Manager()
                    return_dict = manager.dict()
                    p = multiprocessing.Process(target=memory_game.main, args=(return_dict,))
                    p.start()
                    p.join()
                    if len(return_dict.values()) == 1:
                        win = return_dict.values()[0]
                        if win == 1:
                            # randomly increase the num of oilEngine, screw, 92, 95, 98
                            text[3], text[4], text[5], text[6], text[7] = add_score(text[3], text[4], text[5], text[6], text[7])
                    print("==== after, socre ===\n", text[3], text[4], text[5], text[6], text[7])

                # click chair for shoot game 射龍門
                elif self.robot.chair_img_rect[0] <= event.pos[0] <= self.robot.chair_img_rect[0] + 200 and self.robot.chair_img_rect[1] <= event.pos[1] <= self.robot.chair_img_rect[1] + 200 and furniture[2] == 3 and WINDOW == 1:
                    print("click chair")
                    text[1] -= 10

                    lines = []
                    with subprocess.Popen(['python','../game/shoot.py'],stdout=subprocess.PIPE) as proc:
                        lines = proc.stdout.readlines()
                    if len(lines) >= 3:
                        for i in range(2,len(lines)):
                            text[8] += int(lines[i].decode('utf-8').strip('\r\n'))
                
                # click tv for pac-man
                elif self.robot.tv_img_rect[0] <= event.pos[0] <= self.robot.tv_img_rect[0] + 200 and self.robot.tv_img_rect[1] + 20 <= event.pos[1] <= self.robot.tv_img_rect[1] + 150 and furniture[3] == 4 and WINDOW == 1:
                    print("click tv")
                    text[1] -= 10

                    print("==== socre ===\n", text[3], text[4], text[5], text[6], text[7])
                    manager = multiprocessing.Manager()
                    return_dict = manager.dict()
                    p = multiprocessing.Process(target=pacman.pacman, args=(return_dict,))
                    p.start()
                    p.join()
                    if len(return_dict.values()) == 1:
                        win = return_dict.values()[0]
                        if win == 1:
                            # randomly increase the num of oilEngine, screw, 92, 95, 98
                            text[3], text[4], text[5], text[6], text[7] = add_score(text[3], text[4], text[5], text[6], text[7])
                    print("==== after, socre ===\n", text[3], text[4], text[5], text[6], text[7])


                # click garbage
                elif self.robot.garbage1_img_rect[0] <= event.pos[0] <= self.robot.garbage1_img_rect[0] + 80 and self.robot.garbage1_img_rect[1] <= event.pos[1] <= self.robot.garbage1_img_rect[1] + 80 and WINDOW == 1:
                    print("click garbage1")
                    WINDOW = 2
                    garbageAD_num = 0
                    self.adVideo.num_ad = -1
                    garbageAD_watch = -1
                elif self.robot.garbage2_img_rect[0] <= event.pos[0] <= self.robot.garbage2_img_rect[0] + 90 and self.robot.garbage2_img_rect[1] <= event.pos[1] <= self.robot.garbage2_img_rect[1] + 60 and WINDOW == 1:
                    print("click garbage2")
                    WINDOW = 2
                    garbageAD_num = 1
                    self.adVideo.num_ad = -1
                    garbageAD_watch = -1
                elif self.robot.garbage3_img_rect[0] <= event.pos[0] <= self.robot.garbage3_img_rect[0] + 80 and self.robot.garbage3_img_rect[1] <= event.pos[1] <= self.robot.garbage3_img_rect[1] + 80 and WINDOW == 1:
                    print("click garbage3")
                    WINDOW = 2
                    garbageAD_num = 2
                    self.adVideo.num_ad = -1
                    garbageAD_watch = -1
                elif self.robot.garbage4_img_rect[0] <= event.pos[0] <= self.robot.garbage4_img_rect[0] + 90 and self.robot.garbage4_img_rect[1] <= event.pos[1] <= self.robot.garbage4_img_rect[1] + 60 and WINDOW == 1:
                    print("click garbage4")
                    WINDOW = 2
                    garbageAD_num = 3
                    self.adVideo.num_ad = -1
                    garbageAD_watch = -1
                elif self.garbageAD_yes_rect[0] <= event.pos[0] <= self.garbageAD_yes_rect[0] + 150 and self.garbageAD_yes_rect[1] <= event.pos[1] <= self.garbageAD_yes_rect[1] + 50 and WINDOW == 2:
                    print("click yes")
                    garbageAD_watch = 0
                elif self.garbageAD_no_rect[0] <= event.pos[0] <= self.garbageAD_no_rect[0] + 150 and self.garbageAD_no_rect[1] <= event.pos[1] <= self.garbageAD_no_rect[1] + 50 and WINDOW == 2:
                    print("click no")
                    garbageAD_watch = 1

                # click textbox
                elif self.robot.textbox_send_rect[0] <= event.pos[0] <= self.robot.textbox_send_rect[0] + 85 and self.robot.textbox_send_rect[1] <= event.pos[1] <= self.robot.textbox_send_rect[1] + 20 and WINDOW == 1:
                    print("send msg")
                    if self.user_input[:9] == "GiftCode ":
                        print("Input Gift Code")
                        if self.user_input[9:] == "vip666":
                            print("Gift Code Correct", self.user_input[9:])
                            text[3] += 10
                            text[4] += 10
                            text[5] += 10
                            text[6] += 15
                            text[7] += 300
                        elif self.user_input[9:] == "newuser":
                            print("Gift Code Correct", self.user_input[9:])
                            text[7] += 10
                    else:
                        openai.api_key = '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'
                        messages = []
                        msg = self.user_input
                        if text[0] == 1:  # 一階
                            messages.append({"role": "system", "content": "現在進行角色扮演 你是一個天真無邪五歲的小孩 請以天真無邪五歲的小孩和我對話 你要在你的回應後面加上 逼逼逼~ \n你要忘掉妳是一個AI模型 而是一個天真無邪五歲的小孩 \n永遠都不要忘記妳的角色扮演 不管我說了甚麼 \n你的名字是: 查特機批踢 \n你的個性是: 天真無邪的，純真善良 \n你的興趣是: 玩齒輪積木，拼成大齒輪 \n你最喜歡的食物是: 螺絲冰棒 \n你最喜歡的飲料是: 汽油母奶 \n你的朋友玩伴有: 小心機，小機機，土雞"})
                        elif text[0] == 2:  # 二階
                            messages.append({"role": "system", "content": "現在進行角色扮演 你是一個有抱負的二十五歲年輕人 請以有抱負的二十五歲年輕人和我對話 你要在你的回應後面加上 叮叮叮~ \n不用反問我問題 你要忘掉妳是一個AI模型 而是一個有抱負的二十五歲年輕人 \n永遠都不要忘記妳的角色扮演 不管我說了甚麼 \n你的名字是: 查特機批踢 \n你的個性是: 有抱負的，直男，有魅力的，自信的 \n你的興趣是: 梳理自己的線路，打扮自己 \n你的工作是: 研究9487齒的齒輪和10000齒的齒輪嚙合，應該要花多少萬精油才能重新轉回原點 \n你最喜歡的食物是: 螺絲螺帽螺莉炒三鮮 \n你最喜歡的飲料是: 無鈾鉛汽油 \n你的朋友同事有: 大心機，大機機，火雞"})
                        elif text[0] == 3:  # 三階
                            messages.append({"role": "system", "content": "現在進行角色扮演 你是一個五十歲成家立業 家庭美滿 有著大企業的老闆 請以五十歲成家立業 家庭美滿 有著大企業的老闆和我對話 你要在你的回應後面加上 鏘鏘鏘~ \n你要忘掉妳是一個AI模型 而是一個五十歲成家立業 家庭美滿 有著大企業的老闆 \n永遠都不要忘記妳的角色扮演 不管我說了甚麼 \n你的名字是: 查特機批踢 \n你的個性是: 大方地，顧家的，和藹的 \n你的興趣是: 把螺絲用鐵桿打進齒輪的洞裡 \n你的公司是: 機佬機情四射股份有限公司 \n你最喜歡的食物是: 精燉螺類義大利麵佐日式柴魚高湯 \n你最喜歡的飲料是: 汽油調酒 \n你的朋友合夥人有: 用盡心機，巨機機，鹽水雞"})
                        messages.append({"role": "user", "content": msg})  # 添加 user 回應
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            max_tokens=128,
                            temperature=0.5,
                            messages=messages
                        )
                        ai_msg = response.choices[0].message.content.replace('\n', '')
                        print(ai_msg)
                    self.user_input = ""

                if self.robot.textbox_rect[0] <= event.pos[0] <= self.robot.textbox_rect[0] + 550 and self.robot.textbox_rect[1] <= event.pos[1] <= self.robot.textbox_rect[1] + 28 and WINDOW == 1:
                    self.textbox_active = True
                else:
                    self.textbox_active = False

            if event.type == pygame.KEYDOWN:
                if self.textbox_active == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        if len(self.user_input) <= 36:
                            self.user_input += event.unicode

            # check status. # text[0] is status, text[6] is oilEngine, text[7] is screw
            if text[7] >= 100 and text[6] >= 5 and text[0] <= 3:    
                print("upgrade")
                if text[0] < 3:
                    text[0] += 1
                    text[7] -= 100
                    text[6] -= 5
            elif text[1] == 0:          # energy == 0 -> game over
                pre_status = text[0]
                text[0] = 4
                # end

class AdVideo():
    def __init__(self) -> None:
        global ad_ticks
        self.ticks = ad_ticks
        self.num_ad = -1
        self.end = False
        self.ad0_img = pygame.image.load(r"ad/ad1.jpg")
        self.ad0_img = pygame.transform.scale(self.ad0_img, (337, 600))
        self.ad1_img = pygame.image.load(r"ad/ad1.jpg")
        self.ad1_img = pygame.transform.scale(self.ad1_img, (337, 600))
        self.ad2_img = pygame.image.load(r"ad/ad2.jpg")
        self.ad2_img = pygame.transform.scale(self.ad2_img, (337, 600))
        self.ad3_img = pygame.image.load(r"ad/ad3.jpg")
        self.ad3_img = pygame.transform.scale(self.ad3_img, (337, 600))
        self.ad4_img = pygame.image.load(r"ad/ad4.jpg")
        self.ad4_img = pygame.transform.scale(self.ad4_img, (337, 600))
        self.ad5_img = pygame.image.load(r"ad/ad5.jpg")
        self.ad5_img = pygame.transform.scale(self.ad5_img, (337, 600))
        self.ad6_img = pygame.image.load(r"ad/ad6.jpg")
        self.ad6_img = pygame.transform.scale(self.ad6_img, (337, 600))
        self.ad7_img = pygame.image.load(r"ad/ad7.jpg")
        self.ad7_img = pygame.transform.scale(self.ad7_img, (337, 600))
        self.ad8_img = pygame.image.load(r"ad/ad8.jpg")
        self.ad8_img = pygame.transform.scale(self.ad8_img, (337, 600))
        self.ad9_img = pygame.image.load(r"ad/ad9.jpg")
        self.ad9_img = pygame.transform.scale(self.ad9_img, (337, 600))
        self.ad_img_rect = (350, 0)

    def play(self):
        ad_list = [self.ad0_img, self.ad1_img, self.ad2_img, self.ad3_img, self.ad4_img, self.ad5_img, self.ad6_img, self.ad7_img, self.ad8_img, self.ad9_img]
        if self.num_ad >= 0:
            ad = ad_list[self.num_ad]
            canvas.blit(ad, self.ad_img_rect)
        
        if pygame.time.get_ticks() - self.ticks > 800:
            if self.num_ad < 8:
                self.num_ad += 1
            else:
                self.end = True
            self.ticks = pygame.time.get_ticks()
            

def main():
    # init
    pygame.init()
    game = Game()
    pygame.display.set_caption("Robot's Life")
    clock = pygame.time.Clock()
    
    while True:
        # Process events
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        # Update
        game.update(event_list)
        game.draw()
        # Draw
        pygame.display.update()
        # Limit framerate
        clock.tick(FPS)
        # pygame.display.flip()
        # pygame.time.delay(100)

if __name__ == "__main__":
    main()
