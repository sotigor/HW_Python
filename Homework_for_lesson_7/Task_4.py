# Sorting

vehicles = [{'type': 'Sedan', 'weight': 1500, 'year': 2000},
            {'type': 'SUV', 'weight': 2000, 'year': 1999},
            {'type': 'Pickup', 'weight': 2500, 'year': 2011},
            {'type': 'Minivan', 'weight': 1600, 'year': 1999},
            {'type': 'Van', 'weight': 2400, 'year': 2012},
            {'type': 'Semi', 'weight': 13600, 'year': 2015},
            {'type': 'bicycle', 'weight': 7, 'year': 2012},
            {'type': 'Motorcycle', 'weight': 100, 'year': 2008}]

# Sorting list of dicts by key ‘type’.
sorted_vehicles_t = sorted(vehicles, key=lambda item: (item['type']))

# Sorting list of dicts by value of key ‘year’.
sorted_vehicles_y = sorted(vehicles, key=lambda item: (item['year']))

print(sorted_vehicles_t)
print(sorted_vehicles_y)
