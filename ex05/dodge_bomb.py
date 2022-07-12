import pygame as pg
import sys
import random
import time
import pygame.mixer


class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode((wh))      # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)
    def attack(self):
        return Shot(self)


class Bomb:
    def __init__(self, color, size, vxy, scr):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self,scr):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Shot: #追加機能4
    def __init__(self,chr:Bird):
        self.sfc=pg.image.load("fig/beam.png")
        self.sfc=pg.transform(self.sfc,0,0.1)
        self.rct.midright=chr.rct.center
    
    def blit(self,scr):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr):
        self.rct.move_ip(+10,0)
        if check_bound(self.rct,scr.rct)!=(1,1):
            del self
        self.blit(scr)

class Addfunction: 
    def __init__(self):
        self.speed = 1.5
        self.conflict = 0
        self.font= pg.font.Font(None, 300)
        self.conf_font = pg.font.Font(None, 100)
    def show_conflict(self,screen, bombs):
        for _ in bombs:
            x, y = check_bound(screen.rect, _.rect)
            if (x, y) != (1,1):
                self.conflict+=1

        text2 = self.conf_font.render(f"{self.conflict}conflicts", True, (255,255,255)) # 描画する
        screen.disp.blit(text2, [0,0])# 文字列の表示位置

    def GameOver(self,scr): #追加機能その1
        text2 = self.font.render("GAME OVER", True, (255,0,0)) # 描画する文字列の設定
        self.blit(scr)# 文字列の表示位置
        pg.display.update()
        time.sleep(5)

    def speedup(self, screen, bombs): #追加機能その2
        for _ in bombs:
            x, y = check_bound(screen.rect, _.rect)
            if (x, y) != (1,1):
                _.vx *= x*self.speed #yoko
                _.vy *= -y*self.speed #tate
class Add2:
    def __init__(self):
        pass
class Add3:
    def __init__(self):
        pass



def main():
    pg.mixer.init(frequency=44100) #追加機能その3
    pg.mixer.music.load("ONGEN.mp3")
    pg.mixer.music.play(-1)
    time.sleep(1000)
    pg.mixer.stop()
    clock = pg.time.Clock()
    check_Add=Addfunction()
    scr=Screen("逃げろ!こうかとん",(1600,900),"fig/pg_bg.jpg")
    kkt=Bird("fig/6.png",2.0,(900,400))
    bkd=Bomb((255,0,0),10,(+1,+1),scr)



    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                beam=kkt.attack()
        kkt.update(scr)

        bkd.update(scr)
        beam.update(scr)    
        if kkt.rct.colliderect(bkd.rct)!=0:
            check_Add.GameOver(scr)
        
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()