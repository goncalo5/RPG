#!/usr/bin/python
import random
import pygame as pg

# my modules
from settings import BLUE, GREEN, BROWN, GREY
# import caracthers

vec = pg.math.Vector2


class Place(pg.sprite.Sprite):
    def __init__(self, game, x, y, width, height, groups=None):
        if not groups:
            self.group = game.all_sprites
        else:
            self.group = groups
        super(Place, self).__init__(self.group)
        self.game = game
        self.monsters = {}
        self.width, self.height = width, height
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def del_a_monster(self, monster):
        if self.monsters[monster] <= 1:
            self.monsters.pop(monster)
        else:
            self.monsters[monster] -= 1
            # to_exec = 'self.%s = caracthers.Monster(name="%s", caracther_settings=settings.%s)' %
            #     (monster.name, monster.name, monster.name)
            # print to_exec
            # exec to_exec


class Water(Place):
    def __init__(self, game, x, y, width, height):
        groups = game.all_sprites, game.water
        super(Water, self).__init__(game, x, y, width, height, groups)
        self.image.fill(BLUE)


class Ground(Place):
    def __init__(self, game, x, y, width, height):
        groups = game.all_sprites, game.ground
        super(Ground, self).__init__(game, x, y, width, height, groups)
        self.image.fill(BROWN)


class Grass(Place):
    def __init__(self, game, x, y, width, height):
        groups = game.all_sprites, game.grass
        super(Grass, self).__init__(game, x, y, width, height, groups)
        self.image.fill(GREEN)


class Rock(Place):
    def __init__(self, game, x, y, width, height):
        groups = game.all_sprites, game.rocks
        super(Rock, self).__init__(game, x, y, width, height, groups)
        self.image.fill(GREY)
        self.pos = vec(self.rect.midbottom)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


class Forest(Place):
    def __init__(self, game):
        super(Forest, self).__init__(game)
        # self.monsters = settings.forest["monsters"]
        self.create_all_monsters()

    def create_all_monsters(self):
        for monster in settings.forest["monsters"]:
            to_exec = 'self.%s = caracthers.Monster()' %\
                (monster)
            # exec to_exec
        for monster, n_of_monsters in settings.forest["monsters"].items():
            self.monsters[getattr(self, monster)] = n_of_monsters

    def what_happened(self):
        things_in_the_forest = []
        for option, prob in settings.forest["probabilities"].items():
            things_in_the_forest += [option] * int(prob * 10)
        prob_of_something_happen = sum(settings.forest["probabilities"].values())
        if random.random() > prob_of_something_happen:
            return None
        else:
            found = random.choice(things_in_the_forest)
            if found == "monsters":
                all_monsters = []
                for monster, n_of_monsters in self.monsters.items():
                    all_monsters += [monster] * n_of_monsters
                # print "all_monsters", all_monsters
                if len(all_monsters) == 0:
                    return None
                monster_to_fight = random.choice(all_monsters)
                found = monster_to_fight
            return found


class Village(Place):
    def __init__(self):
        pass


class Montain(Place):
    def __init__(self):
        pass


class Desert(Place):
    def __init__(self):
        pass


#
# END
#
