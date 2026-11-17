import queue

class Node:
    def __init__(self, data, cost):
        self.data = data
        self.cost = cost
        self.parent = None
        self.edgeNodes = []

    def addEdgeNode(self, edgeNode):
        if edgeNode not in self.edgeNodes:
            self.edgeNodes.append(edgeNode)
   
    def addParent(self, parentNode):
        self.parent = parentNode

    def __lt__(self, other):
        return self.data < other.data

   
    def __repr__(self):
        return self.data


nodes = {}

amountNode = -1
while amountNode < 1:
    try:
        amountNode = int(input("Enter the number of nodes: "))
        if amountNode < 1:
            print("Please enter a valid number of nodes i.e. greater than 0")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(amountNode):
    current = input("Enter the current node value: ")
    cost = int(input(f"Enter the cost for {current}: "))
    nodes[current] = Node(current, cost)

amountEdge = -1
while amountEdge < amountNode - 1:
    try:
        amountEdge = int(input("Enter the number of edges: "))
        if amountEdge < amountNode - 1:
            print("Please enter a valid number of edges i.e. greater than or equal to one less than the number of nodes")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(amountEdge):
    u = input(f"Enter the starting node for edge {i + 1}: ")
    v = input(f"Enter the ending node for edge {i +  1}: ")
    nodes[u].addEdgeNode(nodes[v])
    nodes[v].addEdgeNode(nodes[u])


def greedy(target, initial):
    for node in nodes.values():
        node.parent = None

    opened = queue.PriorityQueue()
    closed = []
    traversal = []
   
    opened.put((initial.cost, initial))
    in_opened = {initial}
   
    while not opened.empty():
        cost, n = opened.get()
        traversal.append(n.data)
       
        print()
        print("Closed: ", closed)
        print("Popped: ", n.data)
       
        closed.append(n)
       
        if n == target:
            print("Success!")
            path = []
            while n is not None:
                path.insert(0, n.data)
                n = n.parent
            print("Final path: ", path)
            print("Traversal path: ", traversal)
            return
           
        for m in n.edgeNodes:
            if m in closed:
                continue
            if m not in in_opened:
                m.addParent(n)
                opened.put((m.cost, m))
                in_opened.add(m)
                print(m.data, "added to opened")
   
    print("Failed to find the target!")

while True:
    print()

    initial = input("Enter the initial node: ")
    target = input("Enter the target node: ")

    if initial in nodes and target in nodes:
        greedy(nodes[target], nodes[initial])
    else:
        print("Initial or Target node does not exist!")
       
    print()
    while True:
        choice = input("Do you wish to continue (Y/N): ").lower()
        if choice in ["y", "n"]:
            break
        print("Please enter Y or N!")
   
    if choice == "n":
        print("Execution stopped!")
        break