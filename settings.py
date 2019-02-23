import pygame as pg

WHITE = (255, 255, 255)
BLACK = (66, 64, 64)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (37, 219, 46)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKGREEN = (34, 132, 39)

MENU_MUSIC = 'assets/sounds/menu.wav'
STRAW_MUSIC = 'assets/sounds/straw.wav'
CAVE_MUSIC = 'assets/sounds/cave.wav'
LAKE_MUSIC = 'assets/sounds/lake.ogg'
MOB_DEATH = 'assets/sounds/mobdeath.wav'
PLAYER_DEATHS = 'assets/sounds/die.wav'
SWING = 'assets/sounds/swing.wav'
FOOTSTEP = 'assets/sounds/footstep.ogg'

WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Adventure"
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

fighting = 'assets/male/sword.png'
SPEED = 100
PLAYER_FOR = ['assets/male/back/back1.png', 'assets/male/back/back2.png', 'assets/male/back/back3.png',
              'assets/male/back/back4.png', 'assets/male/back/back5.png', 'assets/male/back/back6.png',
              'assets/male/back/back7.png', 'assets/male/back/back8.png', 'assets/male/back/back9.png']
PLAYER_BACK = ['assets/male/forward/forward1.png', 'assets/male/forward/forward2.png',
               'assets/male/forward/forward3.png', 'assets/male/forward/forward4.png',
               'assets/male/forward/forward5.png', 'assets/male/forward/forward6.png',
               'assets/male/forward/forward7.png', 'assets/male/forward/forward8.png',
               'assets/male/forward/forward9.png']
PLAYER_LEFT = ['assets/male/left/left1.png', 'assets/male/left/left2.png', 'assets/male/left/left3.png',
               'assets/male/left/left4.png', 'assets/male/left/left5.png', 'assets/male/left/left6.png',
               'assets/male/left/left7.png', 'assets/male/left/left8.png', 'assets/male/left/left9.png']
PLAYER_RIGHT = ['assets/male/right/right1.png', 'assets/male/right/right2.png', 'assets/male/right/right3.png',
                'assets/male/right/right4.png', 'assets/male/right/right5.png', 'assets/male/right/right6.png',
                'assets/male/right/right7.png', 'assets/male/right/right8.png', 'assets/male/right/right9.png']
PLAYER_DEATH = ['assets/male/death/death1.png', 'assets/male/death/death2.png', 'assets/male/death/death3.png',
                'assets/male/death/death4.png', 'assets/male/death/death5.png', 'assets/male/death/death6.png']
SWORD_LEFT = ['assets/male/swordl/swordl4.png', 'assets/male/swordl/swordl5.png', 'assets/male/swordl/swordl6.png']
SWORD_RIGHT = ['assets/male/swordr/swordr4.png', 'assets/male/swordr/swordr5.png', 'assets/male/swordr/swordr6.png']
SWORD_BACK = ['assets/male/swordf/swordf4.png', 'assets/male/swordf/swordf5.png', 'assets/male/swordf/swordf6.png']
SWORD_FOR = ['assets/male/swordb/swordb4.png', 'assets/male/swordb/swordb5.png', 'assets/male/swordb/swordb6.png']
BOW_FOR = ['assets/male/bow/forward/forward1.png', 'assets/male/bow/forward/forward2.png',
           'assets/male/bow/forward/forward3.png', 'assets/male/bow/forward/forward4.png',
           'assets/male/bow/forward/forward5.png', 'assets/male/bow/forward/forward6.png',
           'assets/male/bow/forward/forward7.png', 'assets/male/bow/forward/forward8.png',
           'assets/male/bow/forward/forward9.png', 'assets/male/bow/forward/forward10.png',
           'assets/male/bow/forward/forward11.png', 'assets/male/bow/forward/forward12.png',
           'assets/male/bow/forward/forward13.png']
BOW_BACK = ['assets/male/bow/back/back1.png', 'assets/male/bow/back/back2.png', 'assets/male/bow/back/back3.png',
            'assets/male/bow/back/back4.png', 'assets/male/bow/back/back5.png', 'assets/male/bow/back/back6.png',
            'assets/male/bow/back/back7.png', 'assets/male/bow/back/back8.png', 'assets/male/bow/back/back9.png',
            'assets/male/bow/back/back10.png', 'assets/male/bow/back/back11.png', 'assets/male/bow/back/back12.png',
            'assets/male/bow/back/back13.png']
BOW_LEFT = ['assets/male/bow/left/left1.png', 'assets/male/bow/left/left2.png', 'assets/male/bow/left/left3.png',
            'assets/male/bow/left/left4.png', 'assets/male/bow/left/left5.png', 'assets/male/bow/left/left6.png',
            'assets/male/bow/left/left7.png', 'assets/male/bow/left/left8.png', 'assets/male/bow/left/left9.png',
            'assets/male/bow/left/left10.png', 'assets/male/bow/left/left11.png', 'assets/male/bow/left/left12.png',
            'assets/male/bow/left/left13.png']
BOW_RIGHT = ['assets/male/bow/right/right1.png', 'assets/male/bow/right/right2.png', 'assets/male/bow/right/right3.png',
             'assets/male/bow/right/right4.png', 'assets/male/bow/right/right5.png', 'assets/male/bow/right/right6.png',
             'assets/male/bow/right/right7.png', 'assets/male/bow/right/right8.png', 'assets/male/bow/right/right9.png',
             'assets/male/bow/right/right10.png', 'assets/male/bow/right/right11.png', 'assets/male/bow/right/right12.png',
             'assets/male/bow/right/right13.png']

HELMAT_FOR = ['assets/male/helmat/back/back1.png', 'assets/male/helmat/back/back2.png', 'assets/male/helmat/back/back3.png',
              'assets/male/helmat/back/back4.png', 'assets/male/helmat/back/back5.png', 'assets/male/helmat/back/back6.png',
              'assets/male/helmat/back/back7.png', 'assets/male/helmat/back/back8.png', 'assets/male/helmat/back/back9.png']
HELMAT_BACK = ['assets/male/helmat/forward/forward1.png', 'assets/male/helmat/forward/forward2.png',
               'assets/male/helmat/forward/forward3.png', 'assets/male/helmat/forward/forward4.png',
               'assets/male/helmat/forward/forward5.png', 'assets/male/helmat/forward/forward6.png',
               'assets/male/helmat/forward/forward7.png', 'assets/male/helmat/forward/forward8.png',
               'assets/male/helmat/forward/forward9.png']
HELMAT_LEFT = ['assets/male/helmat/left/left1.png', 'assets/male/helmat/left/left2.png', 'assets/male/helmat/left/left3.png',
               'assets/male/helmat/left/left4.png', 'assets/male/helmat/left/left5.png', 'assets/male/helmat/left/left6.png',
               'assets/male/helmat/left/left7.png', 'assets/male/helmat/left/left8.png', 'assets/male/helmat/left/left9.png']
HELMAT_RIGHT = ['assets/male/helmat/right/right1.png', 'assets/male/helmat/right/right2.png', 'assets/male/helmat/right/right3.png',
                'assets/male/helmat/right/right4.png', 'assets/male/helmat/right/right5.png', 'assets/male/helmat/right/right6.png',
                'assets/male/helmat/right/right7.png', 'assets/male/helmat/right/right8.png', 'assets/male/helmat/right/right9.png']
HELMAT_DEATH = ['assets/male/helmat/death/death1.png', 'assets/male/helmat/death/death2.png', 'assets/male/helmat/death/death3.png',
                'assets/male/helmat/death/death4.png', 'assets/male/helmat/death/death5.png', 'assets/male/helmat/death/death6.png']
HELMAT_SWORDL = ['assets/male/helmat/swordl/swordl4.png', 'assets/male/helmat/swordl/swordl5.png', 'assets/male/helmat/swordl/swordl6.png']
HELMAT_SWORDR = ['assets/male/helmat/swordr/swordr4.png', 'assets/male/helmat/swordr/swordr5.png', 'assets/male/helmat/swordr/swordr6.png']
HELMAT_SWORDB = ['assets/male/helmat/swordf/swordf4.png', 'assets/male/helmat/swordf/swordf5.png', 'assets/male/helmat/swordf/swordf6.png']
HELMAT_SWORDF = ['assets/male/helmat/swordb/swordb4.png', 'assets/male/helmat/swordb/swordb5.png', 'assets/male/helmat/swordb/swordb6.png']
HELMAT_BOW_FOR = ['assets/male/bow/forward/forward1.png', 'assets/male/bow/forward/forward2.png',
           'assets/male/bow/hforward/hforward3.png', 'assets/male/bow/hforward/hforward4.png',
           'assets/male/bow/hforward/hforward5.png', 'assets/male/bow/hforward/hforward6.png',
           'assets/male/bow/hforward/hforward7.png', 'assets/male/bow/hforward/hforward8.png',
           'assets/male/bow/hforward/hforward9.png', 'assets/male/bow/hforward/hforward10.png',
           'assets/male/bow/hforward/hforward11.png', 'assets/male/bow/hforward/hforward12.png',
           'assets/male/bow/hforward/hforward13.png']
HELMAT_BOW_BACK = ['assets/male/bow/hback/hback1.png', 'assets/male/bow/hback/hback2.png', 'assets/male/bow/hback/hback3.png',
            'assets/male/bow/hback/hback4.png', 'assets/male/bow/hback/hback5.png', 'assets/male/bow/hback/hback6.png',
            'assets/male/bow/hback/hback7.png', 'assets/male/bow/hback/hback8.png', 'assets/male/bow/hback/hback9.png',
            'assets/male/bow/hback/hback10.png', 'assets/male/bow/hback/hback11.png', 'assets/male/bow/hback/hback12.png',
            'assets/male/bow/hback/hback13.png']
HELMAT_BOW_LEFT = ['assets/male/bow/hleft/hleft1.png', 'assets/male/bow/hleft/hleft2.png', 'assets/male/bow/hleft/hleft3.png',
            'assets/male/bow/hleft/hleft4.png', 'assets/male/bow/hleft/hleft5.png', 'assets/male/bow/hleft/hleft6.png',
            'assets/male/bow/hleft/hleft7.png', 'assets/male/bow/hleft/hleft8.png', 'assets/male/bow/hleft/hleft9.png',
            'assets/male/bow/hleft/hleft10.png', 'assets/male/bow/hleft/hleft11.png', 'assets/male/bow/hleft/hleft12.png',
            'assets/male/bow/hleft/hleft13.png']
HELMAT_BOW_RIGHT = ['assets/male/bow/hright/hright1.png', 'assets/male/bow/hright/hright2.png', 'assets/male/bow/hright/hright3.png',
             'assets/male/bow/hright/hright4.png', 'assets/male/bow/hright/hright5.png', 'assets/male/bow/hright/hright6.png',
             'assets/male/bow/hright/hright7.png', 'assets/male/bow/hright/hright8.png', 'assets/male/bow/hright/hright9.png',
             'assets/male/bow/hright/hright10.png', 'assets/male/bow/hright/hright11.png', 'assets/male/bow/hright/hright12.png',
             'assets/male/bow/hright/hright13.png']

PANTS_FOR = ['assets/male/pants/back/back1.png', 'assets/male/pants/back/back2.png', 'assets/male/pants/back/back3.png',
             'assets/male/pants/back/back4.png', 'assets/male/pants/back/back5.png', 'assets/male/pants/back/back6.png',
             'assets/male/pants/back/back7.png', 'assets/male/pants/back/back8.png', 'assets/male/pants/back/back9.png']
