import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  #練習1

    bg_img2 = pg.transform.flip(bg_img,True,False)#練習8
    kk_img = pg.image.load("fig/3.png")#練習3
    kk_img = pg.transform.flip(kk_img,True,False)#練習5
    kk_rct = kk_img.get_rect()#練習10
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200 #練習５
        sum_mv = [-1,0] #練習9
        key_lst =pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            sum_mv[1] -= 1
        if key_lst[pg.K_DOWN]:
            sum_mv[1] += 1
        if key_lst[pg.K_LEFT]:
            sum_mv[0] -= 1
        if key_lst[pg.K_RIGHT]:
            sum_mv[0] += 2
        kk_rct.move_ip(sum_mv) #練習9
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(bg_img2, [-x+1600, 0]) #練習7
        screen.blit(bg_img, [-x+3200, 0]) #練習7
        screen.blit(kk_img, kk_rct) #練習4
        pg.display.update()
        tmr += 1     
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()