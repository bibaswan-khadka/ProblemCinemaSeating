### Instruction to run program
##### To run use the command 
python get_assignments.py [path_to_input] 

##### Example 
python get_assignments.py ./InputOutputs/input1.txt

### Instructions to run tests
##### To run the tests, use the command pytest ./Tests/UnitTests.py or pytest ./Tests/FunctionalTests.py
##### You might have to install pytest if not installed using pip install -U pytest
##### Link to further pytest instructions if needed https://docs.pytest.org/en/7.1.x/getting-started.html

## Approach
Use a greedy apprach. Iteratively place each group in a spot in the cinema where the group creates the least amount of new buffer space. This maximizes the number of customers we can fit in the cinema while following the constraints. 

Running time -   
O ( numOfGroups * (m*n) ) where m = numofrows and n = num of cols in cinema
For each group we iterate through the whole cinema and try to find the best possible seats. 

Space complexity -    
O (m *n) where m = numofrows and n = num of cols in cinema
We need to keep track of which seats have been taken and which seats are reserved. 

## Assumptions

## Space constraint/ Maximizing safety
- Due to covid the cinema is operating at limited capacity to guarantee safety. Thus we buffer groups. We assume the buffer is 3 empty seats to the right, 3 empty seats to the left, and that all seats in the row in front and behind of the groups are left empty. 

## Maximizing customer satisfaction
- We attempt to fit as many customers as possible in the cinema under the current constaints. Customers are likely to be unsatisfied if they do not have seats at all. 
- We assume customers want to be seated together with their group so we seat each group together. If the group cannot be seated we output that there is no space available.
- We prioritize first come first serve. Seats are assigned in order of who ordered first. Customers who order first will be unhappy if they are left out even though they ordered early. Consequently customers who order later are likely to be more understanding if they cannot get seats. 

## Further expansions
- Add support for seperating groups. Suppose a group of 20 cannot fit in the cinema under current conditions, but two groups of 5 can be seated. Break the groups up and give the customer the option. 
- Add further unit, integration and functional tests. 
- You could also optimize the algorithm by seating the largest groups first. This will lead to a better maximization of the space since the largest groups take up the most space. However, this would mean we cannot seat the groups on a first come first serve basis which might lead to lower satisfaction. 

