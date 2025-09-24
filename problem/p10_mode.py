# Write a function mode to find the value that appears most in an array.

# The case where the collection is empty may be ignored. Care must be taken to handle the case where the mode is non-unique.

# If it is not appropriate or possible to support a general collection, use a vector (array), if possible. If it is not appropriate or possible to support an unspecified value type, use integers.

def mode(arr):
    count, ans, ma = {}, [], 0
    for i in arr:
        count[i] = count.get(i, 0) + 1
    for i, c in count.items():
        ma = max(ma, c)
    for i, c in count.items():
        if c == ma:
            ans.append(i)
    return ans

# another version
from collections import Counter
def mode(arr):
    if not arr:
        return []
    # Count occurrences using Counter
    count = Counter(arr)
    # Find the maximum frequency
    max_freq = max(count.values())
    # Return all elements with the maximum frequency
    return [num for num, freq in count.items() if freq == max_freq]