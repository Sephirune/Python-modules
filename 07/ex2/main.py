from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")

print("\nEliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

card = EliteCard("Arcane Warrior", 4, "Legendary", 5, 3, 5)
card_played = card.play({})
print(card_played)
print("\nCombat phase:")
attack = card.attack("Enemy")
print(f"Attack result: {attack}")
defense = card.defend(5)
print(f"Defense result: {defense}")

print("\nMagic phase:")
spell = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
print(f"Spell cast: {spell}")
channel = card.channel_mana(3)
print(f"Mana channel: {channel}")

print("\nMultiple interface implementation successful!")
