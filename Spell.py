class Spell(Card):
    def __init__(self, name, health, attack, cost, text, rarity, hero_class, school):
        super().__init__(name, health, attack, cost, text, rarity, hero_class)
        self.school = school

    