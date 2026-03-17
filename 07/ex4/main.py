from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import Tournament


def main():

    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = Tournament("Fire Dragon", 5, "Legendary", 7, 1200)
    wizard = Tournament("Ice Wizard", 4, "Rare", 5, 1150)

    id1 = platform.register_card(dragon, "dragon_001")
    id2 = platform.register_card(wizard, "wizard_001")

    print(f"{dragon.name} (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print("\n")

    print(f"{wizard.name} (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match(id1, id2)
    print("Match result:", result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    for i, card in enumerate(leaderboard, start=1):
        print(f"{i}. {card['name']} - Rating: {card['rating']} ({card['wins']}-{card['losses']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
