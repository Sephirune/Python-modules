from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory: CardFactory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0

    def configure_engine(self, factory, strategy):
        self.factory = factory
        self.strategy: GameStrategy = strategy

    def simulate_turn(self):
        hand = self.factory.create_themed_deck(3)["deck"]
        battlefield = []
        result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt")
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
        }
