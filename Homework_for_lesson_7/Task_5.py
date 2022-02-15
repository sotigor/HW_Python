# Creating a new dictionary with vehicles with mass less than 2000 kl.

vehicles = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600,
            "Van": 2400, "Semi": 13600, "bycicle": 7, "Motocycle": 100}

sorted_vehicles = {key: value for (key, value) in vehicles.items() if value < 2000}
print(sorted_vehicles)
