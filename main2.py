import pygame
from pygame.locals import *
import random

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



def game():
    greater = False
    less = False
    redb = 0
    greenb = 0
    geen = False
    ree = False
    x = 0
    y = 70
    ry = 430
    w = 10
    speed = 2
    map1 = True
    map2 = False
    count = 0
    isjump = False
    jumpcount = 6
    visible = True
    row = {}
    row2 = {}
    column = []
    we = 0
    while we < 10:
        if we % 2 == 0:
            row[we * 20] = red
        else:
            row[we * 20] = green
        we += 1
    we = 0
    while we < 10:
        if we % 2 == 0:
            row2[we * 20] = green
        else:
            row2[we * 20] = red
        we += 1
    we = 0
    while we < 5:
        if we % 2 == 0:
            column.append(row)
        else:
            column.append(row2)
        we += 1

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

            if keys[pygame.K_d]:
                    xchange = 2

            if keys[pygame.K_a] and x > 0:
                    xchange = -2

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        DS.fill(blue)

        textsurfacse = myfont.render('Red: {}'.format(redb), False, (0, 0, 0))
        DS.blit(textsurfacse, (0, 0))
        textsurfacses = myfont.render('{}'.format(ree), False, (0, 0, 0))
        DS.blit(textsurfacses, (0, 30))
        pygame.draw.rect(DS, red, (100, 10, 20, 20))
        if 100 + 20 > mouse[0] > 100 and 10 + 20 > mouse[1] > 10:

            if click[0] == 1:
                ree = True

        textsurfaace = myfont.render('Green: {}'.format(greenb), False, (0, 0, 0))
        DS.blit(textsurfaace, (130, 0))
        textsurfaacew = myfont.render('{}'.format(geen), False, (0, 0, 0))
        DS.blit(textsurfaacew, (130, 30))
        pygame.draw.rect(DS, green, (255, 10, 20, 20))
        if 255 + 20 > mouse[0] > 255 and 10 + 20 > mouse[1] > 10:

            if click[0] == 1:
                geen = True


        for key, item in row.items():
            if item == blue:
                if x > key:
                    greater = True
                elif x < key:
                    less = True
                if less is True and greater is True:
                    ychange = 2


        num = 5
        while num < 10:
            if num % 2 == 0:
                for key, item in row.items():
                    pygame.draw.rect(DS, item, (key, num*20 , 20, 20))
            else:
                for k, i in row2.items():
                    pygame.draw.rect(DS, i, (k, num*20,20, 20))
            num += 1

        if isjump is False:
            DS.blit(moveimg, (x, round(y)))
        else:
            pass

        num = 5
        while num < 10:
            if num % 2 == 0:
                for key, item in row.items():
                    if key + 20 > mouse[0] > key and num*20 + 20 > mouse[1] > num*20:
                        if click[0] == 1:
                            row[key] = blue
                            count += 1
                            greenb += 1

                    if key + 20 > mouse[0] > key and num*20 + 20 > mouse[1] > num*20:
                        if click[0] == 1:
                            row[key] = blue
                            count += 1
                            redb += 1
            else:
                for k, i in row2.items():
                    if k + 20 > mouse[0] > k and num*20 + 20 > mouse[1] > num*20:
                        if click[0] == 1:
                            row2[k] = blue
                            count += 1
                            greenb += 1

                    if k + 20 > mouse[0] > k and k + 20 > mouse[1] > k:
                        if click[0] == 1:
                            row2[k] = blue
                            count += 1
                            redb += 1
            num += 1
        # for key, item in row.items():
        #     if item == blue and i == blue:
        #         if greenb > 0 and geen is True:
        #             if key + 20 > mouse[0] > key and k + 20 > mouse[1] > k:
        #                 if click[2] == 1:
        #                     row[key] = green
        #                     count -= 1
        #                     greenb -= 1
        #                     ree = False
        #
        #         elif redb > 0 and ree is True:
        #             if key + 20 > mouse[0] > key and k + 20 > mouse[1] > k:
        #                 if click[2] == 1:
        #                     row[key] = red
        #                     count -= 1
        #                     redb -= 1
        #                     geen = False


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



        x += xchange
        y += ychange


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
    game()