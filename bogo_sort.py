import random

def is_sorted(arr):
    """Check if the list is sorted"""
    return arr == sorted(arr)

def bogosort(arr):
    """Sorts an array using Bogosort"""
    while not is_sorted(arr):
        random.shuffle(arr)  # Shuffle the list randomly
    return arr
