from typing import Set


def arch_hunter():
    print("=== Achievement Tracker System ===\n")

    archievement: Set[str] = set(['boss_slayer', 'collector',
                                  'first_kill', 'level_10', 'perfectionist',
                                  'speed_demon', 'treasure_hunter'])
    alice: Set[str] = set(['first_kill', 'level_10', 'treasure_hunter',
                           'speed_demon'])
    bob: Set[str] = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie: Set[str] = set(['level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist'])
    print(f"Player alice archievements: {alice}")
    print(f"Player bob archievements: {bob}")
    print(f"Player charlie archievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique archievements: {archievement}")
    print(f"Total unique archievements: {len(archievement)}\n")

    inter: Set[str] = alice.intersection(bob, charlie)
    bob_only: Set[str] = bob.difference(alice).difference(charlie)
    charlie_only: Set[str] = charlie.difference(alice).difference(bob)
    print(f"Common to all players: {inter}")
    print(f"Rare archievements (1 player): {bob_only}, {charlie_only}\n")

    albo: Set[str] = alice.intersection(bob)
    aluniq: Set[str] = alice.difference(bob)
    boluniq: Set[str] = bob.difference(alice)
    print(f"Alice vs bob common: {albo}")
    print(f"Alice unique: {aluniq}")
    print(f"Bob unique: {boluniq}")


arch_hunter()
