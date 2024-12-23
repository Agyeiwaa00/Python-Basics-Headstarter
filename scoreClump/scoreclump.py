# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true


def scoresClump(scores):

    for i in range(len(scores)-2):
        # extracting 3 conservative scores 
        t1,t2,t3 = scores[i], scores[i+1], scores[i+2]

    # Check if the largest and smallest scores are at most 2 apart
    if t3-t1 <=2: # in this case, t3 is the largest score and t1 is the smallest score. t2 is the medium score
        return True # if group is found return True
    else: 
         return False # If no group is found, return False

result = scoresClump([3, 4, 6])        
print(result)
