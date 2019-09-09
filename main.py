# kivy:
from kivy.app import App
from kivy import properties as kp
from kivy.event import EventDispatcher
from kivy.clock import Clock
# kivy - uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import COINS, INIT, ITEMS, WEAPONS, PLACES


def convert_to_gold(coins):
    print("convert_to_gold", coins)
    try:
        coins = int(coins)
        return coins
    except:
        n_coins, coin_name = coins.split(" ")
        copper = int(n_coins) * COINS.get(coin_name).get("value")
        return copper / 100

class Item(EventDispatcher):
    def __init__(self, settings):
        super().__init__()
        print("Item", settings)
        self.settings = settings
        print("self.settings", self.settings)
        self.cost = convert_to_gold(self.settings.get("cost"))
        print("cost", self.cost)
        self.weight = self.settings.get("weight")


class Weapon(Item):
    def __init__(self, name):
        super().__init__(name)
        self.damage = self.settings.get("damage")
        self.damage_type = self.settings.get("damage_type")


class Place(EventDispatcher):
    def __init__(self, name):
        super().__init__()
        self.settings = PLACES.get(name)
        self.screen = self.settings.get("screen")


class Player(EventDispatcher):
    name = kp.StringProperty()
    place = kp.StringProperty("forest")
    items = kp.ListProperty()
    app = kp.ObjectProperty()
    gold = kp.NumericProperty(INIT.get("gold"))
    # item_selected = kp.ObjectProperty()

    def __init__(self):
        super().__init__()
        Clock.schedule_once(self.init_app, 0)

    def init_app(self, dt):
        self.app = App.get_running_app()

    def change_place(self, new_place, change_screen=True):
        self.place = new_place
        if change_screen:
            self.app.manager.current = new_place

    def add_one_item(self, item):
        self.items.append(item)

    def calc_gold_left(self, item_name):
        print("calc_gold_left", item_name)
        item = getattr(self.app, item_name)
        print(item, item.cost, dir(item))
        self.gold = INIT.get("gold") - item.cost


class Manager(ScreenManager):
    pass


class GameApp(App):
    player = kp.ObjectProperty(Player())
    forest = kp.ObjectProperty(Place("forest"))

    def build(self):
        self.create_all_items()
        return Manager()

    def create_all_items(self):
        dictionary = ITEMS
        for weapon_name, settings in dictionary.items():
            print("\nweapon_name", weapon_name)
            if "cost" not in settings:
                continue
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings))
        dictionary = WEAPONS.get("simple_melee_weapon")
        for weapon_name, settings in dictionary.items():
            print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings))
        dictionary = WEAPONS.get("martial_melee_weapon")
        for weapon_name, settings in dictionary.items():
            print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings))
        dictionary = WEAPONS.get("martial_ranged_weapon")
        for weapon_name, settings in dictionary.items():
            print("\nweapon_name", weapon_name)
            settings = dictionary.get(weapon_name)
            setattr(self, weapon_name, Weapon(settings))



if __name__ == "__main__":
    GameApp().run()