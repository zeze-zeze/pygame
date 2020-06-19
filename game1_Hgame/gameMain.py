#參考網址
#https://books.google.com.tw/books?id=whYqDwAAQBAJ&pg=SA16-PA15&lpg=SA16-PA15&dq=pygame+screen+blit+%E5%88%9D%E5%A7%8B%E4%BD%8D%E7%BD%AE&source=bl&ots=A7nAPY9e12&sig=HP-xTqUTJIY8MTInfuVtPfJwqzw&hl=zh-TW&sa=X&ved=0ahUKEwi3k_-2iLnWAhWBoJQKHb9JALYQ6AEILDAB#v=onepage&q=pygame%20screen%20blit%20%E5%88%9D%E5%A7%8B%E4%BD%8D%E7%BD%AE&f=false
#http://m.jb51.net/article/66437.htm
#https://read01.com/zh-tw/GR0xnG.html#.WcPJAcgjFPY
#http://python.jobbole.com/83525/

#file: gameMain.py
# -*- coding: utf-8 -*-
import pygame
import random
import time
import os
from pygame.locals import *
from sys import *
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('衝阿!為了少子化!')

#顏色
red=pygame.Color(255,0,0)

#香腸圖片
pictureDick='dick.jpg'
dick=pygame.image.load(pictureDick).convert()

#背景音樂 XDD
musicFuck='fuck.mp3'
pygame.mixer.music.load(musicFuck)
pygame.mixer.music.play()

#金子
class Sperm():
    def __init__(self):
        self.pictureSperm='sperm_right.png'
        self.coveredSperm=pygame.image.load(self.pictureSperm).convert_alpha()
        self.spermGet=self.coveredSperm.get_rect()
    def spermDirection(self,head):
        self.pictureSperm=head
        self.coveredSperm=pygame.image.load(self.pictureSperm).convert_alpha()
sperm=Sperm()

#玩家和食物資訊          
class Player():
    screen.blit(dick,(0,0))
    def __init__(self):
        self.direction='right'
        self.change=self.direction
        self.foodPos=[random.randrange(200,500),random.randrange(200,400)]
        self.foodExist=True
        self.score=0
        self.speed=1
    def drawFood(self):
        pygame.draw.rect(screen,red,pygame.Rect(self.foodPos[0],self.foodPos[1],10,10))
player=Player()

#遊戲的程序  
class Game():
    def __init__(self):
        self.pictureMouth='mouth.jpg'
        self.coveredMouth=pygame.image.load(self.pictureMouth).convert()
        self.musicHighlight='highlight.mp3'
        self.mouthExist=False
        self.pictureMission='mission.png'
        self.coveredMission=pygame.image.load(self.pictureMission).convert()
        self.missionComplete=False
        self.pictureMissionFailed='missionFailed.png'
        self.coveredMissionFailed=pygame.image.load(self.pictureMissionFailed).convert()
        self.count=15
        self.timeUp=False
        self.musicMissionFailed='musicMissionFailed.mp3'
        self.failedMusicPlay=1
    #達到過關條件之後出現嘴巴
    def scoreReach(self):        
        self.mouthGet=self.coveredMouth.get_rect()
        screen.blit(self.coveredMouth,(350,20))
    
    #從頭開始
    def reset(self):
        player.direction='right'
        player.change=player.direction
        player.score=0
        player.speed=1
        sperm.spermGet.left=400
        sperm.spermGet.top=300
        pygame.mixer.music.load(musicFuck)
        pygame.mixer.music.play()
        pygame.display.flip()
        self.mouthExist=False
        self.missionComplete=False
        self.count=15
        self.timeUp=False
    def gameStart(self):
        a=0
    
    #遊戲完整結束
    def allOver(self):
        self.missionGet=self.coveredMission.get_rect()
        screen.blit(self.coveredMission,(0,0))

    def gameOver(self):
        #遊戲通關音樂
        pygame.mixer.music.load(self.musicHighlight)
        pygame.mixer.music.play()    
    def Failed(self):
        print('1')
        self.missionFailedGet=self.coveredMissionFailed.get_rect()
        screen.blit(self.coveredMissionFailed,(0,0))
    def failedMusic(self):
        pygame.mixer.music.load(self.musicMissionFailed)
        pygame.mixer.music.play()
game=Game()

#各種顯示文字
class Text():
    def __init__(self):
        self.font=pygame.font.SysFont('arial',30)
    #顯示分數
    def scoreText(self):
        self.scoreFont=self.font.render('SCORE:%d'%(player.score),True,(0,0,0))
        screen.blit(self.scoreFont,(0,0))
    #結束後的提醒文字
    def gameOverText(self):
        self.gameOverFont=self.font.render('Push Enter To restart Or Push ESC To Exit',True,(0,0,0))
        screen.blit(self.gameOverFont,(170,0))
    #顯示計時
    def countTime(self):
        self.timeFont=self.font.render('%d'%(game.count),True,(0,0,0))
        screen.blit(self.timeFont,(700,0))
