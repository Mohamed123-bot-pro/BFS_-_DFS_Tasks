from collections import deque


maze = [
    "###                 #########",
    "#   ###################   # #",
    "# ####                # # # #",
    "# ################### # # # #",
    "#                     # # # #",
    "##################### # # # #",
    "#   ##                # # # #",
    "# # ## ### ## ######### # # #",
    "# #    #   ##B#         # # #",
    "# # ## ################ # # #",
    "### ##             #### # # #",
    "### ############## ## # # #",
    "###             ##    # # # #",
    "###### ######## ####### # # #",
    "###### ####             #   #",
    "A      ######################"
]


for r in range(len(maze)):
    for c in range(len(maze[r])):
        if maze[r][c] == 'A':
            start = (r, c)

        if maze[r][c] == 'B':
            target = (r, c)


queue = deque([(start, [start])])
visited = {start}
explored = 0


while queue:
    (r, c), path = queue.popleft()
    explored += 1

    if (r, c) == target:
        print("Path found!")
        print("Path:", path)
        print("Explored cells:", explored)
        break

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if (
            0 <= nr < len(maze)
            and 0 <= nc < len(maze[nr])
            and maze[nr][nc] != '#'
            and (nr, nc) not in visited
        ):
            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))