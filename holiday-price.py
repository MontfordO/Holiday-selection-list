def hotel_cost(hotel_price,num_nights):
    if hotel_price == "madrid":
        cost = 40
    elif hotel_price == "berlin":
        cost = 50
    elif hotel_price == "new york":
        cost = 80
    elif hotel_price == "paris":
        cost = 90
    elif hotel_price == "tokyo":
        cost = 60
    
    return cost*num_nights

def plane_cost(city_flight):
    if city_flight == "madrid":
        cost = 70
    elif city_flight == "berlin":
        cost = 80
    elif city_flight == "new york":
        cost = 500
    elif city_flight == "paris":
        cost = 100
    elif city_flight == "tokyo":
        cost = 800

    return float(cost)

def car_rental(city_flight,rental_days):
    if city_flight == "madrid":
        cost = 20
    elif city_flight == "berlin":
        cost = 20
    elif city_flight == "new york":
        cost = 30
    elif city_flight == "paris":
        cost = 25
    elif city_flight == "tokyo":
        cost = 30

    return cost*rental_days

def holiday_cost(flight_total,hotel_total,car_total) :
    return flight_total+hotel_total+car_total


print("This program will calculate the cost of a holiday.")
print("The location options are:")
print("Madrid")
print("Berlin")
print("New York")
print("Paris")
print("Tokyo")

print("------------------------------------------------------------")

# Running checks to be sure the input for the location is valid

city_flight = ""
while city_flight != "madrid" and city_flight != "berlin" and city_flight != "new york" and city_flight != "paris" and city_flight != "tokyo" :
    city_flight = input("Where would you like to travel to? : ").lower().strip(" ")
    hotel_price = city_flight
    if city_flight == "madrid" or city_flight == "berlin" or city_flight == "new york" or city_flight == "paris" or city_flight == "tokyo" :
        modified_city_string = city_flight[0].upper() + city_flight[1:]
        print("You have picked: " + (modified_city_string))
    else :
        print("Invalid option")
        print("------------------------------")

# Storing the function return in a variable for later use, then displaying amount to user

flight_total = plane_cost(city_flight)
print(f"Your total flight cost will be £{flight_total}0")

print("------------------------------------------------------------")

# Making sure the input is a number

number_check = False
while number_check is False :
    try :
        num_nights = float(input("How many nights do you want to stay? : "))

    except ValueError :
        print("The input is not a number.")
        print("------------------------------")

    else :
        number_check = True

# Storing the function return in a variable for later use, then displaying amount to user

hotel_total = hotel_cost(hotel_price,num_nights)
print(f"Your total hotel cost will be £{hotel_total}0")

print("------------------------------------------------------------")

# Input validity checks

rental_option = ""
while rental_option != "yes" and rental_option != "no" :
    rental_option = input("Would you like to rent a car? (Yes/No) : ").lower().strip()
    if rental_option == "yes" :
        number_check = False
        while number_check is False:

            while number_check is False :
                try :
                    rental_days = float(input("How many days do you need to rent the car for? : "))

                except ValueError :
                    print("The input is not a number.")
                    print("------------------------------")

                else :
                    number_check = True

            # Making sure that the input given by the user does not exceed the amount of days they are in the location

            if rental_days > (num_nights + 1) :
                num_nights_string = str(num_nights + 2).strip(".0")
                print(f"Your selection has exceeded the number of days you are in the location. Please pick a number of days below {num_nights_string}")
                print("------------------------------")
                number_check = False
    
    # If the user doesn't want a car rental, this option will simply multiply the car rental cost by 0, producing no cost

    elif rental_option == "no" :
        rental_days = 0
        print("No car is required, therefore there will be no further cost on your total.")

    else :
        print("This selection was invalid. Please input only Yes/No.")
        print("------------------------------")

# Storing the function return in a variable for later use, then displaying amount to user

car_total = car_rental(city_flight,rental_days)
print(f"Your total car rental will cost £{car_total}0")

print("------------------------------------------------------------")

# All the totals are displayed, as well as the grand total
# This is made using the holiday_cost function, adding all three

print("Summary:")
print("")
print(f"Your total flight cost will be £{plane_cost(city_flight)}0")
print(f"Your total hotel cost will be £{hotel_cost(hotel_price,num_nights)}0")
print(f"Your total car rental will cost £{car_rental(city_flight,rental_days)}0")
print(f"The grand total for this holiday will be £{holiday_cost(flight_total,hotel_total,car_total)}0")