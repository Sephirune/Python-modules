from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    parse_type = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    return reduce(parse_type[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(value):
        return "Unknown spell"

    @spell.register
    def _(value: int):
        return f"Damage spell: {value}"

    @spell.register
    def _(value: str):
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list):
        return f"Multi-cast: {value}"

    return spell


def main():

    print("\nTesting spell reducer...")
    list_spells = [10, 20, 30, 40]
    reduced = spell_reducer(list_spells, "add")
    mult = spell_reducer(list_spells, "multiply")
    maxi = spell_reducer(list_spells, "max")

    print(f"Sum: {reduced}")
    print(f"Product: {mult}")
    print(f"Max: {maxi}")

    print("\nTesting memoized fibonacci...")

    fibo = memoized_fibonacci(10)
    fibo2 = memoized_fibonacci(15)

    print(f"Fib(10): {fibo}")
    print(f"Fib(15): {fibo2}")


if __name__ == "__main__":
    main()
