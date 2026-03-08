def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda y: f"* {y} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    maximum_power = max(mages, key=lambda z: z["power"])["power"]
    useless_mage = min(mages, key=lambda u: u["power"])["power"]
    quick_math = sum(map(lambda s: s["power"], mages))
    avg = round(quick_math / len(mages, 2))

    return {
        "max_power": maximum_power,
        "min_power": useless_mage,
        "avg_power": avg
        }


def main():
    artifact = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ]

    sorted_artifacts = artifact_sorter(artifact)
    print("\nTesting artifact sorter...")
    print(f"{sorted_artifacts[0]['name']} \
({sorted_artifacts[0]['power']} power) comes before \
{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = [
        "fireball",
        "heal",
        "shield"
    ]
    transformed_spells = spell_transformer(spells)
    print(f"{transformed_spells[0]}{transformed_spells[1]}\
{transformed_spells[2]}")


if __name__ == "__main__":
    main()
