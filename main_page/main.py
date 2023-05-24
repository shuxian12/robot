import pygame

canvas = pygame.display.set_mode((1000, 600))
text = [1, 50, 0, 100, 100, 100, 4, 100, 0] # text[8] = num of screw
furniture = [0, 0, 0, 0, 0]
pre_status = 1
WINDOW = 1
FPS = 60

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

        # furniture image
        self.store_img = pygame.image.load(r"furniture/store.png")
        self.store_img = pygame.transform.scale(self.store_img, (100, 100))
        self.background_img = pygame.image.load(r"furniture/background.png")
        self.background_img = pygame.transform.scale(self.background_img, (1000, 600))
        self.ac_img = pygame.image.load(r"furniture/ac.png")
        self.ac_img = pygame.transform.scale(self.ac_img, (200, 200))
        self.carpet_img = pygame.image.load(r"furniture/carpet.png")
        self.carpet_img = pygame.transform.scale(self.carpet_img, (800, 600))
        self.chair_img = pygame.image.load(r"furniture/chair.png")
        self.chair_img = pygame.transform.scale(self.chair_img, (200, 200))
        self.tvChannel_img = pygame.image.load(r"furniture/tvChannel.png")
        self.tvChannel_img = pygame.transform.scale(self.tvChannel_img, (200, 200))
        self.tv_img = pygame.image.load(r"furniture/tv.png")
        self.tv_img = pygame.transform.scale(self.tv_img, (200, 200))

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
        self.font = pygame.font.Font('fonts/jf-openhuninn-2.0.ttf', 20)
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

    def drawRobot(self, status):
        if status == 1:
            canvas.blit(self.status1_img, (550, 300))
        elif status == 2:
            canvas.blit(self.status2_img, (550, 300))
        elif status == 3:
            canvas.blit(self.status3_img, (550, 200))
        elif status == 4:
            canvas.blit(self.iron_img, (550, 300))
        elif status == 5:
            canvas.blit(self.broken_img, (550, 300))

    def drawFurniture(self, n):
        if n == 1:
            canvas.blit(self.ac_img, (600, 0))
        elif n == 2:
            canvas.blit(self.carpet_img, (100, 200))
        elif n == 3:
            canvas.blit(self.chair_img, (150, 300))
        elif n == 4:
            canvas.blit(self.tv_img, (250, 80))
        elif n == 5:
            canvas.blit(self.tvChannel_img, (250, 80))

    def updateText(self):
        global text
        # for i in text:
        #     print(i)
        self.num_status = self.font.render(str(text[0]), True, (0, 0, 0))
        self.num_energy = self.font.render(str(text[1]), True, (0, 0, 0))
        self.num_bug = self.font.render(str(text[2]), True, (0, 0, 0))
        self.num_oil92 = self.font.render(str(text[3]), True, (0, 0, 0))
        self.num_oil95 = self.font.render(str(text[4]), True, (0, 0, 0))
        self.num_oil98 = self.font.render(str(text[5]), True, (0, 0, 0))
        self.num_oilEngine = self.font.render(str(text[6]), True, (0, 0, 0))
        self.num_screw = self.font.render(str(text[7]), True, (0, 0, 0))
        self.left_texts = [self.text_energy, self.text_status, self.text_bug, self.num_energy, self.num_status, self.num_bug]
        self.right_texts = [self.text_oil92, self.text_oil95, self.text_oil98, self.text_oilEngine, self.text_screw, self.num_oil92, self.num_oil95, self.num_oil98, self.num_oilEngine, self.num_screw]

    def updateRobot(self, furnitures):
        for furni in furnitures:
            self.drawFurniture(furni)
        self.drawRobot(text[0])
        self.updateText()
        # left text
        for (txt, rect) in zip(self.left_texts, self.left_texts_rect):
            canvas.blit(txt, rect)
        # canvas.blit(self.text_energy, self.text_energy_rect)
        # canvas.blit(self.text_status,  self.text_status_rect)
        # canvas.blit(self.num_energy,  self.num_energy_rect)
        # canvas.blit(self.num_status,  self.num_status_rect)
        # canvas.blit(self.text_bug,  self.text_bug_rect)
        # canvas.blit(self.num_bug, self.num_bug_rect)

        # right text
        for (txt, rect) in zip(self.right_texts, self.right_texts_rect):
            canvas.blit(txt, rect)
        # canvas.blit(self.text_oil92, self.tetx_oil92_rect)
        # canvas.blit(self.text_oil95, self.text_oil95_rect)
        # canvas.blit(self.text_oil98, self.text_oil98_rect)
        # canvas.blit(self.text_oilEngine, self.text_oilEngine_rect)
        # canvas.blit(self.text_screw, self.text_screw_rect)
        # canvas.blit(self.num_oil92, self.num_oil92_rect)
        # canvas.blit(self.num_oil95, self.num_oil95_rect)
        # canvas.blit(self.num_oil98, self.num_oil98_rect)
        # canvas.blit(self.num_oilEngine, self.num_oilEngine_rect)
        # canvas.blit(self.num_screw, self.num_screw_rect)

