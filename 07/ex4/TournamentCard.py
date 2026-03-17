from ex0.Card import Card
from ex2.Combatable import Combat
from ex4.Rankable import Rankable


class Tournament(Card, Combat, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_power,
                 rating):
        super().__init__(name, cost, rarity)

        self.wins = 0
        self.losses = 0
        self.rating = rating
        self.attack_power = attack_power
        self.health = 10

    def play(self, game_state):
        return {
            "card_played": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def attack(self, target) -> dict:
        target.health -= self.attack_power
        return {
            "attacker": self.name,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage) -> dict:
        self.health -= incoming_damage
        return {
            "card": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health
        }

    def get_combat_stats(self):
        return {
            "name": self.name,
            "power": self.attack_power,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins * 10) - (self.losses * 5)
        return self.rating

    def update_wins(self, wins):
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses):
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
            }

    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }
