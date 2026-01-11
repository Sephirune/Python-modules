class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass
class WaterError(GardenError):
    pass
class GardenManager:
    def __init__(self):
        self.plants = {}
    def add_plant(self, name):
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 5, "sun": 8}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")
    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"watering {plant} - success")
        except Exception as e:
            print(f"Error while watering: {e}")
        finally:
            print("Closing watering system (cleanup)")
    def check_health(self):
        print("\nChecking plant health...")
        for plant, data in self.plants.items():
            try:
                water = data["water"]
                sun = data["sun"]
                if water > 10:
                    raise ValueError(f"Water level {water} is too high (max 10)")
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
            except ValueError as e:
                print(f"Error checking {plant}: {e}")
    def simulate_error(self):
        raise WaterError("Not enough water in tank")
    
""" def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")  # error

    print("\nWatering plants...")
    manager.water_plants()

    manager.plants["lettuce"]["water"] = 15
    manager.check_health()
    print("\nTesting error recovery...")
    try:
        manager.simulate_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management() """