PANTS_BACK = ['assets/male/pants/forward/forward1.png', 'assets/male/pants/forward/forward2.png',
              'assets/male/pants/forward/forward3.png', 'assets/male/pants/forward/forward4.png',
              'assets/male/pants/forward/forward5.png', 'assets/male/pants/forward/forward6.png',
              'assets/male/pants/forward/forward7.png', 'assets/male/pants/forward/forward8.png',
              'assets/male/pants/forward/forward9.png']
PANTS_LEFT = ['assets/male/pants/left/left1.png', 'assets/male/pants/left/left2.png', 'assets/male/pants/left/left3.png',
              'assets/male/pants/left/left4.png', 'assets/male/pants/left/left5.png', 'assets/male/pants/left/left6.png',
              'assets/male/pants/left/left7.png', 'assets/male/pants/left/left8.png', 'assets/male/pants/left/left9.png']
PANTS_RIGHT = ['assets/male/pants/right/right1.png', 'assets/male/pants/right/right2.png', 'assets/male/pants/right/right3.png',
               'assets/male/pants/right/right4.png', 'assets/male/pants/right/right5.png', 'assets/male/pants/right/right6.png',
               'assets/male/pants/right/right7.png', 'assets/male/pants/right/right8.png', 'assets/male/pants/right/right9.png']
PANTS_DEATH = ['assets/male/pants/death/death1.png', 'assets/male/pants/death/death2.png', 'assets/male/pants/death/death3.png',
               'assets/male/pants/death/death4.png', 'assets/male/pants/death/death5.png', 'assets/male/pants/death/death6.png']
PANTS_SWORDL = ['assets/male/pants/swordl/swordl4.png', 'assets/male/pants/swordl/swordl5.png', 'assets/male/pants/swordl/swordl6.png']
PANTS_SWORDR = ['assets/male/pants/swordr/swordr4.png', 'assets/male/pants/swordr/swordr5.png', 'assets/male/pants/swordr/swordr6.png']
PANTS_SWORDB = ['assets/male/pants/swordf/swordf4.png', 'assets/male/pants/swordf/swordf5.png', 'assets/male/pants/swordf/swordf6.png']
PANTS_SWORDF = ['assets/male/pants/swordb/swordb4.png', 'assets/male/pants/swordb/swordb5.png', 'assets/male/pants/swordb/swordb6.png']
PANTS_BOW_FOR = ['assets/male/bow/pforward/pforward1.png', 'assets/male/bow/pforward/pforward2.png',
           'assets/male/bow/pforward/pforward3.png', 'assets/male/bow/pforward/pforward4.png',
           'assets/male/bow/pforward/pforward5.png', 'assets/male/bow/pforward/pforward6.png',
           'assets/male/bow/pforward/pforward7.png', 'assets/male/bow/pforward/pforward8.png',
           'assets/male/bow/pforward/pforward9.png', 'assets/male/bow/pforward/pforward10.png',
           'assets/male/bow/pforward/pforward11.png', 'assets/male/bow/pforward/pforward12.png',
           'assets/male/bow/pforward/pforward13.png']
PANTS_BOW_BACK = ['assets/male/bow/pback/pback1.png', 'assets/male/bow/pback/pback2.png', 'assets/male/bow/pback/pback3.png',
            'assets/male/bow/pback/pback4.png', 'assets/male/bow/pback/pback5.png', 'assets/male/bow/pback/pback6.png',
            'assets/male/bow/pback/pback7.png', 'assets/male/bow/pback/pback8.png', 'assets/male/bow/pback/pback9.png',
            'assets/male/bow/pback/pback10.png', 'assets/male/bow/pback/pback11.png', 'assets/male/bow/pback/pback12.png',
            'assets/male/bow/pback/pback13.png']
PANTS_BOW_LEFT = ['assets/male/bow/pleft/pleft1.png', 'assets/male/bow/pleft/pleft2.png', 'assets/male/bow/pleft/pleft3.png',
            'assets/male/bow/pleft/pleft4.png', 'assets/male/bow/pleft/pleft5.png', 'assets/male/bow/pleft/pleft6.png',
            'assets/male/bow/pleft/pleft7.png', 'assets/male/bow/pleft/pleft8.png', 'assets/male/bow/pleft/pleft9.png',
            'assets/male/bow/pleft/pleft10.png', 'assets/male/bow/pleft/pleft11.png', 'assets/male/bow/pleft/pleft12.png',
            'assets/male/bow/pleft/pleft13.png']
PANTS_BOW_RIGHT = ['assets/male/bow/pright/pright1.png', 'assets/male/bow/pright/pright2.png', 'assets/male/bow/pright/pright3.png',
             'assets/male/bow/pright/pright4.png', 'assets/male/bow/pright/pright5.png', 'assets/male/bow/pright/pright6.png',
             'assets/male/bow/pright/pright7.png', 'assets/male/bow/pright/pright8.png', 'assets/male/bow/pright/pright9.png',
             'assets/male/bow/pright/pright10.png', 'assets/male/bow/pright/pright11.png', 'assets/male/bow/pright/pright12.png',
             'assets/male/bow/pright/pright13.png']

SHIRT_FOR = ['assets/male/shirt/back/back1.png', 'assets/male/shirt/back/back2.png', 'assets/male/shirt/back/back3.png',
             'assets/male/shirt/back/back4.png', 'assets/male/shirt/back/back5.png', 'assets/male/shirt/back/back6.png',
             'assets/male/shirt/back/back7.png', 'assets/male/shirt/back/back8.png', 'assets/male/shirt/back/back9.png']
SHIRT_BACK = ['assets/male/shirt/forward/forward1.png', 'assets/male/shirt/forward/forward2.png',
              'assets/male/shirt/forward/forward3.png', 'assets/male/shirt/forward/forward4.png',
              'assets/male/shirt/forward/forward5.png', 'assets/male/shirt/forward/forward6.png',
              'assets/male/shirt/forward/forward7.png', 'assets/male/shirt/forward/forward8.png',
              'assets/male/shirt/forward/forward9.png']
SHIRT_LEFT = ['assets/male/shirt/left/left1.png', 'assets/male/shirt/left/left2.png', 'assets/male/shirt/left/left3.png',
              'assets/male/shirt/left/left4.png', 'assets/male/shirt/left/left5.png', 'assets/male/shirt/left/left6.png',
              'assets/male/shirt/left/left7.png', 'assets/male/shirt/left/left8.png', 'assets/male/shirt/left/left9.png']
SHIRT_RIGHT = ['assets/male/shirt/right/right1.png', 'assets/male/shirt/right/right2.png', 'assets/male/shirt/right/right3.png',
               'assets/male/shirt/right/right4.png', 'assets/male/shirt/right/right5.png', 'assets/male/shirt/right/right6.png',
               'assets/male/shirt/right/right7.png', 'assets/male/shirt/right/right8.png', 'assets/male/shirt/right/right9.png']
SHIRT_DEATH = ['assets/male/shirt/death/death1.png', 'assets/male/shirt/death/death2.png', 'assets/male/shirt/death/death3.png',
               'assets/male/shirt/death/death4.png', 'assets/male/shirt/death/death5.png', 'assets/male/shirt/death/death6.png']
SHIRT_SWORDL = ['assets/male/shirt/swordl/swordl4.png', 'assets/male/shirt/swordl/swordl5.png', 'assets/male/shirt/swordl/swordl6.png']
SHIRT_SWORDR = ['assets/male/shirt/swordr/swordr4.png', 'assets/male/shirt/swordr/swordr5.png', 'assets/male/shirt/swordr/swordr6.png']
SHIRT_SWORDB = ['assets/male/shirt/swordf/swordf4.png', 'assets/male/shirt/swordf/swordf5.png', 'assets/male/shirt/swordf/swordf6.png']
SHIRT_SWORDF = ['assets/male/shirt/swordb/swordb4.png', 'assets/male/shirt/swordb/swordb5.png', 'assets/male/shirt/swordb/swordb6.png']
SHIRT_BOW_FOR = ['assets/male/bow/sforward/shirtforward1.png', 'assets/male/bow/sforward/shirtforward2.png',
           'assets/male/bow/sforward/shirtforward3.png', 'assets/male/bow/sforward/shirtforward4.png',
           'assets/male/bow/sforward/shirtforward5.png', 'assets/male/bow/sforward/shirtforward6.png',
           'assets/male/bow/sforward/shirtforward7.png', 'assets/male/bow/sforward/shirtforward8.png',
           'assets/male/bow/sforward/shirtforward9.png', 'assets/male/bow/sforward/shirtforward10.png',
           'assets/male/bow/sforward/shirtforward11.png', 'assets/male/bow/sforward/shirtforward12.png',
           'assets/male/bow/sforward/shirtforward13.png']
SHIRT_BOW_BACK = ['assets/male/bow/sback/sback1.png', 'assets/male/bow/sback/sback2.png', 'assets/male/bow/sback/sback3.png',
            'assets/male/bow/sback/sback4.png', 'assets/male/bow/sback/sback5.png', 'assets/male/bow/sback/sback6.png',
            'assets/male/bow/sback/sback7.png', 'assets/male/bow/sback/sback8.png', 'assets/male/bow/sback/sback9.png',
            'assets/male/bow/sback/sback10.png', 'assets/male/bow/sback/sback11.png', 'assets/male/bow/sback/sback12.png',
            'assets/male/bow/sback/sback13.png']
SHIRT_BOW_LEFT = ['assets/male/bow/sleft/sleft1.png', 'assets/male/bow/sleft/sleft2.png', 'assets/male/bow/sleft/sleft3.png',
            'assets/male/bow/sleft/sleft4.png', 'assets/male/bow/sleft/sleft5.png', 'assets/male/bow/sleft/sleft6.png',
            'assets/male/bow/sleft/sleft7.png', 'assets/male/bow/sleft/sleft8.png', 'assets/male/bow/sleft/sleft9.png',
            'assets/male/bow/sleft/sleft10.png', 'assets/male/bow/sleft/sleft11.png', 'assets/male/bow/sleft/sleft12.png',
            'assets/male/bow/sleft/sleft13.png']
SHIRT_BOW_RIGHT = ['assets/male/bow/sright/sright1.png', 'assets/male/bow/sright/sright2.png', 'assets/male/bow/sright/sright3.png',
             'assets/male/bow/sright/sright4.png', 'assets/male/bow/sright/sright5.png', 'assets/male/bow/sright/sright6.png',
             'assets/male/bow/sright/sright7.png', 'assets/male/bow/sright/sright8.png', 'assets/male/bow/sright/sright9.png',
             'assets/male/bow/sright/sright10.png', 'assets/male/bow/sright/sright11.png', 'assets/male/bow/sright/sright12.png',
             'assets/male/bow/sright/sright13.png']

SHIRTNPANTS_FOR = ['assets/male/shirtNpants/back/back1.png', 'assets/male/shirtNpants/back/back2.png', 'assets/male/shirtNpants/back/back3.png',
                   'assets/male/shirtNpants/back/back4.png', 'assets/male/shirtNpants/back/back5.png', 'assets/male/shirtNpants/back/back6.png',
                   'assets/male/shirtNpants/back/back7.png', 'assets/male/shirtNpants/back/back8.png', 'assets/male/shirtNpants/back/back9.png']
