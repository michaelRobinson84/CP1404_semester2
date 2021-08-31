import random

int_num_of_quick_picks = int(input("How many quick picks? "))

list_of_quick_picks = []
sorted_list_of_quick_picks = []

for i in range(1, int_num_of_quick_picks + 1):
    quick_pick = []
    for j in range(1, 7):
        random_number = random.randint(1, 45)
        quick_pick.append(random_number)
    list_of_quick_picks.append(quick_pick)

for i in range(0, len(list_of_quick_picks)):
    list_of_quick_picks[i].sort()
    print(list_of_quick_picks[i])



