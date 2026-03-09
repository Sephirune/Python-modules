def mage_counter() -> callable:
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> callable:
    init = initial_power

    def charge_power(x):
        nonlocal init
        init += x
        return init

    return init


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return memory


def main():
    print("\nTesting mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")
    sword_ench = enchantment_factory("Flaming")
    shield_ench = enchantment_factory("Frozen")
    print(sword_ench("sword"))
    print(shield_ench("shield"))


if __name__ == "__main__":
    main()
