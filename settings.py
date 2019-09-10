#!/usr/bin/python

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 100)
YELLOW = (255, 255, 0)

# Screen
DISPLAY = {
    'title': "RPG Game",
    'tilesize': 32,
    'width': 360,
    'height': 480,
    'bgcolor': DARKBLUE,
    'fps': 30
}

# Player
PLAYER = {
    'layer': 2
}

ability_score = {
    "strength": {
        "racial_increases": {
            "mountain_dwarf": 2,
            "dragonborn": 2,
            "half-orc": 2,
            "human": 1,
        }
    },
    "dexterity": {
        "racial_increases": {
            "elf": 2,
            "halfling": 2,
            "forest gnome": 1,
            "human": 1,
        }
    },
    "constitution": {
        "racial_increases": {
            "dwarf": 2,
            "stout halfling": 1,
            "rock gnome": 1,
            "half-orc": 1,
            "human": 1,
        }
    },
    "intelligence": {
        "racial_increases": {
            "high elf": 1,
            "gnome": 2,
            "tiefling": 1,
            "human": 1,
        }
    },
    "wisdom": {
        "racial_increases": {
            "high dwarf": 1,
            "wood elf": 1,
            "human": 1,
        }
    },
    "charisma": {
        "racial_increases": {
            "half-elf": 2,
            "drow": 1,
            "lightfoot halfling": 1,
            "dragonborn": 1,
            "human": 1,
            "tiefling": 2,
        }
    },
    "strength": {
        "racial_increases": {
            "mountain_dwarf": 2,
            "dragonborn": 2,
            "half-orc": 2,
            "human": 1,
        }
    },
}

XP_BY_LEVEL = [
    0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000,
    85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000
]

PROFICIENCY_BONUS_BY_LEVEL = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]

dwarf = {
    "alignment": ["lawful_good"],
    "ability_score_increase": {
        "constitution": 2,
    },
    "size": "medium",
    "speed": {
        "walk": 25,
        "walk_with_heavy_armor": 25,
    },
    "darkvision": 60,
    "resilience": ["poison"],
    "proficiency": ["battleaxe", "handaxe", "throwing hammer", "warhammer"],
    "languages": ["common", "dwarvish"],
    "subrace": {
        "hill dwarf": {
            "ability_score_increase": {
                "wisdom": 1,
            },
            "hp_increase_by_level": 1,
            "aspect": {
                "height": {
                    "base": "3'8''",
                    "modifier": "+ 2d4",
                },
                "weight": {
                    "base": "115 lb",
                    "modifier": "* 2d6 lb",
                },
            },

        },
        "montain dwarf": {
            "ability_score_increase": {
                "strength": 2,
            },
            "aspect": {
                "height": {
                    "base": "4'",
                    "modifier": "+ 2d4",
                },
                "weight": {
                    "base": "115 lb",
                    "modifier": "* 2d6 lb",
                },
            },
        },
    }
}
elf = {
    "ability_score_increase": {
        "dexterity": 2,
    },
    "size": "medium",
    "speed": {
        "walk": 30,
    },
    "darkvision": 60,
    "trance": 4,  # don't need to sleep, instead meditate
    "languages": ["common", "elvish"],
    "alignment": ["chaotic_good"],
    "subrace": {
        "high_elf": {
            "ability_score_increase": {
                "intelligence": 1,
            },
            "proficiency": ["longsword", "shortsword", "shortbow", "longbow"],
            "languages": ["extra"],
            "aspect": {
                "hair": ["silver-white", "black", "blue"],
                "eyes": ["blue", "green"],
                "height": {
                    "base": "4'6'",
                    "modifier": "+ 2d10",
                },
                "weight": {
                    "base": "90 lb",
                    "modifier": "* 1d4 lb",
                },
            },
        },
        "wood_elf": {
            "ability_score_increase": {
                "wisdom": 1,
            },
            "proficiency": ["longsword", "shortsword", "shortbow", "longbow"],
            "speed": {
                "walk": 35,
            },
            "aspect": {
                "hair": ["brow", "black"],
                "eyes": ["green, brown", "hazel"],
                "height": {
                    "base": "4'6''",
                    "modifier": "+ 2d10",
                },
                "weight": {
                    "base": "100 lb",
                    "modifier": "* 1d4 lb",
                },
            },
        },
        "dark_elf": {
            "alignment": ["neutral_evil"],
            "ability_score_increase": {
                "charisma": 1,
            },
            "darkvision": 60,
            "proficiency": ["rapier", "shortsword", "hand crossbow"],
            "aspect": {
                "eyes": ["pale lilac", "pale silver", "pale pink", "pale red", "pale blue"],
                "skin": ["black"],
                "hair": ["white", "yellow"],
                "height": {
                    "base": "4'5''",
                    "modifier": "+ 2d6",
                },
                "weight": {
                    "base": "75 lb",
                    "modifier": "* 1d6 lb",
                },
            },
        },
    }
}
halfling = {
    "alignment": ["lawful_good"],
    "ability_score_increase": {
        "dexterity": 2,
    },
    "speed": {
        "walk": 25,
    },
    "1 reroll": ["attack", "ability", "saving_throws"],
    "saving_throws": ["frightened"],
    "move_through": ["> small"],
    "languages": ["common", "halfling"],
    "aspect": {
        "size": "small",
        "height": {
            "base": "2'7''",
            "modifier": "+ 2d4",
        },
        "weight": {
            "base": "35 lb",
            "modifier": "* 1 lb",
        },
    },
    "subrace": {
        "lightfoot": {
            "ability_score_increase": {
                "charisma": 1,
            },
        },
        "stout": {
            "ability_score_increase": {
                "constitution": 1,
            },
            "saving_throws": ["poison"],
            "resistance": ["poison"],
        },
    },
}
human = {
    "alignment": ["all", "neutral"],
    "ability_score_increase": {
        "all": 1,
    },
    "size": "medium",
    "speed": {
        "walk": 30,
    },
    "aspect": {
        "height": {
            "base": "4'8''",
            "modifier": "+ 2d10",
        },
        "weight": {
            "base": "110 lb",
            "modifier": "* 2d4 lb",
        },
    },
}
dragonborn = {
    "aspect": {
        "size": "medium",
        "height": {
            "base": "5'6''",
            "modifier": "+ 2d8",
        },
        "weight": {
            "base": "175 lb",
            "modifier": "* 2d6 lb",
        },

    },
    "ability_score_increase": {
        "strength": 2,
        "charisma": 1,
    },
    "speed": {
        "walk": 30,
    },
    "damage_type_by_color": {
        "black": "acid",
        "blue": "lightning",
        "brass": "fire",
        "bronze": "lightning",
        "copper": "acid",
        "gold": "fire",
        "green": "poison",
        "red": "fire",
        "silver": "cold",
        "white": "cold"
    },
    "damage_resistances": ["self_type"],
    "languages": ["common", "draconic"],
}
gnome = {
    "aspect": {
        "size": "small",
        "height": {
            "base": "2'11''",
            "modifier": "+ 2d4",
        },
        "weight": {
            "base": "35 lb",
            "modifier": "* 1 lb",
        },

    },
    "ability_score_increase": {
        "intelligence": 2,
    },
    "speed": {
        "walk": 25,
    },
    "darkvision": 60,
    "languages": ["common", "gnomish", "small_beasts"],
    "alignment": ["neutral_good"],
    "subrace": {
        "forest gnomes": {
            "ability_score_increase": {
                "dexterity": 1,
            },
            "proficiency": ["longsword", "shortsword", "shortbow", "longbow"],
            "languages": ["extra"]
        },
        "rock gnomes": {
            "ability_score_increase": {
                "constitution": 1,
            },
            "proficiency": ["longsword", "shortsword", "shortbow", "longbow"],
            "speed": {
                "walk": 35,
            },
        },
    },
}
halfelf = {
    "aspect": {
        "size": "medium",
        "height": {
            "base": "4'9''",
            "modifier": "+ 2d8",
        },
        "weight": {
            "base": "110 lb",
            "modifier": "* 2d4 lb",
        },

    },
    "ability_score_increase": {
        "charisma": 2,
        "other": 1,
        "other": 1,
    },
    "speed": {
        "walk": 30,
    },
    "darkvision": 60,
    "saving_throws": ["charm"],
    "immune": ["sleep_by_magic"],
    "proficiency": ["choose_2"],
    "languages": ["common", "elvish", "other"],

}
halforc = {
    "aspect": {
        "size": "medium",
        "height": {
            "base": "4'10''",
            "modifier": "+ 2d10",
        },
        "weight": {
            "base": "140 lb",
            "modifier": "* 2d6 lb",
        },

    },
    "ability_score_increase": {
        "strength": 2,
        "constitution": 1,
    },
    "speed": {
        "walk": 30,
    },
    "darkvision": 60,
    "proficiency": ["intimidation"],
    "languages": ["common", "orc"],
}
tiefling = {
    "aspect": {
        "eyes": ["black", "red", "white", "silver", "gold"],
        "hair": ["dark"],
        "size": "medium",
        "x": "2d8",
        "height": {
            "base": "4'9''",
            "modifier": "+ x",
        },
        "weight": {
            "base": "110 lb",
            "modifier": "+ x * 2d4 lb",
        },
    },
    "ability_score_increase": {
        "intelligence": 1,
        "charisma": 2,
    },
    "speed": {
        "walk": 30,
    },
    "darkvision": 60,
    "resistance": ["fire"],
    "languages": ["common", "infernal"],
}

