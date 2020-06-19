import pygame
import time
import sys
from pygame.locals import *
#重置pygame
pygame.init()
#設定視窗
background=pygame.display.set_mode((600,600))
#設定視窗標題
pygame.display.set_caption('時機很重')
#顏色列表
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
#障礙物的行動
class Block():
    def __init__(self):
        #每一列每一排的位置
        self.blockPosX=[57,100,157,237,250,327,447,487,557]
        self.blockPosy=[57,117,177,237,297,357,417,477,537]
        self.blockPosx=[57,117,177,237,297,357,417,477,537]
        self.blockPosY=[27,197,107,297,207,357,497,417,507]
        #撞到邊緣往回走的判定
        self.changeX=[True,False,True,False,True,False,True,False,True,False]
        self.changeY=[False,True,False,True,False,True,False,True,False,True]
        #障礙物速度
        self.speedX=0.1
        self.speedY=0.1
    #直向行動的障礙物
    def blockColumn(self,blockPosX,blockPosY,numX,numY):
        pygame.draw.rect(background,blue,pygame.Rect(blockPosX,blockPosY,5,5))
        if self.blockPosY[numY]>=595:
            self.changeY[numY]=True
        elif self.blockPosY[numY]<=0:
            self.changeY[numY]=False
        if self.changeY[numY]==True:
            self.blockPosY[numY]=self.blockPosY[numY]-self.speedY
        elif self.changeY[numY]==False:
            self.blockPosY[numY]=self.blockPosY[numY]+self.speedY
    #橫向移動的障礙物  
    def blockRow(self,blockPosX,blockPosY,numX,numY):
        pygame.draw.rect(background,blue,pygame.Rect(blockPosX,blockPosY,5,5))
        if self.blockPosX[numX]>=595:
            self.changeX[numX]=True
        elif self.blockPosX[numX]<=0:
            self.changeX[numX]=False
        if self.changeX[numX]==True:
            self.blockPosX[numX]=self.blockPosX[numX]-self.speedX
        elif self.changeX[numX]==False:
            self.blockPosX[numX]=self.blockPosX[numX]+self.speedX
block=Block()
#有關藝術的東西都在這
class Picture():
    def __init__(self):
        #背景的白色
        self.pictureWhite='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\white.png'
        self.whiteGet=pygame.image.load(self.pictureWhite).convert()
        #文字的設定
        self.font=pygame.font.SysFont('arial',30)
        #背景音樂
        self.japanMusic='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\japanMusic.mp3'
        #過關圖片
        self.pictureWin='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\win.jpg'
        self.winGet=pygame.image.load(self.pictureWin).convert()
        #過關音樂
        self.clapMusic='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\clap.mp3'
        #失敗音樂
        self.bombMusic='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\clap1.mp3'
        #開始前的規則說明
        self.pictureBefore='D:\Myfile\Engineering\PYTHON學習\實作 拉不拉多鄧不利多\遊戲練習3\white2.png'
        self.beforeGet=pygame.image.load(self.pictureBefore).convert()
    #把圖片音樂函數寫在這 以便畫面更新
    def white(self):
        background.blit(self.whiteGet,(0,0))
    def win(self):
        background.blit(self.winGet,(125,250))
    def winText(self):
        self.fontWin=self.font.render('LOLOLOLOLOL!!!!!!!!!!!!GOD!!!!!!!!!!!!LOLOLOLOLOL',True,(0,0,0))
        background.blit(self.fontWin,(0,0))
    def loseText(self):
        self.fontLose=self.font.render('Push Enter To Exit Or Push Esc To Restart',True,(0,0,0))
        background.blit(self.fontLose,(30,150))
    def levelUp(self):
        self.fontLevel=self.font.render('Level%d'%(game.level),True,(0,0,0))
        background.blit(self.fontLevel,(270,270))
    def startMusic(self):
        pygame.mixer.music.load(self.japanMusic)
        pygame.mixer.music.play()
    def winMusic(self):
        pygame.mixer.music.load(self.clapMusic)
        pygame.mixer.music.play()
    def loseMusic(self):
        pygame.mixer.music.load(self.bombMusic)
        pygame.mixer.music.play()
    def before(self):
        background.blit(self.beforeGet,(0,0))
