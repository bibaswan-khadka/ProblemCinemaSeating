from SeatAssignment.cinema import Cinema

# Sample unit tests to test individual units of solution

# Check if program returns invalid when requesting more than 20 seats for a group
def test_no_reservations():
    theater = Cinema()
    theater.read_requests(['R001 21'])
    theater.assign_seats()
    assert theater.seat_assignments == [[(-1,-1)]]


# Check if program places group in lowest cost location
def test_cost():
    theater = Cinema()
    theater.read_requests(['R001 20'])
    theater.assign_seats()
    assert theater.seat_assignments == [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19)]]

# Check if program places group in lowest cost location
def test_cost_2():
    theater = Cinema()
    theater.read_requests(['R001 15','R002 1'])
    theater.assign_seats()
    assert theater.seat_assignments == [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14)], [(0, 18)]]

# Check if cost function is working properly
def test_costfunction():
    theater = Cinema()
    theater.read_requests(['R001 15'])
    cost = theater.cost_function(0,0,15)
    assert cost == 18



