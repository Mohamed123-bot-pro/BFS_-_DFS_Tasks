graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['M'],
    'G': ['N', 'O'],
    'H': ['P'],
    'I': ['Q'],
    'J': ['R', 'V'],
    'K': [],
    'L': ['S'],
    'M': ['T'],
    'N': [],
    'O': ['U'],
    'P': [],
    'Q': [],
    'R': [],
    'V': [],
    'S': [],
    'T': [],
    'U': []
}


def bfs(start, target):
    queue = [start]
    visited = []
    steps = 0
    checks = 0

    while queue:
        node = queue.pop(0)
        checks += 1

        if node not in visited:
            visited.append(node)
            steps += 1
            print("BFS checking:", node)

            if node == target:
                print("Found:", node)
                print("Steps:", steps)
                print("Checks:", checks)
                return

            queue.extend(graph[node])

    print("Target not found")


def dfs(start, target):
    stack = [start]
    visited = []
    steps = 0
    checks = 0

    while stack:
        node = stack.pop()
        checks += 1

        if node not in visited:
            visited.append(node)
            steps += 1
            print("DFS checking:", node)

            if node == target:
                print("Found:", node)
                print("Steps:", steps)
                print("Checks:", checks)
                return

            stack.extend(reversed(graph[node]))

    print("Target not found")


start = input("Start: ").upper()
target = input("Target: ").upper()

bfs(start, target)
dfs(start, target)