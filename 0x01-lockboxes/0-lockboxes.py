#!/usr/bin/python3
"""LOckboxes"""


def canUnlockAll(boxes):
    """
    # check if boxes is a list
    # if the box not a list return False
    # check if the list is empty
    # loop through the keys boxes
    # loop through the boxes
    # check if the box is not in the keys,
    # list and the box is less than the length of the boxes 
    #append the box to the keys list
    # check if the length of the keys,
    # boxes is equal to the length of the boxes
    # return True
    # return False
    """
    if not boxes or not isinstance(boxes, list):
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box < len(boxes) and box not in keys:
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
