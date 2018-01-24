#!/usr/bin/env python3
import pickle

FILENAME = "trips.bin"

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def write_trips(trips):
    with open(FILENAME, "wb") as file:
        pickle.dump(trips, file)

def read_trips():
    trips = []
    with open(FILENAME, "rb") as file:
        trips = pickle.load(file)
        
    return trips

def list_trips(trips):
    print("Distance\tGallons\t\tMPG")

    for trip in trips:
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips()

    list_trips(trips)

    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)

        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trips.append(trip)

        print()

        list_trips(trips)

        print()
        
        more = input("\nMore entries? (y or n): ")
        
    write_trips(trips)
    print("Bye")

if __name__ == "__main__":
    main()

