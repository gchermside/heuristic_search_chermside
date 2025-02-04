[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/C0_SOK5a)
# assignment-1-search


### Task 1
- IDS is signifigantly less expensive than BFS and DFS in the max size of the search frontier. In 10 trials at size 3 IDS has a average max frontier size of 86.2 vs BSF size of 72890.3 and DFS size of 235311.4. At size 2 ran on 10 trials IDS also has a smaller average max frontier size of 6.4 vs BFS's size of 11.7 and DFS's size of 13.0. IDS had the largest average states expanded, while DFS had the smallest average states expanded. When run on 10 trials of size 3, IDS had an average states expanded of 286308.8, while BFS had 165782.3 and DFS had 47518.2. 

If memory is the key contraining factor, IDS is by far the best algorithm, and definity worth the slightly large number of states expanded in order to find a correct solution. If time is the key contraining factor DFS may be the best choice if you are not looking for the optimal path. IDS only expanded on average 1.727 times more states than BFS, but its average max frontier size was 846 times smaller, so despite its slightly larger run time, it is likely the best choice is any situations where memory is a factor. 

Data Collected:
For size 2, 10 trials: 
BFS Average States Expanded:  10.1
DFS Average States Expanded:  16.6
IDS Average States Expanded:  16.8
BFS Average Max Frontier Size:  11.7
DFS Average Max Frontier Size:  13.0
IDS Average Max Frontier Size:  6.4
BFS Average Path Length:  3.2
DFS Average Path Length:  6.0
IDS Average Path Length:  3.2

For size 3, 10 trials:
BFS Average States Expanded:  165782.3
DFS Average States Expanded:  47518.2
IDS Average States Expanded:  286308.8
BFS Average Max Frontier Size:  72890.3
DFS Average Max Frontier Size:  235311.4
IDS Average Max Frontier Size:  86.2
BFS Average Path Length:  9.9
DFS Average Path Length:  45882.7
IDS Average Path Length:  9.9

### Task 4a
my_hueristic checks to see if any of the valid swaps move two tiles into their correct position. For each tile, it checks if a swap puts two tiles in the correct position. If a swap does put two tiles in the correct position, it only adds a cost of 0.5 for each of those tiles. Otherwise, it will add the manhattan distance for each tile not yet in its correct location.

### Task 4b
In the graph, my_hueristic got the highest path length compared to all of the manhattan distance points, but it also expanded less states than lambda = 1 and lambda = 1.26. That being said, it was worse in both path length and states expanded compated to when lambda >= 3.97 using manhattan distance. My_lambda is definelty not the right choice when trying to maximize optimality, but if time is the limiting factor, that using manhattan distance with a higher lambda or my_heuristic may be the best choice.

Side note: When trying to test my_heuristic, I ran my_huestic with the code of admissible_heuristic, and instead of being plotted near lamdba = 1 (because it was the same function) it was plotted with a much greater path length. I went to TA hours and using their sample code the TA got the same results, so I think something may be wrong with the plotting of my_heursitic on the graph.

### Tests
To _check_tilegame I added:
1. a check that the path contains no repeated states
2. a check that the path only contains valid moves

Tests I added:
1. I tested astar on a one-by-one board
2. I tested astar on a board that was already at the goal state
3. I tested that the admissable_heursitics could find the shortest path on starting boards that needed a variety of numbers of swaps
4. tested that astar produced the correct path, with the correct length, cost, states_expanded, and max_frontier on a 2-by-2 tile game.


Collaborators: Bhavani - discussed ways to make astar more efficient such as using a dictionary to store the visited states.

Hours spent on homework: A lot, maybe 8 hours? I defintely didn't count.

Known bugs: None! yay!