RACES = {"dwarf": dwarf, "elf": elf, "human": human, "dragonborn": dragonborn,
         "gnome": gnome, "half-orc": halforc}

CLASSES = ["barbarian", "bard", "cleric", "druid", "fighter", "monk",
           "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

barbarian = {
    "alignment": ["chaotic_neutral"],
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["rage", "unarmored_defense"],          # 1
        ["reckless_attack", "danger_sense"],    # 2
        ["primal_path"],                        # 3
        ["ability_score_improvement"],          # 4
        ["extra_attack", "fast_movement"],      # 5
        ["path_feature"],                       # 6
        ["feral_instinct"],                     # 7
        ["ability_score_improvement"],          # 8
        ["brutal_critical_1die"],               # 9
        ["path_feature"],                       # 10
        ["relentless_rage"],                    # 11
        ["ability_score_improvement"],          # 12
        ["brutal_critical_2dice"],              # 13
        ["path_feature"],                       # 14
        ["persistent_rage"],                    # 15
        ["ability_score_improvement"],          # 16
        ["brutal_critical_3dice"],              # 17
        ["indomitable might"],                  # 18
        ["ability_score_improvement"],          # 19
        ["primal_champion"],                    # 20
    ],
    "rages by level":              [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, "unlimited"],
    "rage damage by level":        [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],

    "abilities order": ["strength", "constitution"],
    "hit dice per level": "1d12",
    "hp level 1": "12+constitution",
    "hp per level": "1d12+constitution",
    "proficiency": {
        "armor": ["ligh", "medium", "shield"],
        "weapons": ["simple", "martial"],
        "saving throw": ["strength", "constitution"],
        "skills": ["choose_2", "animal_handling", "athletics", "intimidation", "nature", "perception", "survival"],
    },
    "equipment": [
        ["choose_1", "greataxe", "martial melee weapon"],
        ["choose_1", "2 handaxe", "simple weapon"],
        ["explorer's pack", "4 javelins"],
    ],
    "wealth": "2d4 * 10 gp",
}
bard = {
    "alignment": ["chaotic_neutral"],
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["spellcasting", "bardic_inspiration (d6)"],                    # 1
        ["jack_of_all_trades", "song_of_rest (d6)"],                    # 2
        ["bard_college", "expertise"],                                  # 3
        ["ability_score_improvement"],                                  # 4
        ["bardic_inspiration (d8)", "font_of_inspiration"],             # 5
        ["countercharm", "bard_college_feature"],                       # 6
        [],                                                             # 7
        ["ability_score_improvement"],                                  # 8
        ["song_of_rest (d8)"],                                          # 9
        ["bardic_inspiration (d10)", "expertise", "magical_secrets"],   # 10
        [],                                                             # 11
        ["ability_score_improvement"],                                  # 12
        ["song_of_rest (d10)"],                                         # 13
        ["magical_secrets", "bard_college_feature"],                    # 14
        ["bardic_inspiration (d12)"],                                   # 15
        ["ability_score_improvement"],                                  # 16
        ["song_of_rest (d12)"],                                         # 17
        ["magical_secrets"],                                            # 18
        ["ability_score_improvement"],                                  # 19
        ["superior_inspiration"],                                       # 20
    ],
    "cantrips known":               [2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    "spells known":                 [4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 15, 16, 18, 19, 19, 20, 22, 22, 22],
    "spell slots per spell level": [
        [2], [3], [4, 2], [4, 3], [4, 3, 2], [4, 3, 3], [4, 3, 3, 1], [4, 3, 3, 1],
        [4, 3, 3, 2], [4, 3, 3, 3, 1], [4, 3, 3, 3, 2], [4, 3, 3, 3, 2, 1], [4, 3, 3, 3, 2, 1, 1],
        [4, 3, 3, 3, 2, 1, 1], [4, 3, 3, 3, 2, 1, 1, 1], [
            4, 3, 3, 3, 2, 1, 1, 1], [4, 3, 3, 3, 2, 1, 1, 1, 1],
        [4, 3, 3, 3, 3, 3, 1, 1, 1, 1], [4, 3, 3, 3, 3, 2, 1, 1, 1], [4, 3, 3, 3, 3, 2, 2, 1, 1]
    ],

    "hit dice per level": "1d8",
    "hp level 1": "8+constitution",
    "hp per level": "1d8+constitution",
    "proficiency": {
        "armor": ["ligh"],
        "weapons": ["simple", "hand crossbow", "longsword", "rapier", "shortsword"],
        "tools": ["choose_3", "musical instrument"],
        "saving throw": ["dexterity", "charisma"],
        "skills": ["choose_3"],
    },
    "equipment": [
        ["choose_1", "rapier", "longsword", "simple weapon"],
        ["choose_1", "diplomat's_pack", "entertainer's pack"],
        ["choose_1", "lute", "any musical instrument"],
        ["leather armor", "dagger"],
    ],
    "wealth": "5d4 * 10 gp",
}
cleric = {
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["spellcasting", "divine_domain"],                          # 1
        ["channel_divinity (1/rest)", "divine_domain feature"],     # 2
        [],                                                         # 3
        ["ability_score_improvement"],                              # 4
        ["destroy_undead (CR 1/2)"],                                # 5
        ["channel_divinity (2/rest)", "divine_domain feature"],     # 6
        [],                                                         # 7
        ["ability_score_improvement", "destroy_undead (CR1)"],      # 8
        [],                                                         # 9
        ["divine_intervention"],                                    # 10
        ["destroy_undead (CR 2)"],                                  # 11
        ["ability_score_improvement"],                              # 12
        [],                                                         # 13
        ["destroy_undead (CR 3"],                                   # 14
        [],                                                         # 15
        ["ability_score_improvement"],                              # 16
        ["destroy_undead (CR 4)", "divine_intervention"],           # 17
        ["channel_divinity (3/rest"],                               # 18
        ["ability_score_improvement"],                              # 19
        ["divine_intervention_improvement"],                        # 20
    ],
    "cantrips known":               [3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    "spell slots per spell level": [
        [2], [3], [4, 2], [4, 3], [4, 3, 2], [4, 3, 3], [4, 3, 3, 1], [4, 3, 3, 1],
        [4, 3, 3, 2], [4, 3, 3, 3, 1], [4, 3, 3, 3, 2], [4, 3, 3, 3, 2, 1], [4, 3, 3, 3, 2, 1, 1],
        [4, 3, 3, 3, 2, 1, 1], [4, 3, 3, 3, 2, 1, 1, 1], [
            4, 3, 3, 3, 2, 1, 1, 1], [4, 3, 3, 3, 2, 1, 1, 1, 1],
        [4, 3, 3, 3, 3, 3, 1, 1, 1, 1], [4, 3, 3, 3, 3, 2, 1, 1, 1], [4, 3, 3, 3, 3, 2, 2, 1, 1]
    ],

    "hit dice per level": "1d8",
    "hp level 1": "8+constitution",
    "hp per level": "1d8+constitution",
    "proficiency": {
        "armor": ["ligh", "medium", "shield"],
        "weapons": ["simple"],
        "saving throw": ["wisdom", "charisma"],
        "skills": ["choose_2", "history", "insight", "medicine", "persuasion", "religion"],
    },
    "equipment": [
        ["choose_1", "mace", "warhammer"],
        ["choose_1", "scale mail", "leather armor", "chain mail"],
        ["choose_1", "light crossbow and 20 bolts", "simple weapon"],
        ["choose_1", "priest's pack", "explorer's, pack"],
        ["shield", "holy symbol"],
    ],
    "wealth": "5d4 * 10 gp",
}
druid = {
    "alignment": ["neutral"],
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["druidic", "spellcasting"],                                # 1
        ["wild_shape", "druid_circle"],                             # 2
        [],                                                         # 3
        ["wild_shape_improvement", "ability_score_improvement"],    # 4
        [],                                                         # 5
        ["druid_circle_feature"],                                   # 6
        [],                                                         # 7
        ["wild_shape_improvement", "ability_score_improvement"],    # 8
        [],                                                         # 9
        ["druid_circle_feature"],                                   # 10
        [],                                                         # 11
        ["ability_score_improvement"],                              # 12
        [],                                                         # 13
        ["druid_circle_feature"],                                   # 14
        [],                                                         # 15
        ["ability_score_improvement"],                              # 16
        [],                                                         # 17
        ["timeless_body", "beast_spells"],                          # 18
        ["ability_score_improvement"],                              # 19
        ["archdruid"],                                              # 20
    ],
    "cantrips":                    [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],

    "abilities order": ["wisdom", "constitution"],
    "hit dice per level": "1d8",
    "hp level 1": "8+constitution",
    "hp per level": "1d8+constitution",
    "proficiency": {
        "armor": ["ligh", "medium", "shield"],
        "weapons": ["club", "dagger", "dart", "javelin", "mace", "quarterstaff",
                    "scimitar", "sickle", "sling", "spear"],
        "tools": ["herbalism kit"],
        "saving throw": ["intelligence", "wisdom"],
        "skills": ["choose_2", "arcana", "animal_handling", "insight", "medicine", "nature",
                   "perception", "religion", "survival"],
    },
    "equipment": [
        ["choose_1", "wooden shield", "simple weapon"],
        ["choose_1", "scimitar", "simple melee weapon"],
        ["leather armor", "explorer's pack", "druidic focus"],
    ],
    "wealth": "2d4 * 10 gp",
    "languages": ["druidic"]
}
fighter = {
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["fighting_style", "second_wind"],          # 1
        ["action_surge (1 use)"],                   # 2
        ["martial_archetype"],                      # 3
        ["ability_score_improvement"],              # 4
        ["extra_attack"],                           # 5
        ["ability_score_improvement"],              # 6
        ["martial_archetype_feature"],              # 7
        ["ability_score_improvement"],              # 8
        ["indomitable (1 use)"],                    # 9
        ["martial_archetype_feature"],              # 10
        ["extra_attack (2)"],                       # 11
        ["ability_score_improvement"],              # 12
        ["indomitable (2 uses"],                    # 13
        ["ability_score_improvement"],              # 14
        ["martial_archetype_feature"],              # 15
        ["ability_score_improvement"],              # 16
        ["action_surge (2 uses)"],                  # 17
        ["martial_archetype_feature"],              # 18
        ["ability_score_improvement"],              # 19
        ["extra_attack (3)"],                       # 20
    ],
    "cantrips known":               [0, 0, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    "spells known":                 [0, 0, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 11, 11, 12, 13],

    "abilities order": ["strength", "dexterity"],
    "hit dice per level": "1d10",
    "hp level 1": "10+constitution",
    "hp per level": "1d10+constitution",
    "proficiency": {
        "armor": ["any", "shield"],
        "weapons": ["simple", "martial"],
        "saving throw": ["strength", "constitution"],
        "skills": ["choose_2", "acrobatics", "animal_handling", "athletics", "history", "insight",
                   "intimidation", "perception", "survival"],
    },
    "equipment": [
        ["choose_1", "chain mail", "leather armor and longbow and 20 arrow"],
        ["choose_1", "martial weapon and shield", "2 martial weapon"],
        ["light crossbow and 20 bolt", "2 handaxe"],
        ["dungeoneer's pack", "explorer's pack"],
    ],
    "wealth": "5d4 * 10 gp",
    "fighting style": {
        "archery": {
            "self": {"bonus": {"ranged_atack": 2}},
        },
        "defense": {
            "self": {
                "condition": {"equipped": "armor"},
                "bonus": {"AC": 1}
            },
        },
        "dueling": {
            "self": {
                "condition": {"equipped": "1 melee weapon"},
                "bonus": {"damage": 2}
            },
        },
        "great weapon fighting": {
            "self": {
                "condition": {
                    "equipped": "two hand meele weapon",
                    "damage roll": "1 or 2",
                },
                "effect": "reroll",
            }
        },
        "protection": {
            "self": {
                "condition": {
                    "equipped": "shield",
                    "distance target1": 5,
                    "see target2": True,
                },
            },
            "target2": {"effect": {"attack": "disadvantage"}},
        },
        "two-weapon fighting": {
            "self": {
                "condition": {"equipped": "2 weapon"},
                "bonus": {"damage": "modifier"},
            },
        },
    },
}
monk = {
    "alignment": ["lawful_neutral"],
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["unarmored_defense", "martial_arts"],                      # 1
        ["ki", "unarmored_movement"],                               # 2
        ["monastic_tradition", "deflect_missiles"],                 # 3
        ["ability_score_improvement"],                              # 4
        ["extra_attack", "stunning_strike"],                        # 5
        ["ki-empowered_strikes", "monastic_tradition_feature"],     # 6
        ["evasion", "stillness_of_mind"],                           # 7
        ["ability_score_improvement"],                              # 8
        ["unarmored_movement_improvement"],                         # 9
        ["purity_of_body"],                                         # 10
        ["monastic_tradition_feature"],                             # 11
        ["ability_score_improvement"],                              # 12
        ["tongue_of_the_sun_and_moon"],                             # 13
        ["diamond_soul"],                                           # 14
        ["timeless_body"],                                          # 15
        ["ability_score_improvement"],                              # 16
        ["monastic_tradition_feature"],                             # 17
        ["empty_body"],                                             # 18
        ["ability_score_improvement"],                              # 19
        ["perfect_self"],                                           # 20
    ],
    "martial_arts": [
        "1d4", "1d4", "1d4", "1d4", "1d6", "1d6", "1d6", "1d6", "1d6", "1d6",
        "1d8", "1d8", "1d8", "1d8", "1d8", "1d8", "1d10", "1d10", "1d10", "1d10"],
    "Ki points":                    [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "unarmored movement":           [0, 10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30, 30],
    "features": [["unarmored defense"]],

    "abilities order": ["strength", "constitution"],
    "hit dice per level": "1d12",
    "hp level 1": "12+constitution",
    "hp per level": "1d12+constitution",
    "proficiency": {
        "armor": ["ligh", "medium", "shield"],
        "weapons": ["simple", "martial"],
        "saving throw": ["strength", "constitution"],
        "skills": ["choose_2", "animal_handling", "athletics", "intimidation", "nature", "perception", "survival"],
    },
    "equipment": [
        ["choose_1", "greataxe", "martial melee weapon"],
        ["choose_1", "2 handaxe", "simple weapon"],
        ["explorer's pack", "4 javelins"],
    ],
    "wealth": "5d4 gp",
}
paladin = {
    "alignment": ["lawful_good"],
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["divine_sense", "lay_on_hands"],                       # 1
        ["fighting_style", "spellcasting", "divine_smite"],     # 2
        ["divine_health", "sacred_oath"],                       # 3
        ["ability_score_improvement"],                          # 4
        ["extra_attack"],                                       # 5
        ["aura_of_protection"],                                 # 6
        ["sacred_oath_feature"],                                # 7
        ["ability_score_improvement"],                          # 8
        [],                                                     # 9
        ["aura_of_courage"],                                    # 10
        ["improved_divine_smite"],                              # 11
        ["ability_score_improvement"],                          # 12
        [],                                                     # 13
        ["cleansing_touch"],                                    # 14
        ["sacred_oath_feature"],                                # 15
        ["ability_score_improvement"],                          # 16
        [],                                                     # 17
        ["aura_improvements"],                                  # 18
        ["ability_score_improvement"],                          # 19
        ["sacred_oath_feature"],                                # 20
    ],

    "abilities order": ["strength", "charisma"],
    "hit dice per level": "1d10",
    "hp level 1": "10+constitution",
    "hp per level": "1d10+constitution",
    "proficiency": {
        "armor": ["all", "shield"],
        "weapons": ["simple", "martial"],
        "saving throw": ["wisdom", "charisma"],
        "skills": ["choose_2", "athletics", "insight", "intimidation", "medicine", "persuasion", "religion"],
    },
    "equipment": [
        ["choose_1", "martial and shield", "2 martial"],
        ["choose_1", "5 javelins", "simple melee weapon"],
        ["priest's pack", "explorer's pack"],
        ["chain mail", "holy symbol"]
    ],
    "wealth": "5d4 * 10 gp",
}
ranger = {
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["favored_enemy", "natural_explorer"],                      # 1
        ["fighting_style", "spellcasting"],                         # 2
        ["ranger_archetype", "primeval_awareness"],                 # 3
        ["ability_score_improvement"],                              # 4
        ["extra_attack"],                                           # 5
        ["favored_enemy_and_natural_explorer_improvements"],        # 6
        ["ranger_archetype_feature"],                               # 7
        ["ability_score_improvement", "land's stride"],             # 8
        [],                                                         # 9
        ["natural_explorer_improvement", "hide_in_plain_sight"],    # 10
        ["ranger_archetype_feature"],                               # 11
        ["ability_score_improvement"],                              # 12
        [],                                                         # 13
        ["favored_enemy_improvement", "vanish"],                    # 14
        ["ranger_archetype_feature"],                               # 15
        ["ability_score_improvement"],                              # 16
        [],                                                         # 17
        ["feral_senses"],                                           # 18
        ["ability_score_improvement"],                              # 19
        ["foe_slayer"],                                             # 20
    ],

    "abilities order": ["dexterity", "wisdom"],
    "hit dice per level": "1d10",
    "hp level 1": "10+constitution",
    "hp per level": "1d10+constitution",
    "proficiency": {
        "armor": ["ligh", "medium", "shield"],
        "weapons": ["simple", "martial"],
        "saving throw": ["strength", "dexterity"],
        "skills": ["choose_3", "animal_handling", "athletics", "insight", "investigation",
                   "nature", "perception", "stealth", "survival"],
    },
    "equipment": [
        ["choose_1", "scale_mail", "leather_armor"],
        ["choose_1", "2 shortsword", "2 simple_melee_weapon"],
        ["choose_1", "dungeoneer's_pack", "explorer's_pack"],
        ["longbow", "20 arrows"],
    ],
    "wealth": "5d4 * 10 gp",
}
rogue = {
    "alignment": ["chaotic_neutral"],
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "sneak_attack": ["1d6", "1d6", "2d6", "2d6", "3d6", "3d6", "4d6", "4d6", "5d6", "5d6", "6d6",
                     "6d6", "7d6", "7d6", "8d6", "8d6", "9d6", "9d6", "10d6", "10d6"],
    "features": [
        ["expertise", "sneak_attack", "thieves'_cant"],     # 1
        ["cunning_action"],                                 # 2
        ["roguish_archetype"],                              # 3
        ["ability_score_improvement"],                      # 4
        ["uncanny_dodge"],                                  # 5
        ["expertise"],                                      # 6
        ["evasion"],                                        # 7
        ["ability_score_improvement"],                      # 8
        ["roguish_archetype_feature"],                      # 9
        ["ability_score_improvement"],                      # 10
        ["reliable_talent"],                                # 11
        ["ability_score_improvement"],                      # 12
        ["roguish_archetype_feature"],                      # 13
        ["blindsense"],                                     # 14
        ["slippery_mind"],                                  # 15
        ["ability_score_improvement"],                      # 16
        ["roguish_archetype_feature"],                      # 17
        ["elusive"],                                        # 18
        ["ability_score_improvement"],                      # 19
        ["stroke_of_luck"],                                 # 20
    ],

    "abilities order": ["dexterity", "intelligence", "charisma"],
    "hit dice per level": "1d8",
    "hp level 1": "8+constitution",
    "hp per level": "1d8+constitution",
    "proficiency": {
        "armor": ["ligh"],
        "weapons": ["simple", "hand_crosssbows", "longsword", "rapiers", "shortsword"],
        "tools": ["thieves'_tool"],
        "saving throw": ["dexterity", "intelligence"],
        "skills": ["choose_4", "acrobatics", "athletics", "deception", "insight", "intimidation",
                   "investigation", "perception", "performance", "persuasion", "sleight_of_hand", "stealth"],
    },
    "equipment": [
        ["choose_1", "rapier", "shortsword"],
        ["choose_1", "shortbow and 20 arrows", "shortsword"],
        ["choose_1", "burglar's_pack", "dungeoneer's_pack", "explorer's_pack"],
        ["leather_armor", "2 dagger", "thieves'_tools"],
    ],
    "wealth": "4d4 * 10 gp",
}
sorcerer = {
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "sorcery_points_by_level":     [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "features": [
        ["spellcasting", "sorcerous_origin"],   # 1
        ["font_of_magic"],                      # 2
        ["metamagic"],                          # 3
        ["ability_score_improvement"],          # 4
        [],                                     # 5
        ["sorcerous_origin_feature"],           # 6
        [],                                     # 7
        ["ability_score_improvement"],          # 8
        [],                                     # 9
        ["metamagic"],                          # 10
        [],                                     # 11
        ["ability_score_improvement"],          # 12
        [],                                     # 13
        ["sorcerous_origin_feature"],           # 14
        [],                                     # 15
        ["ability_score_improvement"],          # 16
        ["metamagic"],                          # 17
        ["sorcerous_origin_feature"],           # 18
        ["ability_score_improvement"],          # 19
        ["sorcerous_restoration"],              # 20
    ],
    "rage damage by level":        [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],

    "abilities order": ["charisma", "constitution"],
    "hit dice per level": "1d6",
    "hp level 1": "6+constitution",
    "hp per level": "1d6+constitution",
    "proficiency": {
        "weapons": ["dagger", "dart", "slings", "quarterstaff", "light_crossbow"],
        "saving throw": ["constitution", "charisma"],
        "skills": ["choose_2", "arcana", "deception", "insight", "intimidation", "persuasion", "religion"],
    },
    "equipment": [
        ["choose_1", "light_crossbow and 20 bolts", "simple_weapon"],
        ["choose_1", "component_pouch", "arcane_focus"],
        ["choose_1", "dungeoneer's_pack", "explorer's_pack"],
        ["2 dagger"]
    ],
    "wealth": "3d4 * 10 gp",
}
warlock = {
    "proficiency_bonus_by_level":  [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["otherworldly_patron", "pact_magic"],      # 1
        ["eldritch_invocations"],                   # 2
        ["pact_boon"],                              # 3
        ["ability_score_improvement"],              # 4
        [],                                         # 5
        ["otherworldly_patron_feature"],            # 6
        [],                                         # 7
        ["ability_score_improvement"],              # 8
        [],                                         # 9
        ["otherworldly_patron_feature"],            # 10
        ["mystic_arcanum (6level)"],                # 11
        ["ability_score_improvement"],              # 12
        ["mystic_arcanum (7level)"],                # 13
        ["otherworldly_patron_feature"],            # 14
        ["mystic_arcanum (8level)"],                # 15
        ["ability_score_improvement"],              # 16
        ["mystic_arcanum (9level"],                 # 17
        [],                                         # 18
        ["ability_score_improvement"],              # 19
        ["eldritch_master"],                        # 20
    ],
    "cantrips_knowns_by_level":     [2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    "spells_knows_by_level":        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],
    "spell_slots_by_level":         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4],
    "slot_level_by_level":          [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    "invocations_known_by_level":   [0, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8],

    "abilities order": ["charisma", "constitution"],
    "hit dice per level": "1d8",
    "hp level 1": "8+constitution",
    "hp per level": "1d8+constitution",
    "proficiency": {
        "armor": ["ligh"],
        "weapons": ["simple"],
        "saving throw": ["wisdom", "charisma"],
        "skills": ["choose_2", "arcana", "deception", "history", "intimidation", "investigation",
                   "nature", "religion"],
    },
    "equipment": [
        ["choose_1", "light_crossbow and 20 bolts", "simple weapon"],
        ["choose_1", "component_pouch", "arcane_focus"],
        ["scholar's_pack", "dungeoneer's_pack"],
        ["leather_armor", "simple_weapon", "2 dagger"]
    ],
    "wealth": "4d4 * 10 gp",
}
wizard = {
    "alignment": ["lawful_neutral"],
    "proficiency_bonus_by_level":   [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    "features": [
        ["spellcasting", "arcane_recovery"],    # 1
        ["arcane_tradition"],                   # 2
        [],                                     # 3
        ["ability_score_improvement"],          # 4
        [],                                     # 5
        ["arcane_tradition_feature"],           # 6
        [],                                     # 7
        ["ability_score_improvement"],          # 8
        [],                                     # 9
        ["arcane_tradition_feature"],           # 10
        [],                                     # 11
        ["ability_score_improvement"],          # 12
        [],                                     # 13
        ["arcane_tradition_feature"],           # 14
        [],                                     # 15
        ["ability_score_improvement"],          # 16
        [],                                     # 17
        ["spell_mastery"],                      # 18
        ["ability_score_improvement"],          # 19
        ["signature_spell"],                    # 20
    ],
    "cantrips_knowns_by_level":     [3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],

    "abilities order": ["intelligence", "constitution", "dexterity", "charisma"],
    "hit dice per level": "1d6",
    "hp level 1": "6+constitution",
    "hp per level": "1d6+constitution",
    "proficiency": {
        "weapons": ["dagger", "dart", "sling", "quarterstaff", "light_crossbow"],
        "saving throw": ["intelligence", "wisdom"],
        "skills": ["choose_2", "arcana", "history", "insight", "investigation", "medicine", "religion"],
    },
    "equipment": [
        ["choose_1", "quarterstaff", "dagger"],
        ["choose_1", "component_pouch", "arcane_focus"],
        ["scholar's_pack", "explorer's_pack"],
        ["spellbook"],
    ],
    "wealth": "4d4 * 10 gp",
}


STANDARD_LANGUAGES = ["common", "dwarvish", "elvish",
                      "giant", "gnomish", "goblin", "halfling", "orc"]
EXOTIC_LANGUAGES = ["abyssal", "celestial", "draconic", "deep_speech", "infernal", "primordial",
                    "sylvan", "undercommon"]
LANGUADES = STANDARD_LANGUAGES + EXOTIC_LANGUAGES

smith = {
    "vendor": ["dwarf", "human"]
}

COINS = {
    "cp": {
        "symbol": "cp",
        "name": "copper",
        "value": 1,
    },
    "sp": {
        "symbol": "sp",
        "name": "silver",
        "value": 10,
    },
    "gp": {
        "symbol": "gp",
        "name": "gold",
        "value": 100,
    },
    "pp": {
        "symbol": "pp",
        "name": "platinum",
        "value": 1000,
    },
    "weight": "0.065 lb",
}

ARMOR = {
    # don = time it takes to put on armor
    # doff = time it takes to take off armor
    "light_armor": {
        "don": "1 min",
        "doff": "1 min",
        "padded": {
            "cost": "5 gp",
            "armor": "11 + dexterity",
            "stealth": "disadvantage",
            "weight": "8 lb",
        },
        "leather": {
            "cost": "10 gp",
            "armor": "11 + dexterity",
            "stealth": "disadvantage",
            "weight": "10 lb",
        },
        "studded_leather": {
            "cost": "45 gp",
            "armor": "12 + dexterity",
            "weight": "13 lb",
        },
    },
    "medium_armor": {
        "don": "5 min",
        "doff": "1 min",
        "hide": {
            "cost": "10 gp",
            "armor": "12 + dexterity",
            "stealth": "disadvantage",
            "weight": "12 lb",
        },
        "chain_shirt": {
            "cost": "50 gp",
            "armor": "13 + dexterity",
            "stealth": "disadvantage",
            "weight": "20 lb",
        },
        "scale_mail": {
            "cost": "50 gp",
            "armor": "14 + dexterity",
            "stealth": "disadvantage",
            "weight": "45 lb",
        },
        "breastplate": {
            "cost": "400 gp",
            "armor": "14 + dexterity",
            "weight": "20 lb",
        },
        "half_plate": {
            "cost": "750 gp",
            "armor": "15 + dexterity",
            "stealth": "disadvantage",
            "weight": "40 lb",
        },
    },
    "heavy_armor": {
        "don": "10 min",
        "doff": "5 min",
        "stealth": "disadvantage",
        "ring_mail": {
            "cost": "30 gp",
            "armor": 14,
            "weight": "8 lb",
        },
        "chain_mail": {
            "cost": "75 gp",
            "armor": 16,
            "weight": "10 lb",
        },
        "splint": {
            "cost": "200 gp",
            "armor": 17,
            "weight": "13 lb",
        },
        "plate": {
            "cost": "1500 gp",
            "armor": 18,
            "weight": "13 lb",
        },
    },
    "shield": {
        "don": "1 action",
        "doff": "1 action",
        "cost": "10 gp",
        "armor": "+ 2",
        "weight": "6 lb",
    },
}

WEAPONS = {
    "melee_range": "5'",
    "categories": ["simple", "martial"],
    "properties": ["ammunition", "finesse", "heavy", "light", "loading", "range", "reach",
                   "special", "thrown", "two-handed", "versatile"],
    "improvised": {
        "damage": "1d4",
        "range": 20,
        "long_range": 60,
    },
    "silvered": {
        "cost": 100,
        "ammunition": 10,
    },
    "lance": {
        "disadvantage": ["distance 5"],
        "properties": {
            "condition": "not mounted",
            "consequence": "two-handed",
        },
    },
    "simple_melee_weapon": {
        "club": {
            "cost": "1 sp",
            "damage": "1d4",
            "damage_type": "bludgeoning",
            "weight": 2,
            "properties": ["light"],
        },
        "dagger": {
            "cost": 2,
            "damage": "1d4",
            "damage_type": "piercing",
            "weight": 1,
            "properties": ["finesse", "light", "thrown (range 20/60)"],
        },
        "greatclub": {
            "cost": "2 sp",
            "damage": "1d8",
            "damage_type": "bludgeoning",
            "weight": 10,
            "properties": ["two-handed"],
        },
        "handaxe": {
            "cost": 5,
            "damage": "1d6",
            "damage_type": "slashing",
            "weight": 2,
            "properties": ["light", "thrown (range 20/60)"],
        },
        "javelin": {
            "cost": "5 sp",
            "damage": "1d6",
            "damage_type": "bludgeoning",
            "weight": 2,
            "properties": ["thrown (range 30/120)"],
        },
        "light_hammer": {
            "cost": 2,
            "damage": "1d4",
            "damage_type": "bludgeoning",
            "weight": 2,
            "properties": ["light", "thrown (range 20/60)"],
        },
        "mace": {
            "cost": 5,
            "damage": "1d6",
            "damage_type": "bludgeoning",
            "weight": 4,
        },
        "quarterstaff": {
            "cost": "2 sp",
            "damage": "1d6",
            "damage_type": "bludgeoning",
            "weight": 4,
            "properties": ["versatile (1d8)"],
        },
        "sickle": {
            "cost": 1,
            "damage": "1d4",
            "damage_type": "slashing",
            "weight": 2,
            "properties": ["light"],
        },
        "spear": {
            "cost": 1,
            "damage": "1d6",
            "damage_type": "piercing",
            "weight": 3,
            "properties": ["thrown (range 20/60)", "versatile (1d8)"],
        },
        "unarmed_strike": {
            "cost": 0,
            "weight": 0,
            "damage": "1",
            "damage_type": "bludgeoning",
        },
    },
    "simple_ranged_weapon": {
        "light_crossbow": {
            "cost": 25,
            "damage": "1d8",
            "damage_type": "piercing",
            "weight": 5,
            "properties": ["ammunition (range 80/320)", "loading", "two-handed"],
        },
        "dart": {
            "cost": "5 cp",
            "damage": "1d4",
            "damage_type": "piercing",
            "weight": 0.25,
            "properties": ["finesse", "thrown (range 20/60)"],
        },
        "shortbow": {
            "cost": 25,
            "damage": "1d6",
            "damage_type": "piercing",
            "weight": 2,
            "properties": ["ammunition (range 80/320)", "two-handed"],
        },
        "sling": {
            "cost": "1 sp",
            "damage": "1d4",
            "damage_type": "bludgeoning",
            "properties": ["ammunition (range 80/320)"],
        },
    },
    "martial_melee_weapon": {
        "battleaxe": {
            "cost": 10,
            "damage": "1d8",
            "damage_type": "slashing",
            "weight": 4,
            "properties": ["versatile (1d10)"],
        },
        "flail": {
            "cost": 10,
            "damage": "1d8",
            "damage_type": "bludgeoning",
            "weight": 2,
        },
        "glaive": {
            "cost": 20,
            "damage": "1d10",
            "damage_type": "slashing",
            "weight": 6,
            "properties": ["heavy", "reach", "two-handed"],
        },
        "greataxe": {
            "cost": 30,
            "damage": "1d12",
            "damage_type": "slashing",
            "weight": 7,
            "properties": ["heavy", "two-handed"],
        },
        "greatsword": {
            "cost": 50,
            "damage": "2d6",
            "damage_type": "slashing",
            "weight": 6,
            "properties": ["heavy", "two-handed"],
        },
        "halberd": {
            "cost": 20,
            "damage": "1d10",
            "damage_type": "slashing",
            "weight": 6,
            "properties": ["heavy", "reach", "two-handed"],
        },
        "lance": {
            "cost": 10,
            "damage": "1d12",
            "damage_type": "piercing",
            "weight": 6,
            "properties": ["reach", "special"],
        },
        "longsword": {
            "cost": 15,
            "damage": "1d8",
            "damage_type": "slashing",
            "weight": 3,
            "properties": ["versatile (1d10)"],
        },
        "maul": {
            "cost": 10,
            "damage": "2d6",
            "damage_type": "bludgeoning",
            "weight": 10,
            "properties": ["heavy", "two-handed"],
        },
        "morningstar": {
            "cost": 10,
            "damage": "1d12",
            "damage_type": "piercing",
            "weight": 4,
        },
        "pike": {
            "cost": 5,
            "damage": "1d10",
            "damage_type": "piercing",
            "weight": 18,
            "properties": ["heavy", "reach", "two-handed"],
        },
        "rapier": {
            "cost": 25,
            "damage": "1d8",
            "damage_type": "piercing",
            "weight": 2,
            "properties": ["finesse"],
        },
        "scimitar": {
            "cost": 25,
            "damage": "1d6",
            "damage_type": "slashing",
            "weight": 3,
            "properties": ["finesse", "light"],
        },
        "shortsword": {
            "cost": 10,
            "damage": "1d6",
            "damage_type": "piercing",
            "weight": 2,
            "properties": ["finesse", "reach"],
        },
        "trident": {
            "cost": 5,
            "damage": "1d6",
            "damage_type": "piercing",
            "weight": 4,
            "properties": ["thrown (range 20/60)", "versatile (1d8)"],
        },
        "war_pick": {
            "cost": 10,
            "damage": "1d8",
            "damage_type": "piercing",
            "weight": 4,
            "properties": ["thrown (range 20/60)", "versatile (1d8)"],
        },
        "warhammer": {
            "cost": 15,
            "damage": "1d8",
            "damage_type": "bludgeoning",
            "weight": 2,
            "properties": ["versatile (1d10)"],
        },
        "whip": {
            "cost": 2,
            "damage": "1d4",
            "damage_type": "piercing",
            "weight": 3,
            "properties": ["finesse", "reach"],
        },
    },
    "martial_ranged_weapon": {
        "blowgun": {
            "cost": 10,
            "damage": "1",
            "damage_type": "piercing",
            "weight": 1,
            "properties": ["ammunition (range 25/100)", "loading"],
        },
        "hand_crossbow": {
            "cost": 75,
            "damage": "1d6",
            "damage_type": "piercing",
            "weight": 3,
            "properties": ["ammunition (range 30/120)", "light", "loading"],
        },
        "heavy_crossbow": {
            "cost": 50,
            "damage": "1d10",
            "damage_type": "piercing",
            "weight": 18,
            "properties": ["ammunition (range 30/120)", "heavy", "loading", "two-handed"],
        },
        "longbow": {
            "cost": 50,
            "damage": "1d8",
            "damage_type": "piercing",
            "weight": 7,
            "properties": ["ammunition (range 150/600)", "heavy", "two-handed"],
        },
        "net": {
            "cost": 1,
            "weight": 3,
            "properties": ["special", "thrown (range 5/15)"],
            "immune": ["huge", "large", "formless"],
        },
    },
}

INIT = {
    "gold": 20,
    "default_place": "village",
    "items_chose": ["backpack", "crowbar", "net", "whip", "pike", "spear", "dagger"]
}



ITEMS = {
    "packs": {
        "burglar's_pack": {
            "cost": 16,
            "content": ["backpack", "ball_bearings", "10 ft string", "bell", "5 candles",
                        "crowbar", "hammer", "10 pitons", "hooded_lantern", "2 oil", "5 rations",
                        "tinderbox", "waterskin", "hempen_rope"],
        },
        "diplomat's_pack": {
            "cost": 39,
            "content": ["chest", "2 map_or_scroll_case", "fine_clothes", "ink", "ink_pen",
                        "lamp", "2 oil", "5 paper", "perfume", "sealing_wax", "soap"],
        },
        "dungeoneer's_pack": {
            "cost": 12,
            "content": ["backpack", "crowbar", "hammer", "10 pitons", "10 torches",
                        "tinderbox", "10 rations", "waterskin", "hempen_rope"],
        },
        "entertainer's_pack": {
            "cost": 40,
            "content": ["backpack", "bedroll", "2 costume_clothes", "5 candles", "5 rations",
                        "waterskin", "disguise_kit"],
        },
        "explorer's_pack": {
            "cost": 10,
            "content": ["backpack", "bedroll", "mess_kit", "tinderbox", "10 torches",
                        "10 rations", "waterskin", "hempen_rope"],
        },
        "priest's_pack": {
            "cost": 19,
            "content": ["backpack", "blanket", "10 candles", "tinderbox", "5 candles",
                        "crowbar", "hammer", "10 pitons", "hooded_lantern", "2 oil", "5 rations",
                        "tinderbox", "waterskin", "hempen_rope"],
        },
        "burglar's_pack": {
            "cost": 16,
            "content": ["backpack", "ball_bearings", "10 ft string", "bell", "5 candles",
                        "crowbar", "hammer", "10 pitons", "hooded_lantern", "2 oil", "5 rations",
                        "tinderbox", "waterskin", "hempen_rope"],
        },
    },
    "abacus": {
        "cost": 2,
        "weight": 2,
    },
    "acid": {
        "container": "vial",
        "cost": 25,
        "weight": 1,
    },
    "alchemist's_fire": {
        "container": "flask",
        "cost": 50,
        "weight": 1,
    },
    "ammunition": {
        "arrows": {
            "quantity": 20,
            "cost": 1,
            "weight": 1,
        },
        "blowgun_needles": {
            "quantity": 50,
            "cost": 1,
            "weight": 1,
        },
        "crossbow_bolts": {
            "quantity": 20,
            "cost": 1,
            "weight": 1.5,
        },
        "sling_bullets": {
            "quantity": 20,
            "cost": "4 cp",
            "weight": 1.5,
        },
    },
    "antitoxin": {
        "container": "vial",
        "cost": 50,
    },
    "arcane_focus": {
        "crystal": {
            "cost": 10,
            "weight": 1,
        },
        "orb": {
            "cost": 20,
            "weight": 3,
        },
        "rod": {
            "cost": 10,
            "weight": 2,
        },
        "staff": {
            "cost": 5,
            "weight": 4,
        },
        "wand": {
            "cost": 10,
            "weight": 1,
        },
    },
    "backpack": {
        "cost": 2,
        "weight": 5,
    },
    "ball_bearings": {
        "container": "bag",
        "quantity": 1000,
        "cost": 1,
        "weight": 2,
    },
    "barrel": {
        "cost": 2,
        "weight": 70,
    },
    "basket": {
        "cost": "4 sp",
        "weight": 2,
    },
    "bedroll": {
        "cost": 1,
        "weight": 7,
    },
    "bell": {
        "cost": 1,
    },
    "blanket": {
        "cost": "5 sp",
        "weight": 3,
    },
    "block_and_tackle": {
        "cost": 1,
        "weight": 5,
    },
    "book": {
        "cost": 25,
        "weight": 5,
    },
    "glass_bottle": {
        "cost": 2,
        "weight": 2,
    },
    "bucket": {
        "cost": "5 cp",
        "weight": 2,
    },
    "caltrops": {
        "container": "bag",
        "quantity": "20",
        "cost": 2,
        "weight": 2,
    },
    "candle": {
        "cost": "1 cp",
        "time": 5
    },
    "crossbow_bolt_case": {
        "cost": 1,
        "weight": 1,
        "max": 12
    },
    "map_or_scroll_case": {
        "cost": 1,
        "weight": 1,
        "max_papers": 10,
        "max_parchment": 5,
    },
    "chain": {
        "size": 10,
        "cost": 5,
        "weight": 10,
        "hp": 10,
    },
    "chalk": {
        "cost": "1 cp",
    },
    "chest": {
        "cost": 5,
        "weight": 25,
    },
    "climber's_kit": {
        "cost": 25,
        "weight": 12,
    },
    "common_clothes": {
        "cost": "5 sp",
        "weight": 3,
    },
    "costume_clothes": {
        "cost": 5,
        "weight": 4,
    },
    "fine_clothes": {
        "cost": 15,
        "weight": 6,
    },
    "traveler's_clothes": {
        "cost": 2,
        "weight": 4,
    },
    "crowbar": {
        "cost": 2,
        "weight": 5,
    },
    "druidic_focus": {
        "sprig_of_mistletoe": {
            "cost": 1,
        },
        "totem": {
            "cost": 1,
        },
        "wooden_staff": {
            "cost": 5,
            "weight": 4,
        },
        "yew_wand": {
            "cost": 10,
            "weight": 1,
        },
    },
    "fishing_tackle": {
        "cost": 1,
        "weight": 4,
    },
    "flask_or_tankard": {
        "cost": "2 cp",
        "weight": 1,
    },
    "grappling_hook": {
        "cost": 2,
        "weight": 4,
    },
    "hammer": {
        "cost": 1,
        "weight": 3,
    },
    "sledge_hammer": {
        "cost": 2,
        "weight": 10,
    },
    "healer's_kit": {
        "cost": 5,
        "weight": 3,
    },
    "holy_symbol": {
        "amulet": {
            "cost": 5,
            "weight": 1,
        },
        "emblem": {
            "cost": 5,
        },
        "reliquary": {
            "cost": 5,
            "weight": 2,
        },
    },
    "holy_water": {
        "container": "flask",
        "cost": 25,
        "weight": 1,
    },
    "hourglass": {
        "cost": 25,
        "weight": 1,
    },
    "hunting_trap": {
        "cost": 5,
        "weight": 25,
    },
    "ink": {
        "container": "bottle",
        "quantity": "1 oz",
        "cost": 10,
    },
    "ink_pen": {
        "cost": "2 cp",
    },
    "jug_or_pitcher": {
        "cost": "2 cp",
        "weight": 4,
    },
    "ladder": {
        "size": 10,
        "cost": "1 sp",
        "weight": 25,
    },
    "lamp": {
        "cost": 5,
        "weight": 1,
    },
    "bullseye_lantern": {
        "cost": 10,
        "weight": 2,
    },
    "hooded_lantern": {
        "cost": 5,
        "weight": 2,
    },
    "lock": {
        "cost": 10,
        "weight": 1,
    },
    "magnifying_glass": {
        "cost": 100,
    },
    "manacles": {
        "cost": 2,
        "weight": 6,
    },
    "mess_kit": {
        "cost": "2 sp",
        "weight": 1,
    },
    "steel_mirror": {
        "cost": 5,
        "weight": 0.5,
    },
    "oil": {
        "container": "flask",
        "cost": "1 sp",
        "weight": 1,
    },
    "paper": {
        "cost": "2 sp",
    },
    "parchment": {
        "cost": "1 sp",
    },
    "perfume": {
        "container": "vial",
        "cost": 5,
    },
    "miner's_pick": {
        "cost": 2,
        "weight": 10,
    },
    "piton": {
        "cost": "5 cp",
        "weight": 0.25,
    },
    "basic_poison": {
        "container": "vial",
        "cost": 100,
    },
    "pole": {
        "size": 10,
        "cost": "5 cp",
        "weight": 7,
    },
    "iron_pot": {
        "cost": 2,
        "weight": 10,
    },
    "potion_of_healing": {
        "cost": 50,
        "weight": 0.5,
    },
    "pouch": {
        "cost": "5 sp",
        "weight": 1,
    },
    "quiver": {
        "cost": 1,
        "weight": 1,
    },
    "portable_ram": {
        "cost": 4,
        "weight": 35,
    },
    "ration": {
        "cost": "5 sp",
        "weight": 2,
    },
    "robes": {
        "cost": 1,
        "weight": 4,
    },
    "hempen_rope": {
        "size": 50,
        "cost": 1,
        "weight": 10,
    },
    "silk_rope": {
        "size": 50,
        "cost": 10,
        "weight": 5,
    },
    "sack": {
        "cost": "1 cp",
        "weight": 0.5,
    },
    "merchant's_scale": {
        "cost": 5,
        "weight": 3,
    },
    "sealing_wax": {
        "cost": "5 sp",
    },
    "shovel": {
        "cost": 2,
        "weight": 5,
    },
    "signal_whistle": {
        "cost": "5 cp",
    },
    "signet_ring": {
        "cost": 5,
    },
    "soap": {
        "cost": "2 cp",
    },
    "spellbook": {
        "cost": 50,
        "weight": 3,
    },
    "iron_spikes": {
        "quantity": 10,
        "cost": 1,
        "weight": 5,
    },
    "spyglass": {
        "cost": 1000,
        "weight": 1,
    },
    "two-person_tent": {
        "cost": 2,
        "weight": 20,
    },
    "tinderbox": {
        "cost": "5 sp",
        "weight": 1,
    },
    "torch": {
        "cost": "1 cp",
        "weight": 1,
    },
    "vial": {
        "cost": 1,
    },
    "waterskin": {
        "cost": "2 sp",
        "weight": 5,
    },
    "whetstone": {
        "cost": "1 cp",
        "weight": 1,
    },
}


hero = {
    "options": ["select item", "explore", "move", "quit"],
    "location": "forest",
    "energy": 100,
    "hp": 10,
    "armor": 10,
    "init": 0,
    "xp": 0,
    "level": 1,

    "strength": 19,
    "dexterity": 10,
    "constitution": 12,
    "intelligence": 8,
    "wisdom": 10,
    "charisma": 10,

    "speed": 30,
    "prof": 2,

    "actions": {
        "main_hand": {
            "to_hit": 0,
            "damage": 1,
            "damage_type": "bludgeoning"
        },
    },
    "stuff": {
        "gold": 0,
        "equipped": {
            "main hand": None,
            "left hand": None,
        },
        "carried": {
        },
    },
    "aspect": {
        "race": "half-orc",
        "gender": "male",
        "height": 1.85,
        "weight": 100,
        "age": 26,
        "eye": "red",
        "hair": "black",
        "skin": "beige",
    }
}

#
# Creatures
#
bat = {
    "type": "beast",
    "size": "tiny",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "1d4-1",
    "speed": {
        "walk": 5,
        "fly": 30,
    },

    "strength": 2,
    "dexterity": 15,
    "constitution": 8,
    "intelligence": 2,
    "wisdom": 12,
    "charisma": 4,
    "senses": {
        "passive_perception": 11,
    },
    "xp": 10,

    "actions": {
        "bite": {
            "to_hit": 0,
            "damage": 1,
            "damage_type": "piercing",
        },
    }
}
black_bear = {
    "type": "beast",
    "size": "medium",
    "alignment": "unaligned",

    "armor": 11,
    "hp": "3d8+6",
    "speed": {
        "walk": 40,
        "climb": 30,
    },

    "strength": 15,
    "dexterity": 10,
    "constitution": 14,
    "intelligence": 2,
    "wisdom": 12,
    "charisma": 7,
    "skills": {
        "perception": 3,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 100,

    "actions": {
        "multiattack": ["bite", "claws"],
        "bite": {
            "to_hit": 3,
            "damage": "1d6+2",
            "damage_type": "piercing",
        },
        "claws": {
            "to_hit": 3,
            "damage": "2d4+2",
            "damage_type": "slashing",
        },
    }
}
boar = {
    "type": "beast",
    "size": "medium",
    "alignment": "unaligned",

    "armor": 11,
    "hp": "2d8+2",
    "speed": {
        "walk": 40,
    },

    "strength": 13,
    "dexterity": 11,
    "constitution": 12,
    "intelligence": 2,
    "wisdom": 9,
    "charisma": 5,
    "senses": {
        "passive_perception": 9,
    },
    "xp": 50,

    "actions": {
        "tusk": {
            "to_hit": 3,
            "damage": "1d6+1",
            "damage_type": "slashing",
        },
    }
}
brown_bear = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 11,
    "hp": "4d10+12",
    "speed": {
        "walk": 40,
        "climb": 30,
    },

    "strength": 19,
    "dexterity": 10,
    "constitution": 16,
    "intelligence": 2,
    "wisdom": 13,
    "charisma": 7,
    "skills": {
        "perception": 3,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 200,

    "actions": {
        "multiattack": ["bite", "claws"],
        "bite": {
            "to_hit": 5,
            "damage": "1d8+4",
            "damage_type": "piercing",
        },
        "claws": {
            "to_hit": 5,
            "damage": "2d6+4",
            "damage_type": "slashing",
        },
    }
}
cat = {
    "type": "beast",
    "size": "tiny",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "1d4",
    "speed": {
        "walk": 40,
        "climb": 30,
    },

    "strength": 3,
    "dexterity": 15,
    "constitution": 10,
    "intelligence": 3,
    "wisdom": 12,
    "charisma": 7,
    "skills": {
        "perception": 3,
        "stealth": 4,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 10,

    "actions": {
        "claws": {
            "to_hit": 0,
            "damage": 1,
            "damage_type": "slashing",
        },
    }
}
constrictor_snake = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "2d10+2",
    "speed": {
        "walk": 30,
        "swim": 30,
    },

    "strength": 15,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 1,
    "wisdom": 10,
    "charisma": 3,
    "senses": {
        "blindsight": 10,
        "passive_perception": 10,
    },
    "xp": 50,

    "actions": {
        "bite": {
            "to_hit": 4,
            "damage": "1d6+2",
            "damage_type": "piercing",
        },
        "constrict": {
            "to_hit": 4,
            "damage": "1d8+2",
            "damage_type": "bludgeoning",
        },
    }
}
crocodile = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "3d10+3",
    "speed": {
        "walk": 20,
        "swim": 30,
    },

    "strength": 15,
    "dexterity": 10,
    "constitution": 13,
    "intelligence": 2,
    "wisdom": 10,
    "charisma": 5,
    "skills": {
        "stealth": 2,
    },
    "senses": {
        "passive_perception": 10,
    },
    "xp": 100,

    "actions": {
        "bite": {
            "to_hit": 4,
            "damage": "1d10+2",
            "damage_type": "piercing",
        },
    }
}
dire_wolf = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 14,
    "hp": "5d10+10",
    "speed": {
        "walk": 50,
    },

    "strength": 17,
    "dexterity": 15,
    "constitution": 15,
    "intelligence": 3,
    "wisdom": 12,
    "charisma": 7,
    "skills": {
        "perception": 3,
        "stealth": 4,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 200,

    "actions": {
        "bite": {
            "to_hit": 5,
            "damage": "2d6+3",
            "damage_type": "piercing",
        },
    }
}
frog = {
    "type": "beast",
    "size": "tiny",
    "alignment": "unaligned",

    "armor": 11,
    "hp": "1d4-1",
    "speed": {
        "walk": 20,
        "swim": 20,
    },

    "strength": 1,
    "dexterity": 13,
    "constitution": 8,
    "intelligence": 1,
    "wisdom": 8,
    "charisma": 3,
    "skills": {
        "perception": 1,
        "stealth": 3
    },
    "senses": {
        "darkvision": 30,
        "passive_perception": 13,
    },
    "xp": 0,
}
giant_eagle = {
    "type": "beast",
    "size": "large",
    "alignment": "neutral good",

    "armor": 13,
    "hp": "4d10+4",
    "speed": {
        "walk": 10,
        "fly": 80,
    },

    "strength": 16,
    "dexterity": 17,
    "constitution": 13,
    "intelligence": 8,
    "wisdom": 14,
    "charisma": 10,
    "skills": {
        "perception": 4,
    },
    "senses": {
        "passive_perception": 14,
    },
    "xp": 200,

    "actions": {
        "multiattack": ["beak", "talons"],
        "bite": {
            "to_hit": 5,
            "damage": "1d6+3",
            "damage_type": "piercing",
        },
        "claws": {
            "to_hit": 5,
            "damage": "2d6+3",
            "damage_type": "slashing",
        },
    }
}
giant_spider = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 14,
    "hp": "4d10+4",
    "speed": {
        "walk": 30,
        "climb": 30,
    },

    "strength": 14,
    "dexterity": 16,
    "constitution": 12,
    "intelligence": 2,
    "wisdom": 11,
    "charisma": 4,
    "skills": {
        "stealth": 7,
    },
    "senses": {
        "blindsight": 10,
        "darkvision": 60,
        "passive_perception": 10,
    },
    "xp": 200,

    "actions": {
        "bite": {
            "to_hit": 5,
            "damage": "1d8+3",
            "damage_type": "piercing",
        },
    }
}
falcon = {
    "type": "beast",
    "size": "tiny",
    "alignment": "unaligned",

    "armor": 13,
    "hp": "1d4-1",
    "speed": {
        "walk": 40,
        "climb": 30,
    },

    "strength": 5,
    "dexterity": 16,
    "constitution": 8,
    "intelligence": 2,
    "wisdom": 14,
    "charisma": 6,
    "skills": {
        "perception": 4,
    },
    "senses": {
        "passive_perception": 14,
    },
    "xp": 10,

    "actions": {
        "claws": {
            "to_hit": 5,
            "damage": 1,
            "damage_type": "slashing",
        },
    }
}
imp = {
    "type": "fiend",
    "size": "tiny",
    "alignment": "lawful evil",

    "armor": 13,
    "hp": "3d4+3",
    "speed": {
        "walk": 20,
        "fly": 40,
    },

    "strength": 6,
    "dexterity": 17,
    "constitution": 13,
    "intelligence": 11,
    "wisdom": 12,
    "charisma": 14,
    "skills": {
        "deception": 4,
        "insight": 3,
        "persuasion": 4,
        "stealth": 5,
    },
    "damage_resistances": ["cold", "bludgeoning", "piercing", "slashing"],
    "damage_immunities": ["fire", "poison"],
    "condition_immunities": ["poisoned"],
    "senses": {
        "darkvision": 120,
        "passive_perception": 11,
    },
    "languages": ["infernal", "common"],
    "xp": 200,

    "actions": {
        "bite": {
            "to_hit": 5,
            "damage": "1d4+3",
            "damage_type": "piercing",
        },
    },
}
lion = {
    "type": "beast",
    "size": "large",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "4d10+4",
    "speed": {
        "walk": 50,
    },

    "strength": 17,
    "dexterity": 15,
    "constitution": 13,
    "intelligence": 3,
    "wisdom": 12,
    "charisma": 8,
    "skills": {
        "perception": 3,
        "stealth": 6,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 200,

    "actions": {
        "bite": {
            "to_hit": 5,
            "damage": "1d8+3",
            "damage_type": "piercing",
        },
        "claws": {
            "to_hit": 5,
            "damage": "1d6+3",
            "damage_type": "slashing",
        },
    }
}
mastiff = {
    "type": "beast",
    "size": "medium",
    "alignment": "unaligned",

    "armor": 12,
    "hp": "1d8+1",
    "speed": {
        "walk": 40,
    },

    "strength": 13,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 2,
    "wisdom": 13,
    "charisma": 7,
    "skills": {
        "perception": 3,
    },
    "senses": {
        "passive_perception": 13,
    },
    "xp": 200,

    "actions": {
        "multiattack": ["bite", "claws"],
        "bite": {
            "to_hit": 5,
            "damage": "1d8+4",
            "damage_type": "piercing",
        },
        "claws": {
            "to_hit": 5,
            "damage": "2d6+4",
            "damage_type": "slashing",
        },
    }
}

# MONSTERS = {"wolf": wolf, "bear": bear, "snake": snake}

ORDER_OF_CARACTERISTICS_TO_PRINT = ["hp", "armor", "init", "speed"]


# Places

forest = {
    "name": "Forest",
    "monsters": {
        "bat": 10,
        # "black_bear": 1,
        # "boar": 3,
    },
    "resources": {
        "wood": 100,
        "fruit": 10,
    },
    "options": {
        "Pick wood": {"energy": -10, "wood": 1},
        "Plant a tree": {"energy": -20, "tree": -1},
        "Pick apples": {"energy": -5, "apples": 1},
    },
    "probabilities": {"monsters": 0.9, "tree": 0.0, "apples": 0.0},
}
plains = {
    "name": "Plains",

}
montain = {
    "name": "Montain",
    "monsters": {
        "bear": 3,
    },
}
desert = {
    "name": "Desert",
    "monsters": {
        "snake": 10,
    },
}
village = {
    "name": "Village",
    "options": ["house", "market", "smith"],
}
mine = {

}

PLACES = {"forest": forest, "plains": plains,
          "montain": montain, "desert": desert, "village": village}


DAMAGE_TYPES = ["acid", "bludgeoning", "cold", "fire", "force", "lightning",
                "necrotic", "piercing", "poison", "psychic", "slashing", "thunder"]

#
# END
#