SHIRTNPANTS_BACK = ['assets/male/shirtNpants/forward/forward1.png', 'assets/male/shirtNpants/forward/forward2.png',
                    'assets/male/shirtNpants/forward/forward3.png', 'assets/male/shirtNpants/forward/forward4.png',
                    'assets/male/shirtNpants/forward/forward5.png', 'assets/male/shirtNpants/forward/forward6.png',
                    'assets/male/shirtNpants/forward/forward7.png', 'assets/male/shirtNpants/forward/forward8.png',
                    'assets/male/shirtNpants/forward/forward9.png']
SHIRTNPANTS_LEFT = ['assets/male/shirtNpants/left/left1.png', 'assets/male/shirtNpants/left/left2.png', 'assets/male/shirtNpants/left/left3.png',
                    'assets/male/shirtNpants/left/left4.png', 'assets/male/shirtNpants/left/left5.png', 'assets/male/shirtNpants/left/left6.png',
                    'assets/male/shirtNpants/left/left7.png', 'assets/male/shirtNpants/left/left8.png', 'assets/male/shirtNpants/left/left9.png']
SHIRTNPANTS_RIGHT = ['assets/male/shirtNpants/right/right1.png', 'assets/male/shirtNpants/right/right2.png', 'assets/male/shirtNpants/right/right3.png',
                     'assets/male/shirtNpants/right/right4.png', 'assets/male/shirtNpants/right/right5.png', 'assets/male/shirtNpants/right/right6.png',
                     'assets/male/shirtNpants/right/right7.png', 'assets/male/shirtNpants/right/right8.png', 'assets/male/shirtNpants/right/right9.png']
SHIRTNPANTS_DEATH = ['assets/male/shirtNpants/death/death1.png', 'assets/male/shirtNpants/death/death2.png', 'assets/male/shirtNpants/death/death3.png',
                     'assets/male/shirtNpants/death/death4.png', 'assets/male/shirtNpants/death/death5.png', 'assets/male/shirtNpants/death/death6.png']
SHIRTNPANTS_SWORDL = ['assets/male/shirtNpants/swordl/swordl4.png', 'assets/male/shirtNpants/swordl/swordl5.png', 'assets/male/shirtNpants/swordl/swordl6.png']
SHIRTNPANTS_SWORDR = ['assets/male/shirtNpants/swordr/swordr4.png', 'assets/male/shirtNpants/swordr/swordr5.png', 'assets/male/shirtNpants/swordr/swordr6.png']
SHIRTNPANTS_SWORDB = ['assets/male/shirtNpants/swordf/swordf4.png', 'assets/male/shirtNpants/swordf/swordf5.png', 'assets/male/shirtNpants/swordf/swordf6.png']
SHIRTNPANTS_SWORDF = ['assets/male/shirtNpants/swordb/swordb4.png', 'assets/male/shirtNpants/swordb/swordb5.png', 'assets/male/shirtNpants/swordb/swordb6.png']
SHIRTNPANTS_BOW_FOR = ['assets/male/bow/snpforward/snpforward1.png', 'assets/male/bow/snpforward/snpforward2.png',
           'assets/male/bow/snpforward/snpforward3.png', 'assets/male/bow/snpforward/snpforward4.png',
           'assets/male/bow/snpforward/snpforward5.png', 'assets/male/bow/snpforward/snpforward6.png',
           'assets/male/bow/snpforward/snpforward7.png', 'assets/male/bow/snpforward/snpforward8.png',
           'assets/male/bow/snpforward/snpforward9.png', 'assets/male/bow/snpforward/snpforward10.png',
           'assets/male/bow/snpforward/snpforward11.png', 'assets/male/bow/snpforward/snpforward12.png',
           'assets/male/bow/snpforward/snpforward13.png']
SHIRTNPANTS_BOW_BACK = ['assets/male/bow/snpback/snpback1.png', 'assets/male/bow/snpback/snpback2.png', 'assets/male/bow/snpback/snpback3.png',
            'assets/male/bow/snpback/snpback4.png', 'assets/male/bow/snpback/snpback5.png', 'assets/male/bow/snpback/snpback6.png',
            'assets/male/bow/snpback/snpback7.png', 'assets/male/bow/snpback/snpback8.png', 'assets/male/bow/snpback/snpback9.png',
            'assets/male/bow/snpback/snpback10.png', 'assets/male/bow/snpback/snpback11.png', 'assets/male/bow/snpback/snpback12.png',
            'assets/male/bow/snpback/snpback13.png']
SHIRTNPANTS_BOW_LEFT = ['assets/male/bow/snpleft/snpleft1.png', 'assets/male/bow/snpleft/snpleft2.png', 'assets/male/bow/snpleft/snpleft3.png',
            'assets/male/bow/snpleft/snpleft4.png', 'assets/male/bow/snpleft/snpleft5.png', 'assets/male/bow/snpleft/snpleft6.png',
            'assets/male/bow/snpleft/snpleft7.png', 'assets/male/bow/snpleft/snpleft8.png', 'assets/male/bow/snpleft/snpleft9.png',
            'assets/male/bow/snpleft/snpleft10.png', 'assets/male/bow/snpleft/snpleft11.png', 'assets/male/bow/snpleft/snpleft12.png',
            'assets/male/bow/snpleft/snpleft13.png']
SHIRTNPANTS_BOW_RIGHT = ['assets/male/bow/snpright/snpright1.png', 'assets/male/bow/snpright/snpright2.png', 'assets/male/bow/snpright/snpright3.png',
             'assets/male/bow/snpright/snpright4.png', 'assets/male/bow/snpright/snpright5.png', 'assets/male/bow/snpright/snpright6.png',
             'assets/male/bow/snpright/snpright7.png', 'assets/male/bow/snpright/snpright8.png', 'assets/male/bow/snpright/snpright9.png',
             'assets/male/bow/snpright/snpright10.png', 'assets/male/bow/snpright/snpright11.png', 'assets/male/bow/snpright/snpright12.png',
             'assets/male/bow/snpright/snpright13.png']

HELMATNPANTS_FOR = ['assets/male/helmatNpants/back/back1.png', 'assets/male/helmatNpants/back/back2.png', 'assets/male/helmatNpants/back/back3.png',
                    'assets/male/helmatNpants/back/back4.png', 'assets/male/helmatNpants/back/back5.png', 'assets/male/helmatNpants/back/back6.png',
                    'assets/male/helmatNpants/back/back7.png', 'assets/male/helmatNpants/back/back8.png', 'assets/male/helmatNpants/back/back9.png']
HELMATNPANTS_BACK = ['assets/male/helmatNpants/forward/forward1.png', 'assets/male/helmatNpants/forward/forward2.png',
                     'assets/male/helmatNpants/forward/forward3.png', 'assets/male/helmatNpants/forward/forward4.png',
                     'assets/male/helmatNpants/forward/forward5.png', 'assets/male/helmatNpants/forward/forward6.png',
                     'assets/male/helmatNpants/forward/forward7.png', 'assets/male/helmatNpants/forward/forward8.png',
                     'assets/male/helmatNpants/forward/forward9.png']
HELMATNPANTS_LEFT = ['assets/male/helmatNpants/left/left1.png', 'assets/male/helmatNpants/left/left2.png', 'assets/male/helmatNpants/left/left3.png',
                     'assets/male/helmatNpants/left/left4.png', 'assets/male/helmatNpants/left/left5.png', 'assets/male/helmatNpants/left/left6.png',
                     'assets/male/helmatNpants/left/left7.png', 'assets/male/helmatNpants/left/left8.png', 'assets/male/helmatNpants/left/left9.png']
HELMATNPANTS_RIGHT = ['assets/male/helmatNpants/right/right1.png', 'assets/male/helmatNpants/right/right2.png', 'assets/male/helmatNpants/right/right3.png',
                      'assets/male/helmatNpants/right/right4.png', 'assets/male/helmatNpants/right/right5.png', 'assets/male/helmatNpants/right/right6.png',
                      'assets/male/helmatNpants/right/right7.png', 'assets/male/helmatNpants/right/right8.png', 'assets/male/helmatNpants/right/right9.png']
HELMATNPANTS_DEATH = ['assets/male/helmatNpants/death/death1.png', 'assets/male/helmatNpants/death/death2.png', 'assets/male/helmatNpants/death/death3.png',
                      'assets/male/helmatNpants/death/death4.png', 'assets/male/helmatNpants/death/death5.png', 'assets/male/helmatNpants/death/death6.png']
HELMATNPANTS_SWORDL = ['assets/male/helmatNpants/swordl/swordl4.png', 'assets/male/helmatNpants/swordl/swordl5.png', 'assets/male/helmatNpants/swordl/swordl6.png']
HELMATNPANTS_SWORDR = ['assets/male/helmatNpants/swordr/swordr4.png', 'assets/male/helmatNpants/swordr/swordr5.png', 'assets/male/helmatNpants/swordr/swordr6.png']
HELMATNPANTS_SWORDB = ['assets/male/helmatNpants/swordf/swordf4.png', 'assets/male/helmatNpants/swordf/swordf5.png', 'assets/male/helmatNpants/swordf/swordf6.png']
HELMATNPANTS_SWORDF = ['assets/male/helmatNpants/swordb/swordb4.png', 'assets/male/helmatNpants/swordb/swordb5.png', 'assets/male/helmatNpants/swordb/swordb6.png']
HELMATNPANTS_BOW_FOR = ['assets/male/bow/hnpforward/hnpforward1.png', 'assets/male/bow/hnpforward/hnpforward2.png',
           'assets/male/bow/hnpforward/hnpforward3.png', 'assets/male/bow/hnpforward/hnpforward4.png',
           'assets/male/bow/hnpforward/hnpforward5.png', 'assets/male/bow/hnpforward/hnpforward6.png',
           'assets/male/bow/hnpforward/hnpforward7.png', 'assets/male/bow/hnpforward/hnpforward8.png',
           'assets/male/bow/hnpforward/hnpforward9.png', 'assets/male/bow/hnpforward/hnpforward10.png',
           'assets/male/bow/hnpforward/hnpforward11.png', 'assets/male/bow/hnpforward/hnpforward12.png',
           'assets/male/bow/hnpforward/hnpforward13.png']
HELMATNPANTS_BOW_BACK = ['assets/male/bow/hnpback/hnpback1.png', 'assets/male/bow/hnpback/hnpback2.png', 'assets/male/bow/hnpback/hnpback3.png',
                         'assets/male/bow/hnpback/hnpback4.png', 'assets/male/bow/hnpback/hnpback5.png', 'assets/male/bow/hnpback/hnpback6.png',
                         'assets/male/bow/hnpback/hnpback7.png', 'assets/male/bow/hnpback/hnpback8.png', 'assets/male/bow/hnpback/hnpback9.png',
                         'assets/male/bow/hnpback/hnpback10.png', 'assets/male/bow/hnpback/hnpback11.png', 'assets/male/bow/hnpback/hnpback12.png',
                         'assets/male/bow/hnpback/hnpback13.png']
