class Unit:
    def __init__(self, health, heat):
        self.__health = health
        self.__heat = heat

    def health(self):
        return self.__health

    def __str__(self):
        return f'Unit: {self.__health}'

    def attack(self, other):
        other.__health = other.__health - self.__heat

    def is_dead(self):
        return self.__health <= 0
