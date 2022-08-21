from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot_contender = Robot('Gearz', 145)
        self.dinosaur_contender = Dinosaur('Peloromoloch', 15, 130)
        pass

    def run_game(self):
        self.display_welcome()
        winner = self.battle_phase()
        self.display_winner(winner)
        pass

    def display_welcome(self):
        print('Welcome to the event of century!')
        fight_bet = input('Place your bets! Who will win? Robot or Dinosaur? ').lower()
        if fight_bet == 'robot':
            print(f'You have chosen {self.robot_contender.name} as your champion!')
        elif fight_bet == 'dinosaur':
            print(f'You have chosen {self.dinosaur_contender.name} as your champion!')
        else:
            print('That contender isn\'t on the list for today, choose again!')
            self.display_welcome()
        print('Grab your popcorn, because this is about to get good!')
        return fight_bet
        pass

    def battle_phase(self):
        print(f'{self.robot_contender.name}\'s health points: {self.robot_contender.health}')
        print(f'{self.dinosaur_contender.name}\'s health points: {self.dinosaur_contender.health}')
        while self.robot_contender.health > 0 and self.dinosaur_contender.health > 0:
            print(f'{self.robot_contender.name} attacks {self.dinosaur_contender.name} with {self.robot_contender.active_weapon.name}')
            self.robot_contender.attack(self.dinosaur_contender)
            print(f'{self.dinosaur_contender.name}\'s health points: {self.dinosaur_contender.health}')
            print(f'{self.dinosaur_contender.name} attacks {self.robot_contender.name}')
            self.dinosaur_contender.attack(self.robot_contender)
            print(f'{self.robot_contender.name}\'s health points: {self.robot_contender.health}')
        if self.robot_contender.health == 0:
            the_winner = self.dinosaur_contender
            return the_winner
        elif self.dinosaur_contender.health == 0:
            the_winner = self.robot_contender
            return the_winner
        return the_winner
        pass
    
    def display_winner(self, winner):
        print(f'And the winner is ... Drumroll Please! ... {winner.name}')
        pass

