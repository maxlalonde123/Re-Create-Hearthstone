class Player:
    def __init__(hero_class, deck)
    self.hero_class = hero_class
    self.deck = deck
    self.mana = 0
    self.hand = 0

    def play_card(card):
        if mana < card.cost:
            return -1

        mana -= card.cost
        hand -= 1

        return card

