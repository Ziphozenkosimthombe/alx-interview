#!/usr/bin/env python3
"""
1. # If boxes is not a list, return False
1. # Check if boxes is a list
2. # Check if the first box is empty
3. # Check if the key is in the boxes
4. # Check if the box is not already in the keys
5. # Check if the box is less than the length of the boxes
6. # Add the box to the keys
7. # Check if the length of the keys is equal to the length of the boxes
8. # Return True if the length of the keys is equal to the length of the boxes
9. # Return False if the length of the keys,
is not equal to the length of the boxes
10. # Return False if boxes is not a list
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
