import pygame
from pygame.locals import *
import pytmx


dis = (1280, 720)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (9, 120, 236)

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 50)
angelfont = pygame.font.SysFont('Comic Sans MS', 30)
back = [pygame.image.load('assets/male/back/back1.png'), pygame.image.load('assets/male/back/back2.png'),
        pygame.image.load('assets/male/back/back3.png'), pygame.image.load('assets/male/back/back4.png'),
        pygame.image.load('assets/male/back/back5.png'), pygame.image.load('assets/male/back/back6.png'),
        pygame.image.load('assets/male/back/back7.png'), pygame.image.load('assets/male/back/back8.png'),
        pygame.image.load('assets/male/back/back9.png')]
forward = [pygame.image.load('assets/male/forward/forward1.png'), pygame.image.load('assets/male/forward/forward2.png'),
           pygame.image.load('assets/male/forward/forward3.png'), pygame.image.load('assets/male/forward/forward4.png'),
           pygame.image.load('assets/male/forward/forward5.png'), pygame.image.load('assets/male/forward/forward6.png'),
           pygame.image.load('assets/male/forward/forward7.png'), pygame.image.load('assets/male/forward/forward8.png'),
           pygame.image.load('assets/male/forward/forward9.png')]
left = [pygame.image.load('assets/male/left/left1.png'), pygame.image.load('assets/male/left/left2.png'),
        pygame.image.load('assets/male/left/left3.png'), pygame.image.load('assets/male/left/left4.png'),
        pygame.image.load('assets/male/left/left5.png'), pygame.image.load('assets/male/left/left6.png'),
        pygame.image.load('assets/male/left/left7.png'), pygame.image.load('assets/male/left/left8.png'),
        pygame.image.load('assets/male/left/left9.png')]
right = [pygame.image.load('assets/male/right/right1.png'), pygame.image.load('assets/male/right/right2.png'),
         pygame.image.load('assets/male/right/right3.png'), pygame.image.load('assets/male/right/right4.png'),
         pygame.image.load('assets/male/right/right5.png'), pygame.image.load('assets/male/right/right6.png'),
         pygame.image.load('assets/male/right/right7.png'), pygame.image.load('assets/male/right/right8.png'),
         pygame.image.load('assets/male/right/right9.png')]
swordb = [pygame.image.load('assets/male/swordb/swordb1.png'), pygame.image.load('assets/male/swordb/swordb2.png'),
          pygame.image.load('assets/male/swordb/swordb3.png'), pygame.image.load('assets/male/swordb/swordb4.png'),
          pygame.image.load('assets/male/swordb/swordb5.png'), pygame.image.load('assets/male/swordb/swordb6.png')]
swordf = [pygame.image.load('assets/male/swordf/swordf1.png'), pygame.image.load('assets/male/swordf/swordf2.png'),
          pygame.image.load('assets/male/swordf/swordf3.png'), pygame.image.load('assets/male/swordf/swordf4.png'),
          pygame.image.load('assets/male/swordf/swordf5.png'), pygame.image.load('assets/male/swordf/swordf6.png')]
swordl = [pygame.image.load('assets/male/swordl/swordl1.png'), pygame.image.load('assets/male/swordl/swordl2.png'),
          pygame.image.load('assets/male/swordl/swordl3.png'), pygame.image.load('assets/male/swordl/swordl4.png'),
          pygame.image.load('assets/male/swordl/swordl5.png'), pygame.image.load('assets/male/swordl/swordl6.png')]
swordr = [pygame.image.load('assets/male/swordr/swordr1.png'), pygame.image.load('assets/male/swordr/swordr2.png'),
          pygame.image.load('assets/male/swordr/swordr3.png'), pygame.image.load('assets/male/swordr/swordr4.png'),
          pygame.image.load('assets/male/swordr/swordr5.png'), pygame.image.load('assets/male/swordr/swordr6.png')]
heart = [pygame.image.load('assets/heart1.png'), pygame.image.load('assets/heart2.png'),
         pygame.image.load('assets/heart3.png'), pygame.image.load('assets/heart4.png')]
coin = [pygame.image.load('assets/coin1.png'), pygame.image.load('assets/coin2.png'),
        pygame.image.load('assets/coin3.png'), pygame.image.load('assets/coin4.png')]
fire = [pygame.image.load('assets/fire1.png'), pygame.image.load('assets/fire2.png'),
        pygame.image.load('assets/fire3.png'), pygame.image.load('assets/fire4.png'),
        pygame.image.load('assets/fire5.png'), pygame.image.load('assets/fire6.png'),
        pygame.image.load('assets/fire7.png')]
