# AI Problem Solving Assignment

**Repository:** AI_ProblemSolving_<RA2411050050001>

## Problem 8: Smart Navigation System
This project implements a smart navigation system required to find routes between different locations, similar to Google Maps.The user can input a start node, a goal node, and a set of connections between locations through an interactive web interface.The system dynamically builds a graph and finds a path between the start and goal nodes.

### Algorithms Used
The solution implements and compares the following search strategies:
**Breadth-First Search (BFS)**
**Depth-First Search (DFS)** 

### Execution Steps
1. Ensure Python is installed on your system.
2. Open your terminal or command prompt and navigate to the project directory.
3. Install the required Flask web framework by running: `pip install Flask`
4. Start the server by executing: `python app.py`
5. Open a web browser and navigate to `http://127.0.0.1:5000`.
6. Use the interface to add node connections (edges), then input your Start and Goal nodes to find the route.

### Sample Output
**Input:**
* Edges Added: A-B, A-C, B-D, C-D, D-E
* Start Node: A
* Goal Node: E

**Output (BFS Result):**
* Path: A → B → D → E
* Nodes Explored (Count): 4
* Exploration Order: A, B, C, D, E

**Output (DFS Result):**
* Path: A → C → D → E
* Nodes Explored (Count): 4
* Exploration Order: A, C, D, E

### Algorithm Comparison
As required by the assignment, here is the comparison between the two methods

**Path Optimality:** BFS always guarantees the optimal (shortest) path in an unweighted graph because it explores all neighbors at the present depth before moving deeper.DFS does not guarantee an optimal path; it returns the first path it finds.
**Number of Nodes Explored:** BFS typically explores more nodes if the goal is deep, as it checks every possibility level by level. DFS can explore fewer nodes if the goal node happens to lie on the first deep path it checks, but it can also explore many more if it goes down the wrong branch.
**Efficiency of Traversal:** BFS requires more memory to store the queue of nodes at the current level.DFS is more memory-efficient as it only needs to store the current path stack, but it can be less efficient in terms of time if it gets stuck exploring deep, incorrect paths.