HELMATNPANTS_BOW_LEFT = ['assets/male/bow/hnpleft/hnpleft1.png', 'assets/male/bow/hnpleft/hnpleft2.png', 'assets/male/bow/hnpleft/hnpleft3.png',
                         'assets/male/bow/hnpleft/hnpleft4.png', 'assets/male/bow/hnpleft/hnpleft5.png', 'assets/male/bow/hnpleft/hnpleft6.png',
                         'assets/male/bow/hnpleft/hnpleft7.png', 'assets/male/bow/hnpleft/hnpleft8.png', 'assets/male/bow/hnpleft/hnpleft9.png',
                         'assets/male/bow/hnpleft/hnpleft10.png', 'assets/male/bow/hnpleft/hnpleft11.png', 'assets/male/bow/hnpleft/hnpleft12.png',
                         'assets/male/bow/hnpleft/hnpleft13.png']
HELMATNPANTS_BOW_RIGHT = ['assets/male/bow/hnpright/hnpright1.png', 'assets/male/bow/hnpright/hnpright2.png', 'assets/male/bow/hnpright/hnpright3.png',
                          'assets/male/bow/hnpright/hnpright4.png', 'assets/male/bow/hnpright/hnpright5.png', 'assets/male/bow/hnpright/hnpright6.png',
                          'assets/male/bow/hnpright/hnpright7.png', 'assets/male/bow/hnpright/hnpright8.png', 'assets/male/bow/hnpright/hnpright9.png',
                          'assets/male/bow/hnpright/hnpright10.png', 'assets/male/bow/hnpright/hnpright11.png', 'assets/male/bow/hnpright/hnpright12.png',
                          'assets/male/bow/hnpright/hnpright13.png']

HELMATNSHIRT_FOR = ['assets/male/helmatNshirt/back/back1.png', 'assets/male/helmatNshirt/back/back2.png', 'assets/male/helmatNshirt/back/back3.png',
                    'assets/male/helmatNshirt/back/back4.png', 'assets/male/helmatNshirt/back/back5.png', 'assets/male/helmatNshirt/back/back6.png',
                    'assets/male/helmatNshirt/back/back7.png', 'assets/male/helmatNshirt/back/back8.png', 'assets/male/helmatNshirt/back/back9.png']
HELMATNSHIRT_BACK = ['assets/male/helmatNshirt/forward/forward1.png', 'assets/male/helmatNshirt/forward/forward2.png',
                     'assets/male/helmatNshirt/forward/forward3.png', 'assets/male/helmatNshirt/forward/forward4.png',
                     'assets/male/helmatNshirt/forward/forward5.png', 'assets/male/helmatNshirt/forward/forward6.png',
                     'assets/male/helmatNshirt/forward/forward7.png', 'assets/male/helmatNshirt/forward/forward8.png',
                     'assets/male/helmatNshirt/forward/forward9.png']
HELMATNSHIRT_LEFT = ['assets/male/helmatNshirt/left/left1.png', 'assets/male/helmatNshirt/left/left2.png', 'assets/male/helmatNshirt/left/left3.png',
                     'assets/male/helmatNshirt/left/left4.png', 'assets/male/helmatNshirt/left/left5.png', 'assets/male/helmatNshirt/left/left6.png',
                     'assets/male/helmatNshirt/left/left7.png', 'assets/male/helmatNshirt/left/left8.png', 'assets/male/helmatNshirt/left/left9.png']
HELMATNSHIRT_RIGHT = ['assets/male/helmatNshirt/right/right1.png', 'assets/male/helmatNshirt/right/right2.png', 'assets/male/helmatNshirt/right/right3.png',
                      'assets/male/helmatNshirt/right/right4.png', 'assets/male/helmatNshirt/right/right5.png', 'assets/male/helmatNshirt/right/right6.png',
                      'assets/male/helmatNshirt/right/right7.png', 'assets/male/helmatNshirt/right/right8.png', 'assets/male/helmatNshirt/right/right9.png']
HELMATNSHIRT_DEATH = ['assets/male/helmatNshirt/death/death1.png', 'assets/male/helmatNshirt/death/death2.png', 'assets/male/helmatNshirt/death/death3.png',
                      'assets/male/helmatNshirt/death/death4.png', 'assets/male/helmatNshirt/death/death5.png', 'assets/male/helmatNshirt/death/death6.png']
HELMATNSHIRT_SWORDL = ['assets/male/helmatNshirt/swordl/swordl4.png', 'assets/male/helmatNshirt/swordl/swordl5.png', 'assets/male/helmatNshirt/swordl/swordl6.png']
HELMATNSHIRT_SWORDR = ['assets/male/helmatNshirt/swordr/swordr4.png', 'assets/male/helmatNshirt/swordr/swordr5.png', 'assets/male/helmatNshirt/swordr/swordr6.png']
HELMATNSHIRT_SWORDB = ['assets/male/helmatNshirt/swordf/swordf4.png', 'assets/male/helmatNshirt/swordf/swordf5.png', 'assets/male/helmatNshirt/swordf/swordf6.png']
HELMATNSHIRT_SWORDF = ['assets/male/helmatNshirt/swordb/swordb4.png', 'assets/male/helmatNshirt/swordb/swordb5.png', 'assets/male/helmatNshirt/swordb/swordb6.png']
HELMATNSHIRT_BOW_FOR = ['assets/male/bow/hnsforward/hnsforward1.png', 'assets/male/bow/hnsforward/hnsforward2.png',
                        'assets/male/bow/hnsforward/hnsforward3.png', 'assets/male/bow/hnsforward/hnsforward4.png',
                        'assets/male/bow/hnsforward/hnsforward5.png', 'assets/male/bow/hnsforward/hnsforward6.png',
                        'assets/male/bow/hnsforward/hnsforward7.png', 'assets/male/bow/hnsforward/hnsforward8.png',
                        'assets/male/bow/hnsforward/hnsforward9.png', 'assets/male/bow/hnsforward/hnsforward10.png',
                        'assets/male/bow/hnsforward/hnsforward11.png', 'assets/male/bow/hnsforward/hnsforward12.png',
                        'assets/male/bow/hnsforward/hnsforward13.png']
HELMATNSHIRT_BOW_BACK = ['assets/male/bow/hnsback/hnsback1.png', 'assets/male/bow/hnsback/hnsback2.png', 'assets/male/bow/hnsback/hnsback3.png',
                         'assets/male/bow/hnsback/hnsback4.png', 'assets/male/bow/hnsback/hnsback5.png', 'assets/male/bow/hnsback/hnsback6.png',
                         'assets/male/bow/hnsback/hnsback7.png', 'assets/male/bow/hnsback/hnsback8.png', 'assets/male/bow/hnsback/hnsback9.png',
                         'assets/male/bow/hnsback/hnsback10.png', 'assets/male/bow/hnsback/hnsback11.png', 'assets/male/bow/hnsback/hnsback12.png',
                         'assets/male/bow/hnsback/hnsback13.png']
HELMATNSHIRT_BOW_LEFT = ['assets/male/bow/hnsleft/hnsleft1.png', 'assets/male/bow/hnsleft/hnsleft2.png', 'assets/male/bow/hnsleft/hnsleft3.png',
                         'assets/male/bow/hnsleft/hnsleft4.png', 'assets/male/bow/hnsleft/hnsleft5.png', 'assets/male/bow/hnsleft/hnsleft6.png',
                         'assets/male/bow/hnsleft/hnsleft7.png', 'assets/male/bow/hnsleft/hnsleft8.png', 'assets/male/bow/hnsleft/hnsleft9.png',
                         'assets/male/bow/hnsleft/hnsleft10.png', 'assets/male/bow/hnsleft/hnsleft11.png', 'assets/male/bow/hnsleft/hnsleft12.png',
                         'assets/male/bow/hnsleft/hnsleft13.png']
HELMATNSHIRT_BOW_RIGHT = ['assets/male/bow/hnsright/hnsright1.png', 'assets/male/bow/hnsright/hnsright2.png', 'assets/male/bow/hnsright/hnsright3.png',
                          'assets/male/bow/hnsright/hnsright4.png', 'assets/male/bow/hnsright/hnsright5.png', 'assets/male/bow/hnsright/hnsright6.png',
                          'assets/male/bow/hnsright/hnsright7.png', 'assets/male/bow/hnsright/hnsright8.png', 'assets/male/bow/hnsright/hnsright9.png',
                          'assets/male/bow/hnsright/hnsright10.png', 'assets/male/bow/hnsright/hnsright11.png', 'assets/male/bow/hnsright/hnsright12.png',
                          'assets/male/bow/hnsright/hnsright13.png']

FULLAMOUR_FOR = ['assets/male/fullamour/back/back1.png', 'assets/male/fullamour/back/back2.png', 'assets/male/fullamour/back/back3.png',
                 'assets/male/fullamour/back/back4.png', 'assets/male/fullamour/back/back5.png', 'assets/male/fullamour/back/back6.png',
                 'assets/male/fullamour/back/back7.png', 'assets/male/fullamour/back/back8.png', 'assets/male/fullamour/back/back9.png']
FULLAMOUR_BACK = ['assets/male/fullamour/forward/forward1.png', 'assets/male/fullamour/forward/forward2.png',
                  'assets/male/fullamour/forward/forward3.png', 'assets/male/fullamour/forward/forward4.png',
                  'assets/male/fullamour/forward/forward5.png', 'assets/male/fullamour/forward/forward6.png',
                  'assets/male/fullamour/forward/forward7.png', 'assets/male/fullamour/forward/forward8.png',
                  'assets/male/fullamour/forward/forward9.png']
FULLAMOUR_LEFT = ['assets/male/fullamour/left/left1.png', 'assets/male/fullamour/left/left2.png', 'assets/male/fullamour/left/left3.png',
                  'assets/male/fullamour/left/left4.png', 'assets/male/fullamour/left/left5.png', 'assets/male/fullamour/left/left6.png',
                  'assets/male/fullamour/left/left7.png', 'assets/male/fullamour/left/left8.png', 'assets/male/fullamour/left/left9.png']
FULLAMOUR_RIGHT = ['assets/male/fullamour/right/right1.png', 'assets/male/fullamour/right/right2.png', 'assets/male/fullamour/right/right3.png',
                   'assets/male/fullamour/right/right4.png', 'assets/male/fullamour/right/right5.png', 'assets/male/fullamour/right/right6.png',
                   'assets/male/fullamour/right/right7.png', 'assets/male/fullamour/right/right8.png', 'assets/male/fullamour/right/right9.png']
FULLAMOUR_DEATH = ['assets/male/fullamour/death/death1.png', 'assets/male/fullamour/death/death2.png', 'assets/male/fullamour/death/death3.png',
                   'assets/male/fullamour/death/death4.png', 'assets/male/fullamour/death/death5.png', 'assets/male/fullamour/death/death6.png']
FULLAMOUR_SWORDL = ['assets/male/fullamour/swordl/swordl4.png', 'assets/male/fullamour/swordl/swordl5.png', 'assets/male/fullamour/swordl/swordl6.png']
FULLAMOUR_SWORDR = ['assets/male/fullamour/swordr/swordr4.png', 'assets/male/fullamour/swordr/swordr5.png', 'assets/male/fullamour/swordr/swordr6.png']
FULLAMOUR_SWORDB = ['assets/male/fullamour/swordf/swordf4.png', 'assets/male/fullamour/swordf/swordf5.png', 'assets/male/fullamour/swordf/swordf6.png']
FULLAMOUR_SWORDF = ['assets/male/fullamour/swordb/swordb4.png', 'assets/male/fullamour/swordb/swordb5.png', 'assets/male/fullamour/swordb/swordb6.png']
FULLAMOUR_BOW_FOR = ['assets/male/bow/fullforward/fullforward1.png', 'assets/male/bow/fullforward/fullforward2.png',
                     'assets/male/bow/fullforward/fullforward3.png', 'assets/male/bow/fullforward/fullforward4.png',
                     'assets/male/bow/fullforward/fullforward5.png', 'assets/male/bow/fullforward/fullforward6.png',
                     'assets/male/bow/fullforward/fullforward7.png', 'assets/male/bow/fullforward/fullforward8.png',
                     'assets/male/bow/fullforward/fullforward9.png', 'assets/male/bow/fullforward/fullforward10.png',
                     'assets/male/bow/fullforward/fullforward11.png', 'assets/male/bow/fullforward/fullforward12.png',
                     'assets/male/bow/fullforward/fullforward13.png']
