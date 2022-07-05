import pygame as pg
import sys
import random
import time
import pygame.mixer


def main():
    #練習1
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    sc_sfc=pg.display.set_mode((1600,900)) #Surface
    sc_rect=sc_sfc.get_rect() #Rect
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rect=bgimg_sfc.get_rect()
    sc_sfc.blit(bgimg_sfc, bgimg_rect)

    kkimg_sfc=pg.image.load("fig/6.png") #Surface
    kkimg_sfc=pg.transform.rotozoom(kkimg_sfc,0,2.0) #Surface
    kkimg_rect=kkimg_sfc.get_rect() #Rect
    kkimg_rect.center=900,400
    sc_sfc.blit(kkimg_sfc, kkimg_rect)

    pg.mixer.init(frequency=44100) #BGMを読み込む
    pg.mixer.music.load("ONGEN.mp3")
    pg.mixer.music.play(1)
    #練習5
    bmimg_sfc=pg.Surface((20,20)) #Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rect=bmimg_sfc.get_rect()
    bmimg_rect.centerx=random.randint(0,sc_rect.width)
    bmimg_rect.centery=random.randint(0,sc_rect.height)
    sc_sfc.blit(bgimg_sfc,bmimg_rect)
    vx,vy=+1,+1
    font = pg.font.Font(None, 300)
    conf_font =  pg.font.Font(None, 100)
    conflict=0

    while True:
        sc_sfc.blit(bgimg_sfc,bgimg_rect)
        text2 = conf_font.render(f"{conflict}conflicts", True, (255,255,255))
        sc_sfc.blit(text2, [0,0])
    #練習2
        for event in pg.event.get():
            if event.type==pg.QUIT:return

        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]==True: kkimg_rect.centery-=1
        if key_states[pg.K_DOWN]==True: kkimg_rect.centery+=1
        if key_states[pg.K_LEFT]==True: kkimg_rect.centerx-=1
        if key_states[pg.K_RIGHT]==True: kkimg_rect.centerx+=1      

        if check_bound(kkimg_rect,sc_rect)!=(1,1):
            if key_states[pg.K_UP]==True: kkimg_rect.centery+=1
            if key_states[pg.K_DOWN]==True: kkimg_rect.centery-=1
            if key_states[pg.K_LEFT]==True: kkimg_rect.centerx+=1
            if key_states[pg.K_RIGHT]==True: kkimg_rect.centerx-=1 


        
        sc_sfc.blit(kkimg_sfc,kkimg_rect)
        bmimg_rect.move_ip(vx,vy) 
        sc_sfc.blit(bmimg_sfc,bmimg_rect)
        yoko,tate=check_bound(bmimg_rect,sc_rect)
        vx*=yoko
        vy*=tate
        

        if kkimg_rect.colliderect(bmimg_rect):
            text = font.render("GAME OVER", True, (255,0,0))   # 描画する文字列の設定
            sc_sfc.blit(text, [200,300])
            pg.display.update()
            vx=0
            vy=0
            time.sleep(5)
            return


        pg.display.update()
        clock.tick(1000)



def check_bound(rct, scr_rct):#Rect, Rect
    #画面内: +1 画面外:-1
    yoko,tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right:yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate= -1
    return yoko,tate

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


