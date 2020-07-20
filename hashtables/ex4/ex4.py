def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for i in a:
        if i > 0:
            cache[i] = 0
    
    for x in a:
        if x < 0:
            pos = -x
            if pos not in cache:
                pass
            else:
                cache[pos] += 1

    for item in cache:
        if cache[item] > 0:
            result.append(item)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