FULLAMOUR_BOW_BACK = ['assets/male/bow/fullback/fullback1.png', 'assets/male/bow/fullback/fullback2.png', 'assets/male/bow/fullback/fullback3.png',
                       'assets/male/bow/fullback/fullback4.png', 'assets/male/bow/fullback/fullback5.png', 'assets/male/bow/fullback/fullback6.png',
                       'assets/male/bow/fullback/fullback7.png', 'assets/male/bow/fullback/fullback8.png', 'assets/male/bow/fullback/fullback9.png',
                       'assets/male/bow/fullback/fullback10.png', 'assets/male/bow/fullback/fullback11.png', 'assets/male/bow/fullback/fullback12.png',
                       'assets/male/bow/fullback/fullback13.png']
FULLAMOUR_BOW_LEFT = ['assets/male/bow/fullleft/fullleft1.png', 'assets/male/bow/fullleft/fullleft2.png', 'assets/male/bow/fullleft/fullleft3.png',
                      'assets/male/bow/fullleft/fullleft4.png', 'assets/male/bow/fullleft/fullleft5.png', 'assets/male/bow/fullleft/fullleft6.png',
                      'assets/male/bow/fullleft/fullleft7.png', 'assets/male/bow/fullleft/fullleft8.png', 'assets/male/bow/fullleft/fullleft9.png',
                      'assets/male/bow/fullleft/fullleft10.png', 'assets/male/bow/fullleft/fullleft11.png', 'assets/male/bow/fullleft/fullleft12.png',
                      'assets/male/bow/fullleft/fullleft13.png']
FULLAMOUR_BOW_RIGHT = ['assets/male/bow/fullright/fullright1.png', 'assets/male/bow/fullright/fullright2.png', 'assets/male/bow/fullright/fullright3.png',
                       'assets/male/bow/fullright/fullright4.png', 'assets/male/bow/fullright/fullright5.png', 'assets/male/bow/fullright/fullright6.png',
                       'assets/male/bow/fullright/fullright7.png', 'assets/male/bow/fullright/fullright8.png', 'assets/male/bow/fullright/fullright9.png',
                       'assets/male/bow/fullright/fullright10.png', 'assets/male/bow/fullright/fullright11.png', 'assets/male/bow/fullright/fullright12.png',
                       'assets/male/bow/fullright/fullright13.png']

GREEN_SLIME_IDLE = ['assets/greenslime/idle/idle1.png', 'assets/greenslime/idle/idle2.png', 'assets/greenslime/idle/idle3.png',
                    'assets/greenslime/idle/idle4.png', 'assets/greenslime/idle/idle5.png', 'assets/greenslime/idle/idle6.png',
                    'assets/greenslime/idle/idle7.png', 'assets/greenslime/idle/idle8.png', 'assets/greenslime/idle/idle9.png',
                    'assets/greenslime/idle/idle10.png']
GREEN_SLIME_ATTACK = ['assets/greenslime/attack/attack1.png', 'assets/greenslime/attack/attack2.png', 'assets/greenslime/attack/attack3.png',
                      'assets/greenslime/attack/attack4.png', 'assets/greenslime/attack/attack5.png', 'assets/greenslime/attack/attack6.png',
                      'assets/greenslime/attack/attack7.png', 'assets/greenslime/attack/attack8.png', 'assets/greenslime/attack/attack9.png',
                      'assets/greenslime/attack/attack10.png']
GREEN_SLIME_DEATH = ['assets/greenslime/death/death1.png', 'assets/greenslime/death/death2.png', 'assets/greenslime/death/death3.png',
                     'assets/greenslime/death/death4.png', 'assets/greenslime/death/death5.png', 'assets/greenslime/death/death6.png',
                     'assets/greenslime/death/death7.png', 'assets/greenslime/death/death8.png', 'assets/greenslime/death/death9.png',
                     'assets/greenslime/death/death10.png']
RED_SLIME_IDLE = ['assets/redslime/idle/idle1.png', 'assets/redslime/idle/idle2.png', 'assets/redslime/idle/idle3.png',
                  'assets/redslime/idle/idle4.png', 'assets/redslime/idle/idle5.png', 'assets/redslime/idle/idle6.png',
                  'assets/redslime/idle/idle7.png', 'assets/redslime/idle/idle8.png', 'assets/redslime/idle/idle9.png',
                  'assets/redslime/idle/idle10.png']
RED_SLIME_ATTACK = ['assets/redslime/attack/attack1.png', 'assets/redslime/attack/attack2.png', 'assets/redslime/attack/attack3.png',
                    'assets/redslime/attack/attack4.png', 'assets/redslime/attack/attack5.png', 'assets/redslime/attack/attack6.png',
                    'assets/redslime/attack/attack7.png', 'assets/redslime/attack/attack8.png', 'assets/redslime/attack/attack9.png',
                    'assets/redslime/attack/attack10.png']
RED_SLIME_DEATH = ['assets/redslime/death/death1.png', 'assets/redslime/death/death2.png', 'assets/redslime/death/death3.png',
                   'assets/redslime/death/death4.png', 'assets/redslime/death/death5.png', 'assets/redslime/death/death6.png',
                   'assets/redslime/death/death7.png', 'assets/redslime/death/death8.png', 'assets/redslime/death/death9.png',
                   'assets/redslime/death/death10.png']
BLUE_SLIME_IDLE = ['assets/blueslime/idle/idle1.png', 'assets/blueslime/idle/idle2.png', 'assets/blueslime/idle/idle3.png',
                   'assets/blueslime/idle/idle4.png', 'assets/blueslime/idle/idle5.png', 'assets/blueslime/idle/idle6.png',
                   'assets/blueslime/idle/idle7.png', 'assets/blueslime/idle/idle8.png', 'assets/blueslime/idle/idle9.png',
                   'assets/blueslime/idle/idle10.png']
BLUE_SLIME_ATTACK = ['assets/blueslime/attack/attack1.png', 'assets/blueslime/attack/attack2.png', 'assets/blueslime/attack/attack3.png',
                     'assets/blueslime/attack/attack4.png', 'assets/blueslime/attack/attack5.png', 'assets/blueslime/attack/attack6.png',
                     'assets/blueslime/attack/attack7.png', 'assets/blueslime/attack/attack8.png', 'assets/blueslime/attack/attack9.png',
                     'assets/blueslime/attack/attack10.png']
BLUE_SLIME_DEATH = ['assets/blueslime/die/die1.png', 'assets/blueslime/die/die2.png', 'assets/blueslime/die/die3.png',
                    'assets/blueslime/die/die4.png', 'assets/blueslime/die/die5.png', 'assets/blueslime/die/die6.png',
                    'assets/blueslime/die/die7.png', 'assets/blueslime/die/die8.png', 'assets/blueslime/die/die9.png',
                    'assets/blueslime/die/die10.png']
SLIME_SPEED = 50
GREEN_SLIME_HEALTH = 50
BLUE_SLIME_HEALTH = 100
RED_SLIME_HEALTH = 150
SLIME_KNOCKBACK = 60

BLUE_SPIDER_FOR = ['assets/bluespider/for/for1.png', 'assets/bluespider/for/for2.png', 'assets/bluespider/for/for3.png',
                   'assets/bluespider/for/for4.png', 'assets/bluespider/for/for5.png', 'assets/bluespider/for/for6.png',
                   'assets/bluespider/for/for7.png', 'assets/bluespider/for/for8.png', 'assets/bluespider/for/for9.png',
                   'assets/bluespider/for/for10.png']
BLUE_SPIDER_BACK = ['assets/bluespider/back/back1.png', 'assets/bluespider/back/back2.png', 'assets/bluespider/back/back3.png',
                    'assets/bluespider/back/back4.png', 'assets/bluespider/back/back5.png', 'assets/bluespider/back/back6.png',
                    'assets/bluespider/back/back7.png', 'assets/bluespider/back/back8.png', 'assets/bluespider/back/back9.png',
                    'assets/bluespider/back/back10.png']
BLUE_SPIDER_LEFT = ['assets/bluespider/left/left1.png', 'assets/bluespider/left/left2.png', 'assets/bluespider/left/left3.png',
                    'assets/bluespider/left/left4.png', 'assets/bluespider/left/left5.png', 'assets/bluespider/left/left6.png',
                    'assets/bluespider/left/left7.png', 'assets/bluespider/left/left8.png', 'assets/bluespider/left/left9.png',
                    'assets/bluespider/left/left10.png']
BLUE_SPIDER_RIGHT = ['assets/bluespider/right/right1.png', 'assets/bluespider/right/right2.png', 'assets/bluespider/right/right3.png',
                     'assets/bluespider/right/right4.png', 'assets/bluespider/right/right5.png', 'assets/bluespider/right/right6.png',
                     'assets/bluespider/right/right7.png', 'assets/bluespider/right/right8.png', 'assets/bluespider/right/right9.png',
                     'assets/bluespider/right/right10.png']
BLUE_SPIDER_DEATH = ['assets/bluespider/death/death1.png', 'assets/bluespider/death/death2.png', 'assets/bluespider/death/death3.png',
                     'assets/bluespider/death/death4.png']

RED_SPIDER_FOR = ['assets/redspider/for/for1.png', 'assets/redspider/for/for2.png', 'assets/redspider/for/for3.png',
                  'assets/redspider/for/for4.png', 'assets/redspider/for/for5.png', 'assets/redspider/for/for6.png',
                  'assets/redspider/for/for7.png', 'assets/redspider/for/for8.png', 'assets/redspider/for/for9.png',
                  'assets/redspider/for/for10.png']
RED_SPIDER_BACK = ['assets/redspider/back/back1.png', 'assets/redspider/back/back2.png', 'assets/redspider/back/back3.png',
                   'assets/redspider/back/back4.png', 'assets/redspider/back/back5.png', 'assets/redspider/back/back6.png',
                   'assets/redspider/back/back7.png', 'assets/redspider/back/back8.png', 'assets/redspider/back/back9.png',
                   'assets/redspider/back/back10.png']
RED_SPIDER_LEFT = ['assets/redspider/left/left1.png', 'assets/redspider/left/left2.png', 'assets/redspider/left/left3.png',
                   'assets/redspider/left/left4.png', 'assets/redspider/left/left5.png', 'assets/redspider/left/left6.png',
                   'assets/redspider/left/left7.png', 'assets/redspider/left/left8.png', 'assets/redspider/left/left9.png',
                   'assets/redspider/left/left10.png']
