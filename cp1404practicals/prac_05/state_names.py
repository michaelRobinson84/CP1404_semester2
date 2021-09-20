CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for key in CODE_TO_NAME.keys():
    print("{:3} is {}".format(key, CODE_TO_NAME[key]))

state_code = input("Enter short state: ")
state_code = state_code.upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    state_code = state_code.upper()
