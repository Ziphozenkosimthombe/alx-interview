#!/usr/bin/python3


def canUnlockAll(boxes):
    visited = set()
    # Initialize a queue to perform BFS
    queue = [0]

    # Start BFS from the first box
    while queue:
        box = queue.pop(0)
        visited.add(box)
        # Add keys from the current box to the queue
        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
