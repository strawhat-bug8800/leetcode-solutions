# LeetCode 1 - Two Sum
# Approach: Hashmap (Dictionary)
# Time: O(n)
# Space: O(n)

def two_sum(nums, target):
    """
    Use a dictionary to store each number as a key and its index as a value.
    For every number, check if the complement (target - num)
    exists in the dictionary.
    """
    # Create an empty dictionary
    dictionary = {}

    # Build the dictionary
    for i in range(len(nums)):
        dictionary[nums[i]] = i  # store index of each number

    # Search for the complement in the dictionary 
    for i in range(len(nums)):
        x = target - nums[i]
        # Make sure we are not using the same number twice
        if x in dictionary and dictionary[x] != i:
            return [i, dictionary[x]]  # return indices, not values

# Example
nums = [5, 2, 4, 8, 9, 11, 6, 7]
target = int(input("Enter your target: "))
print(two_sum(nums, target))
