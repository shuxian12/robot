import sys

import pygame
from pygame.locals import QUIT
import random,cv2


pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
BG= (255, 183, 3)
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))

pygame.display.set_caption('shopping_mall')

window_surface.fill(BG)
class Shopping_mall():
    def __init__(self):
    
            #商品
        self.square_color = (254, 250, 224)
        self.square_width_color=(250,237,205)
        self.list_img=["冷氣.png","地毯.png","書櫃.png","汽油.png",
                "椅子.png","電視.png","機油.jpg","第四台.png"
                ]
        self.list_button=["按鈕_廣告.png","按鈕_螺絲1.png","按鈕_儲值.png",
                          "按鈕_更新商品.png","exit.png"]
        
        
        self.flag_4=0
        self.list_len=7
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
        #底圖的正方形
        self.draw_rec(self.img_x_left,self.img_y_up)
        self.draw_rec(self.img_x_right,self.img_y_up)
        self.draw_rec(self.img_x_left,self.img_y_down)
        self.draw_rec(self.img_x_right,self.img_y_down)

        self.update_img=1
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

      

    def draw_rec(self,center_x,center_y):#圖片背景
        pygame.draw.rect(window_surface, self.square_width_color, (center_x-5 ,center_y-5, self.img_w+10, self.img_h+10),width=5)
        pygame.draw.rect(window_surface, self.square_color, (center_x ,center_y, self.img_w, self.img_h))

    def draw_img(self,flag_update):
        filepath_head="picture/"
        if flag_update==0: #不需要更新的時候
            self.draw_img_1(filepath_head+"螺絲.png",self.img_x_left,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[self.goods1],self.img_x_right,self.img_y_up)
            self.draw_img_1(filepath_head+self.list_img[self.goods2],self.img_x_left,self.img_y_down)
            self.draw_img_1(filepath_head+self.list_img[self.goods3],self.img_x_right,self.img_y_down)
        else:
            if (self.flag_4==1):
                    self.list_len=8
            num1=random.randrange(self.list_len)
            num2=random.randrange(self.list_len)
            num3=random.randrange(self.list_len)
            while (num2==num1):
                num2=random.randrange(self.list_len)
                    
            while (num3==num1 or num3==num2 ):
                num3=random.randrange(self.list_len)
            self.goods1=num1
            self.goods2=num2
            self.goods3=num3

            self.draw_img_1(filepath_head+"螺絲.png",self.img_x_left,self.img_y_up)
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
        filepath_head="picture/"
        self.draw_button_1(filepath_head+self.list_button[0],self.button_x_left,self.button_y_up,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_button[1],self.button_x_right,self.button_y_up,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_button[1],self.button_x_left,self.button_y_down,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_button[2],self.button_x_right,self.button_y_down,self.button_w,self.button_h)
        self.draw_button_1(filepath_head+self.list_button[3],self.button_update_x,self.button_update_y,self.button_update_w,self.button_update_h)
        self.draw_button_1(filepath_head+self.list_button[4],self.button_exit_x,self.button_exit_y,self.button_exit_w,self.button_exit_h)


    def click_event1_video(self):
        self.get_video()
        self.get_sound()
        window_surface.fill(BLACK)
        self.play_vedio = True
        pygame.time.set_timer(pygame.USEREVENT, millis=4500, loops=1)
       
        return #看要return 甚麼參數給螺絲

    def click_event2_buy(self):
        print(2)
        for i in self.list_img:
            if self.list_img[self.goods1]==i:
                 return self.list_img[self.goods1]
        #bug買東西
        return #看要return 甚麼參數給家具
        pass
         
    def click_event3_buy(self):
        print(3)
        for i in self.list_img:
            if self.list_img[self.goods2]==i:
                 print(self.list_img[self.goods2])
                 return self.list_img[self.goods2]
                 
        return
        #bug買東西 #看要return 甚麼參數給家具
        pass
    def click_event4_web(self):
        print(4)
        for i in self.list_img:
            if self.list_img[self.goods3]==i:
                 print(self.list_img[self.goods3])
                 return self.list_img[self.goods3]
        #儲值
        pass

    def click_event5_update_goods(self):
        print(5)
        
        
        pass

    def click_event6_exit(self):
        print(6)
        pygame.quit()
        pass #回到主畫面

    def get_video(self):
        self.cap = cv2.VideoCapture('video/ads.mp4')
        self.success, self.img = self.cap.read()
        self.shape = self.img.shape[1::-1]

    def get_sound(self):
        audio_path = "sounds/ads1_sound.mp3"
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play()

    def update(self,update_img):
        if self.play_vedio:
            self.success, self.img = self.cap.read()
            if self.success:
                
                window_surface.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 50))
        else:
            window_surface.fill(BG)
            self.draw_rec(self.img_x_left,self.img_y_up)
            self.draw_rec(self.img_x_right,self.img_y_up)
            self.draw_rec(self.img_x_left,self.img_y_down)
            self.draw_rec(self.img_x_right,self.img_y_down)
            self.draw_img(update_img) #不用更新圖片
            self.draw_button()

   
         
             
        


def main():
    shopping_mall=Shopping_mall()
    running=True
    clock = pygame.time.Clock()
   
    while running:
        
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                running=False
            #按按鍵
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

               #影片事件
                if shopping_mall.button_x_left<= mouse_x <= shopping_mall.button_x_left+shopping_mall.button_w \
                    and shopping_mall.button_y_up<= mouse_y <= shopping_mall.button_y_up+shopping_mall.button_h:
                    shopping_mall.click_event1_video()
                    shopping_mall.update_img=0

                #螺絲購買事件
                if shopping_mall.button_x_right<= mouse_x <= shopping_mall.button_x_right+shopping_mall.button_w \
                    and shopping_mall.button_y_up<= mouse_y <= shopping_mall.button_y_up+shopping_mall.button_h:
                        shopping_mall.click_event2_buy()

                if shopping_mall.button_x_left<= mouse_x <= shopping_mall.button_x_left+shopping_mall.button_w \
                    and shopping_mall.button_y_down<= mouse_y <= shopping_mall.button_y_down+shopping_mall.button_h:
                        shopping_mall.click_event3_buy()

                #儲值事件
                if shopping_mall.button_x_right<= mouse_x <= shopping_mall.button_x_right+shopping_mall.button_w \
                    and shopping_mall.button_y_down<= mouse_y <= shopping_mall.button_y_down+shopping_mall.button_h:
                        shopping_mall.click_event4_web()

                #更新商品事件
                if shopping_mall.button_update_x<= mouse_x <= shopping_mall.button_update_x+shopping_mall.button_update_w \
                    and shopping_mall.button_update_y<= mouse_y <= shopping_mall.button_update_y+shopping_mall.button_update_h:
                        shopping_mall.click_event1_video()
                        shopping_mall.update_img=1

                if shopping_mall.button_exit_x<= mouse_x <= shopping_mall.button_exit_x+shopping_mall.button_exit_w \
                    and shopping_mall.button_exit_y<= mouse_y <= shopping_mall.button_exit_y+shopping_mall.button_exit_h:
                        shopping_mall.click_event6_exit()
                       
            #播影片結束
            if event.type == pygame.USEREVENT:
                shopping_mall.play_vedio = False
                pygame.mixer.music.stop()
                
                shopping_mall.update(shopping_mall.update_img)

        
        if shopping_mall.play_vedio == True:
            shopping_mall.update(shopping_mall.update_img)
                
        pygame.display.update()
        clock.tick(22)
    pygame.quit()
  

if __name__ == '__main__':
    main()