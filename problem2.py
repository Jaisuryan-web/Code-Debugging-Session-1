# Problem2: Return the second largest unique number in the list.

#def second_largest(nums):
    #nums = list(set(nums))
    #nums.sort()
    #return nums[-2]

#print(second_largest([4, 1, 7, 7, 3]))

def second_largest(nums):
    nums = list(set(nums))
    if len(nums) < 2:
        return None  # or raise ValueError("Not enough unique elements")
    nums.sort()
    return nums[-2]

print(second_largest([4, 1, 7, 7, 3]))  # Output: 4
