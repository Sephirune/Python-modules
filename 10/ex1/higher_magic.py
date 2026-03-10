from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args: Any, **kwargs: Any):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args: Any, **kwargs: Any):
        return (base_spell(*args, **kwargs) * multiplier)
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast_cond(*args: Any, **kwargs: Any):
        if condition(*args, **kwargs) is True:
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled!!"
    return cast_cond


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args: Any, **kwargs: Any):
        return ((spell(*args, **kwargs) for spell in spells))
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combi: callable = spell_combiner(fireball, heal)
    combi_targ: tuple[str, str] = combi("dragon")
    print(f"Combined spell results: {combi_targ[0]}, {combi_targ[1]}")

    print("\nTesting power amplifier")

    def spell_dmg(x: int) -> int:
        return x

    spell_amp: callable = power_amplifier(spell_dmg, 10)
    print(f"Original {spell_dmg(25)}, Amplified: {spell_amp(13)}")


if __name__ == "__main__":
    main()
