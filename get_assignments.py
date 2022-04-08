import sys
from SeatAssignment.cinema import Cinema

def main(*argv, **kwargs):
    if len(sys.argv) < 2:
        print("Please specify the input path")
    try:
        with open(sys.argv[1], "r") as input_file:
            theater = Cinema()
            requests = theater.read_requests(input_file.readlines())
            theater.assign_seats()
            with open(sys.argv[1] + '.output' , "w") as output_file:
                seating_assignments = theater.get_output()
                formatted_text = ''
                for i in seating_assignments:
                    formatted_text += i + '\n'
                
                print('Requests\n',requests,'\n')
                print('Seats\n',formatted_text,'\n')
                output_file.write(formatted_text)
                return sys.argv[1] + '.output'
    except OSError:
        print('Error with input/output')

if __name__ == '__main__':
    main()