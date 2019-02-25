from settings import *
from save import *
vec = pg.math.Vector2
import pygame as pg
from random import uniform, choice

#TODO make health loss and gain for only one character by if i.playernum == "1" or "2" then lower or increse that health
#TODO twick multiplier little more
#TODO fix bug that crashes game when enemny drops a heart or coin

def enemy_hit(sprite, game):
    for i in game.player_group:
        if i.back_rect is True:
            if sprite.rect.colliderect((i.rect.x - 25, i.rect.y + 25,
                                        i.rect.width + 50, i.rect.height)) == 1:
                if sprite.being_attacked is False:
                    sprite.health -= 50
                    sprite.pos = vec(sprite.pos.x,sprite.pos.y + sprite.knockback)
                    sprite.being_attacked = True
        if i.for_rect is True:
            if sprite.rect.colliderect((i.rect.x - 25, i.rect.y - 25,
                                        i.rect.width + 50, i.rect.height)) == 1:
                if sprite.being_attacked is False:
                    sprite.health -= 50
                    sprite.pos = vec(sprite.pos.x, sprite.pos.y - sprite.knockback)
                    sprite.being_attacked = True
        if i.sword_swing_right is True:
            if sprite.rect.colliderect((i.rect.x + 25, i.rect.y + 5,
                                        i.rect.width + 40, i.rect.height - 15)) == 1:
                if sprite.being_attacked is False:
                    sprite.health -= 50
                    sprite.pos = vec(sprite.pos.x + sprite.knockback,sprite.pos.y)
                    sprite.being_attacked = True
        if i.sword_swing_left is True:
            if sprite.rect.colliderect((i.rect.x - 70, i.rect.y + 5,
                                        i.rect.width + 36, i.rect.height - 15)) == 1:
                if sprite.being_attacked is False:
                    sprite.health -= 50
                    sprite.pos = vec(sprite.pos.x - sprite.knockback,sprite.pos.y)
                    sprite.being_attacked = True

