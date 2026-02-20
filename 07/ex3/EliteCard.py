from ex0.Card import Card
from ex3.Combatable import Combat
from ex3.Magical import Magic


class Elitecard(Card, Combat, Magic):
    def __init__(self, name: str, cost: str, 
                 rarity: str, attack_power: str, defense: str, mana: str):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self, game_state) -> dict:
        return {
            'card_played': self.name,
            'card_cost': self.cost,
            'card_effect': 'Elite card enters the battlefield'
            }

    def attack(self, target) -> dict:
        return {
            'attacker': {self.name},
            'target':  target,
            'damage': self.attack_power,
            'combat_type': 'melee'
            }
    
    def defend(self, incoming_damage: int) -> dict:
        bouncing_mirror = min(self.defense, incoming_damage)
        return {
            'defender': {self.name},
            'damage_taken': {bouncing_mirror}
            'damage_taken': 