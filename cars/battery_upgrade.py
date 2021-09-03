from electric_car import ElectricCar

# Create an instance of ElectricCar
model_3 = ElectricCar("tesla", "model 3", 2017)
print(model_3.battery.get_range())
model_3.battery.upgrade_battery()
print(model_3.battery.get_range())