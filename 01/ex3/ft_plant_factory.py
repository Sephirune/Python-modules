class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height
    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

print("=== Plant Factory Output ===")
list_plants = [      #creo una estructura de datos. cada elemento es una tupla. no se pueden modificar
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

plants = []

for data in list_plants:
    plant = Plant(data[0], data[1], data[2])  #llamo a los datos 1,2 y 3 de las tuplas
    plants.append(plant)
    plant.get_info()

print(f"Total plants created: {len(plants)}")