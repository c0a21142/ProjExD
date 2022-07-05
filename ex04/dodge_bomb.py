import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    sc_sfc=pg.display.set_mode((1600,900)) #Surface
    sc_rect=sc_sfc.get_rect() #Rect
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg") #Surface
    bg_rect=bgimg_sfc.get_rect()
    sc_sfc.blit(bgimg_sfc, bg_rect)

    kkimg_sfc=pg.image.load("fig/6.png") #Surface
    kkimg_sfc=pg.transform.rotozoom(kkimg_sfc,0,2.0) #Surface
    kkimg_rect=kkimg_sfc.get_rect() #Rect
    kkimg_rect.center=900,400

    while True:
        sc_sfc.blit(bgimg_sfc,bg_rect)
        sc_sfc.blit(kkimg_sfc,kkimg_rect)
        for event in pg.event.get():
            if event.type==pg.QUIT:return

        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]==True: kkimg_rect.centery-=1
        if key_states[pg.K_DOWN]==True: kkimg_rect.centery+=1
        if key_states[pg.K_LEFT]==True: kkimg_rect.centerx-=1
        if key_states[pg.K_RIGHT]==True: kkimg_rect.centerx+=1            
        pg.display.update()
        clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


