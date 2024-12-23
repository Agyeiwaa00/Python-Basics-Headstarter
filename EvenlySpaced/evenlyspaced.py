# Given three ints, a b c, one of them is small, one is medium and one is large. 
# Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.

# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

def evenlySpaced(a, b, c):
    var = sorted([a,b,c]) # sort the numbers to identify small, medium and large
    small, medium, large = var[0],var[1],var[2]

    if (medium-small) == (large-medium):
        return True
    else:
        return False    

result = evenlySpaced(5, 7, 9)
print(result)