import sys
from typing import Dict, List

print("=== Inventory System Analysis ===")
items: Dict[str, int] = {}
arg: int
for arg in sys.argv[1:]:
    parse: List[str] = arg.split(":")
    item: str = parse[0]
    quantity: int = int(parse[1])
    items[item] = quantity
total_items: int = 0
quantity: int
for quantity in items.values():
    total_items += quantity
unique_type: int = len(items)
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {unique_type}")

print("\n=== Current Inventory ===")
item: str
for item, quantity in items.items():
    percentage = (quantity / total_items) * 100
    print(f"{item}: {quantity} units ({percentage:.1f}%)")

print("\n=== Inventory Statistics ===")
top: int = 1
winner: str = ""
name: str
size: int
for name, size in items.items():
    if size > top:
        top = size
        winner = name
print(f"Most abundant: {winner} ({top} units)")
bot: int = 2
loser: str = ""
name1: str
size1: int
for name1, size1 in items.items():
    if size1 < bot:
        bot = size1
        loser = name1
print(f"Least abundant: {loser} ({bot} units)")

print("\n=== Item Categories ===")
moderate: Dict[str, int] = {}
scarce: Dict[str, int] = {}
for item, quantity in items.items():
    if quantity > 3:
        moderate[item] = quantity
    else:
        scarce[item] = quantity
print(f"Moderate: {moderate}")
print(f"Scarce: {scarce}")

print("\n=== Management Suggestions ===")
restock: List[str] = []
for item, quantity in items.items():
    if quantity == 1:
        restock.append(item)
print(f"Restock needed: {restock}")

print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(items.keys())}")
print(f"Dictionary values: {list(items.values())}")
sword_exist: bool = items.get('sword') is not None
print(f"Sample lookup - 'sword' in inventory: {sword_exist}")
