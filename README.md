# robot
---

## Installing

### Install code with git clone
    
    ```bash
    $ git clone https://github.com/shuxian12/robot.git
    ```

### Setting up the environment

    ```bash
    $ cd robot
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```

## How to use

### Run the code

    ```bash
    $ cd robot/main_page.py
    $ python3 main.py
    ```

## Description

### Main Page
* 資訊介紹
    等級: 共有三級，分別有不同型態及角色設定
    能量: 玩遊戲須消耗能量，加油可增加能量
    92: 加92油可增加5單位能量，玩遊戲可取得
    95: 加95油可增加10單位能量，玩遊戲可取得
    98: 加98油可增加15單位能量，玩遊戲可取得
    機油: 升級須消耗5機油，玩遊戲可取得
    螺絲: 遊戲中的錢，升級須消耗100螺絲，也可用於購買傢俱，玩遊戲可取得
* textbox: 可用於輸入禮包碼(輸入"GiftCode "及禮包碼即可取得)及和機器人對話
* 隨機垃圾: 點擊垃圾可選擇是否觀看廣告，廣告結束後垃圾會消失，若選擇不觀看則保留

### Shopping Mall
* 按螺絲的影片看完回傳一個: b'screw.png\r\n'
* 按2.3個商品回傳:b'該商品的名字.png\r\n'，且main_page判斷並出現家俱
* 按第四個商品連接到儲值網站，回傳值尚未設定。這部分的流程可能還要討論。不確定是怎樣操作。
* 尚未完成:1. 螺絲數量連動主畫面。2. 儲值網站連到商城。
* Top-up website: `app.py` 

### Shopping Mall

### Games

* Memory Game:  `python3 main.py`
* Pacman Game: 
玩家一開始會出生在左上角，吃到螺絲得1分，吃到齒輪得5分並且進入狂暴模式。狂暴模式有15秒的無敵時間，此期間可以吃掉鬼並獲得10分，鬼有15秒的復活時間，在死之前吃完所有螺絲和齒輪則獲勝。
* shoot:
射龍門遊戲。玩家下注後可以開始遊戲。按下開始鍵後，會翻開左邊的牌和右邊的牌。若中間牌的數字在兩張牌之間就算勝利，並能獲得三倍下注金額。若中間牌的數字在兩張牌之外就算輸，並失去下注的金額。若中間牌的數字和其中一張牌的數字相同則稱為"撞柱"，失去下注金額的三倍金額。
* gamble:
十八仔遊戲。玩家可任意下注螺絲在賭盤上(每一格只能下注一顆螺絲)。玩家可依據擲出的骰子獲得對應的獎勵。
* pull_medicine:
資安中藥事件。中毒時只能玩這個遊戲。玩家須將中藥倒至磅秤上，若磅秤上的數值與需求數值誤差在10個單位以內，則算挑戰成功，並有1/3的機率解毒成功(遊戲需玩到解毒成功為止)。當解毒成功，機器人會自動升級一階。

### Special Events
