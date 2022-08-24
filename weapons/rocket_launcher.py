from weapon import Weapon

class Rocket_Launcher(Weapon):
    def __init__(self) -> None:
        super().__init__('Rocket Launcher', 15)