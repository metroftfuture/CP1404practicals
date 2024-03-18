from car import Car

def main():

    limo = Car(fuel=100, name="Limo")

    limo.add_fuel(20)


    print(f"Fuel in {limo.name}: {limo.fuel}")


    distance_driven = limo.drive(115)
    print(f"Distance driven by {limo.name}: {distance_driven} km")


    print(limo)

if __name__ == "__main__":
    main()
