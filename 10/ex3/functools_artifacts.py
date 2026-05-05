from functools import reduce, partial, lru_cache, singledispatch
import operator
from _collections_abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    parse_type: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    return reduce(parse_type[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire: Callable = partial(base_enchantment, 50, "fire")
    ice: Callable = partial(base_enchantment, 50, "ice")
    lightning: Callable = partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def spell(value: object) -> str:
        return "Unknown spell type"

    @spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value}"

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


def main() -> None:

    print("\nTesting spell reducer...")
    list_spells: list[int] = [10, 20, 30, 40]
    reduced: int = spell_reducer(list_spells, "add")
    mult: int = spell_reducer(list_spells, "multiply")
    maxi: int = spell_reducer(list_spells, "max")

    print(f"Sum: {reduced}")
    print(f"Product: {mult}")
    print(f"Max: {maxi}")

    print("\nTesting memoized fibonacci...")

    fibo: int = memoized_fibonacci(0)
    fibo2: int = memoized_fibonacci(1)
    fibo3: int = memoized_fibonacci(10)
    fibo4: int = memoized_fibonacci(15)

    print(f"Fib(10): {fibo}")
    print(f"Fib(15): {fibo2}")
    print(f"Fib(10): {fibo3}")
    print(f"Fib(10): {fibo4}")

    print("\nTesting spell dispatcher...")
    dispatch: Callable = spell_dispatcher()
    print(f"{dispatch(42)} damage")
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "lightning"]))
    print(dispatch(0.5))


if __name__ == "__main__":
    main()
