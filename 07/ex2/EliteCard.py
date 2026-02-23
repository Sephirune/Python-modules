from ex0.Card import Card
from ex2.Combatable import Combat
from ex2.Magical import Magic


class EliteCard(Card, Combat, Magic):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack_power: int, defense: int, mana: int):
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
            'attacker': self.name,
            'target':  target,
            'damage': self.attack_power,
            'combat_type': 'melee'
            }

    def defend(self, incoming_damage: int) -> dict:
        bouncing_mirror = min(self.defense, incoming_damage)
        true_damage = incoming_damage - bouncing_mirror
        return {
            'defender': self.name,
            'damage_taken': true_damage,
            'damage_blocked': bouncing_mirror,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2
        self.mana -= mana_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Elite'
        return info
