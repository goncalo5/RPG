# python:
import random
import re
# kivy:
from kivy.app import App
from kivy import properties as kp
from kivy.event import EventDispatcher
from kivy.clock import Clock
# kivy - uix:
from kivy.uix.screenmanager import ScreenManager, Screen
# mine:
from settings import COINS, INIT, ITEMS, WEAPONS, PLACES, human, ENEMIES


def convert_to_gold(coins):
    # print("convert_to_gold", coins)
    try:
        coins = int(coins)
        return coins
    except:
        n_coins, coin_name = coins.split(" ")
        copper = int(n_coins) * COINS.get(coin_name).get("value")
        return copper / 100


def convert_1_set_dices2value(dices):
    # print("convert_1_set_dices2value", dices)
    if "d" not in dices:
        return dices
    n, dice = dices.split("d")
    # print(n, dice)
    value = int(n) * random.randint(1, int(dice))
    # print(value)
    return value

def convert_dices2value(dices):
    # print("convert_dices2value", dices)
    # pattern = re.compile("([0-9d]+[+-]?)")
    pattern = re.compile("([0-9d]+)([+-])?")
    matches = pattern.findall(dices)
    # print(matches)
    to_eval = ""
    for dices, operation in matches:
        # print(dices, operation)
        one_set = convert_1_set_dices2value(dices)
        # print("one_set", one_set)
        to_eval += str(one_set)
        to_eval += operation
    # print("to_eval", to_eval)
    return eval(to_eval)

# print(convert_dices2value("2d6+4"))

class Item(EventDispatcher):
    damage = kp.StringProperty("")
    damage_type = kp.StringProperty("")
    def __init__(self, settings, item_name):
        super().__init__()
        # print("Item", settings)
        self.name = item_name
        self.settings = settings
        # print("self.settings", self.settings)
        self.cost = convert_to_gold(self.settings.get("cost"))
        # print("cost", self.cost)
        self.weight = self.settings.get("weight")


class Weapon(Item):
    def __init__(self, name, weapon_name):
        super().__init__(name, weapon_name)
        self.damage = self.settings.get("damage", "")
        self.damage_type = self.settings.get("damage_type", "")


class Place(EventDispatcher):
    name = kp.StringProperty()
    def __init__(self, name):
        super().__init__()
        self.settings = PLACES.get(name)
        self.name = self.settings.get("name", "")
        self.enemies = self.settings.get("enemies", [])


class Enemy(EventDispatcher):
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings
        self.img = self.settings.get("img")
        self.atk = self.settings.get("atk", 1)
        # for weapon in self.settings.get("weapons"):

        Clock.schedule_once(self.init_app, 0)
        self.new()
    
    def init_app(self, dt):
        self.app = App.get_running_app()

    def new(self):
        self.hp = convert_dices2value(self.settings.get("hp"))




