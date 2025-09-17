ph_level = input("Enter the pH level: ")

if float(ph_level) > 7:
    print("Basic")
elif float(ph_level) < 7:
    print("Acidic")
else:
    print("Neutral")
