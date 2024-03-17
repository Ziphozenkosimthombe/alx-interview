def canUnlockAll(boxes):
    # Check if boxes is a list
    if not boxes:
        # If boxes is not a list, return False
        return False
    # Check if boxes is a list of lists
    keys = [0]
    # Check if the first box is empty
    for key in keys:
        # Check if the key is in the boxes
        for box in boxes[key]:
            # Check if the box is not already in the keys
            # Check if the box is less than the length of the boxes
            if box not in keys and box < len(boxes):
                # Add the box to the keys
                keys.append(box)
    # Check if the length of the keys is equal to the length of the boxes
    return len(keys) == len(boxes)