slimeidle = [pygame.image.load('assets/slime/idle/idle1.png'), pygame.image.load('assets/slime/idle/idle2.png'),
             pygame.image.load('assets/slime/idle/idle3.png'), pygame.image.load('assets/slime/idle/idle4.png'),
             pygame.image.load('assets/slime/idle/idle5.png'), pygame.image.load('assets/slime/idle/idle6.png'),
             pygame.image.load('assets/slime/idle/idle7.png'), pygame.image.load('assets/slime/idle/idle8.png'),
             pygame.image.load('assets/slime/idle/idle9.png'), pygame.image.load('assets/slime/idle/idle10.png')]
slimedeath = [pygame.image.load('assets/slime/death/death1.png'), pygame.image.load('assets/slime/death/death2.png'),
             pygame.image.load('assets/slime/death/death3.png'), pygame.image.load('assets/slime/death/death4.png'),
             pygame.image.load('assets/slime/death/death5.png'), pygame.image.load('assets/slime/death/death6.png'),
             pygame.image.load('assets/slime/death/death7.png'), pygame.image.load('assets/slime/death/death8.png'),
             pygame.image.load('assets/slime/death/death9.png'), pygame.image.load('assets/slime/death/death10.png')]
slimeattack =[pygame.image.load('assets/slime/attack/attack1.png'),pygame.image.load('assets/slime/attack/attack2.png'),
             pygame.image.load('assets/slime/attack/attack3.png'), pygame.image.load('assets/slime/attack/attack4.png'),
             pygame.image.load('assets/slime/attack/attack5.png'), pygame.image.load('assets/slime/attack/attack6.png'),
             pygame.image.load('assets/slime/attack/attack7.png'), pygame.image.load('assets/slime/attack/attack8.png'),
             pygame.image.load('assets/slime/attack/attack9.png'),pygame.image.load('assets/slime/attack/attack10.png')]
heartfull = pygame.image.load('assets/heartfull.png')
heartfull = pygame.transform.scale(heartfull, (40, 40))
hearthalf = pygame.image.load('assets/hearthalf.png')
hearthalf = pygame.transform.scale(hearthalf, (40, 40))
heartempty = pygame.image.load('assets/heartempty.png')
heartempty = pygame.transform.scale(heartempty, (40, 40))
coinsign = pygame.transform.scale(coin[0], (40, 40))
angel = pygame.image.load('assets/angel.png')
swordim = pygame.image.load('assets/sword.png')
swordim = pygame.transform.scale(swordim, (40, 40))
w = 0
while w < len(swordl):
    swordl[w] = pygame.transform.flip(swordr[w], True, False)
    w += 1
w = 0
while w < len(fire):
    fire[w] = pygame.transform.scale(fire[w], (30, 30))
    w += 1
w = 0
while w < len(coin):
    if w != 2:
        coin[w] = pygame.transform.scale(coin[w], (20, 15))
    else:
        coin[w] = pygame.transform.scale(coin[w], (10, 15))
    w += 1
w = 0
while w < len(heart):
    heart[w] = pygame.transform.scale(heart[w], (30, 30))
    w += 1
w = 0
while w < len(slimeidle):
    slimeidle[w] = pygame.transform.scale(slimeidle[w], (30, 30))
    w += 1
w = 0
while w < len(slimedeath):
    slimedeath[w] = pygame.transform.scale(slimedeath[w], (30, 30))
    w += 1
w = 0
while w < len(slimeattack):
    slimeattack[w] = pygame.transform.scale(slimeattack[w], (30, 30))
    w += 1

DS = pygame.display.set_mode(dis)
pygame.display.set_caption('Adventure')
gameMap = pytmx.load_pygame('assets/maps/map1.tmx', pixelalpha=True)
gameMap4 = pytmx.load_pygame('assets/maps/map4.tmx', pixelalpha=True)
gameMap3 = pytmx.load_pygame('assets/maps/map2.tmx', pixelalpha=True)

player = {'max_health': 300, 'speed': 3, 'got_sword': False, 'map3': {'enemy': True, 'coin': True, 'straw': True},
          'map1': {'enemy': True, 'coin1': True, 'straw': True, 'health': True, 'coin2': True}}


def game():
    x = 660
    y = 660
    health = 150
    money = 0
    fun_map3(money, health, x, y)