RED_SPIDER_RIGHT = ['assets/redspider/right/right1.png', 'assets/redspider/right/right2.png', 'assets/redspider/right/right3.png',
                    'assets/redspider/right/right4.png', 'assets/redspider/right/right5.png', 'assets/redspider/right/right6.png',
                    'assets/redspider/right/right7.png', 'assets/redspider/right/right8.png', 'assets/redspider/right/right9.png',
                    'assets/redspider/right/right10.png']
RED_SPIDER_DEATH = ['assets/redspider/death/death1.png', 'assets/redspider/death/death2.png', 'assets/redspider/death/death3.png',
                    'assets/redspider/death/death4.png']

GREEN_SPIDER_FOR = ['assets/greenspider/for/for1.png', 'assets/greenspider/for/for2.png', 'assets/greenspider/for/for3.png',
                    'assets/greenspider/for/for4.png', 'assets/greenspider/for/for5.png', 'assets/greenspider/for/for6.png',
                    'assets/greenspider/for/for7.png', 'assets/greenspider/for/for8.png', 'assets/greenspider/for/for9.png',
                    'assets/greenspider/for/for10.png']
GREEN_SPIDER_BACK = ['assets/greenspider/back/back1.png', 'assets/greenspider/back/back2.png', 'assets/greenspider/back/back3.png',
                     'assets/greenspider/back/back4.png', 'assets/greenspider/back/back5.png', 'assets/greenspider/back/back6.png',
                     'assets/greenspider/back/back7.png', 'assets/greenspider/back/back8.png', 'assets/greenspider/back/back9.png',
                     'assets/greenspider/back/back10.png']
GREEN_SPIDER_LEFT = ['assets/greenspider/left/left1.png', 'assets/greenspider/left/left2.png', 'assets/greenspider/left/left3.png',
                     'assets/greenspider/left/left4.png', 'assets/greenspider/left/left5.png', 'assets/greenspider/left/left6.png',
                     'assets/greenspider/left/left7.png', 'assets/greenspider/left/left8.png', 'assets/greenspider/left/left9.png',
                     'assets/greenspider/left/left10.png']
GREEN_SPIDER_RIGHT = ['assets/greenspider/right/right1.png', 'assets/greenspider/right/right2.png', 'assets/greenspider/right/right3.png',
                      'assets/greenspider/right/right4.png', 'assets/greenspider/right/right5.png', 'assets/greenspider/right/right6.png',
                      'assets/greenspider/right/right7.png', 'assets/greenspider/right/right8.png', 'assets/greenspider/right/right9.png',
                      'assets/greenspider/right/right10.png']
GREEN_SPIDER_DEATH = ['assets/greenspider/death/death1.png', 'assets/greenspider/death/death2.png', 'assets/greenspider/death/death3.png',
                      'assets/greenspider/death/death4.png']

GOBLIN_LEFT = ['assets/goblin/left/left1.png', 'assets/goblin/left/left2.png', 'assets/goblin/left/left3.png',
               'assets/goblin/left/left4.png', 'assets/goblin/left/left5.png', 'assets/goblin/left/left6.png',
               'assets/goblin/left/left7.png', 'assets/goblin/left/left8.png']
GOBLIN_RIGHT = ['assets/goblin/right/right1.png', 'assets/goblin/right/right2.png', 'assets/goblin/right/right3.png',
                'assets/goblin/right/right4.png', 'assets/goblin/right/right5.png', 'assets/goblin/right/right6.png',
                'assets/goblin/right/right7.png', 'assets/goblin/right/right8.png', ]
GOBLIN_FOR = ['assets/goblin/forward/forward1.png', 'assets/goblin/forward/forward2.png',
              'assets/goblin/forward/forward3.png', 'assets/goblin/forward/forward5.png',
              'assets/goblin/forward/forward5.png', 'assets/goblin/forward/forward6.png',
              'assets/goblin/forward/forward7.png', 'assets/goblin/forward/forward8.png']
GOBLIN_BACK = ['assets/goblin/back/back1.png', 'assets/goblin/back/back2.png', 'assets/goblin/back/back3.png',
               'assets/goblin/back/back4.png', 'assets/goblin/back/back5.png', 'assets/goblin/back/back6.png',
               'assets/goblin/back/back7.png', 'assets/goblin/back/back8.png']                    
GOBLIN_ATTACKB = ['assets/goblin/attackb/attackb1.png', 'assets/goblin/attackb/attackb2.png',
                  'assets/goblin/attackb/attackb3.png', 'assets/goblin/attackb/attackb4.png']
GOBLIN_ATTACKF = ['assets/goblin/attackf/attackf1.png', 'assets/goblin/attackf/attackf2.png',
                  'assets/goblin/attackf/attackf3.png', 'assets/goblin/attackf/attackf4.png']
GOBLIN_ATTACKL = ['assets/goblin/attackl/attackl1.png', 'assets/goblin/attackl/attackl2.png',
                  'assets/goblin/attackl/attackl3.png', 'assets/goblin/attackl/attackl4.png']
GOBLIN_ATTACKR = ['assets/goblin/attackr/attackr1.png', 'assets/goblin/attackr/attackr2.png',
                  'assets/goblin/attackr/attackr3.png', 'assets/goblin/attackr/attackr4.png']
GOBLIN_DEATH = ['assets/goblin/death/death1.png', 'assets/goblin/death/death2.png', 'assets/goblin/death/death3.png',
                'assets/goblin/death/death4.png', 'assets/goblin/death/death5.png']
GOBLIN_SPEED = 150
GOBLIN_HEALTH = 50

SKELETON_LEFT = ['assets/skeleton/left/left1.png', 'assets/skeleton/left/left2.png', 'assets/skeleton/left/left3.png',
                 'assets/skeleton/left/left4.png', 'assets/skeleton/left/left5.png', 'assets/skeleton/left/left6.png',
                 'assets/skeleton/left/left7.png', 'assets/skeleton/left/left8.png', 'assets/skeleton/left/left9.png']
SKELETON_RIGHT = ['assets/skeleton/right/right1.png', 'assets/skeleton/right/right2.png',
                  'assets/skeleton/right/right3.png', 'assets/skeleton/right/right4.png',
                  'assets/skeleton/right/right5.png', 'assets/skeleton/right/right6.png',
                  'assets/skeleton/right/right7.png', 'assets/skeleton/right/right8.png',
                  'assets/skeleton/right/right9.png']
SKELETON_FOR = ['assets/skeleton/forward/forward1.png', 'assets/skeleton/forward/forward2.png',
                'assets/skeleton/forward/forward3.png', 'assets/skeleton/forward/forward4.png',
                'assets/skeleton/forward/forward5.png', 'assets/skeleton/forward/forward6.png',
                'assets/skeleton/forward/forward7.png', 'assets/skeleton/forward/forward8.png',
                'assets/skeleton/forward/forward9.png']
SKELETON_BACK = ['assets/skeleton/back/back1.png', 'assets/skeleton/back/back2.png', 'assets/skeleton/back/back3.png',
                 'assets/skeleton/back/back4.png', 'assets/skeleton/back/back5.png', 'assets/skeleton/back/back6.png',
                 'assets/skeleton/back/back7.png', 'assets/skeleton/back/back8.png', 'assets/skeleton/back/back9.png']
SKELETON_ATTACKB = ['assets/skeleton/attackb/attackb1.png', 'assets/skeleton/attackb/attackb2.png',
                    'assets/skeleton/attackb/attackb3.png', 'assets/skeleton/attackb/attackb4.png',
                    'assets/skeleton/attackb/attackb5.png', 'assets/skeleton/attackb/attackb6.png',
                    'assets/skeleton/attackb/attackb5.png', 'assets/skeleton/attackb/attackb4.png',
                    'assets/skeleton/attackb/attackb3.png', 'assets/skeleton/attackb/attackb2.png',
                    'assets/skeleton/attackb/attackb1.png']
SKELETON_ATTACKF = ['assets/skeleton/attackf/attackf1.png', 'assets/skeleton/attackf/attackf2.png',
                    'assets/skeleton/attackf/attackf3.png', 'assets/skeleton/attackf/attackf4.png',
                    'assets/skeleton/attackf/attackf5.png', 'assets/skeleton/attackf/attackf6.png',
                    'assets/skeleton/attackf/attackf5.png', 'assets/skeleton/attackf/attackf4.png',
                    'assets/skeleton/attackf/attackf3.png', 'assets/skeleton/attackf/attackf2.png',
                    'assets/skeleton/attackf/attackf1.png']
SKELETON_ATTACKL = ['assets/skeleton/attackl/attackl1.png', 'assets/skeleton/attackl/attackl2.png',
                    'assets/skeleton/attackl/attackl3.png', 'assets/skeleton/attackl/attackl4.png',
                    'assets/skeleton/attackl/attackl5.png', 'assets/skeleton/attackl/attackl6.png',
                    'assets/skeleton/attackl/attackl5.png', 'assets/skeleton/attackl/attackl4.png',
                    'assets/skeleton/attackl/attackl3.png', 'assets/skeleton/attackl/attackl2.png',
                    'assets/skeleton/attackl/attackl1.png']
SKELETON_ATTACKR = ['assets/skeleton/attackr/attackr1.png', 'assets/skeleton/attackr/attackr2.png',
                    'assets/skeleton/attackr/attackr3.png', 'assets/skeleton/attackr/attackr4.png',
                    'assets/skeleton/attackr/attackr5.png', 'assets/skeleton/attackr/attackr6.png',
                    'assets/skeleton/attackr/attackr5.png', 'assets/skeleton/attackr/attackr4.png',
                    'assets/skeleton/attackr/attackr3.png', 'assets/skeleton/attackr/attackr2.png',
                    'assets/skeleton/attackr/attackr1.png']
SKELETON_DEATH = ['assets/skeleton/death/death1.png', 'assets/skeleton/death/death2.png',
                  'assets/skeleton/death/death3.png', 'assets/skeleton/death/death4.png',
                  'assets/skeleton/death/death5.png', 'assets/skeleton/death/death6.png']
SKELETON_SPEED = 0
SKELETON_HEALTH = 50

RED_IMP_LEFT = ['assets/redimp/redimpl/left1.png', 'assets/redimp/redimpl/left2.png',
                'assets/redimp/redimpl/left3.png', 'assets/redimp/redimpl/left4.png']
RED_IMP_RIGHT = ['assets/redimp/redimpr/right1.png', 'assets/redimp/redimpr/right2.png',
                 'assets/redimp/redimpr/right3.png', 'assets/redimp/redimpr/right4.png']
RED_IMP_FOR = ['assets/redimp/redimpf/for1.png', 'assets/redimp/redimpf/for2.png',
               'assets/redimp/redimpf/for3.png', 'assets/redimp/redimpf/for4.png']
RED_IMP_BACK = ['assets/redimp/redimpb/back1.png', 'assets/redimp/redimpb/back2.png',
                'assets/redimp/redimpb/back3.png', 'assets/redimp/redimpb/back4.png']
RED_IMP_ATTACKB = ['assets/redimp/redimpatkb/atkb1.png', 'assets/redimp/redimpatkb/atkb2.png',
                   'assets/redimp/redimpatkb/atkb3.png', 'assets/redimp/redimpatkb/atkb4.png']
RED_IMP_ATTACKF = ['assets/redimp/redimpatkf/atkf1.png', 'assets/redimp/redimpatkf/atkf2.png',
                   'assets/redimp/redimpatkf/atkf3.png', 'assets/redimp/redimpatkf/atkf4.png']
