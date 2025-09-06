def length_converter():
    print(" Length Converter")
    print("Choose conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Centimeters to Inches")
    print("6. Inches to Centimeters")

    choice = input("Enter option number (1-6): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km * 0.621371:.4f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles / 0.621371:.4f} km")
    elif choice == "3":
        meters = float(input("Enter meters: "))
        print(f"{meters} m = {meters * 3.28084:.4f} feet")
    elif choice == "4":
        feet = float(input("Enter feet: "))
        print(f"{feet} ft = {feet / 3.28084:.4f} meters")
    elif choice == "5":
        cm = float(input("Enter centimeters: "))
        print(f"{cm} cm = {cm * 0.393701:.4f} inches")
    elif choice == "6":
        inches = float(input("Enter inches: "))
        print(f"{inches} in = {inches / 0.393701:.4f} cm")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    length_converter()
