from weapon import Weapon


class Ion_Phaser(Weapon):
    def __init__(self) -> None:
        super().__init__('Ion Phaser', 10)