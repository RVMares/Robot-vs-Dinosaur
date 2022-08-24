from weapon import Weapon


class Fireball_Cannon(Weapon):
    def __init__(self) -> None:
        super().__init__('Fireball Cannon', 10)