#!/usr/bin/env python3
from os import path
import random
import pygame as pg
from settings import YELLOW, DISPLAY, PLAYER
from places import Water, Ground, Grass, Rock
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER['layer']
        self.groups = game.all_sprites
        super(Player, self).__init__(self.groups)
        self.game = game
        self.image = pg.Surface((DISPLAY['tilesize'], DISPLAY['tilesize']))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.pos = vec(x, y)
        self.vel = vec(0, 0)

        self.rect.midbottom = self.pos

    def events(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -PLAYER['velocity']
        if keys[pg.K_RIGHT]:
            self.vel.x = PLAYER['velocity']
        if keys[pg.K_UP]:
            self.vel.y = -PLAYER['velocity']
        if keys[pg.K_DOWN]:
            self.vel.y = PLAYER['velocity']
        if self.vel.length() > PLAYER['velocity']:
            self.vel.scale_to_length(PLAYER['velocity'])

    def update(self):
        self.events()
        self.pos += self.vel * self.game.dt
        if self.rect.left > DISPLAY['width']:
            self.rect.right = 0

        self.rect.midbottom = self.pos


class Game(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY['width'], DISPLAY['height']))
        pg.display.set_caption(DISPLAY['title'])
        self.clock = pg.time.Clock()

        # variables
        self.cmd_key_down = False

        self.load_data()
        self.new()
        self.run()

        pg.quit()

    def load_a_thing(self, thing_file, thing_dir_list):
        thing_dir = self.dir
        for dir in thing_dir_list:
            thing_dir = path.join(thing_dir, dir)
        thing_path = path.join(thing_dir, thing_file)
        return thing_path

    def load_a_image(self, thing_file, thing_dir_list=['img'],
                     thing_size=None):
        thing_path = self.load_a_thing(thing_file, thing_dir_list)
        thing_img = pg.image.load(thing_path).convert_alpha()
        if thing_size:
            thing_img = pg.transform.scale(thing_img, thing_size)
        return thing_img

    def load_data(self):
        self.dir = path.dirname(__file__)

        pg.mixer.init()  # for sound

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.LayeredUpdates()

        self.tilesize = DISPLAY['tilesize']

        forest_map_file = self.load_a_thing('forest.csv', ['maps'])
        with open(forest_map_file) as map:
            self.map_list = map.readlines()
            # print self.map_list
            new_map = []
            for line in self.map_list:
                line = line.replace('\n', '')
                newline = []
                for word in list(line.strip().split(',')):
                    newline.append(word.strip())
                new_map.append(newline)
            self.map_list = new_map
            self.width = len(self.map_list[0]) * self.tilesize
            self.height = (len(self.map_list)) * self.tilesize
        self.screen = pg.display.set_mode((self.width, self.height))

        for i, line in enumerate(self.map_list):
            for j, tile in enumerate(line):
                x = j * self.tilesize
                y = i * self.tilesize
                if tile == 'water':
                    Water(self, x, y, self.tilesize, self.tilesize)
                if tile == 'ground':
                    Ground(self, x, y, self.tilesize, self.tilesize)
                if tile == 'grass':
                    Grass(self, x, y, self.tilesize, self.tilesize)
                if tile == 'rock':
                    Rock(self, x, y, self.tilesize, self.tilesize)

        self.player = Player(self, 100, 100)

    def run(self):
        # game loop - set  self.playing = False to end the game
        self.running = True
        while self.running:
            self.dt = self.clock.tick(DISPLAY['fps']) / 1000.
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            self.handle_common_events(event)

    def handle_common_events(self, event):
        # check for closing window
        if event.type == pg.QUIT:
            # force quit
            quit()

        if event.type == pg.KEYDOWN:
            if event.key == 310:
                self.cmd_key_down = True
            if self.cmd_key_down and event.key == pg.K_q:
                # force quit
                quit()

        if event.type == pg.KEYUP:
            if event.key == 310:
                self.cmd_key_down = False

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        pg.display.set_caption('%s - fps: %.5s' %
                               (DISPLAY['title'], self.clock.get_fps()))
        self.screen.fill(DISPLAY['bgcolor'])
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def quit(self):
        self.running = False


Game()
