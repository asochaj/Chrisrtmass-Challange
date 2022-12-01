import numpy as np

class Santa_Trip:

    def __init__(self,coordinates,fuel_demand):
        self.coordinates = coordinates
        self.fuel_demand = fuel_demand

    def calc_distance(self):

        distances = []
        cities = len(self.coordinates) - 1
        for city in range(cities):
            distance = np.linalg.norm(np.array(self.coordinates[city]) - np.array(self.coordinates[city + 1]))
            distances.append(distance)

        distance_sum = sum(distances)

        return distance_sum

    def calc_fuel_needed(self,distance_sum):
        petrol_demand = self.fuel_demand / 10  # 20l/10j

        fuel_consumption = round(distance_sum * petrol_demand,2)

        print(f"Mikołaj ma do przejechania {distance_sum} jednostek odległości i potrzebuje {fuel_consumption}l paliwa")

