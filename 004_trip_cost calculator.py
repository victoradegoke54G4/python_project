class TripCostCalculator:
    def __init__(self, days, cost_per_night, flight_cost, car_rental=0, other=0):
        self.days = days
        self.cost_per_night = cost_per_night
        self.flight_cost = flight_cost
        self.car_rental = car_rental
        self.other = other

    def total_cost(self):
        return (self.days * self.cost_per_night) + self.flight_cost + self.car_rental + self.other


def main():
    print('Welcome To The Ultimate Trip Cost Calculator App')

    # user input
    trip_days = float(input('How many days is your trip going to last?: '))
    trip_cost = float(input('How much does your trip cost per night?: '))
    trip_flight_cost = float(input('How much does your flight cost to destination?: '))

    trip_car_rental_cost = 0
    if input('Do you need a car rental? y/n: ').lower() == 'y':
        trip_car_rental_cost = float(input('How much does the car rental cost?: '))

    trip_other_cost = 0
    if input('Do you have other expenses? y/n: ').lower() == 'y':
        trip_other_cost = float(input('How much other costs?: '))

    # create object
    calculator = TripCostCalculator(trip_days, trip_cost, trip_flight_cost, trip_car_rental_cost, trip_other_cost)

    # print result
    print(f'Your total cost for the trip is ${calculator.total_cost():.2f}')


main()
