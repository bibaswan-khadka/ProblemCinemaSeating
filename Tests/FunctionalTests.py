from SeatAssignment.cinema import Cinema
import filecmp

# Example functional tests to test entire program

# Test weather output of input 1 is correct
def test_input1():
    with open('./InputOutputs/input1.txt', "r") as input_file:
            theater = Cinema()
            theater.read_requests(input_file.readlines())
            theater.assign_seats()
            with open('./InputOutputs/input1.txt' + '.output' , "w") as output_file:
                seating_assignments = theater.get_output()
                formatted_text = ''
                for i in seating_assignments:
                    formatted_text += i + '\n'
                output_file.write(formatted_text)
    assert filecmp.cmp('./InputOutputs/input1.txt.output','./Tests/Solutions/input1.txt.output',shallow=False) == True

# Test weather output of input 2 is correct
def test_input2():
    with open('./InputOutputs/input2.txt', "r") as input_file:
            theater = Cinema()
            theater.read_requests(input_file.readlines())
            theater.assign_seats()
            with open('./InputOutputs/input2.txt' + '.output' , "w") as output_file:
                seating_assignments = theater.get_output()
                formatted_text = ''
                for i in seating_assignments:
                    formatted_text += i + '\n'
                output_file.write(formatted_text)
    assert filecmp.cmp('./InputOutputs/input2.txt.output','./Tests/Solutions/input2.txt.output',shallow=False) == True

