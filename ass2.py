import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.edgeNodes = []

    def addEdgeNode(self, edgeNode):
        if edgeNode not in self.edgeNodes:
            self.edgeNodes.append(edgeNode)


nodes = {}

amountNode = -1
while amountNode < 1:
    amountNode = int(input("Enter the number of nodes: "))
    if amountNode < 1:
        print("Please enter a valid number of nodes i.e. greater than 0")

for i in range(amountNode):
    current = input("Enter the current node value: ")
    nodes[current] = Node(current)

while True:
    directionInput = input("Is the graph directed? (y/n): ").lower()
    if directionInput == "y":
        isDirected = True
        break
    elif directionInput == "n":
        isDirected = False
        break
    else:
        print("Please enter y or n!")

amountEdge = -1
while amountEdge < amountNode - 1:
    amountEdge = int(input("Enter the number of edges: "))
    if amountEdge < amountNode - 1:
        print("Please enter a valid number of edges i.e. greater than or equal to one less than the number of nodes")

for i in range(amountEdge):
    u = input(f"Enter the starting node for edge {i + 1}: ")
    v = input(f"Enter the ending node for edge {i +  1}: ")
    nodes[u].addEdgeNode(nodes[v])
    if not isDirected:
        nodes[v].addEdgeNode(nodes[u])


def bfs(target, initial):
    q = queue.Queue()
    visited = []
    path = []

    if target is initial:
        print("Target found!")
        return initial

    q.put(initial)
    visited.append(initial)

    while not q.empty():

        print("Queue:", [node.data for node in list(q.queue)])

        current = q.get()
        path.append(current.data)

        print("Popped:", current.data)
        print("Path:", path)

        for node in current.edgeNodes:
            if node is target:
                path.append(node.data)
                print("Target found!")
                print("Final path:", path)
                return node

            if node not in visited:
                q.put(node)
                visited.append(node)

        print()

    return None


def dfs(target, initial):
    stack = []
    visited = []
    path = []

    if target is initial:
        print("Target found!")
        return initial

    stack.append(initial)
    visited.append(initial)

    while stack:

        print("Stack:", [node.data for node in stack])

        current = stack.pop()
        path.append(current.data)

        print("Popped:", current.data)
        print("Path:", path)

        for node in current.edgeNodes:
            if node is target:
                path.append(node.data)
                print("Target found!")
                print("Final path:", path)
                return node

            if node not in visited:
                stack.append(node)
                visited.append(node)

        print()

    return None


while True:
    print()
    while True:
        choice = input("Choose the search algorithm (BFS/DFS/EXIT): ").lower()
        if choice in ["bfs", "dfs", "exit"]:
            break
        print("Please enter BFS or DFS.")
   
    if choice == "exit":
        print("Execution stopped!")
        break
   
    print()
    initial = input("Enter the initial node: ")
    target = input("Enter the target node: ")

    if choice == "bfs":
        result = bfs(nodes[target], nodes[initial])
    else:
        result = dfs(nodes[target], nodes[initial])

    if result:
        print("\nFound:", result.data)
    else:
        print("Not Found")