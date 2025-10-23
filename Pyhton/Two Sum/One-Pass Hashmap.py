# LeetCode 1 - Two Sum
# Approach: One-Pass Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    """
    Create an empty dictionary, then iterate through the list.
    For each number, calculate its complement (target - nums[i]).
    If the complement exists in the dictionary, return the indices.
    Otherwise, add the current number to the dictionary.

    This approach avoids nested loops and runs in linear time.
    """
    hashmap = {}  # Create empty dictionary

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:  # Check if complement exists in dictionary
            return [i, hashmap[complement]]  # Return indices
        hashmap[nums[i]] = i  # Add current number to dictionary

# Example usage
nums = [5, 2, 4, 8, 9, 11, 6, 7]
target = int(input("Enter your target: "))
print(two_sum(nums, target))
