from typing import List


def validate_ingredients(ingredients: str) -> str:
    valid_elements: List[str] = ["water", "fire", "earth", "air"]
    if any(element in ingredients for element in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
