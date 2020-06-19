#file:game2Main
import pygame,random,time,sys
from pygame.locals import*
pygame.init()
#視窗大小
background=pygame.display.set_mode((800,600)) 
#設定視窗名字
#pygame.display.set_caption('接果子') 
#顏色表
red=(255,0,0) 
yellow=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
#背景音樂
backMusic='./Hero.mp3' 
pygame.mixer.music.load(backMusic)
pygame.mixer.music.play()
#所有的圖片
class Picture():
    def __init__(self):
        #籃子的圖片
        self.pictureBasket=('./win.jpg')
        self.basket=pygame.image.load(self.pictureBasket).convert_alpha()
        self.basketGet=self.basket.get_rect()
    #頻果樹圖片
    def appleTree(self):    
        self.pictureTree=('./win1.png')
        self.tree=pygame.image.load(self.pictureTree).convert()
        background.blit(self.tree,(0,0))
    def brownBasket(self):
        background.blit(self.basket,self.basketGet)
    #結束遊戲時的蘋果蟲圖片
    def apple(self):
        self.pictureAppleWorm=('./win2.png')
        self.appleWorm=pygame.image.load(self.pictureAppleWorm).convert()
        background.blit(self.appleWorm,(0,0))
    #開始前的遊戲說明
    def beforeStart(self):
        self.pictureBeforeStart=('./win.png')
        self.start=pygame.image.load(self.pictureBeforeStart).convert()
        background.blit(self.start,(0,0))
picture=Picture()
picture.basketGet.left=350
picture.basketGet.top=500
#玩家的資訊
class Player():
    def __init__(self):
        self.score=0
        self.leftRight=''
        self.left=False
        self.right=False
        self.miss=0
    #防止超出視窗
    def cross(self):
        if picture.basketGet.left<=50:
            picture.basketGet.left=50
        if picture.basketGet.left>=650:
            picture.basketGet.left=650
player=Player()
#設定7列掉落的方塊
class Fall():
    def __init__(self):
        self.fallTime=2
        self.fallSpeed=4
        self.appleColumn=0
        self.appleFall=False
        self.column1=False
        self.column2=False
        self.column3=False
        self.column4=False
        self.column5=False
        self.column6=False
        self.column7=False
        self.column1Pos=0
        self.column2Pos=0
        self.column3Pos=0
        self.column4Pos=0
        self.column5Pos=0
        self.column6Pos=0
        self.column7Pos=0
        self.color=red
    #隨機選取某一列開始掉落
    def chooseFall(self):
        self.appleColumn=(random.randrange(1,8))
        if self.appleColumn==1:
            self.column1=True
        elif self.appleColumn==2:
            self.column2=True
        elif self.appleColumn==3:
            self.column3=True
        elif self.appleColumn==4:
            self.column4=True
        elif self.appleColumn==5:
            self.column5=True
        elif self.appleColumn==6:
            self.column6=True
        elif self.appleColumn==7:
            self.column7=True   
    #掉落的過程中的判定            
    def fallStart(self):    
        if self.column1==True:
            pygame.draw.rect(background,self.color,pygame.Rect(100,self.column1Pos,15,15))
            self.column1Pos=self.column1Pos+fall.fallSpeed
            if self.column1Pos>=500 and self.column1Pos<=550:
                if picture.basketGet.left>=30 and picture.basketGet.left<=100:
                    player.score=player.score+10
                    self.column1=False
                    self.column1Pos=0
        if self.column2==True:
            pygame.draw.rect(background,self.color,pygame.Rect(200,self.column2Pos,15,15))
            self.column2Pos=self.column2Pos+fall.fallSpeed
            if self.column2Pos>=500 and self.column2Pos<=550:
                if picture.basketGet.left>=140 and picture.basketGet.left<=200:
                    player.score=player.score+10
                    self.column2=False
                    self.column2Pos=0
        if self.column3==True:
            pygame.draw.rect(background,self.color,pygame.Rect(300,self.column3Pos,15,15))
            self.column3Pos=self.column3Pos+fall.fallSpeed
            if self.column3Pos>=500 and self.column3Pos<=550:
                if picture.basketGet.left>=250 and picture.basketGet.left<=300:
                    player.score=player.score+10
                    self.column3=False
                    self.column3Pos=0
        if self.column4==True:
            pygame.draw.rect(background,self.color,pygame.Rect(400,self.column4Pos,15,15))
            self.column4Pos=self.column4Pos+fall.fallSpeed
            if self.column4Pos>=500 and self.column4Pos<=550:
                if picture.basketGet.left>=340 and picture.basketGet.left<=420:
                    player.score=player.score+10
                    self.column4=False
                    self.column4Pos=0
        if self.column5==True:
            pygame.draw.rect(background,self.color,pygame.Rect(500,self.column5Pos,15,15))
            self.column5Pos=self.column5Pos+fall.fallSpeed
            if self.column5Pos>=500 and self.column5Pos<=550:
                if picture.basketGet.left>=430 and picture.basketGet.left<=520:
                    player.score=player.score+10
                    self.column5=False
                    self.column5Pos=0
        if self.column6==True:
            pygame.draw.rect(background,self.color,pygame.Rect(600,self.column6Pos,15,15))
            self.column6Pos=self.column6Pos+fall.fallSpeed
            if self.column6Pos>=500 and self.column6Pos<=550:
                if picture.basketGet.left>=540 and picture.basketGet.left<=630:
                    player.score=player.score+10
                    self.column6=False
                    self.column6Pos=0
        if self.column7==True:
            pygame.draw.rect(background,self.color,pygame.Rect(700,self.column7Pos,15,15)) 
            self.column7Pos=self.column7Pos+fall.fallSpeed
            if self.column7Pos>=500 and self.column7Pos<=550:
                if picture.basketGet.left>=630 and picture.basketGet.left<=800:
                    player.score=player.score+10
                    self.column7=False
                    self.column7Pos=0
    #判定該掉落的時間
    def fallCheck(self):
        if self.fallTime<=0.02:
             self.appleFall=True
    #讓掉落後的方塊判定改變
    def fallReset(self):
        if self.column1Pos>=600:
            self.column1=False
            self.column1Pos=0
            player.miss=player.miss+1
        if self.column2Pos>=600:
            self.column2=False
            self.column2Pos=0
            player.miss=player.miss+1
        if self.column3Pos>=600:
            self.column3=False
            self.column3Pos=0
            player.miss=player.miss+1
        if self.column4Pos>=600:
            self.column4=False
            self.column4Pos=0
            player.miss=player.miss+1
        if self.column5Pos>=600:
            self.column5=False
            self.column5Pos=0
            player.miss=player.miss+1
        if self.column6Pos>=600:
            self.column6=False
            self.column6Pos=0
            player.miss=player.miss+1
        if self.column7Pos>=600:
            self.column7=False
            self.column7Pos=0    
            player.miss=player.miss+1
