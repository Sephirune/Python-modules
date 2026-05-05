from typing import Any
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args: Any, **kwargs: Any):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kwargs: Any):
        return (base_spell(*args, **kwargs) * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_cond(*args: Any, **kwargs: Any):
        if condition(*args, **kwargs) is True:
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled!!"
    return cast_cond


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args: Any, **kwargs: Any):
        return list(spell(*args, **kwargs) for spell in spells)
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} DMG"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    combi: Callable = spell_combiner(fireball, heal)
    combi_targ: tuple[str, str] = combi("dragon", 10)
    print(f"Combined spell results: {combi_targ[0]}, {combi_targ[1]}")

    print("\nTesting power amplifier...")

    def spell_dmg(x: int) -> int:
        return x

    spell_amp: Callable = power_amplifier(spell_dmg, 10)
    print(f"Original {spell_dmg(25)}, Amplified: {spell_amp(13)}")

    print("\nTesting conditional caster...")

    def is_powerful(target: str, power: int) -> bool:
        return power >= 50

    cond_cast: Callable = conditional_caster(is_powerful, fireball)
    print(cond_cast("dragon", 100))
    print(cond_cast("goblin", 10))

    print("\nTesting spell sequence...")

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} for {power} turns"

    sequence: Callable = spell_sequence([fireball, heal, shield])
    results: list = sequence("castle", 30)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
