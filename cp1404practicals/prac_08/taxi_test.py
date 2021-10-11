from taxi import Taxi

new_taxi = Taxi("Prius 1", 100)

new_taxi.drive(40)

print(new_taxi)
temp_fare = new_taxi.price_per_km * new_taxi.current_fare_distance
print("Current fare: ${}".format(temp_fare))

new_taxi.start_fare()

new_taxi.drive(100)

print(new_taxi)
temp_fare = new_taxi.price_per_km * new_taxi.current_fare_distance
print("Current fare: ${}".format(temp_fare))