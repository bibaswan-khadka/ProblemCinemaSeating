import math
class Cinema:

    def __init__(self, rows=10, cols=20):
        self.buffer_size = 3
        self.rows = rows
        self.cols = cols
        self.seat_assignments = []
        self.seats = [['o'] * cols for r in range(rows)]
        self.requests = []

    # Read in requests file
    def read_requests(self, requests):
        for r in requests:
            request_id, num_of_seats = r.split()
            self.requests.append((request_id,num_of_seats))
        return self.requests
    
    # Check if seats have already not been taken or are reserved as a buffer
    def is_open(self, i, j, group_size):
        for k in range(j, j + group_size):
            if 0 <= i < self.rows and 0 <= k < self.cols:
                if self.seats[i][k] == 'o':
                    continue
                else:
                    return False
            else:
                return False
        return True

    # Calculate the cost to seat the group at i,j
    def cost_function(self, i, j, group_size):        
        cost_left = 0 
        for k in range(1, 1+self.buffer_size):
            if 0 <= i < self.rows and 0 <= j - k < self.cols:
                if self.seats[i][j-k] == 'o':
                    cost_left += 1
                elif self.seats[i][j-k] != 'b':
                    return math.inf

        cost_down = 0 
        for k in range(group_size):
            if 0 <= i -1 < self.rows and 0 <= j + k < self.cols:
                if self.seats[i - 1][j + k] == 'o':
                    cost_down += 1
                elif self.seats[i - 1][j + k] != 'b':
                    return math.inf
        
        cost_up = 0
        for k in range(group_size):
            if 0 <= i  + 1 < self.rows and 0 <= j + k < self.cols:
                if self.seats[i + 1][j + k] == 'o':
                    cost_up += 1
                elif self.seats[i + 1][j + k] != 'b':
                    return math.inf
        
        cost_right = 0
        for k in range(self.buffer_size):
            if 0 <= i < self.rows and 0 <= j + group_size + k < self.cols:
                if self.seats[i][j+group_size + k] == 'o':
                    cost_right += 1
                elif self.seats[i][j+group_size + k] != 'b':
                    return math.inf
        return cost_left + cost_right + cost_down + cost_up

    # Set buffers on map
    def set_buffer(self, i, j, group_size):
        for k in range(1, 1 + self.buffer_size):
            if 0 <= i < self.rows and 0 <= j - k < self.cols:
                self.seats[i][j-k] = 'b'
        
        for k in range(group_size):
            if 0 <= i - 1 < self.rows and 0 <= j + k < self.cols:
                self.seats[i - 1][j + k] = 'b'
        
        for k in range(group_size):
            if 0 <= i + 1 < self.rows and 0 <= j + k < self.cols:
                self.seats[i + 1][j + k] = 'b'
        
        for k in range(self.buffer_size):
            if 0 <= i < self.rows and 0 <= j + group_size + k < self.cols:
                self.seats[i][j+group_size + k] = 'b'

        
    # Assign seats using cost function
    def assign_seats(self):
        for idx, request in enumerate(self.requests):
            group_size = int(request[1])
            min_cost = math.inf
            r, c = -1, -1
            for i in range(self.rows):
                for j in range(self.cols - group_size + 1):
                    if not self.is_open(i,j,group_size):
                        continue
                    curr_cost = self.cost_function(i, j, group_size)
                    if curr_cost < min_cost:
                        r, c = i, j
                        min_cost = curr_cost

            if r == -1 and c == -1:
                self.seat_assignments.append([(r, c)])
                continue
            
            self.set_buffer(r,c,group_size)

            assignment = []
            for t in range(group_size):
                x, y = (r, c + t)
                self.seats[x][y] = str(idx + 1)
                assignment.append((x,y))
            self.seat_assignments.append(assignment)
        return

    # Output seating assignment
    def get_output(self):
        s = []
        for i, assignment in enumerate(self.seat_assignments):
            if assignment[0][0] == -1:
                s.append(self.requests[i][0] + ' ' + "cannot fulfill reservation")
            else:
                formatted_assignment = self.requests[i][0] + ' ' 
                for x, y in assignment:
                    formatted_assignment += chr(65 + x) + str(y + 1) + ','
                s.append(formatted_assignment[:-1])
        return s


    