RED_IMP_ATTACKL = ['assets/redimp/redimpatkl/atkl1.png', 'assets/redimp/redimpatkl/atkl2.png',
                   'assets/redimp/redimpatkl/atkl3.png', 'assets/redimp/redimpatkl/atkl4.png']
RED_IMP_ATTACKR = ['assets/redimp/redimpatkr/atkr1.png', 'assets/redimp/redimpatkr/atkr2.png',
                   'assets/redimp/redimpatkr/atkr3.png', 'assets/redimp/redimpatkr/atkr4.png']
RED_IMP_DEATH = ['assets/redimp/redimpdie/death1.png', 'assets/redimp/redimpdie/death2.png',
                 'assets/redimp/redimpdie/death3.png', 'assets/redimp/redimpdie/death4.png',
                 'assets/redimp/redimpdie/death5.png', 'assets/redimp/redimpdie/death6.png',
                 'assets/redimp/redimpdie/death7.png']

GREEN_IMP_LEFT = ['assets/greenimp/greenimpl/greenimpl1.png', 'assets/greenimp/greenimpl/greenimpl2.png',
                  'assets/greenimp/greenimpl/greenimpl3.png', 'assets/greenimp/greenimpl/greenimpl4.png']
GREEN_IMP_RIGHT = ['assets/greenimp/greenimpr/greenimpr1.png', 'assets/greenimp/greenimpr/greenimpr2.png',
                   'assets/greenimp/greenimpr/greenimpr3.png', 'assets/greenimp/greenimpr/greenimpr4.png']
GREEN_IMP_FOR = ['assets/greenimp/greenimpf/greenimpf1.png', 'assets/greenimp/greenimpf/greenimpf2.png',
                 'assets/greenimp/greenimpf/greenimpf3.png', 'assets/greenimp/greenimpf/greenimpf4.png']
GREEN_IMP_BACK = ['assets/greenimp/greenimpb/greenimpb1.png', 'assets/greenimp/greenimpb/greenimpb2.png',
                  'assets/greenimp/greenimpb/greenimpb3.png', 'assets/greenimp/greenimpb/greenimpb4.png']
GREEN_IMP_ATTACKB = ['assets/greenimp/greenimpatkb/atkb1.png', 'assets/greenimp/greenimpatkb/atkb2.png',
                     'assets/greenimp/greenimpatkb/atkb3.png', 'assets/greenimp/greenimpatkb/atkb4.png']
GREEN_IMP_ATTACKF = ['assets/greenimp/greenimpatkf/atkf1.png', 'assets/greenimp/greenimpatkf/atkf2.png',
                     'assets/greenimp/greenimpatkf/atkf3.png', 'assets/greenimp/greenimpatkf/atkf4.png']
GREEN_IMP_ATTACKL = ['assets/greenimp/greenimpatkl/atkl1.png', 'assets/greenimp/greenimpatkl/atkl2.png',
                     'assets/greenimp/greenimpatkl/atkl3.png', 'assets/greenimp/greenimpatkl/atkl4.png']
GREEN_IMP_ATTACKR = ['assets/greenimp/greenimpatkr/atkr1.png', 'assets/greenimp/greenimpatkr/atkr2.png',
                     'assets/greenimp/greenimpatkr/atkr3.png', 'assets/greenimp/greenimpatkr/atkr4.png']
GREEN_IMP_DEATH = ['assets/greenimp/greenimpdie/death1.png', 'assets/greenimp/greenimpdie/death2.png',
                   'assets/greenimp/greenimpdie/death3.png', 'assets/greenimp/greenimpdie/death4.png',
                   'assets/greenimp/greenimpdie/death5.png', 'assets/greenimp/greenimpdie/death6.png',
                   'assets/greenimp/greenimpdie/death7.png']

BLUE_IMP_LEFT = ['assets/blueimp/blueimpl/left1.png', 'assets/blueimp/blueimpl/left2.png',
                 'assets/blueimp/blueimpl/left3.png', 'assets/blueimp/blueimpl/left4.png']
BLUE_IMP_RIGHT = ['assets/blueimp/blueimpr/right1.png', 'assets/blueimp/blueimpr/right2.png',
                  'assets/blueimp/blueimpr/right3.png', 'assets/blueimp/blueimpr/right4.png']
BLUE_IMP_FOR = ['assets/blueimp/blueimpf/for1.png', 'assets/blueimp/blueimpf/for2.png',
                'assets/blueimp/blueimpf/for3.png', 'assets/blueimp/blueimpf/for4.png']
BLUE_IMP_BACK = ['assets/blueimp/blueimpb/back1.png', 'assets/blueimp/blueimpb/back2.png',
                 'assets/blueimp/blueimpb/back3.png', 'assets/blueimp/blueimpb/back4.png']
BLUE_IMP_ATTACKB = ['assets/blueimp/blueimpatkb/atkb1.png', 'assets/blueimp/blueimpatkb/atkb2.png',
                    'assets/blueimp/blueimpatkb/atkb3.png', 'assets/blueimp/blueimpatkb/atkb4.png']
BLUE_IMP_ATTACKF = ['assets/blueimp/blueimpatkf/atkf1.png', 'assets/blueimp/blueimpatkf/atkf2.png',
                    'assets/blueimp/blueimpatkf/atkf3.png', 'assets/blueimp/blueimpatkf/atkf4.png']
BLUE_IMP_ATTACKL = ['assets/blueimp/blueimpatkl/atkl1.png', 'assets/blueimp/blueimpatkl/atkl2.png',
                    'assets/blueimp/blueimpatkl/atkl3.png', 'assets/blueimp/blueimpatkl/atkl4.png']
BLUE_IMP_ATTACKR = ['assets/blueimp/blueimpatkr/atkr1.png', 'assets/blueimp/blueimpatkr/atkr2.png',
                    'assets/blueimp/blueimpatkr/atkr3.png', 'assets/blueimp/blueimpatkr/atkr4.png']
BLUE_IMP_DEATH = ['assets/blueimp/blueimpdie/die1.png', 'assets/blueimp/blueimpdie/die2.png',
                  'assets/blueimp/blueimpdie/die3.png', 'assets/blueimp/blueimpdie/die4.png',
                  'assets/blueimp/blueimpdie/die5.png', 'assets/blueimp/blueimpdie/die6.png',
                  'assets/blueimp/blueimpdie/die7.png']

GOLEM_FOR = ['assets/golem/golemfor/golemfor1.png', 'assets/golem/golemfor/golemfor2.png', 'assets/golem/golemfor/golemfor7.png',
             'assets/golem/golemfor/golemfor4.png', 'assets/golem/golemfor/golemfor5.png', 'assets/golem/golemfor/golemfor6.png',
             'assets/golem/golemfor/golemfor7.png']
GOLEM_BACK = ['assets/golem/golemback/golemback1.png', 'assets/golem/golemback/golemback2.png', 'assets/golem/golemback/golemback7.png',
              'assets/golem/golemback/golemback4.png', 'assets/golem/golemback/golemback5.png', 'assets/golem/golemback/golemback6.png',
              'assets/golem/golemback/golemback7.png']
GOLEM_LEFT = ['assets/golem/golemleft/golemleft1.png', 'assets/golem/golemleft/golemleft2.png', 'assets/golem/golemleft/golemleft7.png',
              'assets/golem/golemleft/golemleft4.png', 'assets/golem/golemleft/golemleft5.png', 'assets/golem/golemleft/golemleft6.png',
              'assets/golem/golemleft/golemleft7.png']
GOLEM_RIGHT = ['assets/golem/golemright/golemright1.png', 'assets/golem/golemright/golemright2.png', 'assets/golem/golemright/golemright7.png',
               'assets/golem/golemright/golemright4.png', 'assets/golem/golemright/golemright5.png', 'assets/golem/golemright/golemright6.png',
               'assets/golem/golemright/golemright7.png']
GOLEM_ATTACKF = ['assets/golem/atkfor/golemfor1.png', 'assets/golem/atkfor/golemfor2.png', 'assets/golem/atkfor/golemfor7.png',
                 'assets/golem/atkfor/golemfor4.png', 'assets/golem/atkfor/golemfor5.png', 'assets/golem/atkfor/golemfor6.png',
                 'assets/golem/atkfor/golemfor7.png']
GOLEM_ATTACKB = ['assets/golem/atkback/golemback1.png', 'assets/golem/atkback/golemback2.png', 'assets/golem/atkback/golemback7.png',
                 'assets/golem/atkback/golemback4.png', 'assets/golem/atkback/golemback5.png', 'assets/golem/atkback/golemback6.png',
                 'assets/golem/atkback/golemback7.png']
GOLEM_ATTACKL = ['assets/golem/atkleft/golemleft1.png', 'assets/golem/atkleft/golemleft2.png', 'assets/golem/atkleft/golemleft7.png',
                 'assets/golem/atkleft/golemleft4.png', 'assets/golem/atkleft/golemleft5.png', 'assets/golem/atkleft/golemleft6.png',
                 'assets/golem/atkleft/golemleft7.png']
GOLEM_ATTACKR = ['assets/golem/atkright/golemright1.png', 'assets/golem/atkright/golemright2.png', 'assets/golem/atkright/golemright7.png',
                 'assets/golem/atkright/golemright4.png', 'assets/golem/atkright/golemright5.png', 'assets/golem/atkright/golemright6.png',
                 'assets/golem/atkright/golemright7.png']
GOLEM_DEATH = ['assets/golem/death/golemdeath1.png', 'assets/golem/death/golemdeath2.png', 'assets/golem/death/golemdeath7.png',
               'assets/golem/death/golemdeath4.png', 'assets/golem/death/golemdeath5.png', 'assets/golem/death/golemdeath6.png',
               'assets/golem/death/golemdeath7.png']

BOSSSPIDER_FOR = ['assets/bossspider/bossspiderfor/spiderfor1.png', 'assets/bossspider/bossspiderfor/spiderfor2.png',
                  'assets/bossspider/bossspiderfor/spiderfor3.png']
BOSSSPIDER_LEFT = ['assets/bossspider/bossspiderl/spiderl1.png', 'assets/bossspider/bossspiderl/spiderl2.png',
                  'assets/bossspider/bossspiderl/spiderl3.png']
BOSSSPIDER_RIGHT = ['assets/bossspider/bossspiderr/spiderr1.png', 'assets/bossspider/bossspiderr/spiderr2.png',
                  'assets/bossspider/bossspiderr/spiderr3.png']
BOSSSPIDER_BACK = ['assets/bossspider/bossspiderb/spiderb1.png', 'assets/bossspider/bossspiderb/spiderb2.png',
                  'assets/bossspider/bossspiderb/spiderb3.png']

BOSSWORM_FOR = ['assets/bossworm/bosswormatkf/atkf1.png', 'assets/bossworm/bosswormatkf/atkf2.png',
                'assets/bossworm/bosswormatkf/atkf3.png', 'assets/bossworm/bosswormatkf/atkf4.png',
                'assets/bossworm/bosswormatkf/atkf5.png']
BOSSWORM_LEFT = ['assets/bossworm/bosswormatkl/atkl1.png', 'assets/bossworm/bosswormatkl/atkl2.png',
                 'assets/bossworm/bosswormatkl/atkl3.png', 'assets/bossworm/bosswormatkl/atkl4.png',
                 'assets/bossworm/bosswormatkl/atkl5.png']
