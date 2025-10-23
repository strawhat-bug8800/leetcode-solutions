# LeetCode Problem 217: Contains Duplicate
# Approach: Hashmap
# Time Complexity: O(n) - we traverse the array once
# Space Complexity: O(n) - extra space for the hashmap

class Solution:
    def containsDuplicate(self, nums):
       
        seen = {}  # Dictionary to store numbers we've seen
        for num in nums:
            if num in seen:  # Duplicate found
                return True
            seen[num] = True  # Mark number as seen
        return False  # No duplicates found

# Example usage:
nums = [1, 2, 3, 3]
solution = Solution()
print(solution.containsDuplicate(nums))  # Output: True
