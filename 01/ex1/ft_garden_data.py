class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

print("=== Garden Plant Registry ===")

plant = Plant("Rose", 30, 25)
plant2 = Plant("Sunflower", 45, 80)
plant3 = Plant("Cactus", 120, 15)

print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")