def fun_map3(money, health, x, y):
    health = health
    money = money
    x = x
    y = y
    on_fire = False
    movement = 0
    objectmovement = 0
    swordmovement = 0
    last_move = ''
    up = False
    down = False
    lefts = False
    rights = False
    swordbs = False
    swordfs = False
    swordls = False
    swordrs = False
    time = 0
    if player['got_sword'] is True:
        sword_isvisible = False
    else:
        sword_isvisible = True
    if player['map3']['enemy'] is True:
        enemy = [(500, 150, 0, 0), (600, 200, 0, 0), (900, 220, 0, 0)]
    enemymovement = 0
    being_attack = False
    if player['map3']['straw'] is False:
        straw = True
    else:
        straw = False
    while True:
        move = True
        xchange = 0
        ychange = 0

        if player['map3']['enemy'] is True:
            try:
                if len(enemy) == 0:
                    player['map3']['enemy'] = False
            except:
                pass

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if straw is True:
            for i in gameMap3.layers:
                if i.name == 'strawb':
                    player['map3']['straw'] = False
                    gameMap3.layers.remove(i)
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if player['got_sword'] is True and swordfs is False and swordbs is False and swordrs is False and swordls is False:
            if keys[pygame.K_SPACE]:

                for tile_object in gameMap3.objects:
                    if round(tile_object.y + tile_object.height) + 20 > y + 40 > round(tile_object.y) + 20 and \
                            round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30) \
                            and tile_object.name == 'straw':
                        straw = True

                try:
                    w = 0
                    while w < len(enemy):
                        if enemy[w][1] + 70 > y + 40 > enemy[w][1] - 30 and enemy[w][0] + 70 > x > enemy[w][0] - 30:
                            enemy.remove(enemy[w])
                        w += 1
                except:
                    pass

                if up is True or last_move == 'up':
                    swordfs = False
                    swordbs = True
                    swordls = False
                    swordrs = False
                    up = False
                    last_move = 'up'
                if lefts is True or last_move == 'left':
                    swordbs = False
                    swordfs = False
                    swordls = True
                    swordrs = False
                    lefts = False
                    last_move = 'left'
                if rights is True or last_move == 'right':
                    swordbs = False
                    swordfs = False
                    swordls = False
                    swordrs = True
                    rights = False
                    last_move = 'right'
                if down is True or last_move == 'down':
                    swordbs = False
                    swordfs = True
                    swordls = False
                    swordrs = False
                    down = False
                    last_move = 'down'

        if swordrs is False and swordls is False and swordfs is False and swordbs is False:
            if keys[pygame.K_w]:

                for tile_object in gameMap3.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'change' and tile_object.name != 'sword' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) >= x >= round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 >= y >= round(tile_object.y - 52) + 20:
                            move = False


                if move is True:
                    if up is True:
                        movement += 1
                    up = True
                    down = False
                    rights = False

                    lefts = False
                    ychange = -player['speed']

                else:
                    ychange = player['speed']

            if keys[pygame.K_s]:

                for tile_object in gameMap3.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'change' and tile_object.name != 'sword' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) >= x >= round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 >= y >= round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if down is True:
                        movement += 1
                    down = True
                    up = False
                    rights = False
                    lefts = False
                    ychange = player['speed']
                else:
                    ychange = -player['speed']
            if keys[pygame.K_d]:


                for tile_object in gameMap3.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'change' and tile_object.name != 'sword' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) >= x >= round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 >= y >= round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if rights is True:
                        movement += 1
                    rights = True
                    up = False
                    lefts = False
                    down = False
                    xchange = player['speed']
                else:
                    xchange = -player['speed']
            if keys[pygame.K_a]:
                for tile_object in gameMap3.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'change' and tile_object.name != 'sword' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) >= x >= round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 >= y >= round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if lefts is True:
                        movement += 1
                    lefts = True
                    up = False
                    rights = False
                    down = False
                    xchange = -player['speed']
                else:
                    xchange = player['speed']
        if keys[pygame.K_w] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_w] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0

        if keys[pygame.K_f]:
            if DS.get_flags() & FULLSCREEN:
                pygame.display.set_mode(dis)
            else:
                pygame.display.set_mode(dis, FULLSCREEN)


        for tile_object in gameMap3.objects:
            if tile_object.name == 'change':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    x = 660
                    y = 200
                    fun_map1(money, health, x, y)
            if tile_object.name == 'heart':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    if health != player['max_health']:
                        health += 50
                        heart_visible = False
                        for i in gameMap3.layers:
                            if i.name == 'heart':
                                gameMap3.layers.remove(i)
            if tile_object.name == 'fire':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    if on_fire is False:
                        health -= 50
                        on_fire = True
        if time > 1000 and on_fire is True:
            on_fire = False
            time = 0

        DS.fill(blue)


        x += xchange
        y += ychange

        for layer in gameMap3.visible_layers:
            if straw is False and layer.name != "straw" and player['got_sword'] is False:
                for x2, y2, gid, in layer:
                    tile = gameMap3.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap3.tilewidth), (y2 * gameMap3.tileheight)))
            if straw is False and player['got_sword'] is True:
                for x2, y2, gid, in layer:
                    tile = gameMap3.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap3.tilewidth), (y2 * gameMap3.tileheight)))
            if layer.name != "straw" and straw is True and player['got_sword'] is True:
                for x2, y2, gid, in layer:
                    tile = gameMap3.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap3.tilewidth), (y2 * gameMap3.tileheight)))

        if sword_isvisible is True:
            DS.blit(swordim, (600, 350))

        if movement >= 14:
            movement = 0
        if swordmovement >= 12:
            swordmovement = 0
            swordfs = False
            swordbs = False
            swordls = False
            swordrs = False

        if objectmovement >= 28:
            objectmovement = 0

            # if coin1_isvisble is True:
            #     DS.blit(coin[objectmovement // 7], (150, 170))
            # if coin2_isvisble is True:
            #     DS.blit(coin[objectmovement // 7], (1100, 140))
            # if heart_visible is True:
            #     DS.blit(heart[objectmovement // 7], (1220, 350))

        if up is True:
            DS.blit(back[movement // 2], (x, round(y)))
        elif down is True:
            DS.blit(forward[movement // 2], (x, round(y)))
        elif lefts is True:
            DS.blit(left[movement // 2], (x, round(y)))
        elif rights is True:
            DS.blit(right[movement // 2], (x, round(y)))
        elif swordbs is True:
            DS.blit(swordb[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordls is True:
            if swordmovement // 2 == 1 or swordmovement // 2 == 2 or swordmovement // 2 == 3:
                DS.blit(swordl[swordmovement // 2], (x, round(y)))
            if swordmovement // 2 == 0 or swordmovement // 2 == 4 or swordmovement // 2 == 5:
                DS.blit(swordl[swordmovement // 2], (x - 57, round(y)))
            swordmovement += 1
        elif swordrs is True:
            DS.blit(swordr[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordfs is True:
            DS.blit(swordf[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        else:
            if last_move == 'up':
                DS.blit(back[0], (x, round(y)))
            elif last_move == 'down':
                DS.blit(forward[0], (x, round(y)))
            elif last_move == 'left':
                DS.blit(left[0], (x, round(y)))
            elif last_move == 'right':
                DS.blit(right[0], (x, round(y)))
            else:
                DS.blit(back[0], (x, round(y)))

        if player['got_sword'] is True:
            enemymove = True
            try:
                w = 0

                while w < len(enemy):
                    for tile_object in gameMap3.objects:
                        if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                           and tile_object.name != 'change' and tile_object.name != 'sword' and tile_object.name != 'fire':
                            if tile_object.x + tile_object.width > enemy[w][0] > tile_object.x and \
                               tile_object.y + tile_object.height + 20 > enemy[w][1] > tile_object.y + 20:
                                enemy[w] = (enemy[w][0] - 1, enemy[w][1], enemy[w][2], enemy[w][3])
                                enemymove = False
                            if tile_object.x + tile_object.width == enemy[w][0] == tile_object.x and \
                                    tile_object.y + tile_object.height + 20 == enemy[w][1] == tile_object.y + 20:
                                print("efefe")
                    w += 1

                w = 0
                while w < len(enemy):
                    if enemymove is True:
                        if x < enemy[w][0]:
                            enemy[w] = (enemy[w][0], enemy[w][1], -(player['speed'] - 1), enemy[w][3])
                        if x > enemy[w][0]:
                            enemy[w] = (enemy[w][0], enemy[w][1], (player['speed'] - 1), enemy[w][3])
                        if y < enemy[w][1]:
                            enemy[w] = (enemy[w][0], enemy[w][1], enemy[w][2], -(player['speed'] - 1))
                        if y > enemy[w][1]:
                            enemy[w] = (enemy[w][0], enemy[w][1], enemy[w][2], (player['speed'] - 1))
                    w += 1
                if enemymove is False:
                    enemy[w] = (enemy[w][0], enemy[w][1], 0, 0)

                w = 0
                while w < len(enemy):
                    enemy[w] = (enemy[w][0] + enemy[w][2], enemy[w][1], enemy[w][2], enemy[w][3])
                    w += 1
                w = 0
                while w < len(enemy):
                    enemy[w] = (enemy[w][0], enemy[w][1] + enemy[w][3], enemy[w][2], enemy[w][3])
                    w += 1

                w = 0
                while w < len(enemy):
                    if y + 35 > enemy[w][1] + 5 > y and x + 30 > enemy[w][0] + 5 > x:
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        if being_attack is False:
                            health += -50
                            being_attack = True
                    else:
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                    w += 1
            except:
                pass

        if health == 300:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartfull, (200, 40))
        elif health == 250:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(hearthalf, (200, 40))
        elif health == 200:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 150:
            DS.blit(heartfull, (100, 40))
            DS.blit(hearthalf, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 100:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 50:
            DS.blit(hearthalf, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 0:
            pass
            # end()

        DS.blit(coinsign, (1050, 40))
        textsurface = myfont.render('{}'.format(money), False, (0, 0, 0))
        DS.blit(textsurface, (1100, 22))

        dt = clock.tick()
        if on_fire is True and being_attack is True:
            time += dt
        for tile_object in gameMap3.objects:
            if tile_object.name == 'sword':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    player['got_sword'] = True
                    sword_isvisible = False
                    while True:
                        for event in pygame.event.get():

                            if event.type == QUIT:
                                pygame.quit()
                                quit()
                        keyss = pygame.key.get_pressed()
                        if keyss[pygame.K_SPACE]:
                            break
                        DS.blit(angel, (520, 350))
                        textsurface = angelfont.render("Those who are able to wield that sword", False, (43, 86, 226))
                        DS.blit(textsurface, (400, 240))
                        textsurfaces = angelfont.render("must remove the curse plaguing this land.", False, (43, 86, 226))
                        DS.blit(textsurfaces, (400, 270))
                        textsurfacee = angelfont.render("Press the space bar to swing it.", False, (43, 86, 226))
                        DS.blit(textsurfacee, (400, 300))
                        pygame.display.update()
                        clock.tick(60)

                    for i in gameMap3.layers:
                        if i.name == 'sword':
                            gameMap3.layers.remove(i)
                    pygame.time.wait(1000)

        objectmovement += 1
        pygame.display.update()
        clock.tick(60)

def fun_map4(money, health, x, y):
    health = health
    money = money
    x = x
    y = y
    on_fire = False
    movement = 0
    objectmovement = 0
    swordmovement = 0
    last_move = ''
    up = False
    down = False
    lefts = False
    rights = False
    swordbs = False
    swordfs = False
    swordls = False
    swordrs = False
    time = 0
    while True:
        move = True
        xchange = 0
        ychange = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if player['got_sword'] is True and swordfs is False and swordbs is False and swordrs is False and swordls is False:
            if keys[pygame.K_SPACE]:

                if up is True or last_move == 'up':
                    swordfs = False
                    swordbs = True
                    swordls = False
                    swordrs = False
                    up = False
                    last_move = 'up'
                if lefts is True or last_move == 'left':
                    swordbs = False
                    swordfs = False
                    swordls = True
                    swordrs = False
                    lefts = False
                    last_move = 'left'
                if rights is True or last_move == 'right':
                    swordbs = False
                    swordfs = False
                    swordls = False
                    swordrs = True
                    rights = False
                    last_move = 'right'
                if down is True or last_move == 'down':
                    swordbs = False
                    swordfs = True
                    swordls = False
                    swordrs = False
                    down = False
                    last_move = 'down'

        if swordrs is False and swordls is False and swordfs is False and swordbs is False:
            if keys[pygame.K_w]:

                for tile_object in gameMap4.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x > round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if up is True:
                        movement += 1
                    up = True
                    down = False
                    rights = False

                    lefts = False
                    ychange = -player['speed']

                else:
                    ychange = 0
            if keys[pygame.K_s]:


                for tile_object in gameMap4.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x > round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if down is True:
                        movement += 1
                    down = True
                    up = False
                    rights = False
                    lefts = False
                    ychange = player['speed']
                else:
                    ychange = 0
            if keys[pygame.K_d]:


                for tile_object in gameMap4.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x > round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if rights is True:
                        movement += 1
                    rights = True
                    up = False
                    lefts = False
                    down = False
                    xchange = player['speed']
                else:
                    xchange = 0
            if keys[pygame.K_a]:


                for tile_object in gameMap4.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x > round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y - 52) + 20:
                            move = False

                if move is True:
                    if lefts is True:
                        movement += 1
                    lefts = True
                    up = False
                    rights = False
                    down = False
                    xchange = -player['speed']
                else:
                    xchange = 0
        if keys[pygame.K_w] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_w] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0

        if keys[pygame.K_f]:
            if DS.get_flags() & FULLSCREEN:
                pygame.display.set_mode(dis)
            else:
                pygame.display.set_mode(dis, FULLSCREEN)

        for tile_object in gameMap.objects:
            if tile_object.name == 'map2':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    x = 8
            if tile_object.name == 'heart':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    if health != player['max_health']:
                        health += 50
                        heart_visible = False
                        for i in gameMap4.layers:
                            if i.name == 'heart':
                                gameMap4.layers.remove(i)
            if tile_object.name == 'fire':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):

                    if on_fire is False:
                        health -= 50
                        on_fire = True
        if time > 1000 and on_fire is True:
            on_fire = False
            time = 0

        DS.fill(blue)

        x += xchange
        y += ychange

        for layer in gameMap4.visible_layers:
                for x2, y2, gid, in layer:
                    tile = gameMap4.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap4.tilewidth), (y2 * gameMap4.tileheight)))

        if movement >= 14:
            movement = 0
        if swordmovement >= 12:
            swordmovement = 0
            swordfs = False
            swordbs = False
            swordls = False
            swordrs = False

        if objectmovement >= 28:
            objectmovement = 0

        if up is True:
            DS.blit(back[movement // 2], (x, round(y)))
        elif down is True:
            DS.blit(forward[movement // 2], (x, round(y)))
        elif lefts is True:
            DS.blit(left[movement // 2], (x, round(y)))
        elif rights is True:
            DS.blit(right[movement // 2], (x, round(y)))
        elif swordbs is True:
            DS.blit(swordb[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordls is True:
            if swordmovement // 2 == 1 or swordmovement // 2 == 2 or swordmovement // 2 == 3:
                DS.blit(swordl[swordmovement // 2], (x, round(y)))
            if swordmovement // 2 == 0 or swordmovement // 2 == 4 or swordmovement // 2 == 5:
                DS.blit(swordl[swordmovement // 2], (x - 57, round(y)))
            swordmovement += 1
        elif swordrs is True:
            DS.blit(swordr[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordfs is True:
            DS.blit(swordf[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        else:
            if last_move == 'up':
                DS.blit(back[0], (x, round(y)))
            elif last_move == 'down':
                DS.blit(forward[0], (x, round(y)))
            elif last_move == 'left':
                DS.blit(left[0], (x, round(y)))
            elif last_move == 'right':
                DS.blit(right[0], (x, round(y)))
            else:
                DS.blit(back[0], (x, round(y)))

        if health == 300:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartfull, (200, 40))
        elif health == 250:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(hearthalf, (200, 40))
        elif health == 200:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 150:
            DS.blit(heartfull, (100, 40))
            DS.blit(hearthalf, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 100:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 50:
            DS.blit(hearthalf, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 0:
            pass
            # end()

        DS.blit(coinsign, (1050, 40))
        textsurface = myfont.render('{}'.format(money), False, (0, 0, 0))
        DS.blit(textsurface, (1100, 22))

        dt = clock.tick()
        if on_fire is True:
            time += dt
        objectmovement += 1
        pygame.display.update()
        clock.tick(60)

def fun_map1(money, health, x, y):
    health = health
    money = money
    x = x
    y = y
    if player['map1']['health'] is True:
        heart_visible = True
    else:
        heart_visible = False

    if player['map1']['coin1'] is True:
        coin1_isvisble = True
    else:
        coin1_isvisble = False
    if player['map1']['coin2'] is True:

        coin2_isvisble = True
    else:

        coin2_isvisble = False
    on_fire = False
    movement = 0
    objectmovement = 0
    swordmovement = 0
    last_move = ''
    if player['map1']['straw'] is True:
        map1straw = False
    else:
        map1straw = True
    up = False
    down = False
    lefts = False
    rights = False
    swordbs = False
    swordfs = False
    swordls = False
    swordrs = False
    time = 0
    enemymovement = 0
    if player['got_sword'] is True:
        enemy = [(650, 600, 0, 0), (950, 300, 0, 0), (950, 600, 0, 0)]
    being_attack = False
    while True:
        move = True
        enemymove = False
        xchange = 0
        ychange = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        try:
            if len(enemy) == 0:
                player['map1']['enemy'] = False
        except:
            pass
        if map1straw is True:
            for i in gameMap.layers:
                if i.name == 'strawb':
                    gameMap.layers.remove(i)
                    player['map1']['straw'] = False

        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if player['got_sword'] is True and swordfs is False and swordbs is False and swordrs is False and swordls is False:
            if keys[pygame.K_SPACE]:
                for tile_object in gameMap.objects:
                    if round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y) + 20 and \
                            round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30) \
                            and tile_object.name == 'straw':
                        map1straw = True
                try:
                    w = 0
                    while w < len(enemy):
                        if enemy[w][1] + 70 > y + 40 > enemy[w][1] - 30 and enemy[w][0] + 70 > x > enemy[w][0] - 30:
                            enemy.remove(enemy[w])
                        w += 1
                except:
                    pass
                if up is True or last_move == 'up':
                    swordfs = False
                    swordbs = True
                    swordls = False
                    swordrs = False
                    up = False
                    last_move = 'up'
                if lefts is True or last_move == 'left':
                    swordbs = False
                    swordfs = False
                    swordls = True
                    swordrs = False
                    lefts = False
                    last_move = 'left'
                if rights is True or last_move == 'right':
                    swordbs = False
                    swordfs = False
                    swordls = False
                    swordrs = True
                    rights = False
                    last_move = 'right'
                if down is True or last_move == 'down':
                    swordbs = False
                    swordfs = True
                    swordls = False
                    swordrs = False
                    down = False
                    last_move = 'down'

        if swordrs is False and swordls is False and swordfs is False and swordbs is False:
            if keys[pygame.K_w]:

                for tile_object in gameMap.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y) + 20 and \
                                round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                            move = False

                if move is True:
                    if up is True:
                        movement += 1
                    up = True
                    down = False
                    rights = False

                    lefts = False
                    ychange = -player['speed']

                else:
                    ychange = 0
            if keys[pygame.K_s]:

               for tile_object in gameMap.objects:
                   if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                           and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                       if round(tile_object.y + tile_object.height) + 20 > y + 45 > round(tile_object.y) + 20 and \
                               round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                           move = False

               if move is True:
                   if down is True:
                       movement += 1
                   down = True
                   up = False
                   rights = False
                   lefts = False
                   ychange = player['speed']
               else:
                   ychange = 0
            if keys[pygame.K_d]:

                for tile_object in gameMap.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x + 30 > round(tile_object.x) and \
                                round(tile_object.y + tile_object.height) + 20 > y > round(tile_object.y - 45) + 20:
                            move = False
                if move is True:
                    if rights is True:
                        movement += 1
                    rights = True
                    up = False
                    lefts = False
                    down = False
                    xchange = player['speed']
                else:
                    xchange = 0
            if keys[pygame.K_a]:

                for tile_object in gameMap.objects:
                    if tile_object.name != 'straw' and tile_object.name != 'coin' and tile_object.name != 'heart' \
                            and tile_object.name != 'map2' and tile_object.name != 'map3' and tile_object.name != 'fire':
                        if round(tile_object.x + tile_object.width) > x > round(tile_object.x) and \
                                round((tile_object.y + 20) + tile_object.height) > y > round(tile_object.y - 45) + 20:
                            move = False
                if move is True:
                    if lefts is True:
                        movement += 1
                    lefts = True
                    up = False
                    rights = False
                    down = False
                    xchange = -player['speed']
                else:
                    xchange = 0
        if keys[pygame.K_w] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_d]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_w] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0
        if keys[pygame.K_s] and keys[pygame.K_a]:
            xchange = 0
            ychange = 0

        if keys[pygame.K_f]:
            if DS.get_flags() & FULLSCREEN:
                pygame.display.set_mode(dis)
            else:
                pygame.display.set_mode(dis, FULLSCREEN)

        if keys[pygame.K_r]:
            game()

        for tile_object in gameMap.objects:
            if tile_object.name == 'map2':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    x = 8
                    fun_map4(money, health, x, y)
            if tile_object.name == 'map3':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    x = 600
                    y = 570
                    fun_map3(money, health, x, y)

            if tile_object.name == 'heart':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    if health != player['max_health']:
                        health += 50
                        heart_visible = False
                        for i in gameMap.layers:
                            if i.name == 'heart':
                                gameMap.layers.remove(i)
                                player['map1']['health'] = False
            if tile_object.name == 'fire':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):

                    if on_fire is False:
                        health -= 50
                        on_fire = True

            if tile_object.name == 'coin1':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    money += 100
                    for i in gameMap.layers:
                        if i.name == 'coin1':
                            gameMap.layers.remove(i)
                            coin1_isvisble = False
                            player['map1']['coin1'] = False
            if tile_object.name == 'coin2':
                if round(tile_object.y + tile_object.height) + 20 > y + 52 > round(tile_object.y) + 20 and \
                        round(tile_object.x + tile_object.width) > x > round(tile_object.x - 30):
                    money += 100
                    for i in gameMap.layers:
                        if i.name == 'coin2':
                            gameMap.layers.remove(i)
                            coin2_isvisble = False
                            player['map1']['coin2'] = False


        if time > 1000 and on_fire is True:
            on_fire = False
            time = 0

        DS.fill(blue)

        x += xchange
        y += ychange

        for layer in gameMap.visible_layers:
            if map1straw is False:
                for x2, y2, gid, in layer:
                    tile = gameMap.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap.tilewidth), (y2 * gameMap.tileheight)))
            if layer.name != "straw" and map1straw is True:
                for x2, y2, gid, in layer:
                    tile = gameMap.get_tile_image_by_gid(gid)
                    if tile is not None:
                        DS.blit(tile, ((x2 * gameMap.tilewidth), (y2 * gameMap.tileheight)))

        if movement >= 14:
            movement = 0
        if swordmovement >= 12:
            swordmovement = 0
            swordfs = False
            swordbs = False
            swordls = False
            swordrs = False

        if objectmovement >= 28:
            objectmovement = 0
        if enemymovement >= 70:
            enemymovement = 0

        DS.blit(fire[objectmovement // 4], (600, 300))
        DS.blit(fire[objectmovement // 4], (600, 400))
        DS.blit(fire[objectmovement // 4], (710, 300))
        DS.blit(fire[objectmovement // 4], (710, 400))
        if coin1_isvisble is True:
            DS.blit(coin[objectmovement // 7], (150, 170))
        if coin2_isvisble is True:
            DS.blit(coin[objectmovement // 7], (1100, 140))
        if heart_visible is True:
            DS.blit(heart[objectmovement // 7], (1220, 350))

        if up is True:
            #pygame.draw.rect(DS, black, (x, y, 30, 45))
            DS.blit(back[movement // 2], (x, round(y)))
        elif down is True:
            #pygame.draw.rect(DS, black, (x, y, 30, 45))
            DS.blit(forward[movement // 2], (x, round(y)))

        elif lefts is True:
            #pygame.draw.rect(DS, black, (x, y, 30, 45))
            DS.blit(left[movement // 2], (x, round(y)))

        elif rights is True:
            #pygame.draw.rect(DS, black, (x, y, 30, 45))
            DS.blit(right[movement // 2], (x, round(y)))

        elif swordbs is True:
            DS.blit(swordb[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordls is True:
            if swordmovement // 2 == 1 or swordmovement // 2 == 2 or swordmovement // 2 == 3:
                DS.blit(swordl[swordmovement // 2], (x, round(y)))
            if swordmovement // 2 == 0 or swordmovement // 2 == 4 or swordmovement // 2 == 5:
                DS.blit(swordl[swordmovement // 2], (x - 57, round(y)))
            swordmovement += 1
        elif swordrs is True:
            DS.blit(swordr[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        elif swordfs is True:
            DS.blit(swordf[swordmovement // 2], (x, round(y)))
            swordmovement += 1
        else:
            if last_move == 'up':
                DS.blit(back[0], (x, round(y)))

            elif last_move == 'down':
                DS.blit(forward[0], (x, round(y)))
            elif last_move == 'left':
                DS.blit(left[0], (x, round(y)))
            elif last_move == 'right':
                DS.blit(right[0], (x, round(y)))
            else:
                DS.blit(back[0], (x, round(y)))
        if player['got_sword'] is True:
            try:
                w = 0
                while w < len(enemy):
                    if x < enemy[w][0] + 300 and y < enemy[w][1] + 300:
                        enemymove = True
                    else:
                        enemymove = False
                    w += 1

                w = 0
                while w < len(enemy):
                    if enemymove is True:
                        if x < enemy[w][0]:
                            enemy[w] = (enemy[w][0], enemy[w][1], -(player['speed'] - 1), enemy[w][3])
                        if x > enemy[w][0]:
                            enemy[w] = (enemy[w][0], enemy[w][1], (player['speed'] - 1), enemy[w][3])
                        if y < enemy[w][1]:
                            enemy[w] = (enemy[w][0], enemy[w][1], enemy[w][2], -(player['speed'] - 1))
                        if y > enemy[w][1]:
                            enemy[w] = (enemy[w][0], enemy[w][1], enemy[w][2], (player['speed'] - 1))
                    w += 1
                if enemymove is False:
                    enemy[w] = (enemy[w][0], enemy[w][1], 0, 0)

                w = 0
                while w < len(enemy):
                    enemy[w] = (enemy[w][0] + enemy[w][2], enemy[w][1], enemy[w][2], enemy[w][3])
                    w += 1
                w = 0
                while w < len(enemy):
                    enemy[w] = (enemy[w][0], enemy[w][1] + enemy[w][3], enemy[w][2], enemy[w][3])
                    w += 1

                w = 0
                while w < len(enemy):
                    if y + 35 > enemy[w][1] + 5 > y and x + 30 > enemy[w][0] + 5 > x:
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeattack[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        if being_attack is False:
                            health += -50
                            being_attack = True
                    else:
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                        DS.blit(slimeidle[enemymovement // 10], (enemy[w][0], enemy[w][1]))
                    w += 1
            except:
                pass

        if time > 1000 and being_attack is True:
            being_attack = False
            time = 0

        if health == 300:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartfull, (200, 40))
        elif health == 250:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(hearthalf, (200, 40))
        elif health == 200:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartfull, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 150:
            DS.blit(heartfull, (100, 40))
            DS.blit(hearthalf, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 100:
            DS.blit(heartfull, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 50:
            DS.blit(hearthalf, (100, 40))
            DS.blit(heartempty, (150, 40))
            DS.blit(heartempty, (200, 40))
        elif health == 0:
            pass
            # end()

        # for tile_object in gameMap.objects:
        #     if tile_object.name == 'fire':
        #         pygame.draw.rect(DS, red, (tile_object.x, tile_object.y+20, tile_object.width, tile_object.height))
        #     if tile_object.name == 'coin':
        #         pygame.draw.rect(DS, red, (tile_object.x, tile_object.y+20, tile_object.width, tile_object.height))
        #     if tile_object.name == 'wall':
        #         pygame.draw.rect(DS, red, (tile_object.x, tile_object.y+20, tile_object.width, tile_object.height))
        #     if tile_object.name == 'change':
        #         pygame.draw.rect(DS, red, (tile_object.x, tile_object.y+20, tile_object.width, tile_object.height))
        #     if tile_object.name == 'breakable':
        #         pygame.draw.rect(DS, red, (tile_object.x, tile_object.y+20, tile_object.width, tile_object.height))

        DS.blit(coinsign, (1050, 40))
        textsurface = myfont.render('{}'.format(money), False, (0, 0, 0))
        DS.blit(textsurface, (1100, 22))

        dt = clock.tick()
        if on_fire is True or being_attack is True:
            time += dt
        objectmovement += 1
        enemymovement += 1
        pygame.display.update()
        pygame.display.set_caption("{:.2f} fps".format(clock.get_fps()))
        clock.tick(120)


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
        pygame.display.set_caption("{:.2f}".format(clock.get_fps()))
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game()
