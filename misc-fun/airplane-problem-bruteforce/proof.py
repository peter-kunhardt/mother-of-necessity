import random

# Instantiate array of randomly ordered passengers
def generate_random_passenger_order():
    return random.sample(range(1, 101), 100)

# Define individual Pasenger Seat Choice func
def passenger_seat_choice(passenger_id, available_seats):
    # For the first passenger to be evaluated, randomly select a seat
    if len(available_seats) == 100:
        chosen_seat = random.choice(available_seats)
        return chosen_seat

    # Check if the passenger's assigned seat is available
    if passenger_id in available_seats:
        return passenger_id

    # Otherwise, randomly select a seat from the available seats
    chosen_seat = random.choice(available_seats)
    return chosen_seat

# Simulate filling the cabin
def fill_cabin(passenger_order):
    
    # create fresh available seat list:
    available_seats = list(range(1, 101))

    # instantiate assignments list:
    seat_assignments = []

    # Loop through each passenger in the order:
    for passenger_id in passenger_order:

        chosen_seat = passenger_seat_choice(passenger_id, available_seats)
        seat_assignments.append({
            "pass": passenger_id,
            "seat": chosen_seat
        })
        # remove the chosen seat from available seats:
        available_seats.remove(chosen_seat)
    # return the assignment:
    return seat_assignments


# Generate a series of fills and summarize the results:
def generate_fills(num_fills):
    results = []
    for _ in range(num_fills):
        passenger_order = generate_random_passenger_order()
        seat_assignments = fill_cabin(passenger_order)
        last_passenger = seat_assignments[-1]
        first_passenger = seat_assignments[0]
        last_is_seated_in_own_seat = last_passenger["pass"] == last_passenger["seat"]
        first_is_seated_in_own_seat = first_passenger["pass"] == first_passenger["seat"]
        results.append({
            "iter": _, 
            "last_pass_correctly_seated": last_is_seated_in_own_seat,
            "first_pass_correctly_seated": first_is_seated_in_own_seat,})
    return results

def main():
    num_fills = 50000
    results = generate_fills(num_fills)
    print("After generating " + str(num_fills) + " fills, the last passenger was seated in their own seat " + 
      str(sum([1 for result in results if result["last_pass_correctly_seated"]]) / num_fills * 100) + "% of the time.")
    print("After generating " + str(num_fills) + " fills, the first passenger was seated in their own seat " + 
      str(sum([1 for result in results if result["first_pass_correctly_seated"]]) / num_fills * 100) + "% of the time.")

if __name__ == "__main__":
    main()