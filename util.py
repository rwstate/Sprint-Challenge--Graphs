def reverse_direction(x):
    if x == "n":
        return "s"
    if x == "s":
        return "n"
    if x == "e":
        return "w"
    if x == "w":
        return "e"

def backtrack(start, graph, traversal_path, path = None):
    if path == None:
        path = []
    for x in graph[start]:
        if graph[start][x] == "?":
            return path

    if graph[start]['backtrack'] == -1:
        return reverse_path(start, graph, traversal_path + path, path)

    next_direction = graph[start]['backtrack']
    next_room = graph[start][next_direction]

    return backtrack(next_room, graph,traversal_path, path + [next_direction])

def reverse_path(start, graph, traversal_path, path = None):
    print(start)
    if path == None:
        path = []
    for x in graph[start]:
        if graph[start][x] == "?":
            return path
    next_direction = reverse_direction(traversal_path[-1])
    next_room = graph[start][next_direction]

    return reverse_path(next_room, graph, traversal_path[:-1], path + [next_direction])