BOSSWORM_RIGHT = ['assets/bossworm/bosswormatkr/atkr1.png', 'assets/bossworm/bosswormatkr/atkr2.png',
                  'assets/bossworm/bosswormatkr/atkr3.png', 'assets/bossworm/bosswormatkr/atkr4.png',
                  'assets/bossworm/bosswormatkr/atkr5.png']
BOSSWORM_BACK = ['assets/bossworm/bosswormatkb/atkb1.png', 'assets/bossworm/bosswormatkb/atkb2.png',
                 'assets/bossworm/bosswormatkb/atkb3.png', 'assets/bossworm/bosswormatkb/atkb4.png',
                 'assets/bossworm/bosswormatkb/atkb5.png']
BOSSWORM_DIRT = ['assets/bossworm/bosswormdirt/dirt1.png', 'assets/bossworm/bosswormdirt/dirt2.png',
                 'assets/bossworm/bosswormdirt/dirt3.png', 'assets/bossworm/bosswormdirt/dirt4.png',
                 'assets/bossworm/bosswormdirt/dirt5.png']
BOSSWORM_INTRO = ['assets/bossworm/bosswormintro/intro1.png', 'assets/bossworm/bosswormintro/intro2.png',
                  'assets/bossworm/bosswormintro/intro3.png', 'assets/bossworm/bosswormintro/intro4.png',
                  'assets/bossworm/bosswormintro/intro5.png', 'assets/bossworm/bosswormintro/intro6.png',
                  'assets/bossworm/bosswormintro/intro7.png', 'assets/bossworm/bosswormintro/intro8.png',
                  'assets/bossworm/bosswormintro/intro9.png', 'assets/bossworm/bosswormintro/intro10.png',
                  'assets/bossworm/bosswormintro/intro11.png', 'assets/bossworm/bosswormintro/intro12.png',
                  'assets/bossworm/bosswormintro/intro13.png', 'assets/bossworm/bosswormintro/intro14.png',
                  'assets/bossworm/bosswormintro/intro15.png', 'assets/bossworm/bosswormintro/intro16.png']
BOSSWORM_JUMPR = ['assets/bossworm/bosswormjumpr/jumpr1.png', 'assets/bossworm/bosswormjumpr/jumpr2.png',
                  'assets/bossworm/bosswormjumpr/jumpr3.png', 'assets/bossworm/bosswormjumpr/jumpr4.png']
BOSSWORM_JUMPB = ['assets/bossworm/bosswormjumpb/jumpb1.png', 'assets/bossworm/bosswormjumpb/jumpb2.png',
                  'assets/bossworm/bosswormjumpb/jumpb3.png', 'assets/bossworm/bosswormjumpb/jumpb4.png']
BOSSWORM_JUMPL = ['assets/bossworm/bosswormjumpl/jumpl1.png', 'assets/bossworm/bosswormjumpl/jumpl2.png',
                  'assets/bossworm/bosswormjumpl/jumpl3.png', 'assets/bossworm/bosswormjumpl/jumpl4.png']
BOSSWORM_JUMPF = ['assets/bossworm/bosswormjumpf/jumpf1.png', 'assets/bossworm/bosswormjumpf/jumpf2.png',
                  'assets/bossworm/bosswormjumpf/jumpf3.png', 'assets/bossworm/bosswormjumpf/jumpf4.png']

WORM_FOR = ['assets/worm/wormatkf/atkfor1.png', 'assets/worm/wormatkf/atkfor2.png', 'assets/worm/wormatkf/atkfor3.png',
            'assets/worm/wormatkf/atkfor4.png', 'assets/worm/wormatkf/atkfor5.png', 'assets/worm/wormatkf/atkfor6.png',
            'assets/worm/wormatkf/atkfor7.png', 'assets/worm/wormatkf/atkfor8.png', 'assets/worm/wormatkf/atkfor9.png']
WORM_LEFT = ['assets/worm/wormatkl/atkl1.png', 'assets/worm/wormatkl/atkl2.png', 'assets/worm/wormatkl/atkl3.png',
             'assets/worm/wormatkl/atkl4.png', 'assets/worm/wormatkl/atkl5.png', 'assets/worm/wormatkl/atkl6.png',
             'assets/worm/wormatkl/atkl7.png', 'assets/worm/wormatkl/atkl8.png', 'assets/worm/wormatkl/atkl9.png']
WORM_RIGHT = ['assets/worm/wormatkr/atkr1.png', 'assets/worm/wormatkr/atkr2.png', 'assets/worm/wormatkr/atkr3.png',
              'assets/worm/wormatkr/atkr4.png', 'assets/worm/wormatkr/atkr5.png', 'assets/worm/wormatkr/atkr6.png',
              'assets/worm/wormatkr/atkr7.png', 'assets/worm/wormatkr/atkr8.png', 'assets/worm/wormatkr/atkr9.png']
WORM_BACK = ['assets/worm/wormatkb/atkb1.png', 'assets/worm/wormatkb/atkb2.png', 'assets/worm/wormatkb/atkb3.png',
             'assets/worm/wormatkb/atkb4.png', 'assets/worm/wormatkb/atkb5.png', 'assets/worm/wormatkb/atkb6.png',
             'assets/worm/wormatkb/atkb7.png', 'assets/worm/wormatkb/atkb8.png', 'assets/worm/wormatkb/atkb9.png']
WORM_DIRT = ['assets/worm/wormdirt/dirt1.png', 'assets/worm/wormdirt/dirt2.png', 'assets/worm/wormdirt/dirt3.png',
             'assets/worm/wormdirt/dirt4.png', 'assets/worm/wormdirt/dirt5.png']
WORM_JUMPR = ['assets/worm/wormjumpr/jumpr1.png', 'assets/worm/wormjumpr/jumpr2.png',
              'assets/worm/wormjumpr/jumpr3.png', 'assets/worm/wormjumpr/jumpr4.png', 'assets/worm/wormjumpr/jumpr5.png']
WORM_JUMPB = ['assets/worm/wormjumpb/jumpb1.png', 'assets/worm/wormjumpb/jumpb2.png',
              'assets/worm/wormjumpb/jumpb3.png', 'assets/worm/wormjumpb/jumpb4.png', 'assets/worm/wormjumpb/jumpb5.png']
WORM_JUMPL = ['assets/worm/wormjumpl/jumpl1.png', 'assets/worm/wormjumpl/jumpl2.png',
              'assets/worm/wormjumpl/jumpl3.png', 'assets/worm/wormjumpl/jumpl4.png', 'assets/worm/wormjumpl/jumpl5.png']
WORM_JUMPF = ['assets/worm/wormjumpf/jumpf1.png', 'assets/worm/wormjumpf/jumpf2.png',
              'assets/worm/wormjumpf/jumpf3.png', 'assets/worm/wormjumpf/jumpf4.png', 'assets/worm/wormjumpf/jumpf5.png']
WORM_DIE = ['assets/worm/wormdie/die1.png', 'assets/worm/wormdie/die2.png', 'assets/worm/wormdie/die3.png']

DORVER = ['assets/dorver/dorver-idle0.png', 'assets/dorver/dorver-idle1.png',
          'assets/dorver/dorver-idle2.png', 'assets/dorver/dorver-idle3.png']

SOLDER_FOR = ['assets/solder/solderf/for1.png', 'assets/solder/solderf/for2.png', 'assets/solder/solderf/for3.png',
              'assets/solder/solderf/for4.png', 'assets/solder/solderf/for5.png', 'assets/solder/solderf/for6.png']
SOLDER_LEFT = ['assets/solder/solderl/left1.png', 'assets/solder/solderl/left2.png', 'assets/solder/solderl/left3.png',
               'assets/solder/solderl/left4.png', 'assets/solder/solderl/left5.png', 'assets/solder/solderl/left6.png']
SOLDER_RIGHT = ['assets/solder/solderr/right1.png', 'assets/solder/solderr/right2.png', 'assets/solder/solderr/right3.png',
                'assets/solder/solderr/right4.png', 'assets/solder/solderr/right5.png', 'assets/solder/solderr/right6.png']
SOLDER_BACK = ['assets/solder/solderb/back1.png', 'assets/solder/solderb/back2.png', 'assets/solder/solderb/back3.png',
               'assets/solder/solderb/back4.png', 'assets/solder/solderb/back5.png', 'assets/solder/solderb/back6.png']

SMOKE_SCREEN = ['assets/smoke/default-hit-01.png', 'assets/smoke/default-hit-02.png',
                'assets/smoke/default-hit-03.png', 'assets/smoke/default-hit-04.png',
                'assets/smoke/default-hit-05.png', 'assets/smoke/default-hit-06.png',
                'assets/smoke/default-hit-07.png', 'assets/smoke/default-hit-08.png',
                'assets/smoke/default-hit-09.png', 'assets/smoke/default-hit-10.png',
                'assets/smoke/default-hit-11.png', 'assets/smoke/default-hit-12.png',
                'assets/smoke/default-hit-13.png']
SMOKE_BOMB = 'assets/smokebomb.png'
SMOKE_TIME = 1500
map1 = 'assets/maps/map1.tmx'
map2 = 'assets/maps/map2.tmx'
map3 = 'assets/maps/map3.tmx'
map4 = 'assets/maps/map4.tmx'
map5 = 'assets/maps/map5.tmx'
map6 = 'assets/maps/map6.tmx'
map7 = 'assets/maps/map7.tmx'
map8 = 'assets/maps/map8.tmx'
map9 = 'assets/maps/map9.tmx'
map10 = 'assets/maps/map10.tmx'
map11 = 'assets/maps/map11.tmx'
HEALTH_HEARTFULL = 'assets/heartfull.png'
HEALTH_HEARTHALF = 'assets/hearthalf.png'
HEALTH_HEARTEMPTY = 'assets/heartempty.png'
COIN = ['assets/coin1.png', 'assets/coin2.png', 'assets/coin3.png', 'assets/coin4.png']
HEART = ['assets/heart1.png', 'assets/heart2.png', 'assets/heart3.png', 'assets/heart4.png']
FIRE = ['assets/fire1.png', 'assets/fire2.png', 'assets/fire3.png', 'assets/fire4.png', 'assets/fire5.png',
        'assets/fire6.png', 'assets/fire7.png']
SWORD = 'assets/sword.png'
HELMAT = 'assets/hat.png'
SHIRT = 'assets/shirt.png'
PANTS = 'assets/pants.png'
ANGEL = 'assets/angel.png'
BLANK = 'assets/blank.png'
BOMB = 'assets/bomb.png'
BOW = 'assets/bow.png'
EXPLOSION = ['assets/explosion/explosion1.png', 'assets/explosion/explosion2.png', 'assets/explosion/explosion3.png',
             'assets/explosion/explosion4.png', 'assets/explosion/explosion6.png', 'assets/explosion/explosion6.png',
             'assets/explosion/explosion7.png', 'assets/explosion/explosion8.png', 'assets/explosion/explosion9.png',
             'assets/explosion/explosion10.png']
BOMB_TIME = 3000
BONE = 'assets/bone.png'
BONE_SPEED = 300
BONE_TIME = 5000
BONE_RATE = 700
EXPLOSION_SOUND = 'assets/sounds/explosion.wav'
ARROW = 'assets/arrow.png'

ADVOID_RADIUS = 50

WALL_LAYER = 1
PLAYER_LAYER = 2
PROJECTILE_LAYER = 4
MOB_LAYER = 2
OBJECT_LAYER = 1
EXPLOSION_LAYER = 5