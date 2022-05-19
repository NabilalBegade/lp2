n = int(input("\nEnter No. of nodes : "))  # no of nodes
graph = {}

print("\nEnter nodes")
for i in range(n):
    node = input("Enter node %s : " % (i + 1))  # inputs node no
    graph[node] = list(
        map(str, input("Enter adjacent nodes : ").rstrip().split()))  # inputs connected nodes for that node

visited = set()  # to not allow duplicates


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def display_graph(graph):
    for i, j in graph.items():
        print(i, "-->", j)


print('\nEntered graph:')
display_graph(graph)

print("\n-----Depth-First Search------")

dfs(visited, graph, '1')

visited = []
queue = []

print("\n\n-----Breadth-First Search----")
bfs(visited, graph, '1')