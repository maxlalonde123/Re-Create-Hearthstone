class Board:
    def __init__(player1, player2):
        self.players = [player1, player2]
        self.fields = [[][]]
        self.graveyards = [[][]]

    def add_card(card, pos):
        if pos > 7 or pos < 1:
            print("Invalid index")
            return -1

        if len(players[card.owner]) >= 7:
            #Range 6 is being used since index 6 is the 7th card and there can only be 7 cards on the field
            for i in range(len(players[card.owner]) - 1, 6, -1):
                players[card.owner].pop(i)
                return -2
                
        players[card.owner].insert(pos - 1, card)
        card.set_pos_num(pos)
        return 0

    def remove_card(card):
        players[card.owner].pop(card.pos)
