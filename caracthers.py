#!/usr/bin/python3
# import os
# import sys
# import time
import random
import pygame as pg

# my modules
from settings import YELLOW, DISPLAY, PLAYER, WATER, GROUND, GRASS, ROCK
# from battle import Battle
from common import roll_the_dices
# from common import derive_ability

vec = pg.math.Vector2


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


def collide_with_walls(sprite, group, direction):
    if direction == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False,
                                       collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2.
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2.
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if direction == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False,
                                       collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2.
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2.
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


class Caracther(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.all_sprites
        super(Caracther, self).__init__(self.group)
        self.name = None
        for hero_setting in PLAYER.items():
            setattr(self, hero_setting[0], hero_setting[1])
        self.alive = True
        self.hp = roll_the_dices(self.hp)
        try:
            self.init
        except AttributeError:
            # if that monster doesn't have init expecificated in the settings, is 0
            self.init = 0
        actions = []
        for action in self.actions:
            # print action, self.actions
            actions.append(Action(
                name=action, damage_type=self.actions[action]["damage_type"],
                to_hit_dices=self.actions[action]["to_hit"], damage_dices=self.actions[action]["damage"]))
        self.actions = actions

        self.game = game
        self.image = pg.Surface((DISPLAY['tilesize'], DISPLAY['tilesize']))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.rect.center = self.pos


class Player(Caracther):
    def __init__(self, game, x, y):
        self._layer = PLAYER['layer']
        self.groups = game.all_sprites
        super(Player, self).__init__(game, x, y)

        self.weight = 100
        self.viscosity = 1
        self.hit_rect = self.rect
        self.hit_rect.center = self.rect.center

        self.image.fill(YELLOW)

    def events(self):
        self.vel = vec(0, 0)
        # self.viscosity = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -self.base_speed * self.viscosity
        if keys[pg.K_RIGHT]:
            self.vel.x = self.base_speed * self.viscosity
        if keys[pg.K_UP]:
            self.vel.y = -self.base_speed * self.viscosity
        if keys[pg.K_DOWN]:
            self.vel.y = self.base_speed * self.viscosity
        if self.vel.length() > self.base_speed:
            self.vel.scale_to_length(self.base_speed)

    def update(self):
        self.step_on_the_floor()
        self.events()

        self.vel += self.acc * self.game.dt
        if self.vel.length() < 1:
            self.vel = vec(0, 0)
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt**2
        if self.rect.left > DISPLAY['width']:
            self.rect.right = 0

        # print(self.vel, self.acc, self.viscosity)
        self.player_collide_with_a_rock()

        self.rect.center = self.pos

    def step_on_the_floor(self):
        self.viscosity = 1
        if pg.sprite.spritecollide(self, self.game.water, False):
            # print('water')
            self.viscosity = min(self.viscosity, WATER['viscosity'])
        if pg.sprite.spritecollide(self, self.game.ground, False):
            # print('ground')
            self.viscosity = min(self.viscosity, GROUND['viscosity'])
        if pg.sprite.spritecollide(self, self.game.grass, False):
            # print('grass')
            self.viscosity = min(self.viscosity, GRASS['viscosity'])
        if pg.sprite.spritecollide(self, self.game.rocks, False):
            # print('rock')
            self.viscosity = min(self.viscosity, ROCK['viscosity'])

    # collisions:
    def player_collide_with_a_rock(self):
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.rocks, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.rocks, 'y')
        self.rect.center = self.hit_rect.center


class Monster(Caracther):
    def __init__(self):
        super(Monster, self).__init__()


class Hero(Caracther):
    def __init__(self):
        super(Hero, self).__init__()
        self.xp_for_next_level = None
        self.calc_xp_of_the_next_level()

    def calc_init_ability_scores(self):
        all_ability_scores = []
        for ability_score in range(0, 6):
            one_ability_score = []
            for dice in range(0, 4):
                one_ability_score.append(random.randint(1, 6))
            one_ability_score = sum(sorted(one_ability_score)[1:])
            all_ability_scores.append(one_ability_score)
        return sorted(all_ability_scores)

    def update_armor(self):
        self.armor = 10 + derive_ability(self.dexterity)

    def calc_xp_of_the_next_level(self):
        self.xp_for_next_level = (self.level + 1) ** 2 - 1

    def evolve_a_level(self, xp_gain):
        self.old_level = self.level
        self.old_xp = self.xp
        self.xp += xp_gain
        while self.xp >= self.xp_for_next_level:
            self.level += 1
            self.calc_xp_of_the_next_level()

    def initiate_a_new_battle(self, enemies=[]):
        self.battle = Battle(self, enemies=enemies)

#
# All Races:
#


# Dwarves
class Dwarf(Hero):
    def __init__(self):
        super(Dwarf, self).__init__()
        pass


class HillDwarf(Dwarf):
    def __init__(self):
        super(MontainDwarf, self).__init__()
        pass


class MontainDwarf(Dwarf):
    def __init__(self):
        super(MontainDwarf, self).__init__()
        pass


# elves
class Elf(Dwarf):
    def __init__(self):
        super(Elf, self).__init__()
        pass


class HighElf(Dwarf):
    def __init__(self):
        super(HighElf, self).__init__()
        pass


class WoodElf(Dwarf):
    def __init__(self):
        super(WoodElf, self).__init__()
        pass


class DarkElf(Dwarf):
    def __init__(self):
        super(DarkElf, self).__init__()
        pass


# Humans
class Human(Dwarf):
    def __init__(self):
        super(Human, self).__init__()
        pass


# Dragonborns
class Dragonborn(Dwarf):
    def __init__(self):
        super(Dragonborn, self).__init__()
        pass


# Gnome
class Gnome(Dwarf):
    def __init__(self):
        super(Gnome, self).__init__()
        pass


class ForestGnome(Dwarf):
    def __init__(self):
        super(ForestGnome, self).__init__()
        pass


class RockGnome(Dwarf):
    def __init__(self):
        super(RockGnome, self).__init__()
        pass


# Half-Orc
class HalfOrc(Dwarf):
    def __init__(self):
        super(HalfOrc, self).__init__()
        pass

#
# All Classes:
#


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Druid(Hero):
    def __init__(self):
        super(Druid, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass


class Barbarian(Hero):
    def __init__(self):
        super(Barbarian, self).__init__()
        pass

#
# All Combinations:
#


class MontainDwarfBarbarian(MontainDwarf, Barbarian):
    def __init__(self):
        super(Hero, self).__init__()
        pass


class Action(object):
    def __init__(self, name, damage_type, to_hit_dices, damage_dices):
        self.name = name
        self.to_hit_dices = to_hit_dices
        self.damage_dices = damage_dices
        self.damage_type = damage_type
        self.critical = False
        self.natural_1 = False
        self.to_hit = None
        self.damage = None
        # import pdb; pdb.set_trace()
        # self.update_values()

    def update(self):
        # print "str(self.to_hit_dices)", str(self.to_hit_dices)
        base_to_hit = roll_the_dices(str(self.to_hit_dices))
        to_hit = roll_the_dices("1d20")
        # print "to_hit", to_hit
        if to_hit == 20:
            self.critical = True
        elif to_hit == 1:
            self.natural_1 = True
        to_hit_dices = str(to_hit) + "+" * (base_to_hit >= 0) + str(base_to_hit)
        # print "to_hit_dices", to_hit_dices
        self.to_hit = roll_the_dices(to_hit_dices)

        self.damage = roll_the_dices(self.damage_dices)


#
# END
#