fall=Fall()
fall2=Fall()
fall2.color=blue
fall3=Fall()
fall3.color=yellow
#遊戲系統設定
class Game():
    def __init__(self):
        self.running=True
        self.fontScore=pygame.font.SysFont('arial',30)
        self.musicBoomCheck=True
        self.startCheck=True
    #分數顯示
    def point(self):
        self.scoreFont=self.fontScore.render('Score:%d'%(player.score),True,(0,0,0))
        background.blit(self.scoreFont,(0,0))
    #失誤次數顯示
    def miss(self):
        self.missFont=self.fontScore.render('Miss:%d'%(player.miss),True,(0,0,0))
        background.blit(self.missFont,(700,0))
    #遊戲結束時顯示的各種東西
    def gameOver(self):
        if player.miss>=10:
            picture.apple()
            self.loseFont=self.fontScore.render('Push Enter To Restart And Push Escape To Exit',True,(0,0,0))
            background.blit(self.loseFont,(100,0))
            if self.musicBoomCheck==True:
                self.musicBomb='./bomb.mp3'
                pygame.mixer.music.load(self.musicBomb)
                pygame.mixer.music.play()
                self.musicBoomCheck=False
    #重新開始鍵
    def reset(self):
        player.score=0
        player.miss=0
        pygame.mixer.music.load(backMusic)
        pygame.mixer.music.play()
        self.musicBoomCheck=True
        fall.fallTime=2
        fall.fallSpeed=4
        fall.appleColumn=0
        fall.appleFall=False
        fall.column1=False
        fall.column2=False
        fall.column3=False
        fall.column4=False
        fall.column5=False
        fall.column6=False
        fall.column7=False
        fall.column1Pos=0
        fall.column2Pos=0
        fall.column3Pos=0
        fall.column4Pos=0
        fall.column5Pos=0
        fall.column6Pos=0
        fall.column7Pos=0
        fall2.column1Pos=0
        fall2.column2Pos=0
        fall2.column3Pos=0
        fall2.column4Pos=0
        fall2.column5Pos=0
        fall2.column6Pos=0
        fall2.column7Pos=0
        fall3.column1Pos=0
        fall3.column2Pos=0
        fall3.column3Pos=0
        fall3.column4Pos=0
        fall3.column5Pos=0
        fall3.column6Pos=0
        fall3.column7Pos=0
        picture.basketGet.left=350
        self.startCheck=False
    #開始前的說明顯示
    def start(self):
        if self.startCheck==True:
            pygame.mixer.music.stop()
            picture.beforeStart()
