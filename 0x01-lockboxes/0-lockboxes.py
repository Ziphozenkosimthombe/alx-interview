#!/usr/bin/python3
"""LOckboxes"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[n]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
