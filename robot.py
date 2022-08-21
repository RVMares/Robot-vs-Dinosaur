from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon('Ion Phaser', 10)
    def attack (self, opponent):
        opponent.health -= self.active_weapon.attack_power
        pass