game=Game()
#主迴圈速度
clock=pygame.time.Clock() #迴圈速度
#主迴圈
while game.running: 
    clock.tick(100) 
    #事件處理器
    for event in pygame.event.get(): 
        #按下鍵盤
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_ESCAPE: 
                pygame.quit() 
                sys.exit() 
            elif event.key==pygame.K_RIGHT: 
                player.leftRight='right'
                player.right=True 
            elif event.key==pygame.K_LEFT: 
                player.leftRight='left' 
                player.left=True 
            elif event.key==pygame.K_RETURN:
                game.reset()
        #點擊視窗叉叉
        if event.type==QUIT: 
            pygame.quit() 
            sys.exit() 
        #滑鼠點擊
        if event.type==MOUSEBUTTONDOWN:
            x,y=event.pos
            if x<=115 and x>=100 and y>=fall.column1Pos and y<=fall.column1Pos+15:
                player.score=player.score+10
                fall.column1=False
                fall.column1Pos=0
            elif x<=215 and x>=200 and y>=fall.column2Pos and y<=fall.column2Pos+15:
                player.score=player.score+10
                fall.column2=False
                fall.column2Pos=0
            elif x<=315 and x>=300 and y>=fall.column3Pos and y<=fall.column3Pos+15:
                player.score=player.score+10
                fall.column3=False
                fall.column3Pos=0
            elif x<=415 and x>=400 and y>=fall.column4Pos and y<=fall.column4Pos+15:
                player.score=player.score+10
                fall.column4=False
                fall.column4Pos=0
            elif x<=515 and x>=500 and y>=fall.column5Pos and y<=fall.column5Pos+15:
                player.score=player.score+10
                fall.column5=False
                fall.column5Pos=0
            elif x<=615 and x>=600 and y>=fall.column6Pos and y<=fall.column6Pos+15:
                player.score=player.score+10
                fall.column6=False
                fall.column6Pos=0
            elif x<=715 and x>=700 and y>=fall.column7Pos and y<=fall.column7Pos+15:
                player.score=player.score+10
                fall.column7=False
                fall.column7Pos=0
    #籃子移動判定
    if player.leftRight=='left' and player.left==True: #當按下左鍵時 往左移100px
        picture.basketGet.move_ip(-100,0) #內建function move_ip
        player.left=False #把判斷變成False 避免讓籃子無限移動
    elif player.leftRight=='right' and player.right==True: #當按下右鍵時 往右移100px
        picture.basketGet.move_ip(100,0) #內建function move_ip
        player.right=False #把判斷變成False 避免讓籃子無限移動
    #每種顏色的掉落速度
    fall.fallTime=fall.fallTime-0.1
    fall2.fallTime=fall2.fallTime-0.05
    fall3.fallTime=fall3.fallTime-0.02
    fall.fallCheck()
    if fall.appleFall==True:
        fall.chooseFall()
        fall.fallTime=fall.fallSpeed
        fall.appleFall=False
        fall.fallTime=1
    fall.fallStart()
    fall.fallReset()
    #升到第二關
    if player.score>=100:
        fall2.fallCheck()
        if fall2.appleFall==True:
            fall2.chooseFall()
            fall2.fallTime=fall2.fallSpeed
            fall2.appleFall=False
            fall2.fallTime=2
        fall2.fallStart()
        fall2.fallReset()
    #升到第三關
    if player.score>=200:
        fall3.fallCheck()
        if fall3.appleFall==True:
            fall3.chooseFall()
            fall3.fallTime=fall3.fallSpeed
            fall3.appleFall=False
            fall3.fallTime=4
        fall3.fallStart()
        fall3.fallReset()
    #升到第四關
    if player.score==300:
        fall.fallSpeed=fall.fallSpeed+2
        player.score=player.score+10
    #升到第五關
    if player.score==400:
        fall.fallSpeed=fall.fallSpeed+2
        player.score=player.score+10
    #升到第六關
    if player.score==500:
        fall.fallSpeed=fall.fallSpeed+2
        player.score=player.score+10
    #各種遊戲判定
    game.gameOver()
    player.cross() 
    game.start()
    #更新畫面
    pygame.display.update() 
    #顯示圖片
    picture.appleTree() 
    picture.brownBasket() 
    #計算分數與失誤
    game.point()
    game.miss()
    