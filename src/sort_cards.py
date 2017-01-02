def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.
    
    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    
    """
    new_cards = []
    if len(cards) > 1:
        pile1 = sort_cards(cards[:len(cards) // 2])
        pile2 = sort_cards(cards[len(cards) // 2:])
        while len(pile1) > 0 and len(pile2) > 0:
            if enum(pile1[0]) > enum(pile2[0]):
                new_cards.append(pile2[0])
                pile2 = pile2[1:]
            else:
                new_cards.append(pile1[0])
                pile1 = pile1[1:]
        return new_cards + pile1 + pile2
    else:
        return cards

def enum(card):
    cards = {
                'A': 0,
                '2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                'T': 9,
                'J': 10,
                'Q': 11,
                'K': 12,
            }
    return cards[card]