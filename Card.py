class Card:
    def __init__(self, name, health, attack, cost, text, rarity, hero_class):
        #Owner can either be 0 or 1 since this is a two player game. When the game starts 
        self.owner = None
        self.pos_num = None
        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
        self.text = text
        self.rarity = rarity
        self.hero_class = hero_class
        self.on_board = False

    def set_pos_num(num):
        self.pos_num = num
    
    def attack(target):
        if on_board:
            self.health -= target.attack
            target.health -= self.attack

    def print_card():
        return None #TODO write this
        