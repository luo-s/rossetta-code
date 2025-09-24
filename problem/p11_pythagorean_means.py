# Compute all three of the Pythagorean means of the set of integers 1 through 10 (inclusive).

# https://en.wikipedia.org/wiki/Pythagorean_means

# https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/averagespythagorean-means

def pythagorean(arr):
    total, prod, reci, l = 0, 1, 0, len(arr)
    for i in arr:
        total += i
        prod *= i
        reci += 1/i
    am = total / l
    gm = pow(prod, 1/l)
    hm = l / reci 
    
    ans = {
        "values": {
            "Arithmetic": am,
            "Geometric": gm,
            "Harmonic": hm
        },
        "test": f"is A >= G >= H ? {'yes' if am >= gm >= hm else 'no'}"
    }

    return ans

print(pythagorean([1,2,3,4,5,6,7,8,9,10]))