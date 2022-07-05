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

    while True:
        sc_sfc.blit(bgimg_sfc,bg_rect)
        for event in pg.event.get():
            if event.type==pg.QUIT:return

        pg.display.update()
        clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