text=Text()

#障礙物
#class Block():

#金子初始
sperm.spermGet.left=400
sperm.spermGet.top=300
pygame.display.flip()

#迴圈速度
clock=pygame.time.Clock()

#主迴圈 
while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            #控制精子方向
            if event.key==pygame.K_UP:
                player.change='up'
            if event.key==pygame.K_DOWN:
                player.change='down'
            if event.key==pygame.K_RIGHT:
                player.change='right'
            if event.key==pygame.K_LEFT:
                player.change='left'
            if event.key==pygame.K_RETURN:
                game.reset()
        
        elif event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    #預防超線
    if sperm.spermGet.left<=80:
        sperm.spermGet.left=80
    elif sperm.spermGet.right>=710:
        sperm.spermGet.right=710
    elif sperm.spermGet.top<=20:
        sperm.spermGet.top=20   
    elif sperm.spermGet.bottom>=550:
        sperm.spermGet.bottom=550

    #金子的方向
    if player.change=='up' :
        player.direction='up'
    elif player.change=='down':
        player.direction='down'
    elif player.change=='right':
        player.direction='right'
    elif player.change=='left' :
        player.direction='left'
    
    #金子的移動和圖片變更和偵測有沒有吃到食物
    if player.direction=='up':
        sperm.spermGet.move_ip(0,player.speed*-1)
        sperm.spermDirection('sperm_up.png')
        if sperm.spermGet.top==player.foodPos[1] and sperm.spermGet.left+12<=player.foodPos[0] and sperm.spermGet.left+26>=player.foodPos[0]:
            player.foodExist=False
            player.score=player.score+10
            player.speed=player.speed+0.5
    elif player.direction=='down':
        sperm.spermGet.move_ip(0,player.speed)
        sperm.spermDirection('sperm_down.png')
        if sperm.spermGet.top+45==player.foodPos[1] and sperm.spermGet.left+12<=player.foodPos[0] and sperm.spermGet.left+26>=player.foodPos[0]:
            player.foodExist=False
            player.score=player.score+10
            player.speed=player.speed+0.5
    elif player.direction=='right':
        sperm.spermGet.move_ip(player.speed,0)
        sperm.spermDirection('sperm_right.png')
        if sperm.spermGet.left+45==player.foodPos[0] and sperm.spermGet.top+12<=player.foodPos[1] and sperm.spermGet.top+26>=player.foodPos[1]:
            player.foodExist=False
            player.score=player.score+10      
            player.speed=player.speed+0.5  
    elif player.direction=='left':
        sperm.spermGet.move_ip(player.speed*-1,0)
        sperm.spermDirection('sperm_left.png')
        if sperm.spermGet.left==player.foodPos[0] and sperm.spermGet.top+12<=player.foodPos[1] and sperm.spermGet.top+26>=player.foodPos[1]:
            player.foodExist=False
            player.score=player.score+10
            player.speed=player.speed+0.5

    #食物的出現
    if game.mouthExist==False:
        player.drawFood()
    if player.foodExist==False:
        player.foodPos=[random.randrange(200,500),random.randrange(200,400)]
        player.foodExist=True

    #終點出現
    if player.score>=30:
        game.mouthExist=True
        if game.mouthExist==True:    
            game.scoreReach()
        #碰到終點
        if sperm.spermGet.left+19<=420 and sperm.spermGet.left+19>=360 and sperm.spermGet.top+5<=90 and sperm.spermGet.top+5>=30 and game.mouthExist==True:
            game.gameOver()
            game.mouthExist=False
            game.missionComplete=True

    #贏了
    screen.blit(sperm.coveredSperm,sperm.spermGet)
    if game.missionComplete==True:
        game.count=999
        game.allOver()
        text.gameOverText()
        
    #計時和時間到了
    if game.count>=0:    
        game.count=game.count-0.01
        if game.count<=0.01:
            game.timeUp=True
            game.failedMusicPlay=game.failedMusicPlay-1
    if game.timeUp==True:
        game.Failed() 
        text.gameOverText() 
        if game.failedMusicPlay==0:
            game.failedMusic()  
    
    pygame.display.flip()
    #顯示背景圖片
    screen.blit(dick,(0,0))
    
    #顯示分數
    text.scoreText()

    #顯示時間
    text.countTime()
    
    
        
        