from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    user_choice_of_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")

    user_choice = input(">>> ")
    user_choice = user_choice.upper()

    while user_choice != "Q":

        if user_choice == "C":

            user_choice_of_taxi = choose_taxi(taxis)
            print("Bill to date: ${:.2f}".format(bill_to_date))

        elif user_choice == "D":

            float_price_to_charge = drive(user_choice_of_taxi, taxis)
            bill_to_date += float_price_to_charge
            print("Bill to date: ${:.2f}".format(bill_to_date))

        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(bill_to_date))

        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ")
        user_choice = user_choice.upper()

    print("Total trip cost: ${:.2f}".format(bill_to_date))

    index = 0

    print("Taxis are now:")

    for taxi in taxis:

        print("{} - {}".format(index, str(taxi)))

        index += 1


def choose_taxi(taxis):

    index = 0

    print("Taxis available:")

    for taxi in taxis:

        print("{} - {}".format(index, str(taxi)))

        index += 1

    user_choice = input("Choose taxi: ")

    if int(user_choice) > len(taxis) - 1 or int(user_choice) < 0:
        print("Invalid taxi choice")
        return None
    else:
        return int(user_choice)


def drive(user_choice_of_taxi, taxis):

    if user_choice_of_taxi is None:

        print("You need to choose a taxi before you can drive")
        return 0
    else:
        distance_to_drive = input("Drive how far? ")
        taxis[user_choice_of_taxi].start_fare()
        taxis[user_choice_of_taxi].drive(int(distance_to_drive))
        print("Your {} trip cost you ${:.2f}".format(taxis[user_choice_of_taxi].name, taxis[user_choice_of_taxi].get_fare()))

        return taxis[user_choice_of_taxi].get_fare()


main()
