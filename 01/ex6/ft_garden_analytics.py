class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
    def get_info(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}"

class GardenManager:
    total_gardens = 0 # esto es el atributo de clase. representa los huertos que hay

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1
    
    # método de clase
    @classmethod
    def create_garden_network(cls): # en los métodos de clase se usa cls y sirven para trabajar con la clase en general. En este caso, cuenta los huertos.
        print(f"Total gardens managed: {cls.total_gardens}")
    
    # método estático. Principalmente se usa para organizar, es decir, en cálculos o validaciones. 
    @staticmethod
    def validate_height(height): 
        return height >= 0
    
    class GardenStats:
        @staticmethod
        def total_height(plants):
            total = 0
            for plant in plants:
                total += plant.height
            return total
    
    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
    
    def garden_info(self):
        print(f"=== {self.owner}'s Garden Report ===")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        total = self.GardenStats.total_height(self.plants)
        print(f"Total height: {total}cm")
    
    # el ejercicio nos pide que empleemos distintos métodos. El primero será el de instancia. Este trabaja sobre un huerto concreto.
    def add_plant(self, plant):
        if not self.validate_height(plant.height):
            print(f"Invalid height for {plant.name}, rejected")
            return
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

alice_garden = GardenManager("Alice")
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

alice_garden.help_plants_grow()
print("=== Alice's Garden Report ===")
alice_garden.garden_info()
