from time import sleep


class Aquarium:
    def __init__(self):
        self.capacity = 60
        self.fish_population = 25

    def water_change(self, gallons):
        if gallons > 60:
            sleep(5) # Overflow the tank
            sleep(3) # Water damage everywhere
            raise OverflowError

        else:
            sleep(3) # Clean filters
            sleep(4) # Scrub algae
            return 'Copacetic'
