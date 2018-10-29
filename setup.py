#!/usr/bin/env python3
from os import path
# import random
import pygame as pg
from settings import DISPLAY
from places import Camera, Water, Ground, Grass, Rock, House, Floor, Door, TiledMap, Obstacle
from caracthers import Player
vec = pg.math.Vector2


class Game(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY['width'], DISPLAY['height']))
        pg.display.set_caption(DISPLAY['title'])
        self.clock = pg.time.Clock()

        # variables
        self.cmd_key_down = False
        self.debug = False
        self.map_group = None

        self.load_data()
        self.new()
        self.run()

        pg.quit()

    def load_a_thing(self, thing_dir_list, thing_file):
        thing_dir = self.dir
        for dir in thing_dir_list:
            thing_dir = path.join(thing_dir, dir)
        thing_path = path.join(thing_dir, thing_file)
        return thing_path

    def load_a_image(self, thing_file, thing_dir_list=['img'],
                     thing_size=None):
        thing_path = self.load_a_thing(thing_dir_list, thing_file)
        thing_img = pg.image.load(thing_path).convert_alpha()
        if thing_size:
            thing_img = pg.transform.scale(thing_img, thing_size)
        return thing_img

    def load_a_map_list(self, dir, file):
        forest_map_file = self.load_a_thing(dir, file)
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
        return new_map

    def load_the_map(self):

        # map_path = self.load_a_thing(['maps'], 'sample_map.tmx')
        # map_path = self.load_a_thing(['maps'], 'tiledTemplate_isometric2.tmx')
        map_path = self.load_a_thing(['maps'], 'test.tmx')
        print(map_path)
        self.map = TiledMap(map_path)
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        print(self.map.width, self.map.height)
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'tree':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name == 'player':
                Player.load(self)
                self.player = Player(self, obj_center.x, obj_center.y)
            # if tile_object.name == 'zombie':
            #     Mob(self, obj_center.x, obj_center.y)
            # if tile_object.name in ['health', 'shotgun']:
            #     Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        # if self.map_group:
        #     for sprite in self.map_group:
        #         sprite.kill()
        # self.map_group = pg.sprite.Group()
        # self.map_width = len(self.current_map[0]) * self.tilesize
        # self.map_height = (len(self.current_map)) * self.tilesize
        # self.width = DISPLAY['width']
        # self.height = DISPLAY['height']
        #
        # # self.screen = pg.display.set_mode((self.width,
        # #                                    self.height))
        # self.screen = pg.display.set_mode((DISPLAY['width'],
        #                                    DISPLAY['height']))
        #
        # for i, line in enumerate(self.current_map):
        #     for j, tile in enumerate(line):
        #         x = j * self.tilesize
        #         y = i * self.tilesize
        #         if tile == 'water':
        #             self.map_group.add(Water(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'ground':
        #             self.map_group.add(Ground(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'grass':
        #             self.map_group.add(Grass(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'rock':
        #             self.map_group.add(Rock(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'house':
        #             self.map_group.add(House(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'floor':
        #             self.map_group.add(Floor(self, x, y, self.tilesize, self.tilesize))
        #         if tile == 'door':
        #             self.map_group.add(Door(self, x, y, self.tilesize, self.tilesize))

    def load_data(self):
        self.dir = path.dirname(__file__)

        pg.mixer.init()  # for sound

    def new(self):
        # start a new game
        self.now = pg.time.get_ticks()

        # sprites:
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.water = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.rocks = pg.sprite.Group()
        self.trees = pg.sprite.Group()
        self.houses = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.doors = pg.sprite.Group()

        # self.tilesize = DISPLAY['tilesize']

        self.forest = self.load_a_map_list(['maps'], 'forest.csv')
        self.house1 = self.load_a_map_list(['maps'], 'house1.csv')
        self.current_map = self.forest
        self.load_the_map()

    def run(self):
        # game loop - set  self.playing = False to end the game
        self.running = True
        while self.running:
            self.dt = self.clock.tick(DISPLAY['fps']) / 1000.
            self.now = pg.time.get_ticks()
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
            # quit
            if event.key == 310:
                self.cmd_key_down = True
            if self.cmd_key_down and event.key == pg.K_q:
                # force quit
                quit()

            # debug
            if event.key == pg.K_d:
                self.debug = not self.debug

        if event.type == pg.KEYUP:
            if event.key == 310:
                self.cmd_key_down = False

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        pg.display.set_caption('%s - fps: %.5s' %
                               (DISPLAY['title'], self.clock.get_fps()))

        self.screen.blit(self.map_img, self.camera.apply(rect=self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # self.screen.fill(DISPLAY['bgcolor'])
        # self.all_sprites.draw(self.screen)
        if self.debug:
            pg.draw.rect(self.screen, (100, 100, 100), self.player.hit_rect, 1)

        pg.display.flip()

    def quit(self):
        self.running = False


Game()
