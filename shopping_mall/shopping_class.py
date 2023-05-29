import pygame
from pygame.locals import QUIT
import random,cv2
import re
import sys


pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE=(255,255,255)
BG= (255, 255, 255)
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))

window_surface.fill(BG)
class Shopping_mall():
    def __init__(self,money,ac,carpet,chair,tv):
        
            #商品
        self.money=money
        self.square_color = (254, 250, 224)
        self.square_width_color=(212,163,115)
        self.list_img=["ac.png","carpet.png","oil.png",
                "chair.png","tv.png","oilEngine.jpg"
                ]
        self.list_buy_button=["button_50.png","button_20.png","button_10.png",
                "button_30.png","button_40.png","button_10.png","button_20.png"]
        self.list_button=["按鈕_廣告.png","按鈕_螺絲1.png","按鈕_儲值.png",
                          "按鈕_更新商品.png","exit.png","ok.png"]
        self.commonly_used=["screw.png","bg_4.jpg"]
        self.furniture_state=[ac,carpet,chair,tv]
        self.furniture_name=["ac","carpet","chair","tv"]
        #print(self.furniture_state)
        
        
        self.flag_4=0
        self.list_len=6
        #圖片參數
        self.img_h=250
        self.img_w=250
        self.img_x_left=75
        self.img_y_up=10
        self.img_x_right=380
        self.img_y_down=280

        #商品紀錄(用於回傳)
        self.goods1=0
        self.goods2=0
        self.goods3=0
        #背景
        image = pygame.image.load('../shopping_mall/picture/'+self.commonly_used[1]).convert_alpha()
        image.set_alpha(128)
        image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        window_surface.blit(image, (0, 0))
        #底圖的正方形
        self.draw_rec(self.img_x_left,self.img_y_up)
        self.draw_rec(self.img_x_right,self.img_y_up)
        self.draw_rec(self.img_x_left,self.img_y_down)
        self.draw_rec(self.img_x_right,self.img_y_down)

        self.update_img=1
        self.update_notice=1
        self.draw_img(self.update_img)

        self.get_video()

        self.play_vedio = False

        #按鈕參數
        self.button_w=180
        self.button_h=80
        self.button_x_left=150
        self.button_y_up=190
        self.button_x_right=450
        self.button_y_down=460

        self.button_update_w=120
        self.button_update_h=80
        self.button_update_x=650
        self.button_update_y=350

        self.button_exit_w=120
        self.button_exit_h=80
        self.button_exit_x=650
        self.button_exit_y=460

      
        self.draw_button()

        #是否關閉通知
        self.notice_flag=0
        self.good_name=""

        self.draw_money_num()
      

    def draw_rec(self,center_x,center_y):#圖片背景
        pygame.draw.rect(window_surface, self.square_width_color, (center_x-5 ,center_y-5, self.img_w+10, self.img_h+10),width=5)
        pygame.draw.rect(window_surface, self.square_color, (center_x ,center_y, self.img_w, self.img_h))

    def draw_img(self,flag_update):
        filepath_head="../shopping_mall/picture/"
        if flag_update==0: #不需要更新的時候
           
            self.draw_img_1(filepath_head+self.commonly_used[0],self.img_x_left,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[self.goods1],self.img_x_right,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[self.goods2],self.img_x_left,self.img_y_down)
            self.draw_img_1(filepath_head+self.list_img[self.goods3],self.img_x_right,self.img_y_down)
        else:
            if (self.flag_4==1):
                    self.list_len=7
            num1=random.randrange(len(self.list_img))
            num2=random.randrange(len(self.list_img))
            num3=random.randrange(len(self.list_img))
            while (num2==num1):
                num2=random.randrange(len(self.list_img))
                    
            while (num3==num1 or num3==num2 ):
                num3=random.randrange(len(self.list_img))
            self.goods1=num1
            self.goods2=num2
            self.goods3=num3
            
            self.draw_img_1(filepath_head+self.commonly_used[0],self.img_x_left,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[num1],self.img_x_right,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[num2],self.img_x_left,self.img_y_down)
            self.draw_img_1(filepath_head+self.list_img[num3],self.img_x_right,self.img_y_down)

    def draw_img_1(self,path,center_x,center_y):
    
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (self.img_w, self.img_h))
        window_surface.blit(image, (center_x, center_y))

    def draw_button_1(self,path,center_x,center_y,w,h):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (w,h))
        window_surface.blit(image, (center_x, center_y))

    def draw_button(self):
        filepath_head="../shopping_mall/picture/"
        self.draw_button_1(filepath_head+self.list_button[0],self.button_x_left,self.button_y_up,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_buy_button[self.goods1],self.button_x_right,self.button_y_up,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_buy_button[self.goods2],self.button_x_left,self.button_y_down,self.button_w,self.button_h)
         #儲值
        self.draw_button_1(filepath_head+self.list_button[2],self.button_x_right,self.button_y_down,self.button_w,self.button_h)
        #更新商品
        self.draw_button_1(filepath_head+self.list_button[3],self.button_update_x,self.button_update_y,self.button_update_w,self.button_update_h)
        #離開
        self.draw_button_1(filepath_head+self.list_button[4],self.button_exit_x,self.button_exit_y,self.button_exit_w,self.button_exit_h)
    
    def draw_money_num(self):
        filepath_head="../shopping_mall/picture/"
        image = pygame.image.load(filepath_head+self.commonly_used[0])
        image = pygame.transform.scale(image, (60, 60))
        window_surface.blit(image, (680, 10))
        #字
        font = pygame.font.Font("../shopping_mall/font/kaiu.ttf", 25)
        text = "*"+str(self.money)
        
        text_surface = font.render(text, True,BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (760,40)
        window_surface.blit(text_surface, text_rect)
    
    def draw_notice(self,goods,money_enough,return_goods):

        
        pygame.draw.rect(window_surface, (255,175,204), (195 ,195, 410, 210))
        pygame.draw.rect(window_surface, WHITE, (200 ,200, 400, 200))
        image = pygame.image.load('../shopping_mall/picture/'+self.list_button[5])
        image = pygame.transform.scale(image, (140, 80))
        window_surface.blit(image, (330, 320))

        font = pygame.font.Font("../shopping_mall/font/kaiu.ttf", 25)
        if money_enough==1:#夠錢
            if goods=="screw":
                text = "你已獲得"+goods+"*2"
            else:
                text = "你已獲得"+goods
            print(return_goods)
        elif money_enough==2:#已擁有
             text="你已經買過了啦"
        else:
             text="你的錢不夠QQ 嗚嗚"
        text_surface = font.render(text, True,(255,175,204))
        text_rect = text_surface.get_rect()
        text_rect.center = (330,250)
        window_surface.blit(text_surface, text_rect)
        

    def click_event1_video(self,input):
        self.money=self.money+input
        self.get_video()
        self.get_sound()
        window_surface.fill(BLACK)
        self.play_vedio = True
        pygame.time.set_timer(pygame.USEREVENT, millis=4500, loops=1)
       
        return #看要return 甚麼參數給螺絲

    def click_event2_buy(self):
        self.update_notice=1
        str_good =self.list_img[self.goods1]
        sale=self.list_buy_button[self.goods1].replace("button_","")
        sale=sale.replace(".png","")
        if str_good.find(".png")!=-1:
             str_good=str_good.replace(".png","")
        elif str_good.find(".jpg")!=-1:
             str_good=str_good.replace(".jpg","")
             
        money_enough=2
        for i in range(len(self.furniture_name)):
            if str_good==self.furniture_name[i] and self.furniture_state[i]=='False':#確定還沒買
                sale=int(sale)
                if self.money>=sale:
                    self.money=self.money-sale
                    money_enough=1
                    self.furniture_state[i]='True'
                else:
                    money_enough=0
        if str_good=="oil" or str_good=="oilEngine":
            sale=int(sale)
            if self.money>=sale:
                    self.money=self.money-sale
                    money_enough=1
                    
            else:
                    money_enough=0
        self.draw_notice(str_good,money_enough,self.list_img[self.goods1])
        
         
    def click_event3_buy(self):
        str_good =self.list_img[self.goods2]
        sale=self.list_buy_button[self.goods2].replace("button_","")
        sale=sale.replace(".png","")
        if str_good.find(".png")!=-1:
            str_good=str_good.replace(".png","")
          
        elif str_good.find(".jpg")!=-1:
            str_good=str_good.replace(".jpg","")
        money_enough=2
        for i in range(len(self.furniture_name)):
            if str_good==self.furniture_name[i] and self.furniture_state[i]=='False':#確定還沒買
                sale=int(sale)
                if self.money>=sale:
                    self.money=self.money-sale
                    money_enough=1
                    self.furniture_state[i]='True'
                else:
                    money_enough=0
        if str_good=="oil" or str_good=="oilEngine":
            sale=int(sale)
            if self.money>=sale:
                    self.money=self.money-sale
                    money_enough=1
                    
            else:
                    money_enough=0
        self.draw_notice(str_good,money_enough,self.list_img[self.goods2])
                 
        
        #bug買東西 #看要return 甚麼參數給家具
    def click_event4_web(self):
        
        str_good =self.list_img[self.goods3]
        if str_good.find(".png")!=-1:
             str_good=str_good.replace(".png","")
        elif str_good.find(".jpg")!=-1:
             str_good=str_good.replace(".jpg","")
        
        
        import webbrowser, threading
        def open_web():
            webbrowser.open('http://127.0.0.1:5000')
        thread2 = threading.Thread(target=open_web, )
        thread2.run()
        money_enough=2
        for i in range(len(self.furniture_name)):
            if str_good==self.furniture_name[i] and self.furniture_state[i]=='False':#確定還沒買
                money_enough=1
                print("if 1")
                
                self.furniture_state[i]='True'
                
        if str_good=="oil" or str_good=="oilEngine":
            money_enough=1
            print("if 3")
        self.draw_notice(str_good,money_enough,self.list_img[self.goods3]+"_top-up")

    def click_event5_update_goods(self):

        pass

    def click_event6_exit(self):
        pygame.quit()
        exit()
    
    def close_notice(self):
         pass
         
    def get_video(self):
        self.cap = cv2.VideoCapture('../shopping_mall/video/ads.mp4')
        self.success, self.img = self.cap.read()
        self.shape = self.img.shape[1::-1]

    def get_sound(self):
        audio_path = "../shopping_mall/sounds/ads1_sound.mp3"
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play()

    def update(self,update_img,update_notice,goods):
        if self.play_vedio:
            self.success, self.img = self.cap.read()
            if self.success:
                
                window_surface.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 50))
        else:
            window_surface.fill(BG)
            image = pygame.image.load('../shopping_mall/picture/'+self.commonly_used[1]).convert_alpha()
            image.set_alpha(128)
            image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
            window_surface.blit(image, (0, 0))
            self.draw_rec(self.img_x_left,self.img_y_up)
            self.draw_rec(self.img_x_right,self.img_y_up)
            self.draw_rec(self.img_x_left,self.img_y_down)
            self.draw_rec(self.img_x_right,self.img_y_down)
            self.draw_img(update_img) #不用更新圖片
            self.draw_button()
            self.draw_money_num()
            if update_notice==1:
                
                self.draw_notice(goods,1,goods)#看完影片買螺絲之後，要更新公告

