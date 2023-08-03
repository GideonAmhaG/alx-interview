#!/usr/bin/python3
"""
module for unlocking lists or boxes
"""


def canUnlockAll(boxes):
    """
    given a list of lists, returns true if the indexes of the all the
    sub lists are located in thee sub lists
    """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
