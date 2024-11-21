
node = int(input())
link = int(input())

graph = [[] for _ in range(node)]
for _ in range(link):
    i,j = map(int,input().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)


def dfs_recursion(graph, start, visited = None):
    if visited is None:
        visited = []
    
    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
             dfs_recursion(graph, neighbor, visited)

    return visited

print(len(dfs_recursion(graph, 0))-1) 