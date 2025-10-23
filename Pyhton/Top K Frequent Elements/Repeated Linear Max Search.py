

# LeetCode Problem 347: Top K Frequent Elements
# Approach: Approach: Hashmap + Repeated Linear Max Search
# Time Complexity: O(k * n) (≈ O(n²) worst case)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums, k):
        
        # Count frequencies
        count = {}
        element = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:#we can use get instead
                count[num] = 1
                element.append(num) #append unique numbers

        # Pick top k frequent elements
        result = []
        for _ in range(k): #each time we extract the max and we remove it from the heap
            maximum = 0 #reset max to 0 each time
            for num in element:
                if count[num] > maximum:
                    maximum = count[num]
                    top = num
            result.append(top)
            element.remove(top)

        return result

# Example usage:
nums = [1, 2, 3, 3, 4, 5, 5, 6, 6, 6]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))  # Output: [6, 3] or similar
