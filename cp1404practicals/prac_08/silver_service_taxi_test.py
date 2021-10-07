from prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)

hummer.drive(18)

print(hummer)

print("Fare of ${:.2f}".format(hummer.get_fare()))
