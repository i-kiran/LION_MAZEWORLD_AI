# LION_MAZEWORLD_AI
A Lion lives in a world with twisted and molded corridors and rounded treats. Navigation to the
world is not straightforward due to the twisting nature of surroundings. Efficient navigation is Lion's
first and foremost goal to find food (meat).
We provide a game model environment to implement and understand the working of different types of
search algorithms. In this assignment, you need to build search algorithms so that Lion navigates
through the world efficiently to quickly find the food.
If the Lion gets stuck at some locations during the search, you can forcefully quit the environment by
typing CTRL-c into your terminal.
The Lion starts at the starting point (blue cell) of the grid while the meat is at the bottom right corner,
as shown in the figure below.
It's time to write full-fledged generic search functions to help the Lion. Remember that a search node
must contain a state and the information necessary to reconstruct the path (plan) that gets to that state.
Important note: All of your search functions need to return a list of actions that will lead the agent (in
our case Lion) from the start to the goal. These actions all have to be legal moves (right directions, no
moving through walls).
**Question 1 **: Finding Food using Depth First Search

Implement the depth-first search (DFS) algorithm in the search_algo function in lion_in_maze.py. To
make your algorithm complete, write the graph search version of DFS, which avoids expanding any
already visited states.
Considering each step incurs a cost of 3 units, find the total cost for the Lion in the case of
DFS. Does DFS follow completeness and optimality in this case? Analyze the time complexity of the
search in proper steps.

**Question 2: Breadth-First Search

Implement the breadth-first search (BFS) algorithm in the search_algo function in lion_in_maze.py. To
make your algorithm complete, write the graph search version of BFS, which avoids expanding any
already visited states.
Is BFS successful in finding the solution? Justify your statement.
Consider each step incurs 5 units cost, find the total cost for BFS implementation. Also, discuss
the space complexity of the approach in detail.

**Question 3 : Varying the Cost Function

BFS may or may not find the best solution, but our task is to find the best or optimal solution. For this,
implement a Varying Cost Search (VCS) algorithm.
Use the following cost function: For each step, the cost of vertical movement towards the target is 3
units otherwise the step cost is always 2 units. Implement the approach in search_algo function in
lion_in_maze.py (obviously the Lion would always try to save its energy by taking a least cost path).
What is the total cost of search using VCS? Comment on the completeness of VCS. Also, discuss its
time complexity.

**Question 4: A* search

Implement A* search in the search_algo function in lion_in_maze.py. A* takes a heuristic function as
an argument. The heuristics function here takes two arguments: a state in the search problem (the
main argument) and the search problem itself (for reference information).
You can test your A* implementation on the problem of finding a path to a fixed position in
the environment using the Manhattan distance heuristic or Diagonal distance heuristic.
Use the cost function same as VCS and find the cost of the A* approach. Compare the complexity of
A* with VCS and state whether A* is optimal and complete.
