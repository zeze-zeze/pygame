#https://read01.com/zh-tw/GR0xnG.html#.WcPJAcgjFPY
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('自己做的無聊遊戲')
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf=pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()
    
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
            
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
            
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
            
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
            self.rect.left=self.rect.left+5
            
        if self.rect.left<=0:
            self.rect.left=0
        elif self.rect.right>=800:
            self.rect.right=800
        elif self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=600:
            self.rect.bottom=600            

player=Player()
  
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type==QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(player.surf,player.rect)
        pressed_keys=pygame.key.get_pressed()
        player.update(pressed_keys)
        pygame.display.update()






