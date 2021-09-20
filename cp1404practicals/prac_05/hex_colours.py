COLOUR_TO_CODE = {"aliceblue": "#f0f8ff", "beige": "#f5f5dc", "cornflowerblue": "#6495ed", "firebrick": "#b22222",
                "hotpink": "#ff69b4", "khaki": "#f0e68c", "magenta": "#ff00ff", "navyblue": "#000080",
                "salmon": "	#fa8072", "turquoise": "#40e0d0"}

colour_name = input("Enter colour name: ")
colour_name = colour_name.lower()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
    colour_name = colour_name.lower()