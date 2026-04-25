from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    
    if start == goal:
        return [start], [start]
        
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    visited.append(node)
                    visited.append(neighbour)
                    return new_path, visited
            visited.append(node)
            
    return None, visited

# Depth-First Search (DFS)
def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    
    if start == goal:
        return [start], [start]
        
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path, visited
                
            neighbours = graph.get(node, [])
            for neighbour in reversed(neighbours): # Reversed for standard DFS left-to-right logic
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
    return None, visited

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_path', methods=['POST'])
def find_path():
    data = request.json
    edges = data.get('edges', [])
    start_node = data.get('start')
    goal_node = data.get('goal')
    
    # Dynamically build the graph
    graph = {}
    for u, v in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u) # Assuming undirected graph for navigation

    # Run BFS
    bfs_path, bfs_explored = bfs(graph, start_node, goal_node)
    
    # Run DFS
    dfs_path, dfs_explored = dfs(graph, start_node, goal_node)

    return jsonify({
        'bfs': {
            'path': bfs_path if bfs_path else "No Path Found",
            'explored': bfs_explored,
            'nodes_explored_count': len(bfs_explored)
        },
        'dfs': {
            'path': dfs_path if dfs_path else "No Path Found",
            'explored': dfs_explored,
            'nodes_explored_count': len(dfs_explored)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)