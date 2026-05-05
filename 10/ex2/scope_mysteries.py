from typing import Any
from _collections_abc import Callable


def mage_counter() -> Callable:
    counter: int = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> Callable:
    init: int = initial_power

    def charge_power(x: int) -> int:
        nonlocal init
        init += x
        return init

    return charge_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator: Callable = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    sword_ench: Callable = enchantment_factory("Flaming")
    shield_ench: Callable = enchantment_factory("Frozen")
    print(sword_ench("Sword"))
    print(shield_ench("Shield"))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