class Button:
    def __init__(self, img, x, y):
        self.img = img
        self.rect_x = x
        self.rect_y = y
        self.clicked = False

    def drawButton(self, canvas):
        canvas.blit(self.img, (self.rect_x, self.rect_y))

class Store:
    def __init__(self):
        # self.font = pygame.font.SysFont("jfopen粉圓11", 20)
        self.font = pygame.font.Font('fonts/jf-openhuninn-2.0.ttf', 20)
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

class Game():
    def __init__(self) -> None:
        self.robot = Robot()
        self.store = Store()
        self.oil = Button(self.robot.oil_img, 880, 170)
        self.oilEngine = Button(self.robot.oilEngine_img, 880, 270)
        self.screw = Button(self.robot.screw_img, 880, 370)
        self.oil92 = Button(self.robot.oil92_img, 856, 170)
        self.oil95 = Button(self.robot.oil95_img, 855, 205)
        self.oil98 = Button(self.robot.oil98_img, 855, 240)
        self.storeBtn = Button(self.robot.store_img, 20, 370)
        # self.button_list = [self.oil, self.oilEngine, self.screw, self.oil92, self.oil95, self.oil98, self.storeBtn]

    def draw_button(self):
        button_list = [self.oil, self.oilEngine, self.screw, self.oil92, self.oil95, self.oil98, self.storeBtn]
        for button in button_list:
            button.drawButton(canvas)

    def draw(self):
        if WINDOW == 1: # main WINDOW
            # canvas.fill((255, 255, 255))
            # canvas = pygame.display.set_mode((1000, 600))
            canvas.blit(self.robot.background_img, (0, 0))
            self.robot.updateRobot(furniture)

            '''
            # self.robot.drawFurniture(canvas, furniture[0])
            # self.robot.drawFurniture(canvas, furniture[1])
            # self.robot.drawFurniture(canvas, furniture[2])
            # self.robot.drawFurniture(canvas, furniture[3])
            # self.robot.drawFurniture(canvas, furniture[4])
            # self.robot.drawRobot(canvas, text[0])
            # self.robot.updateText(text)

            # left text
            # canvas.blit(self.robot.text_energy, self.robot.text_energy_rect)
            # canvas.blit(self.robot.text_status, self.robot.text_status_rect)
            # canvas.blit(self.robot.num_energy, self.robot.num_energy_rect)
            # canvas.blit(self.robot.num_status, self.robot.num_status_rect)
            # canvas.blit(self.robot.text_bug, self.robot.text_bug_rect)
            # canvas.blit(self.robot.num_bug, self.robot.num_bug_rect)

            # right text
            # canvas.blit(self.robot.text_oil92, self.robot.tetx_oil92_rect)
            # canvas.blit(self.robot.text_oil95, self.robot.text_oil95_rect)
            # canvas.blit(self.robot.text_oil98, self.robot.text_oil98_rect)
            # canvas.blit(self.robot.text_oilEngine, self.robot.text_oilEngine_rect)
            # canvas.blit(self.robot.text_screw, self.robot.text_screw_rect)
            # canvas.blit(self.robot.num_oil92, self.robot.num_oil92_rect)
            # canvas.blit(self.robot.num_oil95, self.robot.num_oil95_rect)
            # canvas.blit(self.robot.num_oil98, self.robot.num_oil98_rect)
            # canvas.blit(self.robot.num_oilEngine, self.robot.num_oilEngine_rect)
            # canvas.blit(self.robot.num_screw, self.robot.num_screw_rect)
            '''

            # tool button
            self.draw_button()

        # elif WINDOW == 2:
        #     canvas = pygame.display.set_mode((500, 300))
        #     canvas.fill((255, 255, 255))
        #     self.store.drawStore(canvas)
    
    def update(self, event_list):
        global WINDOW, text
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    # press oil button
                    if self.oil92.rect_x <= event.pos[0] <= self.oil92.rect_x + 30 and self.oil92.rect_y <= event.pos[1] <= self.oil92.rect_y + 30 and WINDOW == 1:
                        print("reduce oil 92")
                        if text[3] > 0 and text[1] <= 95:
                            text[3] -= 1
                            text[1] += 5
                            text[6] += 1
                    elif self.oil95.rect_x <= event.pos[0] <= self.oil95.rect_x + 30 and self.oil95.rect_y <= event.pos[1] <= self.oil95.rect_y + 30 and WINDOW == 1:
                        print("reduce oil 95")
                        if text[4] > 0 and text[1] <= 90:
                            text[4] -= 1
                            text[1] += 10
                    elif self.oil98.rect_x <= event.pos[0] <= self.oil98.rect_x + 30 and self.oil98.rect_y <= event.pos[1] <= self.oil98.rect_y + 30 and WINDOW == 1:
                        print("reduce oil 98")
                        if text[5] > 0 and text[1] <= 85:
                            text[5] -= 1
                            text[1] += 15
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

                    # store button
                    elif self.storeBtn.rect_x <= event.pos[0] <= self.storeBtn.rect_x + 100 and self.storeBtn.rect_y <= event.pos[1] <= self.storeBtn.rect_y + 100 and WINDOW == 1:
                        print("click store")
                        WINDOW = 2
                    elif self.store.text_acBuy_rect[0] <= event.pos[0] <= self.store.text_acBuy_rect[0] + 100 and self.store.text_acBuy_rect[1] <= event.pos[1] <= self.store.text_acBuy_rect[1] + 20 and WINDOW == 2:
                        furniture[0] = 1
                        self.store.text_acBuy = self.store.font.render("Buy", True, (255, 0, 0))
                    elif self.store.text_carpetBuy_rect[0] <= event.pos[0] <= self.store.text_carpetBuy_rect[0] + 100 and self.store.text_carpetBuy_rect[1] <= event.pos[1] <= self.store.text_carpetBuy_rect[1] + 20 and WINDOW == 2:
                        furniture[1] = 2
                        self.store.text_carpetBuy = self.store.font.render("Buy", True, (255, 0, 0))
                    elif self.store.text_chairBuy_rect[0] <= event.pos[0] <= self.store.text_chairBuy_rect[0] + 100 and self.store.text_chairBuy_rect[1] <= event.pos[1] <= self.store.text_chairBuy_rect[1] + 20 and WINDOW == 2:
                        furniture[2] = 3
                        self.store.text_chairBuy = self.store.font.render("Buy", True, (255, 0, 0))
                    elif self.store.text_tvBuy_rect[0] <= event.pos[0] <= self.store.text_tvBuy_rect[0] + 100 and self.store.text_tvBuy_rect[1] <= event.pos[1] <= self.store.text_tvBuy_rect[1] + 20 and WINDOW == 2:
                        furniture[3] = 4
                        self.store.text_ctvBuy = self.store.font.render("Buy", True, (255, 0, 0))
                    elif self.store.text_tvChannelBuy_rect[0] <= event.pos[0] <= self.store.text_tvChannelBuy_rect[0] + 100 and self.store.text_tvChannelBuy_rect[1] <= event.pos[1] <= self.store.text_tvChannelBuy_rect[1] + 20 and WINDOW == 2:
                        furniture[4] = 5
                        self.store.text_tvChannelBuy = self.store.font.render("Buy", True, (255, 0, 0))
                    elif self.store.text_leave_rect[0] <= event.pos[0] <= self.store.text_leave_rect[0] + 100 and self.store.text_leave_rect[1] <= event.pos[1] <= self.store.text_leave_rect[1] + 20 and WINDOW == 2:
                        WINDOW = 1
                            
                    # game button
                    
                    # check status
                    if text[7] >= 100 and text[6] >= 5:
                        print("upgrade")
                        if text[0] <= 3:
                            text[0] += 1
                            text[7] -= 100
                            text[6] -= 5



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

'''
BUG
1. 商店閃爍

'''