def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda y: f"* {y} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    maximum_power: int = max(mages, key=lambda z: z["power"])["power"]
    useless_mage: int = min(mages, key=lambda u: u["power"])["power"]
    quick_math: int = sum(map(lambda s: s["power"], mages))
    avg: float = round(quick_math / len(mages), 2)

    return {
        "max_power": maximum_power,
        "min_power": useless_mage,
        "avg_power": avg
        }


def main() -> None:
    artifact: list[dict[str, str | int]] = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ]

    sorted_artifacts: list[dict[str, str | int]] = artifact_sorter(artifact)
    print("\nTesting artifact sorter...")
    print(f"{sorted_artifacts[0]['name']} \
({sorted_artifacts[0]['power']} power) comes before \
{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells: list[str] = [
        "fireball",
        "heal",
        "shield"
    ]
    transformed_spells: list[str] = spell_transformer(spells)
    print(f"{transformed_spells[0]}{transformed_spells[1]}\
{transformed_spells[2]}")

    mage_list: list[dict[str, str | int]] = [
        {"name": "Veigar", "power": 1081},
        {"name": "Skidoodle", "power": 1000},
        {"name": "Peter the mage", "power": 0}
        ]

    mage_rank: dict[str, int | float] = mage_stats(mage_list)
    print("\nTesting mage ranking...")
    print(f"Most Powerful Mage: {mage_rank['max_power']}")
    print(f"Most useless mage of all time: {mage_rank['min_power']}")
    print(f"Average of power: {mage_rank['avg_power']}")


if __name__ == "__main__":
    main()