picture=Picture()
#有關遊玩者的資料都在這
class Player():
    def __init__(self):
        #遊戲者初始位置
        self.posX=545
        self.posY=545
        #終點初始位置
        self.destinationX=5
        self.destinationY=5
        #判定贏
        self.win=False
        #判定輸
        self.lose=False
        #判定是否開始
        self.start=False
    #終點的位置畫面
    def destination(self):
        pygame.draw.rect(background,green,pygame.Rect(self.destinationX,self.destinationY,50,50))
    #遊戲者的位置畫面
    def userMove(self):    
        pygame.draw.rect(background,red,pygame.Rect(self.posX,self.posY,50,50))
    #讓遊戲者不能超出邊邊
    def line(self):
        if self.posX>=545:
            self.posX=545
        if self.posY>=545:
            self.posY=545
        if self.posX<=5:
            self.posX=5
        if self.posY<=5:
            self.posY=5
player=Player()
#跟遊戲系統有關的都在這
class Game():
    def __init__(self):
        #執行主迴圈(while)判定
        self.running=True
        #關卡數
        self.level=1
        #判定關卡文字的出現(2秒 因為迴圈速度1秒100次)
        self.countPictureLevel=2
        #判定是否播放音樂
        self.musicCheck=True
        #第五關的重置判定
        self.level5=False
    #遊戲者處發的事件
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                #判定ESC鍵
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #判定右鍵
                if event.key==pygame.K_RIGHT:
                    player.posX=player.posX+30
                #判定左鍵
                if event.key==pygame.K_LEFT:
                    player.posX=player.posX-30
                #判定上鍵
                if event.key==pygame.K_UP:
                    player.posY=player.posY-30
                #判定下鍵
                if event.key==pygame.K_DOWN:
                    player.posY=player.posY+30
                #判定ENTER鍵
                if event.key==pygame.K_RETURN:
                    self.reset()
            #判定是否按了叉叉
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    #遊戲者跟終點有關的資訊
    def reach(self):
        #判定是否碰到終點
        if player.posX==player.destinationX and player.posY==player.destinationY:
            #增加關卡數
            self.level=self.level+1
            #讓關卡數出現的判別
            self.countPictureLevel=2
            #障礙物加速
            block.speedX=block.speedX+0.05
            block.speedY=block.speedY+0.05
            #到了第三關 重新播放音樂
            #if self.level==3:
            #    picture.startMusic()
        #讓關卡數出現
        if self.countPictureLevel>=0:
            picture.levelUp()
            self.countPictureLevel=self.countPictureLevel-0.01
        #判定終點位置 奇數的話在左上角 偶數在右下角
        if self.level%2==1:
            player.destinationX=5
            player.destinationY=5
        elif self.level%2==0:
            player.destinationX=545
            player.destinationY=545
    #遊戲者跟障礙物有關的資訊
    def bump(self):
        for x in range(9):
            for y in range(9):
                #關卡數在5以內時的障礙物(列)
                if self.level<5:   
                    #直著走
                    block.blockColumn(block.blockPosx[x],block.blockPosY[y],x,y)
                    #判定是否撞到(這個刪掉就無敵了)
                    if block.blockPosY[y]>=player.posY and block.blockPosY[y]<=player.posY+50 and block.blockPosx[x]>=player.posX and block.blockPosx[x]<=player.posX+50:
                        player.lose=True
                        #第五關重置障礙物位子
                        if self.level5==False:
                            self.blockPosX=[57,100,157,237,250,327,447,487,557]
                            self.blockPosy=[57,117,177,237,297,357,417,477,537]
                            self.blockPosx=[57,117,177,237,297,357,417,477,537]
                            self.blockPosY=[27,197,107,297,207,357,497,417,507]
                            self.changeX=[True,False,True,False,True,False,True,False,True,False]
                            self.changeY=[False,True,False,True,False,True,False,True,False,True]
                            #讓這裡不再被執行
                            self.level5=True
                #關卡5時的變化
                elif self.level>=5:
                    #把速度調回來
                    block.speedX=0.1
                    block.speedY=0.1
                    #斜著走
                    block.blockColumn(block.blockPosX[x],block.blockPosY[y],x,y)
                    #判定是撞到障礙物的判定稍微改一下
                    if block.blockPosY[y]>=player.posY and block.blockPosY[y]<=player.posY+50 and block.blockPosX[x]>=player.posX and block.blockPosX[x]<=player.posX+50:
                        player.lose=True
                        #第五關重置障礙物位子
                        if self.level5==False:
                            self.blockPosX=[57,100,157,237,250,327,447,487,557]
                            self.blockPosy=[57,117,177,237,297,357,417,477,537]
                            self.blockPosx=[57,117,177,237,297,357,417,477,537]
                            self.blockPosY=[27,197,107,297,207,357,497,417,507]
                            self.changeX=[True,False,True,False,True,False,True,False,True,False]
                            self.changeY=[False,True,False,True,False,True,False,True,False,True]
                            #讓這裡不再被執行
                            self.level5=True
        for m in range(9):
            for n in range(9):
                #關卡樹在5以內時的障礙物(行)
                if self.level<5:
                    #直著走    
                    block.blockRow(block.blockPosX[m],block.blockPosy[n],m,n)
                    #判定是否撞到(這個刪掉就無敵了)
                    if block.blockPosX[n]>=player.posX and block.blockPosX[n]<=player.posX+50 and block.blockPosy[m]>=player.posY and block.blockPosy[m]<=player.posY+50:
                        player.lose=True 
                #關卡5時的變化
                elif self.level>=5:
                    #斜著走(速度上面調過了)
                    block.blockRow(block.blockPosX[m],block.blockPosY[n],m,n)
                    #判定是撞到障礙物的判定稍微改一下
                    if block.blockPosX[n]>=player.posX and block.blockPosX[n]<=player.posX+50 and block.blockPosY[m]>=player.posY and block.blockPosY[m]<=player.posY+50:
                        player.lose=True 
                
    #重新開始的設定
    def reset(self):
        #音樂重新播放
        picture.startMusic()
        #終點位置重置
        player.destinationX=5
        player.destinationY=5
        #遊戲者位置重置
        player.posX=545
        player.posY=545
        #關卡重置
        self.level=1
        #關卡文字出現判定重置
        self.countPictureLevel=2
        #判定贏重置
        player.win=False
        #判定是否播音樂重置
        self.musicCheck=True
        #判定輸重置
        player.lose=False
        #判定開始重置
        player.start=True
        #重置障礙物位置
        block.blockPosX=[57,100,157,237,250,327,447,487,557]
        block.blockPosy=[57,117,177,237,297,357,417,477,537]
        block.blockPosx=[57,117,177,237,297,357,417,477,537]
        block.blockPosY=[27,197,107,297,207,357,497,417,507]
        #重置撞到邊緣往回走的判定
        block.changeX=[True,False,True,False,True,False,True,False,True,False]
        block.changeY=[False,True,False,True,False,True,False,True,False,True]
    #當玩家贏了或輸了
    def over(self):
        #第5關過了就贏了
        if self.level>5:
            #顯示過關文字
            picture.winText()
            #顯示過關圖片
            picture.win()
            #判定贏
            player.win=True
            #判定贏音樂播放(只播一次)
            if self.musicCheck==True:
                picture.winMusic()
                self.musciCheck=False
        #碰到障礙物輸了
        elif player.lose==True:
            #顯示失敗文字
            picture.loseText()
            #判定失敗音樂播放(只播一次)
            if self.musicCheck==True:
                picture.loseMusic()
                self.musicCheck=False
game=Game()
#迴圈的速度
clock=pygame.time.Clock()
#主迴圈(上面寫的到這裡才用到)
while game.running==True:
    #設定讓他1秒跑100次
    clock.tick(100)
    game.event() 
    picture.white()
    #判定輸 贏 開始
    if player.win==False and player.lose==False and player.start==True:
        player.destination()
        game.reach() 
        player.userMove() 
        game.bump()
        player.line()
    #判定開始 沒開始就顯示字很醜的那張圖 
    elif player.start==False:
        picture.before()
    game.over()
    #更新圖片畫面
    pygame.display.flip()