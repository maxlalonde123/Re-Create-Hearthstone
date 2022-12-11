class Minion(card):
    def __init__(self, name, health, attack, cost, text, rarity, hero_class, species):
        super().__init__(name, health, attack, cost, text, rarity, hero_class)
        self.species = species