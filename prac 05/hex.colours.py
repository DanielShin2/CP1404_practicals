color_to_code = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0",
                 "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}
print(color_to_code)

color = input("Enter the color: ")
while color != "":
    if color in color_to_code:
        print(color, "=", color_to_code[color])
    else:
        print("Invalid color name")
    color = input("Enter the color: ")