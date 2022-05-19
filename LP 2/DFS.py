graph = {
  '1' : ['2','3'],
  '2' : ['3'],
  '3' : ['4'],
  '4' : ['1'],
}

def dfs(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

print (dfs(graph, '2'))
