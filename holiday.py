city_flight = input("enter the city you will be flying to: ").lower().strip()
num_nights = int(input ("enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("enter the number of days for which you will be hiring a car: "))


def plane_cost (city):
    if city == "manchester":
        return 100
    elif city == "edinburgh":
        return 150
    elif city == "london":
        return 200
    else:
         return round(float(input("enter the price of the flight ticket: £")),2)
    
def hotel_cost(nights):
    return nights * 50
    
def car_rental (days):
    return days * 100


def holiday_cost(flight, hotel, car):
    return flight + hotel + car

flight_price = plane_cost (city_flight)
hotel_price = hotel_cost(num_nights)
car_price = car_rental (rental_days)
total_cost = holiday_cost (flight_price, hotel_price, car_price)
    

print (f"the total cost of your flight is: £{flight_price}")

print (f"the total hotel cost is: £{hotel_price} ")

print (f"the total cost of your car rental is: £{car_price}")

print(f"the total holiday cost is: £{total_cost}")
