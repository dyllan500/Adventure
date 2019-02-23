import pygame
from pygame.locals import *
import random
import socket
import threading

host = "127.0.0.1"
port = 5051
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
buffer = 6400
num = "p1"

maps = {"map1":True, "map2":False}

def setup():
    if num == "p2":
        cThread = threading.Thread(target=send)
        cThread.daemon = True
        cThread.start()
        game(2)
    elif num == "p1":
        cThread = threading.Thread(target=send)
        cThread.daemon = True
        cThread.start()
        game(1)
    else:
        cThread = threading.Thread(target=send)
        cThread.daemon = True
        cThread.start()
        game(1)

def p2w(x2, y2, m):
    x2 = x2
    y2 = y2
    if maps[m] is True:
        DS.blit(moveimg, (x2, round(y2)))
        pygame.display.update()
    elif maps[m] is False:
        pass


def send():
    x2 = 126
    y2 = 60
    m = ''
    while True:
        cThread = threading.Thread(target=p2w, args=(x2,y2,m))
        cThread.daemon = True
        try:
            p2 = s.recv(buffer)
            p2 = p2.decode("utf-8")
            data = p2.split(',')
            x2 = int(data[0])
            y2 = int(data[1])
            m = str(data[2])
            if m == '':
                m = 'map1'
            elif m == 'map1126':
                m = 'map1'

            cThread.start()
        except:
            pass



center = 7
index = 0
display_x = 544
display_y = 433
dis = (600, 600)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (9, 120, 236)

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

moveimg = pygame.image.load('pinkiemove.png')
jumpimg = pygame.image.load('Pallet.png')
Route1 = pygame.image.load('Route1.png')

DS = pygame.display.set_mode(dis)
pygame.display.set_caption('Pinkie Run')

def game(playernum):
    playnum = playernum
    x = 126
    y = 60
    ry = 430
    w = 10
    speed = 2

    isjump = False
    jumpcount = 6

    while True:
        xchange = 0

        ychange = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if isjump is False:

            if keys[pygame.K_SPACE]:
                isjump = True
            if keys[pygame.K_w] and y > -10:
                if maps['map1'] is True and y < 65 and not (x > 266 and x < 305):
                    ychange = 0
                else:
                    ychange = -2

            if keys[pygame.K_s] and y + 30 < 650:
                if maps['map1'] is True and y + 30 > 356:
                    ychange = 0
                else:
                    ychange = 2

            if keys[pygame.K_d] and x + 32 < 650:
                if maps['map1'] is True and y < 60 and x < 305:
                    xchange = 0
                elif maps['map1'] is True and x > 402:
                    xchange = 0
                elif maps['map2'] is True and x > 402:
                    xchange = 0
                else:
                    xchange = 2

            if keys[pygame.K_a]:
                if maps['map1'] is True and y < 60 and x > 266:
                    xchange = 0
                elif maps['map1'] is True and x < 107:
                    xchange = 0
                elif maps['map2'] is True and x < 107:
                    xchange = 0
                else:
                    xchange = -2

        if isjump is True:

            if jumpcount >= -6:
                neg = 1

                if jumpcount < 0:
                    neg = -1
                y -= (jumpcount ** 2) * .2 * neg
                jumpcount -= .3

            else:
                isjump = False
                jumpcount = 6


        DS.fill(blue)

        x += xchange
        y += ychange
        if maps['map1'] is True:
            DS.blit(jumpimg, (0, 0))
        if maps['map1'] is True and y < 0:
            maps['map1'] = False
            maps['map2'] = True
            y = 609
        if maps['map2'] is True:
            DS.blit(Route1, (0, 0))
        if maps['map2'] is True and y > 610:
            maps['map1'] = True
            maps['map2'] = False
            y = 0

        if isjump is False:
            DS.blit(moveimg, (x, round(y)))
        else:
            pass
        if maps['map1'] is True:
            s.send((str(x) + "," + str(y) + "," + "map1").encode("utf-8"))
        elif maps['map2'] is True:
            s.send((str(x) + "," + str(y) + "," + "map2").encode("utf-8"))



        pygame.display.update()
        clock.tick(60)


def end():

    while True:

        textsurface = myfont.render('Game Over', False, (0, 0, 0))
        DS.blit(textsurface, (320, 160))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(DS, green, (280, 220, 110, 30))
        textsurfacea = myfont.render('Restart', False, (0, 0, 0))
        DS.blit(textsurfacea, (280, 213))

        if 280 + 100 > mouse[0] > 280 and 220 + 30 > mouse[1] > 220:

            if click[0] == 1:
                game()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    setup()