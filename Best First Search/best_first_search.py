
from queue import PriorityQueue
v = 13
graph = [[] for i in range(v)]
 
# Function For Implementing Best First Search
# Gives output path having lowest cost
 
 
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
     
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
 
# Function for adding edges to graph
 
 
def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
 
# The nodes shown in above example(by alphabets) are
# implemented u_sing integers added_ge(x,y,cost);
add_edge(0, 1, 12)
add_edge(0, 2, 4)
add_edge(1, 3, 7)
add_edge(1, 4, 3)
add_edge(2, 5, 8)
add_edge(2, 6, 2)
add_edge(5, 8, 4)
add_edge(6, 9, 9)
add_edge(6, 7, 0)
 
source = int(input("Enter the starting node. "))
target = int(input("Enter the target node."))
best_first_search(source, target, v)
 