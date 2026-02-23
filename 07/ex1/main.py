from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    spell = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 5, "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Epic", 6, 4)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    deck.shuffle()

    while True:
        card = deck.draw_card()
        if not card:
            break

        info = card.get_card_info()
        print(f"Drew: {card.name} ({info['type']})")

        result = card.play({})
        print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface, \
different card behaviors!")


if __name__ == "__main__":
    main()