class Player(EventDispatcher):
    name = kp.StringProperty()
    place_name = kp.StringProperty(INIT.get("default_place"))
    place = kp.ObjectProperty(Place(INIT.get("default_place")))
    app = kp.ObjectProperty()
    gold = kp.NumericProperty(INIT.get("gold"))
    level = kp.NumericProperty(1)
    xp = kp.NumericProperty(0)
    speed = kp.NumericProperty(human.get("speed").get("walk"))
    carried = kp.NumericProperty()
    # combat:
    hp = kp.NumericProperty(INIT.get("hp"))
    atk = kp.StringProperty("1")
    # items:
    items = kp.ListProperty()
    items_names = kp.ListProperty()
    items_in_use = kp.ListProperty()
    items_in_use_names = kp.ListProperty()
    items_unuse = kp.ListProperty()
    items_availables_names = kp.ListProperty([" - "])
    equiped = {
        "off_hand": " - ",
        "main_hand": " - ",
        "armor": " - "
    }

    def __init__(self):
        super().__init__()
        Clock.schedule_once(self.init_app, 0)
        Clock.schedule_once(self.on_place_name, 0)

    def init_app(self, dt):
        self.app = App.get_running_app()

    def change_place(self, new_place):
        self.place_name = new_place

    def on_place_name(self, *args):
        print("on_place_name", args)
        self.place = getattr(self.app, self.place_name)
        print(self.place.name)
        self.app.manager.over_view.place_name = self.place.name

    def add_one_item(self, item_name):
        print("add_one_item", item_name)
        item = getattr(self.app, item_name)
        self.items.append(item)
        self.items_names.append(item.name)
        self.items_unuse.append(item)
        self.items_availables_names.append(item.name)

    def on_items(self, *args):
        print("on_items", args)
        self.update_the_weight_carried()

    def update_the_weight_carried(self):
        print("update_the_weight_carried")
        self.carried = 0
        for item in self.items:
            self.carried += item.weight

    def calc_gold_left(self, item_name):
        print("calc_gold_left", item_name)
        item = getattr(self.app, item_name)
        print(item, item.cost, dir(item))
        self.gold = INIT.get("gold") - item.cost
    
    def change_equipment(self, spinner, new_equipment_name, side_name):
        if spinner.selected:
            return
        spinner.selected = True
        print()
        print("change_equipment", new_equipment_name, side_name)
        print("equiped: %s, items_in_use: %s, items_availables_names: %s" % \
            (self.equiped, self.items_in_use_names, self.items_availables_names))
        
        if new_equipment_name not in self.items_availables_names:
            spinner.text = " - "
            spinner.selected = False
            return

        if new_equipment_name == " - ":
            previous = self.equiped[side_name]
            print("previous", previous)
            self.items_in_use_names.remove(previous)
            self.items_availables_names.append(previous)
            self.equiped[side_name] = " - "
        else:
            self.equiped[side_name] = new_equipment_name
            self.items_in_use_names.append(new_equipment_name)
            self.items_availables_names.remove(new_equipment_name)

        print("equiped: %s, items_in_use: %s, self.items_availables_names: %s" % \
            (self.equiped, self.items_in_use_names, self.items_availables_names))
        self.update_atk()
        spinner.selected = False

    def update_atk(self):
        print("update_atk")
        if self.equiped["main_hand"] == " - ":
            equiped = "unarmed_strike"
        else:
            equiped = self.equiped["main_hand"]
        main_hand = getattr(self.app, equiped)
        self.atk = main_hand.damage


class OverView(Screen):
    place_name = kp.StringProperty()


class ExploreMenu(Screen):
    enemy_name = kp.StringProperty()
    enemy_img = kp.StringProperty()
    enemy_hp = kp.StringProperty()
    enemy_atk = kp.StringProperty()

    def find_another_enemy(self, app):
        print("find_another_enemy")
        list_possible_enemies = (app.player.place.enemies)
        self.enemy_name = random.choice(list_possible_enemies)
        print(self.enemy_name)
        enemy = getattr(app, self.enemy_name)
        self.enemy_img = enemy.img
        self.enemy_hp = str(enemy.hp)
        self.enemy_atk = str(enemy.atk)


class MenuManager(ScreenManager):
    pass


class Manager(ScreenManager):
    pass


class GameApp(App):
    manager = kp.ObjectProperty(None)
    player = kp.ObjectProperty(Player())

    def build(self):
        self.new()
        self.manager = Manager()
        return self.manager

    def new(self):

        # Items:
        dictionary = ITEMS
        for item_name, settings in dictionary.items():
            # print("\nitem_name", item_name)
            if "cost" not in settings:
                continue
            settings = dictionary.get(item_name)
            setattr(self, item_name, Item(settings, item_name))
        # Weapons:
        dictionary = WEAPONS.get("simple_melee_weapon")
        for weapon_name, settings in dictionary.items():
            # print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings, weapon_name))
        dictionary = WEAPONS.get("martial_melee_weapon")
        for weapon_name, settings in dictionary.items():
            # print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings, weapon_name))
        dictionary = WEAPONS.get("martial_ranged_weapon")
        for weapon_name, settings in dictionary.items():
            # print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings, weapon_name))

        # Places:
        for place_name in PLACES:
            setattr(self, place_name, Place(place_name))

        # Enemies:
        for enemy_name, enemy_settings in ENEMIES.items():
            setattr(self, enemy_name, Enemy(enemy_name, enemy_settings))



if __name__ == "__main__":
    GameApp().run()