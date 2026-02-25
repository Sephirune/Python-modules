from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        damage = 0
        cards_played = []
        for card in hand:
            cards_played.append(card)
            damage += getattr(card, "power", 0)

        return {
            'Strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'damage_dealt': damage
            }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
