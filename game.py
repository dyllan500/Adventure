from sprites import *
from tileset import *
from save import *
import pygame as pg

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

        #self.joy = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
        #self.joy[0].init()
        #self.joy = self.joy[0]

    def load_data(self):
        self.player2_on = False
        self.map1_on = MAP1_ON
        self.map1_enemies = MAP1_ENEMIES
        self.map1_straw = MAP1_STRAW
        self.map1_coin1 = MAP1_COIN1
        self.map1_coin2 = MAP1_COIN2
        self.map1_heart = MAP1_HEART
        self.map2_on = MAP2_ON
        self.map2_enemies = MAP2_EMEMIES
        self.map2_straw = MAP2_STRAW
        self.map2_coin = MAP2_COIN
        self.map4_on = MAP4_ON
        self.map4_coin1 = MAP4_COIN1
        self.map4_coin2 = MAP4_COIN2
        self.map4_coin3 = MAP4_COIN3
        self.map4_coin4 = MAP4_COIN4
        self.map4_heart1 = MAP4_HEART1
        self.map4_heart2 = MAP4_HEART2
        self.map4_enemies = MAP4_ENEMIES
        self.map3_on = MAP3_ON
        self.map3_coin1 = MAP3_COIN1
        self.map3_coin2 = MAP3_COIN2
        self.map3_coin3 = MAP3_COIN3
        self.map3_coin4 = MAP3_COIN4
        self.map3_heart = MAP3_HEART
        self.map3_enemies = MAP3_ENEMIES
        self.map5_on = MAP5_ON
        self.map5_enemies = MAP5_ENEMIES
        self.map6_on = MAP6_ON
        self.map6_enemies = MAP6_ENEMIES
        self.map6_heart1 = MAP6_HEART1
        self.map6_heart2 = MAP6_HEART2
        self.map6_heart3 = MAP6_HEART3
        self.map7_on = MAP7_ON
        self.map7_enemies = MAP7_ENEMIES
        self.map7_heart = MAP7_HEART
        self.map8_on = MAP8_ON
        self.map8_enemies = MAP8_ENEMIES
        self.map8_heart = MAP8_HEART
        self.map9_on = MAP9_ON
        self.map9_enemies = MAP9_ENEMIES
        self.map9_heart1 = MAP9_HEART1
        self.map9_heart2 = MAP9_HEART2
        self.map10_on = MAP10_ON
        self.map10_enemies = MAP10_ENEMIES
        self.map11_on = MAP11_ON
        self.map11_enemies = MAP11_ENEMIES
        self.got_sword = GOT_SWORD
        self.map2_to_map1 = MAP2_T0_MAP1
        self.map3_to_map1 = MAP3_TO_MAP1
        self.map4_to_map3 = MAP4_TO_MAP3
        self.map5_to_map4 = MAP5_TO_MAP4
        self.map6_to_map4 = MAP6_TO_MAP4
        self.map7_to_map6 = MAP7_TO_MAP6
        self.map8_to_map6 = MAP8_TO_MAP6
        self.map9_to_map6 = MAP9_TO_MAP6
        self.money = MONEY
        self.health = HEALTH
        self.health2 = HEALTH
        self.got_pants = GOT_PANTS
        self.got_hat = GOT_HAT
        self.got_shirt = GOT_SHIRT
        self.max_health = HEALTH
        self.arrows = ARROWS
        self.player_bombs = BOMBS
        self.got_bow = GOT_BOW
        self.player_smoke_bombs = SMOKE_BOMBS
        self.smokebomb_on = SMOKE_BOMB_ON
        self.sword_on = SWORD_ON
        self.bow_on = BOW_ON
        self.bomb_on = BOMB_ON

        self.myfont = pg.font.SysFont('font/CompHand.ttf', 80)
        self.angelfont = pg.font.SysFont('font/DancingScript-Regular.ttf', 30)
        self.forward = []
        self.back = []
        self.left = []
        self.right = []
        self.death = []
        self.sword_left = []
        self.sword_right = []
        self.sword_forward = []
        self.sword_back = []
        self.bow_for = []
        self.bow_back = []
        self.bow_left = []
        self.bow_right = []
        self.helmat_bow_for = []
        self.helmat_bow_back = []
        self.helmat_bow_left = []
        self.helmat_bow_right = []
        self.shirt_bow_for = []
        self.shirt_bow_back = []
        self.shirt_bow_left = []
        self.shirt_bow_right = []
        self.pants_bow_for = []
        self.pants_bow_back = []
        self.pants_bow_left = []
        self.pants_bow_right = []
        self.hnp_bow_for = []
        self.hnp_bow_back = []
        self.hnp_bow_left = []
        self.hnp_bow_right = []
        self.hns_bow_for = []
        self.hns_bow_back = []
        self.hns_bow_left = []
        self.hns_bow_right = []
        self.snp_bow_for = []
        self.snp_bow_back = []
        self.snp_bow_left = []
        self.snp_bow_right = []
        self.full_bow_for = []
        self.full_bow_back = []
        self.full_bow_left = []
        self.full_bow_right = []
        self.helmat_forward = []
        self.helmat_back = []
        self.helmat_left = []
        self.helmat_right = []
        self.helmat_death = []
        self.helmat_swordl = []
        self.helmat_swordr = []
        self.helmat_swordf = []
        self.helmat_swordb = []
        self.pants_forward = []
        self.pants_back = []
        self.pants_left = []
        self.pants_right = []
        self.pants_death = []
        self.pants_swordl = []
        self.pants_swordr = []
        self.pants_swordf = []
        self.pants_swordb = []
        self.shirt_forward = []
        self.shirt_back = []
        self.shirt_left = []
        self.shirt_right = []
        self.shirt_death = []
        self.shirt_swordl = []
        self.shirt_swordr = []
        self.shirt_swordf = []
        self.shirt_swordb = []
        self.shirtNpants_forward = []
        self.shirtNpants_back = []
        self.shirtNpants_left = []
        self.shirtNpants_right = []
        self.shirtNpants_death = []
        self.shirtNpants_swordl = []
        self.shirtNpants_swordr = []
        self.shirtNpants_swordf = []
        self.shirtNpants_swordb = []
        self.helmatNpants_forward = []
        self.helmatNpants_back = []
        self.helmatNpants_left = []
        self.helmatNpants_right = []
        self.helmatNpants_death = []
        self.helmatNpants_swordl = []
        self.helmatNpants_swordr = []
        self.helmatNpants_swordf = []
        self.helmatNpants_swordb = []
        self.helmatNshirt_forward = []
        self.helmatNshirt_back = []
        self.helmatNshirt_left = []
        self.helmatNshirt_right = []
        self.helmatNshirt_death = []
        self.helmatNshirt_swordl = []
        self.helmatNshirt_swordr = []
        self.helmatNshirt_swordf = []
        self.helmatNshirt_swordb = []
        self.fullamour_forward = []
        self.fullamour_back = []
        self.fullamour_left = []
        self.fullamour_right = []
        self.fullamour_death = []
        self.fullamour_swordl = []
        self.fullamour_swordr = []
        self.fullamour_swordf = []
        self.fullamour_swordb = []
        self.green_slime_idle = []
        self.green_slime_death = []
        self.green_slime_attack = []
        self.red_slime_idle = []
        self.red_slime_death = []
        self.red_slime_attack = []
        self.blue_slime_idle = []
        self.blue_slime_death = []
        self.blue_slime_attack = []
        self.blue_spider_for = []
        self.blue_spider_back = []
        self.blue_spider_left = []
        self.blue_spider_right = []
        self.blue_spider_death = []
        self.red_spider_for = []
        self.red_spider_back = []
        self.red_spider_left = []
        self.red_spider_right = []
        self.red_spider_death = []
        self.green_spider_for = []
        self.green_spider_back = []
        self.green_spider_left = []
        self.green_spider_right = []
        self.green_spider_death = []
        self.coin = []
        self.heart = []
        self.fire = []
        self.goblin_for = []
        self.goblin_back = []
        self.goblin_right = []
        self.goblin_left = []
        self.goblin_attackf = []
        self.goblin_attackb = []
        self.goblin_attackl = []
        self.goblin_attackr = []
        self.goblin_death = []
        self.skeleton_for = []
        self.skeleton_back = []
        self.skeleton_right = []
        self.skeleton_left = []
        self.skeleton_attackf = []
        self.skeleton_attackb = []
        self.skeleton_attackl = []
        self.skeleton_attackr = []
        self.skeleton_death = []
        self.red_imp_for = []
        self.red_imp_back = []
        self.red_imp_right = []
        self.red_imp_left = []
        self.red_imp_attackf = []
        self.red_imp_attackb = []
        self.red_imp_attackl = []
        self.red_imp_attackr = []
        self.red_imp_death = []
        self.green_imp_for = []
        self.green_imp_back = []
        self.green_imp_right = []
        self.green_imp_left = []
        self.green_imp_attackf = []
        self.green_imp_attackb = []
        self.green_imp_attackl = []
        self.green_imp_attackr = []
        self.green_imp_death = []
        self.blue_imp_for = []
        self.blue_imp_back = []
        self.blue_imp_right = []
        self.blue_imp_left = []
        self.blue_imp_attackf = []
        self.blue_imp_attackb = []
        self.blue_imp_attackl = []
        self.blue_imp_attackr = []
        self.blue_imp_death = []
        self.golem_back = []
        self.golem_for = []
        self.golem_left = []
        self.golem_right = []
        self.golem_attackf = []
        self.golem_attackb = []
        self.golem_attackr = []
        self.golem_attackl = []
        self.golem_death = []
        self.spiderboss_for = []
        self.spiderboss_left = []
        self.spiderboss_right = []
        self.spiderboss_back = []
        self.wormboss_intro = []
        self.wormboss_back = []
        self.wormboss_for = []
        self.wormboss_left = []
        self.wormboss_right = []
        self.wormboss_jumpf = []
        self.wormboss_jumpb = []
        self.wormboss_jumpl = []
        self.wormboss_jumpr = []
        self.wormboss_dirt = []
        self.worm_back = []
        self.worm_for = []
        self.worm_left = []
        self.worm_right = []
        self.worm_jumpf = []
        self.worm_jumpb = []
        self.worm_jumpl = []
        self.worm_jumpr = []
        self.worm_dirt = []
        self.worm_die = []
        self.dorver = []
        self.solder_for = []
        self.solder_back = []
        self.solder_left = []
        self.solder_right = []
        self.explosion = []
        self.smoke_screen = []
        for img in PLAYER_FOR:
            self.forward.append(pg.image.load(img))
        for img in PLAYER_BACK:
            self.back.append(pg.image.load(img))
        for img in PLAYER_LEFT:
            self.left.append(pg.image.load(img))
        for img in PLAYER_RIGHT:
            self.right.append(pg.image.load(img))
        for img in SWORD_RIGHT:
            self.sword_right.append(pg.image.load(img))
        for img in SWORD_LEFT:
            self.sword_left.append(pg.image.load(img))
        for img in SWORD_FOR:
            self.sword_back.append(pg.image.load(img))
        for img in SWORD_BACK:
            self.sword_forward.append(pg.image.load(img))
        for img in GREEN_SLIME_IDLE:
            self.green_slime_idle.append(pg.image.load(img))
        for img in GREEN_SLIME_DEATH:
            self.green_slime_death.append(pg.image.load(img))
        for img in GREEN_SLIME_ATTACK:
            self.green_slime_attack.append(pg.image.load(img))
        for img in RED_SLIME_IDLE:
            self.red_slime_idle.append(pg.image.load(img))
        for img in RED_SLIME_DEATH:
            self.red_slime_death.append(pg.image.load(img))
        for img in RED_SLIME_ATTACK:
            self.red_slime_attack.append(pg.image.load(img))
        for img in BLUE_SLIME_IDLE:
            self.blue_slime_idle.append(pg.image.load(img))
        for img in BLUE_SLIME_DEATH:
            self.blue_slime_death.append(pg.image.load(img))
        for img in BLUE_SLIME_ATTACK:
            self.blue_slime_attack.append(pg.image.load(img))
        for img in COIN:
            self.coin.append(pg.image.load(img))
        for img in HEART:
            self.heart.append(pg.image.load(img))
        for img in FIRE:
            self.fire.append(pg.image.load(img))
        for img in GOBLIN_FOR:
            self.goblin_for.append(pg.image.load(img))
        for img in GOBLIN_BACK:
            self.goblin_back.append(pg.image.load(img))
        for img in GOBLIN_LEFT:
            self.goblin_left.append(pg.image.load(img))
        for img in GOBLIN_RIGHT:
            self.goblin_right.append(pg.image.load(img))
        for img in GOBLIN_ATTACKR:
            self.goblin_attackr.append(pg.image.load(img))
        for img in GOBLIN_ATTACKL:
            self.goblin_attackl.append(pg.image.load(img))
        for img in GOBLIN_ATTACKF:
            self.goblin_attackf.append(pg.image.load(img))
        for img in GOBLIN_ATTACKB:
            self.goblin_attackb.append(pg.image.load(img))
        for img in GOBLIN_DEATH:
            self.goblin_death.append(pg.image.load(img))
        for img in SKELETON_FOR:
            self.skeleton_for.append(pg.image.load(img))
        for img in SKELETON_BACK:
            self.skeleton_back.append(pg.image.load(img))
        for img in SKELETON_LEFT:
            self.skeleton_left.append(pg.image.load(img))
        for img in SKELETON_RIGHT:
            self.skeleton_right.append(pg.image.load(img))
        for img in SKELETON_ATTACKR:
            self.skeleton_attackr.append(pg.image.load(img))
        for img in SKELETON_ATTACKL:
            self.skeleton_attackl.append(pg.image.load(img))
        for img in SKELETON_ATTACKF:
            self.skeleton_attackf.append(pg.image.load(img))
        for img in SKELETON_ATTACKB:
            self.skeleton_attackb.append(pg.image.load(img))
        for img in SKELETON_DEATH:
            self.skeleton_death.append(pg.image.load(img))
        for img in HELMAT_FOR:
            self.helmat_forward.append(pg.image.load(img))
        for img in HELMAT_LEFT:
            self.helmat_left.append(pg.image.load(img))
        for img in HELMAT_RIGHT:
            self.helmat_right.append(pg.image.load(img))
        for img in HELMAT_BACK:
            self.helmat_back.append(pg.image.load(img))
        for img in HELMAT_SWORDB:
            self.helmat_swordb.append(pg.image.load(img))
        for img in HELMAT_SWORDF:
            self.helmat_swordf.append(pg.image.load(img))
        for img in HELMAT_SWORDR:
            self.helmat_swordr.append(pg.image.load(img))
        for img in HELMAT_SWORDL:
            self.helmat_swordl.append(pg.image.load(img))
        for img in HELMAT_DEATH:
            self.helmat_death.append(pg.image.load(img))
        for img in HELMATNPANTS_FOR:
            self.helmatNpants_forward.append(pg.image.load(img))
        for img in HELMATNPANTS_LEFT:
            self.helmatNpants_left.append(pg.image.load(img))
        for img in HELMATNPANTS_RIGHT:
            self.helmatNpants_right.append(pg.image.load(img))
        for img in HELMATNPANTS_BACK:
            self.helmatNpants_back.append(pg.image.load(img))
        for img in HELMATNPANTS_SWORDB:
            self.helmatNpants_swordb.append(pg.image.load(img))
        for img in HELMATNPANTS_SWORDF:
            self.helmatNpants_swordf.append(pg.image.load(img))
        for img in HELMATNPANTS_SWORDR:
            self.helmatNpants_swordr.append(pg.image.load(img))
        for img in HELMATNPANTS_SWORDL:
            self.helmatNpants_swordl.append(pg.image.load(img))
        for img in HELMATNPANTS_DEATH:
            self.helmatNpants_death.append(pg.image.load(img))
        for img in HELMATNSHIRT_FOR:
            self.helmatNshirt_forward.append(pg.image.load(img))
        for img in HELMATNSHIRT_LEFT:
            self.helmatNshirt_left.append(pg.image.load(img))
        for img in HELMATNSHIRT_RIGHT:
            self.helmatNshirt_right.append(pg.image.load(img))
        for img in HELMATNSHIRT_BACK:
            self.helmatNshirt_back.append(pg.image.load(img))
        for img in HELMATNSHIRT_SWORDB:
            self.helmatNshirt_swordb.append(pg.image.load(img))
        for img in HELMATNSHIRT_SWORDF:
            self.helmatNshirt_swordf.append(pg.image.load(img))
        for img in HELMATNSHIRT_SWORDR:
            self.helmatNshirt_swordr.append(pg.image.load(img))
        for img in HELMATNSHIRT_SWORDL:
            self.helmatNshirt_swordl.append(pg.image.load(img))
        for img in HELMATNSHIRT_DEATH:
            self.helmatNshirt_death.append(pg.image.load(img))
        for img in SHIRT_FOR:
            self.shirt_forward.append(pg.image.load(img))
        for img in SHIRT_LEFT:
            self.shirt_left.append(pg.image.load(img))
        for img in SHIRT_RIGHT:
            self.shirt_right.append(pg.image.load(img))
        for img in SHIRT_BACK:
            self.shirt_back.append(pg.image.load(img))
        for img in SHIRT_SWORDB:
            self.shirt_swordb.append(pg.image.load(img))
        for img in SHIRT_SWORDF:
            self.shirt_swordf.append(pg.image.load(img))
        for img in SHIRT_SWORDR:
            self.shirt_swordr.append(pg.image.load(img))
        for img in SHIRT_SWORDL:
            self.shirt_swordl.append(pg.image.load(img))
        for img in SHIRT_DEATH:
            self.shirt_death.append(pg.image.load(img))
        for img in SHIRTNPANTS_FOR:
            self.shirtNpants_forward.append(pg.image.load(img))
        for img in SHIRTNPANTS_LEFT:
            self.shirtNpants_left.append(pg.image.load(img))
        for img in SHIRTNPANTS_RIGHT:
            self.shirtNpants_right.append(pg.image.load(img))
        for img in SHIRTNPANTS_BACK:
            self.shirtNpants_back.append(pg.image.load(img))
        for img in SHIRTNPANTS_SWORDB:
            self.shirtNpants_swordb.append(pg.image.load(img))
        for img in SHIRTNPANTS_SWORDF:
            self.shirtNpants_swordf.append(pg.image.load(img))
        for img in SHIRTNPANTS_SWORDR:
            self.shirtNpants_swordr.append(pg.image.load(img))
        for img in SHIRTNPANTS_SWORDL:
            self.shirtNpants_swordl.append(pg.image.load(img))
        for img in SHIRTNPANTS_DEATH:
            self.shirtNpants_death.append(pg.image.load(img))
        for img in PANTS_FOR:
            self.pants_forward.append(pg.image.load(img))
        for img in PANTS_LEFT:
            self.pants_left.append(pg.image.load(img))
        for img in PANTS_RIGHT:
            self.pants_right.append(pg.image.load(img))
        for img in PANTS_BACK:
            self.pants_back.append(pg.image.load(img))
        for img in PANTS_SWORDB:
            self.pants_swordf.append(pg.image.load(img))
        for img in PANTS_SWORDF:
            self.pants_swordb.append(pg.image.load(img))
        for img in PANTS_SWORDR:
            self.pants_swordr.append(pg.image.load(img))
        for img in PANTS_SWORDL:
            self.pants_swordl.append(pg.image.load(img))
        for img in PANTS_DEATH:
            self.pants_death.append(pg.image.load(img))
        for img in FULLAMOUR_FOR:
            self.fullamour_forward.append(pg.image.load(img))
        for img in FULLAMOUR_LEFT:
            self.fullamour_left.append(pg.image.load(img))
        for img in FULLAMOUR_RIGHT:
            self.fullamour_right.append(pg.image.load(img))
        for img in FULLAMOUR_BACK:
            self.fullamour_back.append(pg.image.load(img))
        for img in FULLAMOUR_SWORDB:
            self.fullamour_swordb.append(pg.image.load(img))
        for img in FULLAMOUR_SWORDF:
            self.fullamour_swordf.append(pg.image.load(img))
        for img in FULLAMOUR_SWORDR:
            self.fullamour_swordr.append(pg.image.load(img))
        for img in FULLAMOUR_SWORDL:
            self.fullamour_swordl.append(pg.image.load(img))
        for img in FULLAMOUR_DEATH:
            self.fullamour_death.append(pg.image.load(img))
        for img in RED_IMP_FOR:
            self.red_imp_for.append(pg.image.load(img))
        for img in RED_IMP_BACK:
            self.red_imp_back.append(pg.image.load(img))
        for img in RED_IMP_LEFT:
            self.red_imp_left.append(pg.image.load(img))
        for img in RED_IMP_RIGHT:
            self.red_imp_right.append(pg.image.load(img))
        for img in RED_IMP_ATTACKR:
            self.red_imp_attackr.append(pg.image.load(img))
        for img in RED_IMP_ATTACKL:
            self.red_imp_attackl.append(pg.image.load(img))
        for img in RED_IMP_ATTACKF:
            self.red_imp_attackf.append(pg.image.load(img))
        for img in RED_IMP_ATTACKB:
            self.red_imp_attackb.append(pg.image.load(img))
        for img in RED_IMP_DEATH:
            self.red_imp_death.append(pg.image.load(img))
        for img in GREEN_IMP_FOR:
            self.green_imp_for.append(pg.image.load(img))
        for img in GREEN_IMP_BACK:
            self.green_imp_back.append(pg.image.load(img))
        for img in GREEN_IMP_LEFT:
            self.green_imp_left.append(pg.image.load(img))
        for img in GREEN_IMP_RIGHT:
            self.green_imp_right.append(pg.image.load(img))
        for img in GREEN_IMP_ATTACKR:
            self.green_imp_attackr.append(pg.image.load(img))
        for img in GREEN_IMP_ATTACKL:
            self.green_imp_attackl.append(pg.image.load(img))
        for img in GREEN_IMP_ATTACKF:
            self.green_imp_attackf.append(pg.image.load(img))
        for img in GREEN_IMP_ATTACKB:
            self.green_imp_attackb.append(pg.image.load(img))
        for img in GREEN_IMP_DEATH:
            self.green_imp_death.append(pg.image.load(img))
        for img in BLUE_IMP_FOR:
            self.blue_imp_for.append(pg.image.load(img))
        for img in BLUE_IMP_BACK:
            self.blue_imp_back.append(pg.image.load(img))
        for img in BLUE_IMP_LEFT:
            self.blue_imp_left.append(pg.image.load(img))
        for img in BLUE_IMP_RIGHT:
            self.blue_imp_right.append(pg.image.load(img))
        for img in BLUE_IMP_ATTACKR:
            self.blue_imp_attackr.append(pg.image.load(img))
        for img in BLUE_IMP_ATTACKL:
            self.blue_imp_attackl.append(pg.image.load(img))
        for img in BLUE_IMP_ATTACKF:
            self.blue_imp_attackf.append(pg.image.load(img))
        for img in BLUE_IMP_ATTACKB:
            self.blue_imp_attackb.append(pg.image.load(img))
        for img in BLUE_IMP_DEATH:
            self.blue_imp_death.append(pg.image.load(img))
        for img in EXPLOSION:
            self.explosion.append(pg.image.load(img))
        for img in BOW_FOR:
            self.bow_for.append(pg.image.load(img))
        for img in BOW_BACK:
            self.bow_back.append(pg.image.load(img))
        for img in BOW_RIGHT:
            self.bow_right.append(pg.image.load(img))
        for img in BOW_LEFT:
            self.bow_left.append(pg.image.load(img))
        for img in HELMAT_BOW_FOR:
            self.helmat_bow_for.append(pg.image.load(img))
        for img in HELMAT_BOW_BACK:
            self.helmat_bow_back.append(pg.image.load(img))
        for img in HELMAT_BOW_RIGHT:
            self.helmat_bow_right.append(pg.image.load(img))
        for img in HELMAT_BOW_LEFT:
            self.helmat_bow_left.append(pg.image.load(img))
        for img in SHIRT_BOW_FOR:
            self.shirt_bow_for.append(pg.image.load(img))
        for img in SHIRT_BOW_BACK:
            self.shirt_bow_back.append(pg.image.load(img))
        for img in SHIRT_BOW_RIGHT:
            self.shirt_bow_right.append(pg.image.load(img))
        for img in SHIRT_BOW_LEFT:
            self.shirt_bow_left.append(pg.image.load(img))
        for img in PANTS_BOW_FOR:
            self.pants_bow_for.append(pg.image.load(img))
        for img in PANTS_BOW_BACK:
            self.pants_bow_back.append(pg.image.load(img))
        for img in PANTS_BOW_RIGHT:
            self.pants_bow_right.append(pg.image.load(img))
        for img in PANTS_BOW_LEFT:
            self.pants_bow_left.append(pg.image.load(img))
        for img in HELMATNPANTS_BOW_FOR:
            self.hnp_bow_for.append(pg.image.load(img))
        for img in HELMATNPANTS_BOW_BACK:
            self.hnp_bow_back.append(pg.image.load(img))
        for img in HELMATNPANTS_BOW_RIGHT:
            self.hnp_bow_right.append(pg.image.load(img))
        for img in HELMATNPANTS_BOW_LEFT:
            self.hnp_bow_left.append(pg.image.load(img))
        for img in HELMATNSHIRT_BOW_FOR:
            self.hns_bow_for.append(pg.image.load(img))
        for img in HELMATNSHIRT_BOW_BACK:
            self.hns_bow_back.append(pg.image.load(img))
        for img in HELMATNSHIRT_BOW_RIGHT:
            self.hns_bow_right.append(pg.image.load(img))
        for img in HELMATNSHIRT_BOW_LEFT:
            self.hns_bow_left.append(pg.image.load(img))
        for img in SHIRTNPANTS_BOW_FOR:
            self.snp_bow_for.append(pg.image.load(img))
        for img in SHIRTNPANTS_BOW_BACK:
            self.snp_bow_back.append(pg.image.load(img))
        for img in SHIRTNPANTS_BOW_RIGHT:
            self.snp_bow_right.append(pg.image.load(img))
        for img in SHIRTNPANTS_BOW_LEFT:
            self.snp_bow_left.append(pg.image.load(img))
        for img in FULLAMOUR_BOW_FOR:
            self.full_bow_for.append(pg.image.load(img))
        for img in FULLAMOUR_BOW_BACK:
            self.full_bow_back.append(pg.image.load(img))
        for img in FULLAMOUR_BOW_RIGHT:
            self.full_bow_right.append(pg.image.load(img))
        for img in FULLAMOUR_BOW_LEFT:
            self.full_bow_left.append(pg.image.load(img))
        for img in SMOKE_SCREEN:
            self.smoke_screen.append(pg.image.load(img))
        for img in GOLEM_BACK:
            self.golem_back.append(pg.image.load(img))
        for img in GOLEM_FOR:
            self.golem_for.append(pg.image.load(img))
        for img in GOLEM_RIGHT:
            self.golem_right.append(pg.image.load(img))
        for img in GOLEM_LEFT:
            self.golem_left.append(pg.image.load(img))
        for img in GOLEM_ATTACKB:
            self.golem_attackb.append(pg.image.load(img))
        for img in GOLEM_ATTACKF:
            self.golem_attackf.append(pg.image.load(img))
        for img in GOLEM_ATTACKL:
            self.golem_attackl.append(pg.image.load(img))
        for img in GOLEM_ATTACKR:
            self.golem_attackr.append(pg.image.load(img))
        for img in GOLEM_DEATH:
            self.golem_death.append(pg.image.load(img))
        for img in BOSSSPIDER_BACK:
            self.spiderboss_back.append(pg.image.load(img))
        for img in BOSSSPIDER_FOR:
            self.spiderboss_for.append(pg.image.load(img))
        for img in BOSSSPIDER_LEFT:
            self.spiderboss_left.append(pg.image.load(img))
        for img in BOSSSPIDER_RIGHT:
            self.spiderboss_right.append(pg.image.load(img))
        for img in BOSSWORM_BACK:
            self.wormboss_back.append(pg.image.load(img))
        for img in BOSSWORM_FOR:
            self.wormboss_for.append(pg.image.load(img))
        for img in BOSSWORM_LEFT:
            self.wormboss_left.append(pg.image.load(img))
        for img in BOSSWORM_RIGHT:
            self.wormboss_right.append(pg.image.load(img))
        for img in BOSSWORM_JUMPB:
            self.wormboss_jumpb.append(pg.image.load(img))
        for img in BOSSWORM_JUMPF:
            self.wormboss_jumpf.append(pg.image.load(img))
        for img in BOSSWORM_JUMPL:
            self.wormboss_jumpl.append(pg.image.load(img))
        for img in BOSSWORM_JUMPR:
            self.wormboss_jumpr.append(pg.image.load(img))
        for img in BOSSWORM_DIRT:
            self.wormboss_dirt.append(pg.image.load(img))
        for img in BOSSWORM_INTRO:
            self.wormboss_intro.append(pg.image.load(img))
        for img in WORM_BACK:
            self.worm_back.append(pg.image.load(img))
        for img in WORM_FOR:
            self.worm_for.append(pg.image.load(img))
        for img in WORM_LEFT:
            self.worm_left.append(pg.image.load(img))
        for img in WORM_RIGHT:
            self.worm_right.append(pg.image.load(img))
        for img in WORM_JUMPB:
            self.worm_jumpb.append(pg.image.load(img))
        for img in WORM_JUMPF:
            self.worm_jumpf.append(pg.image.load(img))
        for img in WORM_JUMPL:
            self.worm_jumpl.append(pg.image.load(img))
        for img in WORM_JUMPR:
            self.worm_jumpr.append(pg.image.load(img))
        for img in WORM_DIRT:
            self.worm_dirt.append(pg.image.load(img))
        for img in WORM_DIE:
            self.worm_die.append(pg.image.load(img))
        for img in DORVER:
            self.dorver.append(pg.image.load(img))
        for img in SOLDER_FOR:
            self.solder_for.append(pg.image.load(img))
        for img in SOLDER_BACK:
            self.solder_back.append(pg.image.load(img))
        for img in SOLDER_LEFT:
            self.solder_left.append(pg.image.load(img))
        for img in SOLDER_RIGHT:
            self.solder_right.append(pg.image.load(img))
        for img in BLUE_SPIDER_BACK:
            self.blue_spider_back.append(pg.image.load(img))
        for img in BLUE_SPIDER_RIGHT:
            self.blue_spider_right.append(pg.image.load(img))
        for img in BLUE_SPIDER_LEFT:
            self.blue_spider_left.append(pg.image.load(img))
        for img in BLUE_SPIDER_FOR:
            self.blue_spider_for.append(pg.image.load(img))
        for img in BLUE_SPIDER_DEATH:
            self.blue_spider_death.append(pg.image.load(img))
        for img in GREEN_SPIDER_BACK:
            self.green_spider_back.append(pg.image.load(img))
        for img in GREEN_SPIDER_RIGHT:
            self.green_spider_right.append(pg.image.load(img))
        for img in GREEN_SPIDER_LEFT:
            self.green_spider_left.append(pg.image.load(img))
        for img in GREEN_SPIDER_FOR:
            self.green_spider_for.append(pg.image.load(img))
        for img in GREEN_SPIDER_DEATH:
            self.green_spider_death.append(pg.image.load(img))
        for img in RED_SPIDER_BACK:
            self.red_spider_back.append(pg.image.load(img))
        for img in RED_SPIDER_RIGHT:
            self.red_spider_right.append(pg.image.load(img))
        for img in RED_SPIDER_LEFT:
            self.red_spider_left.append(pg.image.load(img))
        for img in RED_SPIDER_FOR:
            self.red_spider_for.append(pg.image.load(img))
        for img in RED_SPIDER_DEATH:
            self.red_spider_death.append(pg.image.load(img))
        w = 0
        while w < len(self.smoke_screen):
            self.smoke_screen[w] = pg.transform.scale(self.smoke_screen[w], (350, 350))
            w += 1
        w = 0
        while w < len(self.blue_slime_attack):
            self.blue_slime_attack[w] = pg.transform.scale(self.blue_slime_attack[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.blue_slime_death):
            self.blue_slime_death[w] = pg.transform.scale(self.blue_slime_death[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.blue_slime_idle):
            self.blue_slime_idle[w] = pg.transform.scale(self.blue_slime_idle[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.green_slime_attack):
            self.green_slime_attack[w] = pg.transform.scale(self.green_slime_attack[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.green_slime_death):
            self.green_slime_death[w] = pg.transform.scale(self.green_slime_death[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.green_slime_idle):
            self.green_slime_idle[w] = pg.transform.scale(self.green_slime_idle[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.red_slime_attack):
            self.red_slime_attack[w] = pg.transform.scale(self.red_slime_attack[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.red_slime_death):
            self.red_slime_death[w] = pg.transform.scale(self.red_slime_death[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.red_slime_idle):
            self.red_slime_idle[w] = pg.transform.scale(self.red_slime_idle[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.coin):
            if w != 2:
                self.coin[w] = pg.transform.scale(self.coin[w], (20, 15))
            else:
                self.coin[w] = pg.transform.scale(self.coin[w], (10, 15))
            w += 1
        w = 0
        while w < len(self.heart):
            self.heart[w] = pg.transform.scale(self.heart[w], (30, 30))
            w += 1
        w = 0
        while w < len(self.fire):
            self.fire[w] = pg.transform.scale(self.fire[w], (30, 30))
            w += 1
        self.remove = False
        self.map1 = TiledMap(map1)
        self.map1_im = self.map1.make_map(self.remove)
        self.map1_rect = self.map1_im.get_rect()
        self.map2 = TiledMap(map2)
        self.map2_im = self.map2.make_map(self.remove)
        self.map2_rect = self.map2_im.get_rect()
        self.map3 = TiledMap(map3)
        self.map3_im = self.map3.make_map(self.remove)
        self.map3_rect = self.map3_im.get_rect()
        self.map4 = TiledMap(map4)
        self.map4_im = self.map4.make_map(self.remove)
        self.map4_rect = self.map4_im.get_rect()
        self.map5 = TiledMap(map5)
        self.map5_im = self.map5.make_map(self.remove)
        self.map5_rect = self.map5_im.get_rect()
        self.map6 = TiledMap(map6)
        self.map6_im = self.map6.make_map(self.remove)
        self.map6_rect = self.map6_im.get_rect()
        self.map7 = TiledMap(map7)
        self.map7_im = self.map7.make_map(self.remove)
        self.map7_rect = self.map7_im.get_rect()
        self.map8 = TiledMap(map8)
        self.map8_im = self.map8.make_map(self.remove)
        self.map8_rect = self.map8_im.get_rect()
        self.map9 = TiledMap(map9)
        self.map9_im = self.map9.make_map(self.remove)
        self.map9_rect = self.map9_im.get_rect()
        self.heartfull = pg.image.load(HEALTH_HEARTFULL)
        self.heartfull = pg.transform.scale(self.heartfull, (40, 40))
        self.hearthalf = pg.image.load(HEALTH_HEARTHALF)
        self.hearthalf = pg.transform.scale(self.hearthalf, (40, 40))
        self.heartempty = pg.image.load(HEALTH_HEARTEMPTY)
        self.heartempty = pg.transform.scale(self.heartempty, (40, 40))
        self.coinsign = pg.transform.scale(self.coin[0], (40, 40))
        self.angel = pg.image.load(ANGEL)
        self.sword = pg.image.load(SWORD)
        self.pants = pg.image.load(PANTS)
        self.pants = pg.transform.scale(self.pants, (90, 90))
        self.shirt = pg.image.load(SHIRT)
        self.shirt = pg.transform.scale(self.shirt, (90, 90))
        self.helmat = pg.image.load(HELMAT)
        self.helmat = pg.transform.scale(self.helmat, (90, 90))
        self.sword = pg.transform.scale(self.sword, (40, 40))
        self.blank = pg.image.load(BLANK)
        self.bone = pg.image.load(BONE)
        self.bone = pg.transform.scale(self.bone, (24, 24))
        self.bomb = pg.image.load(BOMB)
        self.bomb = pg.transform.scale(self.bomb, (20, 40))
        self.arrow = pg.image.load(ARROW)
        self.swing_sound = pg.mixer.Sound(SWING)
        self.player_die = pg.mixer.Sound(PLAYER_DEATHS)
        self.mob_die = pg.mixer.Sound(MOB_DEATH)
        self.footstep = pg.mixer.Sound(FOOTSTEP)
        self.explosion_sound = pg.mixer.Sound(EXPLOSION_SOUND)
        self.smoke_bomb = pg.image.load(SMOKE_BOMB)
        self.smoke_bomb = pg.transform.scale(self.smoke_bomb, (20, 25))
        self.bow = pg.image.load(BOW)

    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        if self.player2_on == True:
            self.player2_goup = pg.sprite.Group()
        self.player_goup = pg.sprite.Group()
        self.bomb_group = pg.sprite.Group()
        self.smoke_bomb_group = pg.sprite.Group()
        self.smoke_group = pg.sprite.Group()
        self.explosion_group = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mob = pg.sprite.Group()
        self.coin_group = pg.sprite.Group()
        self.heart_group = pg.sprite.Group()
        self.fire_group = pg.sprite.Group()
        self.map1_group = pg.sprite.Group()
        self.map2_group = pg.sprite.Group()
        self.map3_group = pg.sprite.Group()
        self.map4_group = pg.sprite.Group()
        self.map5_group = pg.sprite.Group()
        self.map6_group = pg.sprite.Group()
        self.map7_group = pg.sprite.Group()
        self.map8_group = pg.sprite.Group()
        self.map9_group = pg.sprite.Group()
        self.map10_group = pg.sprite.Group()
        self.map11_group = pg.sprite.Group()
        self.water = pg.sprite.Group()
        self.straw_group = pg.sprite.Group()
        self.sword_group = pg.sprite.Group()
        self.strawb_group = pg.sprite.Group()
        self.bone_group = pg.sprite.Group()
        self.arrow_group = pg.sprite.Group()
        self.helmat_group = pg.sprite.Group()
        self.pants_group = pg.sprite.Group()
        self.shirt_group = pg.sprite.Group()
        self.impfall_group = pg.sprite.Group()

        pg.mixer.music.stop()

        if self.map1_on is True:
            self.new_map1()
        elif self.map2_on is True:
            self.new_map2()
        elif self.map3_on is True:
            self.new_map3()
        elif self.map4_on is True:
            self.new_map4()
        elif self.map5_on is True:
            self.new_map5()
        elif self.map6_on is True:
            self.new_map6()
        elif self.map7_on is True:
            self.new_map7()
        elif self.map8_on is True:
            self.new_map8()
        elif self.map9_on is True:
            self.new_map9()
        elif self.map10_on is True:
            self.new_map10()
        elif self.map11_on is True:
            self.new_map11()

    def run(self):
        while True:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        quit()

    def update(self):
        self.all_sprites.move_to_back(self.player)
        if self.player2_on:
            self.all_sprites.move_to_back(self.player)
        self.all_sprites.update()

        # for m in self.walls:
        #     self.player.unoffset_image()
        #     if m.rect.colliderect((self.player.rect.x - 21, self.player.rect.y - 21,
        #                            self.player.rect.width + 42, self.player.rect.height + 42)) == 1:
        #         self.wall_hit = True
        #     self.player.offset_image()
        # if self.wall_hit is False:
        #     hits = pg.sprite.spritecollide(self.player, self.mob, False, collide_hit_rect)
        #     for m in self.mob:
        #         if hits and m.mob_death is False:
        #             self.player.pos += vec(20, 0).rotate(-hits[0].rot)
        # elif self.wall_hit is True:
        #     self.wall_hit = False


        #todo remove commets
        #if self.health <= 0:
         #   self.show_death_screen()

    def draw(self):
        pg.display.set_caption("{:.2f} fps    VERSION: ALPHA 1.00".format(self.clock.get_fps()))
        pg.display.set_icon(self.back[0])
        if self.map1_on is True:
            self.draw_map1()
        elif self.map2_on is True:
            self.draw_map2()
        elif self.map3_on is True:
            self.draw_map3()
        elif self.map4_on is True:
            self.draw_map4()
        elif self.map5_on is True:
            self.draw_map5()
        elif self.map6_on is True:
            self.draw_map6()
        elif self.map7_on is True:
            self.draw_map7()
        elif self.map8_on is True:
            self.draw_map8()
        elif self.map9_on is True:
            self.draw_map9()
        elif self.map10_on is True:
            self.draw_map10()
        elif self.map11_on is True:
            self.draw_map11()
        self.all_sprites.draw(self.screen)
        self.hud()
       # self.debug()
        pg.display.flip()

    def debug(self):
        self.player.unoffset_image()
        pg.draw.rect(self.screen, WHITE, (self.player.rect.x - 30, self.player.rect.y - 10, self.player.rect.width + 60,
                                          self.player.rect.height + 60), 2)
        if self.player.back_rect is True:
            pg.draw.rect(self.screen, WHITE, (self.player.rect.x - 25, self.player.rect.y + 25,
                                              self.player.rect.width + 50, self.player.rect.height), 2)

        if self.player.for_rect is True:
            pg.draw.rect(self.screen, WHITE, (self.player.rect.x - 25, self.player.rect.y - 25,
                                              self.player.rect.width + 50, self.player.rect.height), 2)

        if self.player.sword_swing_right is True:
            pg.draw.rect(self.screen, WHITE, (self.player.rect.x + 25, self.player.rect.y + 5,
                                              self.player.rect.width + 40, self.player.rect.height - 15), 2)

        if self.player.sword_swing_left is True:
            pg.draw.rect(self.screen, WHITE, (self.player.rect.x - 70, self.player.rect.y + 5,
                                              self.player.rect.width + 36, self.player.rect.height - 15), 2)

        for i in self.mob:
            pg.draw.rect(self.screen, WHITE, (i.rect.x, i.rect.y, i.rect.width, i.rect.height), 2)
        self.player.offset_image()

        for i in self.bomb_group:
            pg.draw.rect(self.screen, WHITE, (i.rect.x - 40, i.rect.y - 30, i.rect.width + 80, i.rect.height + 80), 2)

        for i in self.smoke_group:
            pg.draw.rect(self.screen, WHITE, (i.rect.x + 40, i.rect.y + 20, i.rect.width - 80, i.rect.height - 40), 2)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.quit()
                if event.key == pg.K_ESCAPE:
                    self.pause_menu()
            if event.type == pg.JOYBUTTONDOWN:
                if self.got_sword is True and self.player.sword_swing_back is False and self.player.sword_swing_forward is False and \
                        self.player.sword_swing_left is False and self.player.sword_swing_right is False:
                    if self.joy.get_button(0) == 1:
                        self.swing_sound.play()
                        if self.player.forward_on is True:
                            self.player.sword_swing_back = True
                            self.player.for_rect = True
                        elif self.player.back_on is True:
                            self.player.sword_swing_forward = True
                            self.player.back_rect = True
                        elif self.player.left_on is True:
                            self.player.left_rect = True
                            self.player.sword_swing_left = True
                        elif self.player.right_on is True:
                            self.player.sword_swing_right = True
                            self.player.right_rect = True
            if event.type == pg.JOYHATMOTION:
                if self.player.sword_swing_back is False and self.player.sword_swing_forward is False and self.player.sword_swing_left is False and \
                        self.player.sword_swing_right is False:
                    if self.joy.get_hat(0) == (0, 1):
                        self.player.joy_for = True
                    elif self.joy.get_hat(0) == (0, -1):
                        self.player.joy_back = True
                    elif self.joy.get_hat(0) == (1, 0):
                        self.player.joy_right = True
                    elif self.joy.get_hat(0) == (-1, 0):
                        self.player.joy_left = True
                    elif self.joy.get_hat(0) == (0, 0):
                        self.player.joy_for = False
                        self.player.joy_back = False
                        self.player.joy_right = False
                        self.player.joy_left = False
            if event.type == pg.JOYAXISMOTION:
                if self.player.sword_swing_back is False and self.player.sword_swing_forward is False and self.player.sword_swing_left is False and \
                        self.player.sword_swing_right is False:
                    if self.joy.get_axis(1) < -0.5:
                        self.player.joy_for = True
                        self.player.joy_back = False
                        self.player.joy_left = False
                        self.player.joy_right = False
                    if self.joy.get_axis(1) > 0.5:
                        self.player.joy_back = True
                        self.player.joy_left = False
                        self.player.joy_right = False
                        self.player.joy_for = False
                    if self.joy.get_axis(0) > 0.5:
                        self.player.joy_right = True
                        self.player.joy_left = False
                        self.player.joy_for = False
                        self.player.joy_back = False
                    if self.joy.get_axis(0) < -0.5:
                        self.player.joy_left = True
                        self.player.joy_right = False
                        self.player.joy_for = False
                        self.player.joy_back = False
                    if self.joy.get_axis(0) == 0.0:
                        self.player.joy_left = False
                        self.player.joy_right = False
                    if self.joy.get_axis(1) == 0.0:
                        self.player.joy_for = False
                        self.player.joy_back = False

    def hud(self):
        if self.sword_on is True:
            pg.draw.rect(self.screen, BLACK, (600, 10, 40, 50))
            self.screen.blit(self.sword, (601, 14))
        elif self.bow_on is True:
            pg.draw.rect(self.screen, BLACK, (600, 10, 40, 50))
            self.screen.blit(self.bow, (590, 4))
        pg.draw.rect(self.screen, WHITE, (600, 10, 40, 50), 2)
        if self.bomb_on is True:
            pg.draw.rect(self.screen, BLACK, (700, 10, 40, 50))
            self.screen.blit(self.bomb, (710, 11))
        elif self.smokebomb_on is True:
            pg.draw.rect(self.screen, BLACK, (700, 10, 40, 50))
            self.screen.blit(self.smoke_bomb, (710, 20))
        pg.draw.rect(self.screen, WHITE, (700, 10, 40, 50), 2)
        self.screen.blit(self.coinsign, (1050, 20))
        textsurface = self.myfont.render('{}'.format(self.money), False, (0, 0, 0))
        self.screen.blit(textsurface, (1100, 15))
        if self.max_health == 300:
            if self.health == 300:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
            elif self.health == 250:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.hearthalf, (200, 20))
            elif self.health == 200:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
            elif self.health == 150:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.hearthalf, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
            elif self.health == 100:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
            elif self.health == 50:
                self.screen.blit(self.hearthalf, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
            elif self.health == 0:
                self.screen.blit(self.heartempty, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
        elif self.max_health == 400:
            if self.health == 400:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
            elif self.health == 350:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.hearthalf, (250, 20))
            elif self.health == 300:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 250:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.hearthalf, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 200:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 150:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.hearthalf, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 100:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 50:
                self.screen.blit(self.hearthalf, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
            elif self.health == 0:
                self.screen.blit(self.heartempty, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
        elif self.max_health == 500:
            if self.health == 500:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartfull, (300, 20))
            elif self.health == 450:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.hearthalf, (300, 20))
            elif self.health == 400:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 350:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.hearthalf, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 300:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 250:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.hearthalf, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 200:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 150:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.hearthalf, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 100:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 50:
                self.screen.blit(self.hearthalf, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
            elif self.health == 0:
                self.screen.blit(self.heartempty, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
        elif self.max_health == 600:
            if self.health == 600:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartfull, (300, 20))
                self.screen.blit(self.heartfull, (350, 20))
            elif self.health == 550:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartfull, (300, 20))
                self.screen.blit(self.hearthalf, (350, 20))
            elif self.health == 500:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartfull, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 450:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.hearthalf, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 400:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartfull, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 350:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.hearthalf, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 300:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartfull, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 250:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.hearthalf, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 200:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartfull, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 150:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.hearthalf, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 100:
                self.screen.blit(self.heartfull, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 50:
                self.screen.blit(self.hearthalf, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))
            elif self.health == 0:
                self.screen.blit(self.heartempty, (100, 20))
                self.screen.blit(self.heartempty, (150, 20))
                self.screen.blit(self.heartempty, (200, 20))
                self.screen.blit(self.heartempty, (250, 20))
                self.screen.blit(self.heartempty, (300, 20))
                self.screen.blit(self.heartempty, (350, 20))

    def new_map1(self):
        if self.map1_straw is False:
            self.map1_im = self.map1.make_map(True)
        pg.mixer.music.load(STRAW_MUSIC)
        pg.mixer.music.play(-1)
        for tile_object in self.map1.tmxdata.objects:
            if tile_object.name == 'player':
                if self.map2_to_map1 is False and self.map3_to_map1 is False:
                    self.player = Player(self, tile_object.x, tile_object.y, "1")
                    if self.player2_on is True:
                        self.player = Player(self, tile_object.x+10, tile_object.y, "2")
            if tile_object.name == 'playerfrommap2':
                if self.map2_to_map1 is True and self.map3_to_map1 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map2_to_map1 = False
            if tile_object.name == 'playerfrommap3':
                if self.map3_to_map1 is True and self.map2_to_map1 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map3_to_map1 = False
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map1_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin1':
                if self.map1_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map1_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart':
                if self.map1_heart is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'fire':
                Fire(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map2':
                Map2(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map3':
                Map3(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'straw' and self.map1_straw is True:
                Straw(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'breakable' and self.map1_straw is True:
                Strawb(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'goblin':
                if self.got_sword is True and self.map1_enemies is True:
                    pass
                Goblin(self, tile_object.x, tile_object.y)

    def new_map2(self):
        self.map2_to_map1 = True
        self.map2_im = self.map2.make_map(True)
        pg.mixer.music.load(CAVE_MUSIC)
        pg.mixer.music.play(-1)
        for tile_object in self.map2.tmxdata.objects:
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map2_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y, "1")
            if tile_object.name == 'coin' and self.map2_coin is True:
                Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart':
                Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'fire':
                Fire(self, tile_object.x, tile_object.y)
            if tile_object.name == 'sword':
                if self.got_sword is False:
                    Sword(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'straw' and self.map2_straw is True:
                Straw(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'strawb' and self.map2_straw is True:
                Strawb(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'change':
                Map1(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map3(self):
        pg.mixer.music.load(STRAW_MUSIC)
        pg.mixer.music.play(-1)
        self.map3_to_map1 = True
        for tile_object in self.map3.tmxdata.objects:
            if tile_object.name == 'heart':
                if self.map3_heart is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map3_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map4_to_map3 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap4':
                if self.map4_to_map3 is True:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map4_to_map3 = False
            if tile_object.name == 'coin1':
                if self.map3_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map3_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map3_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map3_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map3_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map1':
                Map1(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map4':
                Map4(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'goblin':
                if self.got_sword is True and self.map3_enemies is True:
                    Goblin(self, tile_object.x, tile_object.y)

    def new_map4(self):
        pg.mixer.music.load(LAKE_MUSIC)
        pg.mixer.music.play(-1)
        self.map4_to_map3 = True
        for tile_object in self.map4.tmxdata.objects:
            if tile_object.name == 'heart1':
                if self.map4_heart1 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart2':
                if self.map4_heart2 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map4_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map5_to_map4 is False and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap5':
                if self.map5_to_map4 is True and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map5_to_map4 = False
            if tile_object.name == 'playerfrommap6':
                if self.map6_to_map4 is True and self.map5_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map6_to_map4 = False
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map3':
                Map3(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map5':
                Map5(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map4_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map5(self):
        self.map5_to_map4 = True
        for tile_object in self.map5.tmxdata.objects:
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map4_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map5_to_map4 is False and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap5':
                if self.map5_to_map4 is True and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map5_to_map4 = False
            if tile_object.name == 'playerfrommap6':
                if self.map6_to_map4 is True and self.map5_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map6_to_map4 = False
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map5':
                Map5(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map4_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map6(self):
        pg.mixer.music.load(LAKE_MUSIC)
        pg.mixer.music.play(-1)
        self.map6_to_map4 = True
        for tile_object in self.map6.tmxdata.objects:
            if tile_object.name == 'heart1':
                if self.map6_heart1 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart2':
                if self.map6_heart2 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart3':
                if self.map6_heart3 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map4_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map7_to_map6 is False and self.map8_to_map6 is False and self.map9_to_map6 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap7':
                if self.map7_to_map6 is True and self.map8_to_map6 is False and self.map9_to_map6 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map7_to_map6 = False
            if tile_object.name == 'playerfrommap8':
                if self.map8_to_map6 is True and self.map7_to_map6 is False  and self.map9_to_map6 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map8_to_map6 = False
            if tile_object.name == 'playerfrommap9':
                if self.map9_to_map6 is True and self.map7_to_map6 is False and self.map8_to_map6 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map9_to_map6 = False
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map4':
                Map4(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map7':
                Map7(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map8':
                Map8(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map9':
                Map9(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map4_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'goblin':
                if self.got_sword is True and self.map4_enemies is True:
                    Goblin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'goblinfall':
                Imp_Fall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map7(self):
        pg.mixer.music.load(CAVE_MUSIC)
        pg.mixer.music.play(-1)
        self.map7_to_map6 = True
        for tile_object in self.map7.tmxdata.objects:
            if tile_object.name == 'heart':
                if self.map7_heart is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map7_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map7_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'helmat':
                Helmat(self, tile_object.x, tile_object.y)
            if tile_object.name == 'imp':
                if self.got_sword is True and self.map7_enemies is True:
                    Imp(self, tile_object.x, tile_object.y)
            if tile_object.name == 'impfall':
                Imp_Fall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map8(self):
        pg.mixer.music.load(CAVE_MUSIC)
        pg.mixer.music.play(-1)
        self.map8_to_map6 = True
        for tile_object in self.map8.tmxdata.objects:
            if tile_object.name == 'heart':
                if self.map8_heart is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map8_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
               self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map8_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'pants':
                Pants(self, tile_object.x, tile_object.y)
            if tile_object.name == 'imp':
                if self.got_sword is True and self.map8_enemies is True:
                    Imp(self, tile_object.x, tile_object.y)
            if tile_object.name == 'impfall':
                Imp_Fall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map9(self):
        pg.mixer.music.load(CAVE_MUSIC)
        pg.mixer.music.play(-1)
        self.map9_to_map6 = True
        for tile_object in self.map9.tmxdata.objects:
            if tile_object.name == 'heart1':
                if self.map9_heart1 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'heart2':
                if self.map9_heart2 is True:
                    Heart(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map9_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map9_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'shirt':
                Shirt(self, tile_object.x, tile_object.y)
            if tile_object.name == 'imp':
                if self.got_sword is True and self.map9_enemies is True:
                    Imp(self, tile_object.x, tile_object.y)
            if tile_object.name == 'impfall':
                Imp_Fall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map10(self):
        for tile_object in self.map10.tmxdata.objects:
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map4_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map5_to_map4 is False and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap5':
                if self.map5_to_map4 is True and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map5_to_map4 = False
            if tile_object.name == 'playerfrommap6':
                if self.map6_to_map4 is True and self.map5_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map6_to_map4 = False
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map5':
                Map5(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map4_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def new_map11(self):
        for tile_object in self.map11.tmxdata.objects:
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'slime':
                if self.got_sword is True and self.map4_enemies is True:
                    Slime(self, tile_object.x, tile_object.y)
            if tile_object.name == 'player':
                if self.map5_to_map4 is False and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'playerfrommap5':
                if self.map5_to_map4 is True and self.map6_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map5_to_map4 = False
            if tile_object.name == 'playerfrommap6':
                if self.map6_to_map4 is True and self.map5_to_map4 is False:
                    self.player = Player(self, tile_object.x, tile_object.y)
                    self.map6_to_map4 = False
            if tile_object.name == 'coin1':
                if self.map4_coin1 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin2':
                if self.map4_coin2 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin3':
                if self.map4_coin3 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'coin4':
                if self.map4_coin4 is True:
                    Coin(self, tile_object.x, tile_object.y)
            if tile_object.name == 'map5':
                Map5(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'map6':
                Map6(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'skeleton':
                if self.got_sword is True and self.map4_enemies is True:
                    Skeleton(self, tile_object.x, tile_object.y)
            if tile_object.name == 'water':
                Water(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def draw_map1(self):
        self.screen.blit(self.map1_im, (self.map1_rect.x, self.map1_rect.y))

    def draw_map2(self):
        self.screen.blit(self.map2_im, (self.map2_rect.x, self.map2_rect.y))

    def draw_map3(self):
        self.screen.blit(self.map3_im, (self.map3_rect.x, self.map3_rect.y))

    def draw_map4(self):
        self.screen.blit(self.map4_im, (self.map4_rect.x, self.map4_rect.y))

    def draw_map5(self):
        self.screen.blit(self.map5_im, (self.map5_rect.x, self.map5_rect.y))

    def draw_map6(self):
        self.screen.blit(self.map6_im, (self.map6_rect.x, self.map6_rect.y))

    def draw_map7(self):
        self.screen.blit(self.map7_im, (self.map7_rect.x, self.map7_rect.y))

    def draw_map8(self):
        self.screen.blit(self.map8_im, (self.map8_rect.x, self.map8_rect.y))

    def draw_map9(self):
        self.screen.blit(self.map9_im, (self.map9_rect.x, self.map9_rect.y))

    def draw_map10(self):
        self.screen.blit(self.map10_im, (self.map10_rect.x, self.map10_rect.y))

    def draw_map11(self):
        self.screen.blit(self.map11_im, (self.map11_rect.x, self.map11_rect.y))

    def map2_cutscean(self):
        self.got_sword = True
        self.sword_on = True
        while True:
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            keyss = pg.key.get_pressed()
            if keyss[pg.K_SPACE]:
                for tile_object in self.map2.tmxdata.objects:
                    if tile_object.name == 'slime':
                        if self.got_sword is True:
                            Slime(self, tile_object.x, tile_object.y)
                self.map2_im = self.map2.make_map(False)
                break
            self.screen.blit(self.angel, (520, 350))
            textsurface = self.angelfont.render("Those who are able to wield that sword", False, (43, 86, 226))
            self.screen.blit(textsurface, (400, 240))
            textsurfaces = self.angelfont.render("must remove the curse plaguing this land.", False, (43, 86, 226))
            self.screen.blit(textsurfaces, (400, 270))
            textsurfacee = self.angelfont.render("Press the space bar to swing it.", False, (43, 86, 226))
            self.screen.blit(textsurfacee, (400, 300))
            pg.display.update()
            self.clock.tick(60)


    def show_menu(self):
        bk = pg.image.load('assets/menu/background.png')
        time = 0
        last_time = 0
        dt = self.clock.tick(FPS) / 1000
        pg.mixer.music.load(MENU_MUSIC)
        pg.mixer.music.play(-1)
        self.break_me = False
        while True:
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if self.break_me is True:
                break
            for event in pg.event.get():
                if event.type == pg.JOYBUTTONDOWN:
                    if self.joy.get_button(0) == 1:
                        pg.mixer.music.stop()
                        self.break_me = True
                if event.type == pg.JOYAXISMOTION:
                    print(self.joy.get_axis(0), self.joy.get_axis(1))
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            keyss = pg.key.get_pressed()
            if keyss[pg.K_SPACE]:
                pg.mixer.music.stop()
                break
            elif keyss[pg.K_f]:
                if self.screen.get_flags() & pg.FULLSCREEN:
                    pg.display.set_mode((WIDTH, HEIGHT))
                else:
                    pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
            self.screen.blit(bk, (0, 0))
            textsurfacee = self.myfont.render("Welcome!", False, (255, 255, 255))
            self.screen.blit(textsurfacee, (550, 100))
            texstsurfacee = self.myfont.render("Press space to begin or click button", False, (255, 255, 255))
            self.screen.blit(texstsurfacee, (150, 180))

            if time > 100:
                pg.draw.rect(self.screen, GREEN, (450, 250, 180, 80))
            else:
                pg.draw.rect(self.screen, DARKGREEN, (450, 250, 180, 80))

            if time > 200:
                time = 0
            if 450 + 180 > mouse[0] > 450 and 250 + 80 > mouse[1] > 250:
                if click[0] == 1:
                    self.player2_on = True
                    pg.mixer.music.stop()
                    break
            textsurqfacee = self.myfont.render("START", False, (0, 0, 0))
            self.screen.blit(textsurqfacee, (450, 265))
            time += dt
            pg.display.update()
            self.clock.tick(60)

    def show_death_screen(self):
        time = 0
        dt = self.clock.tick(FPS) / 1000
        while True:
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            textsurfacee = self.myfont.render("GAME OVER", False, (255, 255, 255))
            self.screen.blit(textsurfacee, (550, 100))
            texstsurfacee = self.myfont.render("Press space to begin or click button", False, (255, 255, 255))
            self.screen.blit(texstsurfacee, (150, 180))

            if time > 100:
                pg.draw.rect(self.screen, GREEN, (450, 250, 260, 80))
            else:
                pg.draw.rect(self.screen, DARKGREEN, (450, 250, 260, 80))
            textsurqfacee = self.myfont.render("RESTART", False, (0, 0, 0))
            self.screen.blit(textsurqfacee, (450, 265))

            if time > 200:
                time = 0
            if 450 + 260 > mouse[0] > 450 and 250 + 80 > mouse[1] > 250:
                if click[0] == 1:
                    self.load_data()
                    self.new()
                    self.run()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            keyss = pg.key.get_pressed()
            if keyss[pg.K_SPACE]:
                self.load_data()
                self.new()
                self.run()
            time += dt
            pg.display.update()
            self.clock.tick(60)

    def pause_menu(self):
        time = 0
        dt = self.clock.tick(FPS) / 1000
        sword = pg.image.load(SWORD)
        bow = pg.image.load(BOW)
        while True:
            self.hud()
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            textsurfacee = self.myfont.render("Paused", False, (255, 255, 255))
            self.screen.blit(textsurfacee, (550, 100))
            texstsurfacee = self.myfont.render("Press space to begin or click button", False, (255, 255, 255))
            self.screen.blit(texstsurfacee, (150, 180))
            if self.sword_on is True and self.bow_on is False and self.got_bow is True:
                pg.draw.rect(self.screen, BLACK, (600, 60, 40, 50))
                self.screen.blit(bow, (590, 55))

            if self.bow_on is True and self.sword_on is False and self.got_sword is True:
                pg.draw.rect(self.screen, BLACK, (600, 60, 40, 50))
                self.screen.blit(sword, (610, 65))

            if self.smokebomb_on is True:
                pg.draw.rect(self.screen, BLACK, (700, 60, 45, 45))
                self.screen.blit(self.bomb, (710, 60))

            if self.bomb_on is True:
                pg.draw.rect(self.screen, BLACK, (700, 60, 45, 45))
                self.screen.blit(self.smoke_bomb, (710, 68))

            if time > 100:
                pg.draw.rect(self.screen, GREEN, (450, 250, 260, 80))
            else:
                pg.draw.rect(self.screen, DARKGREEN, (450, 250, 260, 80))
            textsurqfacee = self.myfont.render("Resume", False, (0, 0, 0))
            self.screen.blit(textsurqfacee, (450, 265))

            if time > 200:
                time = 0
            if 450 + 260 > mouse[0] > 450 and 250 + 80 > mouse[1] > 250:
                if click[0] == 1:
                    break
            if 590 + 60 > mouse[0] > 590 and 55 + 80 > mouse[1] > 55 and self.sword_on is True and self.bow_on is False:
                if click[0] == 1:
                    self.sword_on = False
                    self.bow_on = True
            elif 590 + 60 > mouse[0] > 590 and 55 + 80 > mouse[1] > 55 and self.bow_on is True and self.sword_on is False:
                if click[0] == 1:
                    self.bow_on = False
                    self.sword_on = True

            if 710 + 20 > mouse[0] > 710 and 60 + 30 > mouse[1] > 60 and self.bomb_on is True and self.smokebomb_on is False:
                if click[0] == 1:
                    self.bomb_on = False
                    self.smokebomb_on = True
            elif 710 + 20 > mouse[0] > 590 and 68 + 30 > mouse[1] > 68 and self.smokebomb_on is True and self.bomb_on is False:
                if click[0] == 1:
                    self.bomb_on = True
                    self.smokebomb_on = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            keyss = pg.key.get_pressed()
            if keyss[pg.K_SPACE]:
                break

            time += dt
            pg.display.update()
            self.clock.tick(60)


g = Game()
g.show_menu()
while True:
    g.new()
    g.run()