def collision(sprite, group, dirs):
    if dirs == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2
            sprite.vel.x = 0
            sprite.rect.centerx = sprite.pos.x
    if dirs == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centery > sprite.rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height / 2
            if hits[0].rect.centery < sprite.rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.rect.height / 2
            sprite.vel.y = 0
            sprite.rect.centery = sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, player_num):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.player_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0
        self.current_sword = 0
        if self.game.got_pants is False and self.game.got_hat is False and self.game.got_shirt is False:
            self.image = game.forward[self.current_frame]
        elif self.game.got_pants is True and self.game.got_hat is False and self.game.got_shirt is False:
            self.image = game.pants_forward[self.current_frame]
        elif self.game.got_pants is True and self.game.got_hat is True and self.game.got_shirt is False:
            self.image = game.helmatNpants_forward[self.current_frame]
        elif self.game.got_pants is False and self.game.got_hat is True and self.game.got_shirt is False:
            self.image = game.helmat_forward[self.current_frame]
        elif self.game.got_pants is False and self.game.got_hat is False and self.game.got_shirt is True:
            self.image = game.shirt_forward[self.current_frame]
        elif self.game.got_pants is True and self.game.got_hat is False and self.game.got_shirt is True:
            self.image = game.shirtNpants_forward[self.current_frame]
        elif self.game.got_pants is False and self.game.got_hat is True and self.game.got_shirt is True:
            self.image = game.helmatNpants_forward[self.current_frame]
        elif self.game.got_pants is True and self.game.got_hat is True and self.game.got_shirt is True:
            self.image = game.fullamour_forward[self.current_frame]
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.back_on = False
        self.forward_on = True
        self.left_on = False
        self.right_on = False
        self.sword_swing_left = False
        self.sword_swing_right = False
        self.sword_swing_back = False
        self.sword_swing_forward = False
        self.bow_left = False
        self.bow_right = False
        self.bow_back = False
        self.bow_forward = False
        self.being_attacked = False
        self.damage_time = 0
        self.map1_on = True
        self.map2_on = False
        self.left_rect = False
        self.right_rect = False
        self.for_rect = False
        self.back_rect = False
        self.joy_for = False
        self.joy_back = False
        self.joy_left = False
        self.joy_right = False
        self.nor_rect = self.rect
        self.r_rect = self.rect
        self.wall_hit = False
        self.bomb_droped = False
        self.bomb_time = 0
        self.bow_frame = 0
        self.visible = True
        self.player_num = player_num
        self.SPEED = SPEED

    def get_keys(self):
        for i in self.game.player_group:
            if i.player_num == "1":
                i.vel = vec(0, 0)
                keys = pg.key.get_pressed()
                if i.sword_swing_back is False and i.sword_swing_forward is False and i.sword_swing_left is False and \
                        i.sword_swing_right is False and i.bow_left is False and i.bow_right is False and \
                        i.bow_back is False and i.bow_forward is False:
                    if keys[pg.K_e]:
                        if i.game.player_bombs > 0 and i.bomb_droped is False:
                            if i.game.smokebomb_on is True:
                                Smoke_Bomb(i.game, i.pos)
                                i.game.player_smoke_bombs -= 1
                                i.bomb_droped = True
                            elif i.game.bomb_on is True:
                                Bomb(i.game, i.pos)
                                i.game.player_bombs -= 1
                                i.bomb_droped = True
                    if keys[pg.K_w] or i.joy_for is True:

                        i.vel.y = -i.SPEED
                        if i.forward_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = False
                        i.right_on = False
                        i.forward_on = True
                    elif keys[pg.K_s] or i.joy_back is True:

                        i.vel.y = i.SPEED
                        if i.back_on is True:
                            i.current_frame += 1
                        i.back_on = True
                        i.left_on = False
                        i.right_on = False
                        i.forward_on = False
                    elif keys[pg.K_d] or i.joy_right is True:

                        i.vel.x = i.SPEED
                        if i.right_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = False
                        i.right_on = True
                        i.forward_on = False
                    elif keys[pg.K_a] or i.joy_left is True:

                        i.vel.x = -i.SPEED
                        if i.left_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = True
                        i.right_on = False
                        i.forward_on = False
                if keys[pg.K_q]:
                    pg.quit()
                elif keys[pg.K_f]:
                    if i.game.screen.get_flags() & pg.FULLSCREEN:
                        pg.display.set_mode((WIDTH, HEIGHT))
                    else:
                        pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
                if (i.game.got_sword is True or i.game.got_bow) and i.sword_swing_back is False and \
                        i.sword_swing_forward is False and i.sword_swing_left is False and \
                        i.sword_swing_right is False and i.bow_left is False and \
                        i.bow_right is False and i.bow_back is False and i.bow_forward is False:
                    if keys[pg.K_SPACE]:

                        #for m in i.game.mob:
                         #   if i.rect.colliderect((m.rect.x - 30, m.rect.y - 30, m.rect.width + 60, m.rect.height + 60)) == 1:
                          #      m.death()
                        if i.forward_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 30, i.game.player.rect.y - 30,
                                                       i.game.player.rect.width + 50, i.game.player.rect.height + 10)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_back = True
                                    i.for_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on:
                                i.bow_forward = True

                        elif i.back_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 30, i.game.player.rect.y + 30,
                                                           i.game.player.rect.width + 50, i.game.player.rect.height + 5)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_forward = True
                                    i.back_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_back = True

                        elif i.left_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 70, i.game.player.rect.y + 5,
                                                          i.game.player.rect.width + 36,
                                                          i.game.player.rect.height - 15)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.left_rect = True
                                    i.sword_swing_left = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_left = True

                        elif i.right_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x + 25, i.game.player.rect.y + 5,
                                                      i.game.player.rect.width + 40, i.game.player.rect.height - 15)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_right = True
                                    i.right_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_right = True
            if i.player_num == "2":
                i.vel = vec(0, 0)
                keys = pg.key.get_pressed()
                if i.sword_swing_back is False and i.sword_swing_forward is False and i.sword_swing_left is False and \
                        i.sword_swing_right is False and i.bow_left is False and i.bow_right is False and \
                        i.bow_back is False and i.bow_forward is False:
                    if keys[pg.K_PERIOD]:
                        if i.game.player_bombs > 0 and i.bomb_droped is False:
                            if i.game.smokebomb_on is True:
                                Smoke_Bomb(i.game, i.pos)
                                i.game.player_smoke_bombs -= 1
                                i.bomb_droped = True
                            elif i.game.bomb_on is True:
                                Bomb(i.game, i.pos)
                                i.game.player_bombs -= 1
                                i.bomb_droped = True
                    if keys[pg.K_UP] or i.joy_for is True:

                        i.vel.y = -i.SPEED
                        if i.forward_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = False
                        i.right_on = False
                        i.forward_on = True
                    elif keys[pg.K_DOWN] or i.joy_back is True:

                        i.vel.y = i.SPEED
                        if i.back_on is True:
                            i.current_frame += 1
                        i.back_on = True
                        i.left_on = False
                        i.right_on = False
                        i.forward_on = False
                    elif keys[pg.K_RIGHT] or i.joy_right is True:

                        i.vel.x = i.SPEED
                        if i.right_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = False
                        i.right_on = True
                        i.forward_on = False
                    elif keys[pg.K_LEFT] or i.joy_left is True:

                        i.vel.x = -i.SPEED
                        if i.left_on is True:
                            i.current_frame += 1
                        i.back_on = False
                        i.left_on = True
                        i.right_on = False
                        i.forward_on = False
                if keys[pg.K_q]:
                    pg.quit()
                elif keys[pg.K_f]:
                    if i.game.screen.get_flags() & pg.FULLSCREEN:
                        pg.display.set_mode((WIDTH, HEIGHT))
                    else:
                        pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
                if (i.game.got_sword is True or i.game.got_bow) and i.sword_swing_back is False and \
                        i.sword_swing_forward is False and i.sword_swing_left is False and \
                        i.sword_swing_right is False and i.bow_left is False and \
                        i.bow_right is False and i.bow_back is False and i.bow_forward is False:
                    if keys[pg.K_PAGEDOWN]:

                        # for m in i.game.mob:
                        #   if i.rect.colliderect((m.rect.x - 30, m.rect.y - 30, m.rect.width + 60, m.rect.height + 60)) == 1:
                        #      m.death()
                        if i.forward_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 30, i.game.player.rect.y - 30,
                                                           i.game.player.rect.width + 50,
                                                           i.game.player.rect.height + 10)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_back = True
                                    i.for_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on:
                                i.bow_forward = True

                        elif i.back_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 30, i.game.player.rect.y + 30,
                                                           i.game.player.rect.width + 50,
                                                           i.game.player.rect.height + 5)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_forward = True
                                    i.back_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_back = True

                        elif i.left_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x - 70, i.game.player.rect.y + 5,
                                                           i.game.player.rect.width + 36,
                                                           i.game.player.rect.height - 15)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.left_rect = True
                                    i.sword_swing_left = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_left = True

                        elif i.right_on is True:
                            if i.game.sword_on is True:
                                for m in i.game.walls:
                                    i.unoffset_image()
                                    if m.rect.colliderect((i.game.player.rect.x + 25, i.game.player.rect.y + 5,
                                                           i.game.player.rect.width + 40,
                                                           i.game.player.rect.height - 15)) == 1:
                                        i.wall_hit = True
                                    i.offset_image()
                                if i.wall_hit is False:
                                    i.game.swing_sound.play()
                                    i.sword_swing_right = True
                                    i.right_rect = True
                                elif i.wall_hit is True:
                                    i.wall_hit = False
                            elif i.game.bow_on is True:
                                i.bow_right = True

    def update(self):
        for e in self.game.player_group:
            e.get_keys()
            if len(e.game.smoke_group) == 0:
               e.visible = True
            for i in e.game.smoke_group:
               if e.rect.colliderect(i.rect.x + 40, i.rect.y + 20, i.rect.width - 80, i.rect.height - 40) == 1:
                   e.visible = False
               else:
                   e.visible = True
            if e.current_frame >= 80:
                e.current_frame = 0
            if e.current_sword >= 36:
                e.current_sword = 0
                e.sword_swing_back = False
                e.sword_swing_forward = False
                e.sword_swing_left = False
                e.sword_swing_right = False
                e.left_rect = False
                e.right_rect = False
                e.for_rect = False
                e.back_rect = False
            if e.bow_frame >= 84:
                e.bow_frame = 0
                e.bow_right = False
                e.bow_left = False
                e.bow_forward = False
                e.bow_back = False
            if e.bow_frame >= 63:
                if e.game.arrows > 0:
                    Arrow(e.game, e.pos)
                    e.game.arrows -= 1
            if e.game.got_pants is False and e.game.got_hat is False and e.game.got_shirt is False:
                if e.forward_on is True:
                    e.image = e.game.forward[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.back[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.sword_back[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.sword_forward[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.sword_left[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.sword_right[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is True and e.game.got_hat is False and e.game.got_shirt is False:
                if e.forward_on is True:
                    e.image = e.game.pants_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.pants_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.pants_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.pants_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.pants_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.pants_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.pants_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.pants_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.pants_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.pants_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.pants_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.pants_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is True and e.game.got_hat is True and e.game.got_shirt is False:
                if e.forward_on is True:
                    e.image = e.game.helmatNpants_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.helmatNpants_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.helmatNpants_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.helmatNpants_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.helmatNpants_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.helmatNpants_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.helmatNpants_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.helmatNpants_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.hnp_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.hnp_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.hnp_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.hnp_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is True and e.game.got_hat is False and e.game.got_shirt is True:
                if e.forward_on is True:
                    e.image = e.game.shirtNpants_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.shirtNpants_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.shirtNpants_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.shirtNpants_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.shirtNpants_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.shirtNpants_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.shirtNpants_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.shirtNpants_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.snp_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.snp_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.snp_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.snp_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is False and e.game.got_hat is True and e.game.got_shirt is True:
                if e.forward_on is True:
                    e.image = e.game.helmatNshirt_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.helmatNshirt_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.helmatNshirt_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.helmatNshirt_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.helmatNshirt_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.helmatNshirt_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.helmatNshirt_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.helmatNshirt_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.hns_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.hns_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.hns_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.hns_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is False and e.game.got_hat is False and e.game.got_shirt is True:
                if e.forward_on is True:
                    e.image = e.game.shirt_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.shirt_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.shirt_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.shirt_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.shirt_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.shirt_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.shirt_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.shirt_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.shirt_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.shirt_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.shirt_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.shirt_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is False and e.game.got_hat is True and e.game.got_shirt is False:
                if e.forward_on is True:
                    e.image = e.game.helmat_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.helmat_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.helmat_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.helmat_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.helmat_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.helmat_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.helmat_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.helmat_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.helmat_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.helmat_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.helmat_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.helmat_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            elif e.game.got_pants is True and e.game.got_hat is True and e.game.got_shirt is True:
                if e.forward_on is True:
                    e.image = e.game.fullamour_back[e.current_frame//10]
                elif e.back_on is True:
                    e.image = e.game.fullamour_forward[e.current_frame//10]
                elif e.left_on is True:
                    e.image = e.game.fullamour_left[e.current_frame//10]
                elif e.right_on is True:
                    e.image = e.game.fullamour_right[e.current_frame//10]
                if e.sword_swing_back is True:
                    e.image = e.game.fullamour_swordb[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_forward is True:
                    e.image = e.game.fullamour_swordf[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_left is True:
                    e.image = e.game.fullamour_swordl[e.current_sword//12]
                    e.current_sword += 1
                elif e.sword_swing_right is True:
                    e.image = e.game.fullamour_swordr[e.current_sword//12]
                    e.current_sword += 1
                if e.bow_back is True:
                    e.image = e.game.full_bow_back[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_forward is True:
                    e.image = e.game.full_bow_for[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_left is True:
                    e.image = e.game.full_bow_left[e.bow_frame//7]
                    e.bow_frame += 1
                elif e.bow_right is True:
                    e.image = e.game.full_bow_right[e.bow_frame//7]
                    e.bow_frame += 1
            
            if e.being_attacked is True:
                if round(e.damage_time // .2) % 2 == 0:
                    e.image = e.game.blank
            e.rect.center = e.pos
            e.pos += e.vel * e.game.dt
            e.rect.centerx = e.pos.x
            collision(e, e.game.walls, 'x')
            collision(e, e.game.strawb_group, 'x')
            collision(e, e.game.water, 'x')
            collision(e, e.game.mob, 'x')
            e.rect.centery = e.pos.y
            collision(e, e.game.walls, 'y')
            collision(e, e.game.strawb_group, 'y')
            collision(e, e.game.water, 'y')
            collision(e, e.game.mob, 'y')
            e.offset_image()
            if e.bomb_droped is True:
                e.bomb_time += e.game.dt
            if e.bomb_time >= 1:
                e.bomb_droped = False
                e.bomb_time = 0
            if e.being_attacked is True:
                e.damage_time += e.game.dt
            if e.damage_time >= 5:
                e.being_attacked = False
                e.damage_time = 0

    def offset_image(self):
        if self.image == self.game.sword_right[0] or self.image == self.game.shirt_swordr[0]  \
                or self.image == self.game.pants_swordr[0] or self.image == self.game.helmat_swordr[0]\
                or self.image == self.game.shirtNpants_swordr[0] or self.image == self.game.helmatNshirt_swordr[0]\
                or self.image == self.game.helmatNpants_swordr[0] or self.image == self.game.fullamour_swordr[0]:
            self.rect.x = self.rect.x - 6
            self.rect.y = self.rect.y

        if self.image == self.game.sword_left[0] or self.image == self.game.shirt_swordl[0]  \
                or self.image == self.game.pants_swordl[0] or self.image == self.game.helmat_swordl[0]\
                or self.image == self.game.shirtNpants_swordl[0] or self.image == self.game.helmatNshirt_swordl[0]\
                or self.image == self.game.helmatNpants_swordl[0] or self.image == self.game.fullamour_swordl[0]:
            self.rect.x = self.rect.x - 16
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_left[1] or self.image == self.game.shirt_swordl[1]  \
                or self.image == self.game.pants_swordl[1] or self.image == self.game.helmat_swordl[1]\
                or self.image == self.game.shirtNpants_swordl[1] or self.image == self.game.helmatNshirt_swordl[1]\
                or self.image == self.game.helmatNpants_swordl[1] or self.image == self.game.fullamour_swordl[1]:
            self.rect.x = self.rect.x - 69
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_left[2] or self.image == self.game.shirt_swordl[2]  \
                or self.image == self.game.pants_swordl[2] or self.image == self.game.helmat_swordl[2]\
                or self.image == self.game.shirtNpants_swordl[2] or self.image == self.game.helmatNshirt_swordl[2]\
                or self.image == self.game.helmatNpants_swordl[2] or self.image == self.game.fullamour_swordl[2]:
            self.rect.x = self.rect.x - 67
            self.rect.y = self.rect.y

        if self.image == self.game.sword_forward[0] or self.image == self.game.shirt_swordf[0]  \
                or self.image == self.game.pants_swordf[0] or self.image == self.game.helmat_swordf[0]\
                or self.image == self.game.shirtNpants_swordf[0] or self.image == self.game.helmatNshirt_swordf[0]\
                or self.image == self.game.helmatNpants_swordf[0] or self.image == self.game.fullamour_swordf[0]:
            self.rect.x = self.rect.x - 29
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_forward[1] or self.image == self.game.shirt_swordf[1]  \
                or self.image == self.game.pants_swordf[1] or self.image == self.game.helmat_swordf[1]\
                or self.image == self.game.shirtNpants_swordf[1] or self.image == self.game.helmatNshirt_swordf[1]\
                or self.image == self.game.helmatNpants_swordf[1] or self.image == self.game.fullamour_swordf[1]:
            self.rect.x = self.rect.x - 33
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_forward[2] or self.image == self.game.shirt_swordf[2]  \
                or self.image == self.game.pants_swordf[2] or self.image == self.game.helmat_swordf[2]\
                or self.image == self.game.shirtNpants_swordf[2] or self.image == self.game.helmatNshirt_swordf[2]\
                or self.image == self.game.helmatNpants_swordf[2] or self.image == self.game.fullamour_swordf[2]:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y

        if self.image == self.game.sword_back[0] or self.image == self.game.shirt_swordb[0]  \
                or self.image == self.game.pants_swordb[0] or self.image == self.game.helmat_swordb[0]\
                or self.image == self.game.shirtNpants_swordb[0] or self.image == self.game.helmatNshirt_swordb[0]\
                or self.image == self.game.helmatNpants_swordb[0] or self.image == self.game.fullamour_swordb[0]:
            self.rect.x = self.rect.x - 30
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_back[1] or self.image == self.game.shirt_swordb[1]  \
                or self.image == self.game.pants_swordb[1] or self.image == self.game.helmat_swordb[1]\
                or self.image == self.game.shirtNpants_swordb[1] or self.image == self.game.helmatNshirt_swordb[1]\
                or self.image == self.game.helmatNpants_swordb[1] or self.image == self.game.fullamour_swordb[1]:
            self.rect.x = self.rect.x - 29
            self.rect.y = self.rect.y - 21

        elif self.image == self.game.sword_back[2] or self.image == self.game.shirt_swordb[2]  \
                or self.image == self.game.pants_swordb[2] or self.image == self.game.helmat_swordb[2]\
                or self.image == self.game.shirtNpants_swordb[2] or self.image == self.game.helmatNshirt_swordb[2]\
                or self.image == self.game.helmatNpants_swordb[2] or self.image == self.game.fullamour_swordb[2]:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - 21

    def unoffset_image(self):
        if self.image == self.game.sword_right[0] or self.image == self.game.shirt_swordr[0]  \
                or self.image == self.game.pants_swordr[0] or self.image == self.game.helmat_swordr[0]\
                or self.image == self.game.shirtNpants_swordr[0] or self.image == self.game.helmatNshirt_swordr[0]\
                or self.image == self.game.helmatNpants_swordr[0] or self.image == self.game.fullamour_swordr[0]:
            self.rect.x = self.rect.x + 6
            self.rect.y = self.rect.y

        if self.image == self.game.sword_left[0] or self.image == self.game.shirt_swordl[0]  \
                or self.image == self.game.pants_swordl[0] or self.image == self.game.helmat_swordl[0]\
                or self.image == self.game.shirtNpants_swordl[0] or self.image == self.game.helmatNshirt_swordl[0]\
                or self.image == self.game.helmatNpants_swordl[0] or self.image == self.game.fullamour_swordl[0]:
            self.rect.x = self.rect.x + 16
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_left[1] or self.image == self.game.shirt_swordl[1]  \
                or self.image == self.game.pants_swordl[1] or self.image == self.game.helmat_swordl[1]\
                or self.image == self.game.shirtNpants_swordl[1] or self.image == self.game.helmatNshirt_swordl[1]\
                or self.image == self.game.helmatNpants_swordl[1] or self.image == self.game.fullamour_swordl[1]:
            self.rect.x = self.rect.x + 69
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_left[2] or self.image == self.game.shirt_swordl[2]  \
                or self.image == self.game.pants_swordl[2] or self.image == self.game.helmat_swordl[2]\
                or self.image == self.game.shirtNpants_swordl[2] or self.image == self.game.helmatNshirt_swordl[2]\
                or self.image == self.game.helmatNpants_swordl[2] or self.image == self.game.fullamour_swordl[2]:
            self.rect.x = self.rect.x + 67
            self.rect.y = self.rect.y

        if self.image == self.game.sword_forward[0] or self.image == self.game.shirt_swordf[0]  \
                or self.image == self.game.pants_swordf[0] or self.image == self.game.helmat_swordf[0]\
                or self.image == self.game.shirtNpants_swordf[0] or self.image == self.game.helmatNshirt_swordf[0]\
                or self.image == self.game.helmatNpants_swordf[0] or self.image == self.game.fullamour_swordf[0]:
            self.rect.x = self.rect.x + 29
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_forward[1] or self.image == self.game.shirt_swordf[1]  \
                or self.image == self.game.pants_swordf[1] or self.image == self.game.helmat_swordf[1]\
                or self.image == self.game.shirtNpants_swordf[1] or self.image == self.game.helmatNshirt_swordf[1]\
                or self.image == self.game.helmatNpants_swordf[1] or self.image == self.game.fullamour_swordf[1]:
            self.rect.x = self.rect.x + 33
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_forward[2] or self.image == self.game.shirt_swordf[2]  \
                or self.image == self.game.pants_swordf[2] or self.image == self.game.helmat_swordf[2]\
                or self.image == self.game.shirtNpants_swordf[2] or self.image == self.game.helmatNshirt_swordf[2]\
                or self.image == self.game.helmatNpants_swordf[2] or self.image == self.game.fullamour_swordf[2]:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y

        if self.image == self.game.sword_back[0] or self.image == self.game.shirt_swordb[0]  \
                or self.image == self.game.pants_swordb[0] or self.image == self.game.helmat_swordb[0]\
                or self.image == self.game.shirtNpants_swordb[0] or self.image == self.game.helmatNshirt_swordb[0]\
                or self.image == self.game.helmatNpants_swordb[0] or self.image == self.game.fullamour_swordb[0]:
            self.rect.x = self.rect.x + 30
            self.rect.y = self.rect.y

        elif self.image == self.game.sword_back[1] or self.image == self.game.shirt_swordb[1]  \
                or self.image == self.game.pants_swordb[1] or self.image == self.game.helmat_swordb[1]\
                or self.image == self.game.shirtNpants_swordb[1] or self.image == self.game.helmatNshirt_swordb[1]\
                or self.image == self.game.helmatNpants_swordb[1] or self.image == self.game.fullamour_swordb[1]:
            self.rect.x = self.rect.x + 29
            self.rect.y = self.rect.y + 21

        elif self.image == self.game.sword_back[2] or self.image == self.game.shirt_swordb[2]  \
                or self.image == self.game.pants_swordb[2] or self.image == self.game.helmat_swordb[2]\
                or self.image == self.game.shirtNpants_swordb[2] or self.image == self.game.helmatNshirt_swordb[2]\
                or self.image == self.game.helmatNpants_swordb[2] or self.image == self.game.fullamour_swordb[2]:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + 21

class Arrow(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.arrow_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = PROJECTILE_LAYER
        for i in self.game.player_group:
            if i.bow_left is True:
                self.image = game.arrow
            elif i.bow_right is True:
                self.image = pg.transform.rotate(self.game.arrow, 180)
            elif i.bow_forward is True:
                self.image = pg.transform.rotate(self.game.arrow, 90)
                self.image = pg.transform.flip(self.image, 0, 180)
            elif i.bow_back is True:
                self.image = pg.transform.rotate(self.game.arrow, 270)
                self.image = pg.transform.flip(self.image, 0, 180)
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        for i in self.game.player_group:
            if i.bow_back is True:
                self.vel = vec(0, 1) * BONE_SPEED * uniform(0.9, 1.1)
            elif i.bow_forward is True:
                self.vel = vec(0, -1) * BONE_SPEED * uniform(0.9, 1.1)
            elif i.bow_left is True:
                self.vel = vec(-1, 0) * BONE_SPEED * uniform(0.9, 1.1)
            elif i.bow_right is True:
                self.vel = vec(1, 0) * BONE_SPEED * uniform(0.9, 1.1)
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.sprite.spritecollideany(self, self.game.strawb_group):
            self.kill()
        if pg.sprite.spritecollideany(self, self.game.bomb_group):
            self.kill()
        for m in self.game.mob:
            if m.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) == 1:
                if m.being_attacked is False:
                    m.health -= 50
                    m.being_attacked = True
                self.kill()
        for b in self.game.bomb_group:
            if b.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) == 1:
                b.bomb_time = 0
        for b in self.game.bone_group:
            if b.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) == 1:
                b.kill()
                self.kill()
        if pg.time.get_ticks() - self.spawn_time > BONE_TIME:
            self.kill()


class Smoke_Bomb(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.smoke_bomb_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = EXPLOSION_LAYER
        self.image = self.game.smoke_bomb
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()
        self.bomb_time = SMOKE_TIME

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if pg.time.get_ticks() - self.spawn_time > self.bomb_time:
                self.kill()
                Smoke(self.game, self.pos)
            i.offset_image()


class Smoke(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.smoke_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = PROJECTILE_LAYER
        self.image = self.game.smoke_screen[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()
        self.current_frame = 1

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if self.current_frame > 120:
                self.current_frame = 1
                self.kill()

            if self.current_frame//10 == 4:
                self.current_frame += .05
            else:
                self.current_frame += 1
            self.image = self.game.smoke_screen[round(self.current_frame)//10]
            i.offset_image()



class Bomb(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.bomb_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = PROJECTILE_LAYER
        self.image = self.game.bomb
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()
        self.bomb_time = BOMB_TIME

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if pg.time.get_ticks() - self.spawn_time > self.bomb_time:
                self.game.explosion_sound.play()
                for b in self.game.bomb_group:
                    if b.rect.colliderect(self.rect.x - 40, self.rect.y - 30, self.rect.width + 80, self.rect.height + 80) == 1:
                        b.bomb_time = 0
                for m in self.game.mob:
                    if m.rect.colliderect(self.rect.x - 40, self.rect.y - 30, self.rect.width + 80, self.rect.height + 80) == 1:
                        if m.being_attacked is False:
                            m.health -= 50
                            m.being_attacked = True
                for i in self.game.player_group:
                    if i.rect.colliderect(self.rect.x - 40, self.rect.y - 30, self.rect.width + 80, self.rect.height + 80) == 1:
                        if i.being_attacked is False:
                            self.game.health -= 50
                            i.being_attacked = True
                self.kill()
                Explosion(self.game, self.pos)
            i.offset_image()


class Explosion(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.explosion_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = EXPLOSION_LAYER
        self.image = self.game.explosion[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()
        self.current_frame = 1

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if self.current_frame > 90:
                self.current_frame = 1
                self.kill()
            self.image = self.game.explosion[self.current_frame//10]
            i.offset_image()
            self.current_frame += 1


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Water(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.water
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Slime(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = MOB_LAYER
        self.color = choice(("green", "red", "blue"))
        if self.color == "green":
            self.image = game.green_slime_idle[0]
        elif self.color == "blue":
            self.image = game.blue_slime_idle[0]
        elif self.color == "red":
            self.image = game.red_slime_idle[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        if self.color == "red":
            self.health = RED_SLIME_HEALTH
        elif self.color == "blue":
            self.health = BLUE_SLIME_HEALTH
        elif self.color == "green":
            self.health = GREEN_SLIME_HEALTH
        self.current_frame = 0
        self.mob_death = False
        if not self.game.player2_on:
            self.knockback = SLIME_KNOCKBACK
        else:
            self.knockback = SLIME_KNOCKBACK/2
        if not self.game.player2_on:
            self.speed = SLIME_SPEED
        else:
            self.speed = SLIME_SPEED/2

        self.mob_agro = True
        self.being_attacked = False
        self.damage_time = 0

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.current_frame = 0
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 1:
                self.being_attacked = False
                self.damage_time = 0

            if self.current_frame == 90:
                self.current_frame = 0
                if self.mob_death is True:
                    choices = choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                    if choices == 1:
                        Coin(self.game, self.pos.x, self.pos.y)
                    #elif choices == 2:
                    #    HEART(self.game, self.pos.x, self.pos.y)
                    self.kill()
            if self.rect.colliderect((i.rect.x - 70, i.rect.y - 70,
                                  i.rect.width + 140, i.rect.height + 140)) == 1 and self.mob_death is False:
                if self.color == "green":
                    self.image = self.game.green_slime_attack[self.current_frame // 10]
                elif self.color == "red":
                    self.image = self.game.red_slime_attack[self.current_frame // 10]
                elif self.color == "blue":
                    self.image = self.game.blue_slime_attack[self.current_frame // 10]
            elif self.mob_death is False:
                if self.color == "green":
                    self.image = self.game.green_slime_idle[self.current_frame // 10]
                elif self.color == "blue":
                    self.image = self.game.blue_slime_idle[self.current_frame // 10]
                elif self.color == "red":
                    self.image = self.game.red_slime_idle[self.current_frame // 10]
            else:
                if self.color == "green":
                    self.image = self.game.green_slime_death[self.current_frame // 10]
                elif self.color == "red":
                    self.image = self.game.red_slime_death[self.current_frame // 10]
                elif self.color == "blue":
                        self.image = self.game.blue_slime_death[self.current_frame // 10]
            if self.rect.colliderect((i.rect.x - 10, i.rect.y - 10,
                                  i.rect.width + 20, i.rect.height + 20)) == 1:
                if self.game.health > 0 and i.being_attacked is False and self.mob_death is False:
                    self.game.health -= 50
                    i.being_attacked = True
                    if i.back_on:
                        i.pos = vec(i.pos.x,i.pos.y-self.knockback)
                    elif i.forward_on:
                        i.pos = vec(i.pos.x,i.pos.y+self.knockback)
                    elif i.left_on:
                        i.pos = vec(i.pos.x-self.knockback,i.pos.y)
                    elif i.right_on:
                        i.pos = vec(i.pos.x+self.knockback,i.pos.y-self.knockback)
            if i.visible is True:
                self.rot = (i.pos - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(self.speed)
            if self.mob_death is False:
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            collision(self, self.game.walls, 'x')
            collision(self, self.game.player_group, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.water, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.water, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            i.offset_image()
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank


class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coin_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = game.coin[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0

    def update(self):
        if self.current_frame == 30:
            self.current_frame = 0
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                  i.rect.width, i.rect.height)) == 1:
                if self.rect.x == 154:
                    self.game.map1_coin1 = False
                elif self.rect.x == 1118:
                    self.game.map1_coin2 = False
                if self.rect.x == 154:
                    self.game.map2_coin = False
                if self.rect.x == 207:
                    self.game.map3_coin1 = False
                elif self.rect.x == 142:
                    self.game.map3_coin2 = False
                elif self.rect.x == 1106:
                    self.game.map3_coin3 = False
                elif self.rect.x == 1090:
                    self.game.map3_coin4 = False
                if self.rect.x == 102:
                    self.game.map4_coin1 = False
                elif self.rect.x == 376:
                    self.game.map4_coin2 = False
                elif self.rect.x == 1141:
                    self.game.map4_coin3 = False
                elif self.rect.x == 1006:
                    self.game.map4_coin4 = False
                self.game.money += 100
                self.kill()
        self.image = self.game.coin[self.current_frame // 10]
        self.current_frame += 1


class Heart(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.heart_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = game.heart[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0

    def update(self):
        if self.current_frame == 30:
            self.current_frame = 0
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x - 20, i.rect.y - 20,
                                  i.rect.width + 40, i.rect.height + 40)) == 1:
                if self.game.health < 300:
                    self.game.health += 50
                    self.kill()
                    if self.game.map1_on is True:
                        self.game.map1_heart = False
                    elif self.game.map3_on is True:
                        self.game.map3_heart = False
                    elif self.game.map4_on is True:
                        if self.pos.x == 242.424:
                            self.game.map4_heart1 = False
                        elif self.pos.x == 1059.09:
                            self.game.map4_heart2 = False
                    elif self.game.map6_on is True:
                        if self.pos.x == 926.467:
                            self.game.map6_heart1 = False
                        elif self.pos.x == 341.12:
                            self.game.map6_heart2 = False
                        elif self.pos.x == 299.973:
                            self.game.map6_heart3 = False
                    elif self.game.map7_on is True:
                        self.game.map7_heart = False
                    elif self.game.map8_on is True:
                        self.game.map8_heart = False
                    elif self.game.map9_on is True:
                        if self.pos.x == 1094.67:
                            self.game.map9_heart1 = False
                        elif self.pos.x == 800:
                            self.game.map9_heart2 = False
        self.image = self.game.heart[self.current_frame // 10]
        self.current_frame += 1


class Fire(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = OBJECT_LAYER
        self.groups = game.all_sprites, game.fire_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.fire[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0
        self.time = 0

    def update(self):
        if self.current_frame == 60:
            self.current_frame = 0
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                  i.rect.width, i.rect.height)) == 1:
                if self.game.health > 0 and i.being_attacked is False:
                    self.game.health -= 50
                    i.being_attacked = True
        self.image = self.game.fire[self.current_frame // 10]
        self.current_frame += 1


class Map2(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map2_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                  i.rect.width, i.rect.height)) == 1:
                self.game.map1_on = False
                self.game.map2_on = True
                self.game.new()


class Map3(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map3_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                  i.rect.width, i.rect.height)) == 1:
                self.game.map1_on = False
                self.game.map3_on = True
                self.game.map4_on = False
                self.game.new()


class Map4(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map4_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map4_on = True
                self.game.map3_on = False
                self.game.map6_on = False
                self.game.map5_on = False
                self.game.new()


class Straw(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.straw_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                if i.sword_swing_right is True or i.sword_swing_left is True or \
                   i.sword_swing_forward is True or i.sword_swing_back is True:
                    if self.game.map2_on is True:
                        for w in self.game.strawb_group:
                            w.kill()
                        self.game.map2_im = self.game.map2.make_map(True)
                        self.game.map2_straw = False
                        self.kill()
                    if self.game.map1_on is True:
                        for w in self.game.strawb_group:
                            w.kill()
                        self.game.map1_im = self.game.map1.make_map(True)
                        self.game.map1_straw = False
                        self.kill()


class Sword(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.sword_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = self.game.sword
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map2_cutscean()
                self.kill()


class Strawb(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.strawb_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Map1(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map3_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map1_on = True
                self.game.map3_on = False
                self.game.map2_on = False
                self.game.new()


class Goblin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = game.goblin_back[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.health = GOBLIN_HEALTH
        self.current_frame = 0
        self.current_frame_attack = 0
        self.attack = False
        self.fallback = True
        self.flank = vec(0)
        self.fallback_set = False
        self.last_pos = vec(0)
        self.fallback_points = []
        self.points_init = False
        self.mob_death = False
        self.mob_agro = True
        self.health = GREEN_SLIME_HEALTH
        self.being_attacked = False
        self.damage_time = 0

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.current_frame = 0
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            if i.visible is False:
                self.attack = False
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 1:
                self.being_attacked = False
                self.damage_time = 0

            if self.points_init is False:
                for m in self.game.impfall_group:
                    self.fallback_points.append((m.x, m.y))
                self.points_init = True
            if self.attack is True:
                for i in self.game.player_group:
                    self.flank = vec(i.pos.x, i.pos.y)
            if self.fallback is True and self.fallback_set is False and self.attack is False:
                choices = choice(self.fallback_points)
                self.flank = vec(choices[0], choices[1])
                self.fallback_set = True
            if self.rect.colliderect((self.fallback_points[0][0], self.fallback_points[0][1],
                                      i.rect.width, i.rect.height)) == 1:
                choices = choice((0, 1, 2))
                if choices == 1 or choices == 2 and self.attack is False:
                    self.flank = vec(i.pos.x, i.pos.y)
                    self.fallback_set = False
                    self.fallback = False
                    self.attack = True
            if self.rect.colliderect((self.fallback_points[1][0], self.fallback_points[1][1],
                                      i.rect.width, i.rect.height)) == 1:
                choices = choice((0, 1, 2))
                if choices == 1 or choices == 2 and self.attack is False and self.mob_death is False:
                    self.flank = vec(i.pos.x, i.pos.y)
                    self.fallback_set = False
                    self.fallback = False
                    self.attack = True

            w = 0
            while w < len(self.fallback_points):
                if self.rect.colliderect((self.fallback_points[w][0], self.fallback_points[w][1],
                                          i.rect.width, i.rect.height)) == 1:
                    choices = choice((0, 1, 2))
                    if choices == 1 or choices == 2 and self.attack is False:
                        self.flank = vec(i.pos.x, i.pos.y)
                        self.fallback_set = False
                        self.fallback = False
                        self.attack = True
                w += 1
            if self.rect.colliderect((i.rect.x - 20, i.rect.y + 15,
                                          i.rect.width, i.rect.height - 20)) == 1:
                if self.game.health > 0 and i.being_attacked is False:
                    self.fallback = True
                    self.attack = False
                    self.game.health -= 50
                    i.being_attacked = True

            if self.current_frame == 70:
                self.current_frame = 0
            if self.current_frame_attack == 30:
                self.current_frame_attack = 0
            if self.current_frame == 40 and self.mob_death is True:
                choices = choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                if choices == 1:
                    Coin(self.game, self.pos.x, self.pos.y)
                elif choices == 2:
                    HEART(self.game, self.pos.x, self.pos.y)
                self.kill()
            if self.rect.colliderect((i.rect.x - 30, i.rect.y - 10,
                                      i.rect.width + 60, i.rect.height + 60)) == 1 and self.mob_death is False:
                if i.forward_on is True:
                    self.image = self.game.goblin_attackb[self.current_frame_attack // 10]
                elif i.back_on is True:
                    self.image = self.game.goblin_attackf[self.current_frame_attack // 10]
                elif i.right_on is True:
                    self.image = self.game.goblin_attackr[self.current_frame_attack // 10]
                elif i.left_on is True:
                    self.image = self.game.goblin_attackl[self.current_frame_attack // 10]

            elif self.mob_death is False:
                if (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                   (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    self.image = self.game.goblin_for[self.current_frame // 10]
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                    self.image = self.game.goblin_left[self.current_frame // 10]
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    self.image = self.game.goblin_right[self.current_frame // 10]
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                    self.image = self.game.goblin_back[self.current_frame // 10]
            else:
                self.image = self.game.goblin_death[self.current_frame // 10]
            if self.mob_agro is True:
                self.rot = (self.flank - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(GOBLIN_SPEED)
            if self.mob_death is False:
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            collision(self, self.game.walls, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.water, 'x')
            collision(self, self.game.player_group, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.water, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            self.current_frame_attack += 1
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank
            if i.rect.colliderect((self.rect.x - 120, self.rect.y - 120, self.rect.width + 240, self.rect.height + 240)) == 1:
                self.mob_agro = True
            i.offset_image()


class Skeleton(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = MOB_LAYER
        self.image = game.skeleton_for[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect_center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.health = SKELETON_HEALTH
        self.current_frame = 0
        self.current_frame_attack = 0
        self.last_throw = 0
        self.mob_death = False
        self.death_frame = 0
        self.health = GREEN_SLIME_HEALTH
        self.damage_time = 0
        self.being_attacked = False

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.death_frame = 0
            self.game.mob_die.play()

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.death_frame == 50 and self.mob_death is True:
                self.death_frame = 0
                choices = choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                if choices == 1:
                    Coin(self.game, self.pos.x, self.pos.y)
                elif choices == 2:
                    HEART(self.game, self.pos.x, self.pos.y)
                self.kill()
            if self.current_frame == 10:
                self.current_frame = 0
            if self.current_frame_attack == 110:
                self.current_frame_attack = 0

            if i.pos.y > self.rect_center.y and self.mob_death is False:
                self.image = self.game.skeleton_attackf[self.current_frame_attack // 10]
            elif i.pos.y < self.rect_center.y and self.mob_death is False:
                self.image = self.game.skeleton_attackb[self.current_frame_attack // 10]
            elif self.mob_death is False:
                self.image = self.game.skeleton_for[self.current_frame // 10]
            else:
                self.image = self.game.skeleton_death[self.death_frame // 10]
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                if self.game.health > 0 and i.being_attacked is False:
                    #self.game.health -= 50
                    #i.being_attacked = True
                    pass

            now = pg.time.get_ticks()
            self.rot = (i.pos - self.pos).angle_to(vec(1, 0))
            if self.current_frame_attack == 50 and self.mob_death is False and i.visible is True:
                ran = choice((0, 1))
                if ran == 1:
                    if now - self.last_throw > BONE_RATE:
                        self.last_throw = now
                        dire = vec(1, 0).rotate(-self.rot)
                        Bone(self.game, self.pos, dire)
                elif choice((0, 1)) == 0:
                    if now - self.last_throw > BONE_RATE:
                        self.last_throw = now
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank



            self.rect.center = self.pos
            self.acc = vec(SKELETON_SPEED, 0).rotate(-self.rot)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            collision(self, self.game.walls, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.water, 'x')
            collision(self, self.game.player_group, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.water, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            self.current_frame_attack += 1
            self.death_frame += 1
            i.offset_image()


class Bone(pg.sprite.Sprite):
    def __init__(self, game, pos, dire):
        self.groups = game.all_sprites, game.bone_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = PROJECTILE_LAYER
        self.image = game.bone
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        self.vel = dire * BONE_SPEED * uniform(0.9, 1.1)
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if i.back_rect is True:
                if self.rect.colliderect((i.rect.x - 25, i.rect.y + 25,
                                                    i.rect.width + 50, i.rect.height)) == 1:
                    self.kill()
            if i.for_rect is True:
                if self.rect.colliderect((i.rect.x - 25, i.rect.y - 25,
                                                    i.rect.width + 50, i.rect.height)) == 1:
                    self.kill()
            if i.sword_swing_right is True:
                if self.rect.colliderect((i.rect.x + 25, i.rect.y + 5,
                                                   i.rect.width + 40, i.rect.height - 15)) == 1:
                    self.kill()
            if i.sword_swing_left is True:
                if self.rect.colliderect((i.rect.x - 70, i.rect.y + 5,
                                              i.rect.width + 36, i.rect.height - 15)) == 1:
                    self.kill()

            self.pos += self.vel * self.game.dt
            self.rect.center = self.pos
            if pg.sprite.spritecollideany(self, self.game.walls):
                self.kill()
            if pg.sprite.spritecollideany(self, self.game.strawb_group):
                self.kill()
            if self.rect.colliderect(i.rect):
                self.kill()
                if self.game.health > 0 and i.being_attacked is False:
                    self.game.health -= 50
                    i.being_attacked = True

            if pg.time.get_ticks() - self.spawn_time > BONE_TIME:
                self.kill()
            i.offset_image()



class Map5(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map5_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map5_on = True
                self.game.map4_on = False
                self.game.new()

class Map6(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map6_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map6_on = True
                self.game.map4_on = False
                self.game.map7_on = False
                self.game.map8_on = False
                self.game.map9_on = False
                self.game.new()



class Map7(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map7_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map7_on = True
                self.game.map6_on = False
                self.game.new()



class Map8(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map8_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map8_on = True
                self.game.map6_on = False
                self.game.new()


class Map9(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map9_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map9_on = True
                self.game.map6_on = False
                self.game.new()


class Map10(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map10_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map10_on = True
                self.game.map3_on = False
                self.game.map11_on = False
                self.game.new()


class Map11(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.map11_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.image = self.game.blank
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.game.map10_on = False
                self.game.map11_on = True
                self.game.new()


class Helmat(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.helmat_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = game.helmat
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x - 20, i.rect.y - 20,
                                      i.rect.width + 40, i.rect.height + 40)) == 1:

                self.game.max_health += 100
                self.game.health += 100
                self.kill()
                self.game.got_hat = True


class Shirt(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.shirt_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = game.shirt
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x - 20, i.rect.y - 20,
                                      i.rect.width + 40, i.rect.height + 40)) == 1:

                self.game.max_health += 100
                self.game.health += 100
                self.kill()
                self.game.got_shirt = True



class Pants(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.pants_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = OBJECT_LAYER
        self.image = game.pants
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.current_frame = 0

    def update(self):
        for i in self.game.player_group:
            if self.rect.colliderect((i.rect.x - 20, i.rect.y - 20,
                                      i.rect.width + 40, i.rect.height + 40)) == 1:

                self.game.max_health += 100
                self.game.health += 100
                self.kill()
                self.game.got_pants = True

class Imp(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.color = choice(("green", "red", "blue"))
        if self.color == "green":
            self.image = game.green_imp_for[0]
        elif self.color == "blue":
            self.image = game.blue_imp_for[0]
        elif self.color == "red":
            self.image = game.red_imp_for[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.health = GOBLIN_HEALTH
        self.current_frame = 0
        self.current_frame_attack = 0
        self.attack = False
        self.fallback = True
        self.fallback_set = False
        self.last_pos = vec(0)
        self.flank = vec(0)
        self.fallback_points = []
        self.points_init = False
        self.mob_death = False
        self.death_frame = 0
        if self.color == "green":
            self.health = GREEN_SLIME_HEALTH
        elif self.color == "blue":
            self.health = BLUE_SLIME_HEALTH
        elif self.color == "red":
            self.health = RED_SLIME_HEALTH
        self.being_attacked = False
        self.damage_time = 0

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            if i.visible is False:
                self.attack = False
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.points_init is False:
                for m in self.game.impfall_group:
                    self.fallback_points.append((m.x, m.y))
                self.points_init = True
            if self.attack is True:
                self.flank = vec(i.pos.x, i.pos.y)
            if self.fallback is True and self.fallback_set is False and self.attack is False:
                choices = choice(self.fallback_points)
                self.flank = vec(choices[0], choices[1])
                self.fallback_set = True
            if self.rect.colliderect((self.fallback_points[0][0], self.fallback_points[0][1],
                                      i.rect.width, i.rect.height)) == 1:
                choices = choice((0, 1, 2))
                if choices == 1 or choices == 2 and self.attack is False:
                    self.flank = vec(i.pos.x, i.pos.y)
                    self.fallback_set = False
                    self.fallback = False
                    self.attack = True

            if self.rect.colliderect((self.fallback_points[1][0], self.fallback_points[1][1],
                                      i.rect.width, i.rect.height)) == 1:
                choices = choice((0, 1, 2))
                if choices == 1 or choices == 2 and self.attack is False:
                    self.flank = vec(i.pos.x, i.pos.y)
                    self.fallback_set = False
                    self.fallback = False
                    self.attack = True
            w = 0
            while w < len(self.fallback_points):
                if self.rect.colliderect((self.fallback_points[w][0], self.fallback_points[w][1],
                                          i.rect.width, i.rect.height)) == 1:
                    choices = choice((0, 1, 2))
                    if choices == 1 or choices == 2 and self.attack is False:
                        self.flank = vec(i.pos.x, i.pos.y)
                        self.fallback_set = False
                        self.fallback = False
                        self.attack = True
                w += 1

            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                self.fallback = True
                self.attack = False
                if self.game.health > 0 and i.being_attacked is False:
                    self.game.health -= 50
                    i.being_attacked = True
            if self.current_frame == 30:
                self.current_frame = 0
            if self.current_frame_attack == 30:
                self.current_frame_attack = 0
            if self.death_frame == 70:
                self.death_frame = 0
                choices = choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                if choices == 1:
                    Coin(self.game, self.pos.x, self.pos.y)
                elif choices == 2:
                    HEART(self.game, self.pos.x, self.pos.y)
                self.kill()
            if self.rect.colliderect((i.rect.x - 30, i.rect.y - 10,
                                      i.rect.width + 60, i.rect.height + 60)) == 1 and self.mob_death is False:
                if i.forward_on is True:
                    if self.color == "red":
                        self.image = self.game.red_imp_attackb[self.current_frame_attack // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_imp_attackb[self.current_frame_attack // 10]
                    elif self.color == "green":
                        self.image = self.game.green_imp_attackb[self.current_frame_attack // 10]
                elif i.back_on is True:
                    if self.color == "red":
                        self.image = self.game.red_imp_attackf[self.current_frame_attack // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_imp_attackf[self.current_frame_attack // 10]
                    elif self.color == "green":
                        self.image = self.game.green_imp_attackf[self.current_frame_attack // 10]
                elif i.right_on is True:
                    if self.color == "red":
                        self.image = self.game.red_imp_attackr[self.current_frame_attack // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_imp_attackr[self.current_frame_attack // 10]
                    elif self.color == "green":
                        self.image = self.game.green_imp_attackr[self.current_frame_attack // 10]
                elif i.left_on is True:
                    if self.color == "red":
                        self.image = self.game.red_imp_attackl[self.current_frame_attack // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_imp_attackl[self.current_frame_attack // 10]
                    elif self.color == "green":
                        self.image = self.game.green_imp_attackl[self.current_frame_attack // 10]

                elif self.mob_death is False:
                    if (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                       (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                        if self.color == "red":
                            self.image = self.game.red_imp_back[self.current_frame // 10]
                        elif self.color == "blue":
                            self.image = self.game.blue_imp_back[self.current_frame // 10]
                        elif self.color == "green":
                            self.image = self.game.green_imp_back[self.current_frame // 10]
                    elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                         (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                        if self.color == "red":
                            self.image = self.game.red_imp_left[self.current_frame // 10]
                        elif self.color == "blue":
                            self.image = self.game.blue_imp_left[self.current_frame // 10]
                        elif self.color == "green":
                            self.image = self.game.green_imp_left[self.current_frame // 10]
                    elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                         (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                        if self.color == "red":
                            self.image = self.game.red_imp_right[self.current_frame // 10]
                        elif self.color == "blue":
                            self.image = self.game.blue_imp_right[self.current_frame // 10]
                        elif self.color == "green":
                            self.image = self.game.green_imp_right[self.current_frame // 10]
                    elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                         (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                        if self.color == "red":
                            self.image = self.game.red_imp_for[self.current_frame // 10]
                        elif self.color == "blue":
                            self.image = self.game.blue_imp_for[self.current_frame // 10]
                        elif self.color == "green":
                            self.image = self.game.green_imp_for[self.current_frame // 10]
                elif self.mob_death is True:
                    if self.color == "red":
                        self.image = self.game.red_imp_death[self.death_frame // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_imp_death[self.death_frame // 10]
                    elif self.color == "green":
                        self.image = self.game.green_imp_death[self.death_frame // 10]
            if self.mob_death is False:
                self.rot = (self.flank - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(GOBLIN_SPEED)
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            self.last_pos = self.pos
            collision(self, self.game.walls, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.player_group, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            self.current_frame_attack += 1
            if self.mob_death is True:
                self.death_frame += 1
            i.offset_image()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 1:
                self.being_attacked = False
                self.damage_time = 0
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank

class Imp_Fall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.impfall_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = WALL_LAYER
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Golem(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = MOB_LAYER
        self.image = self.game.golem_for[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.health = GOBLIN_HEALTH
        self.current_frame = 0
        self.current_frame_attack = 0
        self.attack = False
        self.mob_death = False
        self.current_frame = 0
        self.current_frame_attack = 0
        self.attack = False
        self.fallback = True
        self.fallback_set = False
        self.last_pos = vec(0)
        self.flank = vec(0)
        self.fallback_points = []
        self.points_init = False
        self.mob_death = False
        self.death_frame = 0
        self.health = GREEN_SLIME_HEALTH
        self.being_attacked = False
        self.damage_time = 0
        self.forward_on = True
        self.back_on = False
        self.left_on = False
        self.right_on = False

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            if i.visible is False:
                self.attack = False
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.attack is True:
                self.flank = vec(i.pos.x, i.pos.y)

            if self.rect.colliderect((i.rect.x, i.rect.y,
                                      i.rect.width, i.rect.height)) == 1:
                if self.game.health > 0 and i.being_attacked is False:
                    self.game.health -= 50
                    i.being_attacked = True
            if self.current_frame == 70:
                self.current_frame = 0
            if self.current_frame_attack == 70:
                self.current_frame_attack = 0
            if self.death_frame == 70:
                self.death_frame = 0
                choices = choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                if choices == 1:
                    Coin(self.game, self.pos.x, self.pos.y)
                elif choices == 2:
                    HEART(self.game, self.pos.x, self.pos.y)
                self.kill()
            if self.rect.colliderect((i.rect.x - 30, i.rect.y - 10,
                                      i.rect.width + 60, i.rect.height + 60)) == 1 and self.mob_death is False:
                if i.forward_on is True:
                    self.image = self.game.golem_attackb[self.current_frame_attack // 10]
                elif i.back_on is True:
                    self.image = self.game.golem_attackf[self.current_frame_attack // 10]
                elif i.right_on is True:
                    self.image = self.game.golem_attackr[self.current_frame_attack // 10]
                elif i.left_on is True:
                    self.image = self.game.golem_attackl[self.current_frame_attack // 10]

            elif self.mob_death is False:
                if (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                   (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    self.image = self.game.golem_for[self.current_frame // 10]
                    self.forward_on = True
                    self.back_on = False
                    self.left_on = False
                    self.right_on = False

                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                      self.image = self.game.golem_left[self.current_frame // 10]
                      self.forward_on = False
                      self.back_on = False
                      self.left_on = True
                      self.right_on = False
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                      self.image = self.game.golem_right[self.current_frame // 10]
                      self.forward_on = False
                      self.back_on = False
                      self.left_on = False
                      self.right_on = True
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                      self.image = self.game.golem_back[self.current_frame // 10]
                      self.forward_on = False
                      self.back_on = True
                      self.left_on = False
                      self.right_on = False
            elif self.mob_death is True:
                self.image = self.game.golem_death[self.death_frame // 10]
            if self.mob_death is False:
                self.rot = (i.pos - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(SLIME_SPEED)
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            self.last_pos = self.pos
            collision(self, self.game.walls, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.player_group, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            self.current_frame_attack += 1
            if self.mob_death is True:
                self.death_frame += 1
            i.offset_image()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 5:
                self.being_attacked = False
                self.damage_time = 0

class Spider(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = MOB_LAYER
        self.color = choice(("green", "red", "blue"))
        if self.color == "green":
            self.image = game.green_spider_for[0]
        elif self.color == "blue":
            self.image = game.blue_spider_for[0]
        elif self.color == "red":
            self.image = game.red_spider_for[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        if self.color == "red":
            self.health = RED_SLIME_HEALTH
        elif self.color == "blue":
            self.health = BLUE_SLIME_HEALTH
        elif self.color == "green":
            self.health = GREEN_SLIME_HEALTH
        self.current_frame = 0
        self.mob_death = False
        self.slime_knockback = SLIME_KNOCKBACK
        self.mob_agro = True
        self.being_attacked = False
        self.damage_time = 0
        self.forward_on = True
        self.back_on = False
        self.left_on = False
        self.right_on = False
        self.death_frame = 0

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.death_frame = 0
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            enemy_hit(self, self.game)
            if self.health < 1:
                self.death()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 5:
                self.being_attacked = False
                self.damage_time = 0
            if self.death_frame == 40:
                self.death_frame = 0
                self.kill()
            if self.current_frame == 100:
                self.current_frame = 0
                if self.mob_death is True:
                    choices = choice(
                        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                    if choices == 1:
                        Coin(self.game, self.pos.x, self.pos.y)
                    elif choices == 2:
                        HEART(self.game, self.pos.x, self.pos.y)
                    self.kill()

            elif self.mob_death is False:
                if (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                   (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    if self.color == "green":
                        self.image = self.game.green_spider_back[self.current_frame // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_spider_back[self.current_frame // 10]
                    elif self.color == "red":
                        self.image = self.game.red_spider_back[self.current_frame // 10]
                    self.forward_on = True
                    self.back_on = False
                    self.left_on = False
                    self.right_on = False
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                    if self.color == "green":
                        self.image = self.game.green_spider_left[self.current_frame // 10]
                    elif self.color == "blue":
                        self.image = self.game.blue_spider_left[self.current_frame // 10]
                    elif self.color == "red":
                        self.image = self.game.red_spider_left[self.current_frame // 10]
                    self.forward_on = False
                    self.back_on = False
                    self.left_on = True
                    self.right_on = False
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                     if self.color == "green":
                         self.image = self.game.green_spider_right[self.current_frame // 10]
                     elif self.color == "blue":
                         self.image = self.game.blue_spider_right[self.current_frame // 10]
                     elif self.color == "red":
                         self.image = self.game.red_spider_right[self.current_frame // 10]
                     self.forward_on = False
                     self.back_on = False
                     self.left_on = False
                     self.right_on = True
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                     if self.color == "green":
                         self.image = self.game.green_spider_for[self.current_frame // 10]
                     elif self.color == "blue":
                         self.image = self.game.blue_spider_for[self.current_frame // 10]
                     elif self.color == "red":
                         self.image = self.game.red_spider_for[self.current_frame // 10]
                     self.forward_on = False
                     self.back_on = True
                     self.left_on = False
                     self.right_on = False
            else:
                if self.color == "green":
                    self.image = self.game.green_spider_death[self.death_frame // 10]
                elif self.color == "red":
                    self.image = self.game.red_spider_death[self.death_frame // 10]
                elif self.color == "blue":
                    self.image = self.game.blue_spider_death[self.death_frame // 10]

            if self.rect.colliderect((i.rect.x - 10, i.rect.y - 10,
                                      i.rect.width + 20, i.rect.height + 20)) == 1:
                if self.game.health > 0 and i.being_attacked is False and self.mob_death is False:
                    self.game.health -= 50
                    i.being_attacked = True
            if i.visible is True:
                self.rot = (i.pos - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(SLIME_SPEED)
            if self.mob_death is False:
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            collision(self, self.game.walls, 'x')
            collision(self, self.game.player_group, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.water, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.water, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            self.current_frame += 1
            if self.mob_death is True:
                self.death_frame += 1

            i.offset_image()
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank

class Worm(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mob
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = MOB_LAYER
        self.color = choice(("green", "red", "blue"))
        if self.color == "green":
            self.image = game.green_spider_for[0]
        elif self.color == "blue":
            self.image = game.blue_spider_for[0]
        elif self.color == "red":
            self.image = game.red_spider_for[0]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        if self.color == "red":
            self.health = RED_SLIME_HEALTH
        elif self.color == "blue":
            self.health = BLUE_SLIME_HEALTH
        elif self.color == "green":
            self.health = GREEN_SLIME_HEALTH
        self.current_frame = 0
        self.mob_death = False
        self.slime_knockback = SLIME_KNOCKBACK
        self.mob_agro = True
        self.being_attacked = False
        self.damage_time = 0
        self.forward_on = True
        self.back_on = False
        self.left_on = False
        self.right_on = False
        self.death_frame = 0
        self.dirt_on = True
        self.dirt_frame = 0

    def death(self):
        if self.mob_death is False:
            self.mob_death = True
            self.death_frame = 0
            self.game.mob_die.play()

    def avoid_mobs(self):
        for mob in self.game.mob:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < ADVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        for i in self.game.player_group:
            i.unoffset_image()
            if self.health < 1:
                self.death()
            if self.being_attacked is True:
                self.damage_time += self.game.dt
            if self.damage_time >= 1:
                self.being_attacked = False
                self.damage_time = 0
            if self.death_frame == 30:
                self.death_frame = 0
                self.kill()
            if self.dirt_frame == 100:
                self.dirt_frame = 0
                self.dirt_on = False
            if self.current_frame == 90:
                self.current_frame = 0
                self.dirt_on = True
            if self.mob_death is True:
                choices = choice(
                    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
                if choices == 1:
                    Coin(self.game, self.pos.x, self.pos.y)
                elif choices == 2:
                    HEART(self.game, self.pos.x, self.pos.y)
                self.kill()
            elif self.mob_death is False:
                if (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                   (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    if self.dirt_on is False:
                        self.image = self.game.worm_back[self.current_frame // 10]
                    else:
                        self.image = self.game.worm_dirt[self.dirt_frame // 20]
                    self.forward_on = True
                    self.back_on = False
                    self.left_on = False
                    self.right_on = False
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x < 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                    if self.dirt_on is False:
                        self.image = self.game.worm_left[self.current_frame // 10]
                    else:
                        self.image = self.game.worm_dirt[self.dirt_frame // 20]
                    self.forward_on = False
                    self.back_on = False
                    self.left_on = True
                    self.right_on = False
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y > 0:
                    if self.dirt_on is False:
                        self.image = self.game.worm_right[self.current_frame // 10]
                    else:
                        self.image = self.game.worm_dirt[self.dirt_frame // 20]
                    self.forward_on = False
                    self.back_on = False
                    self.left_on = False
                    self.right_on = True
                elif (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).x > 0 and \
                     (self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2).y < 0:
                    if self.dirt_on is False:
                        self.image = self.game.worm_for[self.current_frame // 10]
                    else:
                        self.image = self.game.worm_dirt[self.dirt_frame // 20]
                    self.forward_on = False
                    self.back_on = True
                    self.left_on = False
                    self.right_on = False
            else:
                self.image = self.game.worm_die[self.death_frame // 10]

            if self.rect.colliderect((i.rect.x - 10, i.rect.y - 10,
                                      i.rect.width + 20, i.rect.height + 20)) == 1:
                if self.game.health > 0 and i.being_attacked is False and self.mob_death is False and self.dirt_on is False:
                    self.game.health -= 50
                    i.being_attacked = True
            if i.visible is True:
                self.rot = (i.pos - self.pos).angle_to(vec(1, 0))
                self.rect.center = self.pos
                self.acc = vec(1, 0).rotate(-self.rot)
                self.avoid_mobs()
                self.acc.scale_to_length(SLIME_SPEED)
            if self.mob_death is False:
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.centerx = self.pos.x
            collision(self, self.game.walls, 'x')
            collision(self, self.game.player_group, 'x')
            collision(self, self.game.strawb_group, 'x')
            collision(self, self.game.water, 'x')
            self.rect.centery = self.pos.y
            collision(self, self.game.walls, 'y')
            collision(self, self.game.strawb_group, 'y')
            collision(self, self.game.water, 'y')
            collision(self, self.game.player_group, 'y')
            self.rect.center = self.rect.center
            if self.dirt_on is False:
                self.current_frame += 1
            if self.mob_death is True:
                self.death_frame += 1
            if self.dirt_on is True:
                self.dirt_frame += 1
            if self.dirt_on is False:
                enemy_hit(self, self.game)

            i.offset_image()
            if self.being_attacked is True:
                if round(self.damage_time // .2) % 2 == 0:
                    self.image = self.game.blank

