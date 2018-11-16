"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""

    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    max_distance = 0
    
    for i in range(num_holes):
        min_distance = cafes[0] - i
        if min_distance < 0:
            min_distance = -min_distance
        for cafe in cafes:

            distance = i - cafe
            if distance < 0:
                distance = distance * -1
                
            if distance < min_distance:
                min_distance = distance
    
        if min_distance > max_distance:
            max_distance = min_distance

    return max_distance



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
