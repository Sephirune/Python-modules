from typing import Any


def mage_counter() -> callable:
    counter: int = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> callable:
    init: int = initial_power

    def charge_power(x: int):
        nonlocal init
        init += x
        return init

    return init


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return memory


def main() -> None:
    print("\nTesting mage counter...")
    counter: callable = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")
    sword_ench: callable = enchantment_factory("Flaming")
    shield_ench: callable = enchantment_factory("Frozen")
    print(sword_ench("sword"))
    print(shield_ench("shield"))


if __name__ == "__main__":
    main()
