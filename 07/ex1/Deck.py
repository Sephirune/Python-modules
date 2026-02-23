from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)
    """"pop quita el primer elemento de la lista, es decir, la primera carta"""

    def get_deck_stats(self) -> dict:
        if not self.cards:
            return {
                'total_cards': 0,
                'creatures': 0,
                'spells': 0,
                'artifacts': 0,
                'avg_cost': 0
            }

        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self.cards:
            info = card.get_card_info()
            total_cost += card.cost

            if info['type'] == 'Creature':
                creatures += 1
            elif info['type'] == 'Spell':
                spells += 1
            elif info['type'] == 'Artifact':
                artifacts += 1

            avg_cost = total_cost / len(self.cards)

            return {
                'total_cards': len(self.cards),
                'creatures': creatures,
                'spells': spells,
                'artifacts': artifacts,
                'avg_cost': avg_cost
            }
