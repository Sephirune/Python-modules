from ex4.TournamentCard import Tournament
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: dict[str, Tournament] = {}
        self.matches_played = 0
        self.next_id = 1

    def register_card(self, card: Tournament, card_id: str) -> str:
        card_id = "card_" + str(self.next_id)
        self.cards[card_id] = card
        self.next_id += 1
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        winner = random.choice([card1, card2])

        if winner == card1:
            loser = card2
        else:
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1
        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        """Para hacer la tabla, se utiliza sorted. Como sorted ordena números, hay que indicar qué es lo que queremos que se use para ordernar. En este caso, se ordenará según el rating de las cartas. Para eso se usa key=lambda."""
        """El leaderboard del ejemplo está ordenado al revés, por eso se usa reverse=True"""
        ranking = sorted(self.cards.values(), key=lambda card: card.rating,
                         reverse=True)

        result = []
        for card in ranking:
            result.append(card.get_rank_info())

        return result

    def generate_tournament_report(self) -> dict:
        ratings = [card.rating for card in self.cards.values()]
        avg = sum(ratings) // len(ratings)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
            }
