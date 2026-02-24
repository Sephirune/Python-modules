from GameStrategy import GameStrategy


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        damage = 0
        cards_played = []
        for card in hand:
            cards_played.append(card)
            damage += getattr(card, "power")

        return {
            'Strategy': self.get_strategy_name,
            'cards_played': cards_played,
            'damage_dealt': damage
            }

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

