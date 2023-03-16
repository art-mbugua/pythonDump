# The graph is illustrated using an adjacency list in a dictionary
graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

# List for visited nodes.
visited = [] 
#Initialize a queue to keep track of nodes currently in the queue
queue = [] 
node = input('Enter the starting node //a number between 1-6//: ')    

#function for BFS
# the arguments are for the visited nodes, the graph and the starting node
def bfs(visited, graph, node): 

  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, node)    # function calling