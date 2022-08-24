from weapon import Weapon


class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = self.choose_weapon()

    def choose_weapon(self):
        chosen_weapon = input (f'Choose a weapon for {self.name}. Your choices: Rocket Launcher, Fireball Cannon, or Ion phaser! ').lower()
        if chosen_weapon == 'fireball cannon':
            print ('A formidable weapon!')
            print (' ')
            return Weapon('Fireball Cannon', 13)
            pass
        elif chosen_weapon == 'ion phaser':
            print ('A fine choice!')
            print (' ')
            return Weapon('Ion Phaser', 10)
            pass
        elif chosen_weapon == 'rocket launcher':
            print ('Marvelous machinery!')
            print (' ')
            return Weapon('Rocket Launcher', 15)
            pass
        else:
            print ('I don\'t see that weapon here, please choose again')
            print (' ')
            self.choose_weapon()
        
    def attack (self, opponent):
        opponent.health -= self.active_weapon.attack_power
        pass
