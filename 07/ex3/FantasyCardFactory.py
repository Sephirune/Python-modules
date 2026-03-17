import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex3.CardFactory import BasicCard


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creatures = ["Dragon", "Goblin"]
        self.spells = ["Fireball", "Lightning Bolt", "Ice Ball"]
        self.artifacts = ["Mana Ring", "Crystal Staff", "Magic Ruby"]

    def create_creature(self, name_or_power=None) -> Card:
        name = random.choice(self.creatures)
        return BasicCard(name, random.randint(1, 5), "common")

    def create_spell(self, name_or_power=None) -> Card:
        name = random.choice(self.spells)
        return Card(name, random.randint(1, 5))

    def create_artifact(self, name_or_power=None) -> Card:
        name = random.choice(self.artifacts)
        return Card(name, random.randint(1, 5))

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            deck.append(self.create_creature())
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": self.creatures,
            "spells": self.spells,
            "artifacts": self.artifacts
        }
