class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self._battery_capacity = battery_capacity  # Protected attribute

    def get_battery_info(self):
        return f"{self.brand} {self.model} has a battery capacity of {self._battery_capacity}mAh."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

# Subclass with additional attributes and methods
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_capacity, camera_megapixels):
        super().__init__(brand, model, battery_capacity)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_megapixels}MP camera."

# Example of creating objects
phone1 = Smartphone("BrandX", "ModelA", 4000)
phone2 = SmartphoneWithCamera("BrandY", "ModelB", 4500, 108)

print(phone1.get_battery_info())
print(phone2.get_battery_info())
print(phone2.take_photo())
