graph = {
  '1' : ['2','3'],
  '2' : ['3'],
  '3' : ['4'],
  '4' : ['1'],
}

def bfs(graph, node): 

  visited = [] 
  queue = []  

  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = "->") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(graph, '2') 

print("\n")

def dfs(graph, node):
    visited = [node]
    stack = [node]
    print(node,end = "->")
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
            print (node,end = "->") 
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

print("Following is the Depth-First Search")
dfs(graph, '2')