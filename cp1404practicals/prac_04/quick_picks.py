import random

int_num_of_quick_picks = int(input("How many quick picks? "))

for i in range(1, int_num_of_quick_picks + 1):
    quick_pick = []
    for j in range(1, 7):

        is_repeated = True
        random_number = random.randint(1, 45)
        while is_repeated:
            if random_number not in quick_pick:
                is_repeated = False
                quick_pick.append(random_number)
            else:
                random_number = random.randint(1, 45)
    for number in quick_pick:
        print("{:2}".format(number), end=" ")
    print()