def main(money,ac,carpet,chair,tv):
    pygame.init()
    pygame.display.set_caption('shopping_mall')
    shopping_mall=Shopping_mall(money,ac,carpet,chair,tv)
    running=True
    clock = pygame.time.Clock()
    
   
    while running:
        
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                running=False
                pygame.quit()
            #按按鍵
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

               #影片事件
                if shopping_mall.button_x_left<= mouse_x <= shopping_mall.button_x_left+shopping_mall.button_w \
                    and shopping_mall.button_y_up<= mouse_y <= shopping_mall.button_y_up+shopping_mall.button_h:
                    #print(shopping_mall.commonly_used[0])
                    shopping_mall.update_notice=1
                    shopping_mall.click_event1_video(2)
                    shopping_mall.update_img=0
                    shopping_mall.good_name="screw"
                    shopping_mall.notice_flag=1

                #螺絲購買事件
                if shopping_mall.button_x_right<= mouse_x <= shopping_mall.button_x_right+shopping_mall.button_w \
                    and shopping_mall.button_y_up<= mouse_y <= shopping_mall.button_y_up+shopping_mall.button_h:
                        shopping_mall.notice_flag=1
                        shopping_mall.click_event2_buy()

                if shopping_mall.button_x_left<= mouse_x <= shopping_mall.button_x_left+shopping_mall.button_w \
                    and shopping_mall.button_y_down<= mouse_y <= shopping_mall.button_y_down+shopping_mall.button_h:
                        shopping_mall.notice_flag=1
                        shopping_mall.click_event3_buy()

                #儲值事件
                if shopping_mall.button_x_right<= mouse_x <= shopping_mall.button_x_right+shopping_mall.button_w \
                    and shopping_mall.button_y_down<= mouse_y <= shopping_mall.button_y_down+shopping_mall.button_h:
                        shopping_mall.notice_flag=1
                        shopping_mall.click_event4_web()

                #更新商品事件
                if shopping_mall.button_update_x<= mouse_x <= shopping_mall.button_update_x+shopping_mall.button_update_w \
                    and shopping_mall.button_update_y<= mouse_y <= shopping_mall.button_update_y+shopping_mall.button_update_h:
                        shopping_mall.click_event1_video(0)
                        shopping_mall.update_img=1
                        shopping_mall.update_notice=0
                        shopping_mall.good_name=""


                if shopping_mall.button_exit_x<= mouse_x <= shopping_mall.button_exit_x+shopping_mall.button_exit_w \
                    and shopping_mall.button_exit_y<= mouse_y <= shopping_mall.button_exit_y+shopping_mall.button_exit_h:
                        shopping_mall.click_event6_exit()

                #如果有跳出通知
                if shopping_mall.notice_flag==1:
                    if 330<= mouse_x <= 330+140 and 320<= mouse_y <= 320+80:
                         shopping_mall.update_img=0
                         shopping_mall.update_notice=0
                         shopping_mall.update(shopping_mall.update_img,shopping_mall.update_notice,"")
                       
            #播影片結束
            if event.type == pygame.USEREVENT:
                shopping_mall.play_vedio = False
                pygame.mixer.music.stop()
                shopping_mall.update(shopping_mall.update_img,shopping_mall.update_notice,shopping_mall.good_name)

        
        if shopping_mall.play_vedio == True:
            shopping_mall.update(shopping_mall.update_img,shopping_mall.update_notice,shopping_mall.good_name)
                
        pygame.display.update()
        clock.tick(22)
    pygame.quit()

  

if __name__ == '__main__':
    money=int(sys.argv[1])
    input_ac=sys.argv[2]
    input_carpet=sys.argv[3]
    input_chair=sys.argv[4]
    input_tv=sys.argv[5]
    main(money,input_ac,input_carpet,input_chair,input_tv)