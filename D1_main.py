import D1_fuel_consumption_functions

coordinates = [(1,1),
              (4,5),
              (11,5)]

fuel_demand = 20

Trip = D1_fuel_consumption_functions.Santa_Trip(coordinates,fuel_demand)
distance = Trip.calc_distance()
fuel = Trip.calc_fuel_needed(distance)

