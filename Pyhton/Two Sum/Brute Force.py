# LeetCode 1 - Two Sum
# Approach: Brute Force
# Time: O(n^2), Space: O(1)

def two_sum(nums, target):
    """
    Brute Force Approach:
    Add each number in the list to every other number until the pair equals the target.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example
nums = [5, 2, 4, 8, 9, 11, 6, 7]
target = int(input("Enter your target: "))
print(two_sum(nums, target))
