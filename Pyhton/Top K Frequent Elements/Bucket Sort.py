# Approach: Hashmap + Bucket Sort
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def topKFrequent(self, nums, k):
        
        
        # Count frequencies
        count = {}  # empty dictionary 
        element = []  # empty list
        for num in nums:
            if num in count:
                count[num] += 1 
            else:  # we can use get() instead
                count[num] = 1
                element.append(num)  # append unique numbers

        heap = []
        # Create buckets: index = frequency(count), value = list of numbers
        for _ in range(len(nums) + 1): #+1 because we start from 0 'we don't need 0 here' and in this case the index is important the index need to be equal to len(nums)
            heap.append([])  # use a list because multiple numbers can have the same frequency
        
        for num in element:
            heap[count[num]].append(num)  # the index in 'heap' is the frequency (count),
                                          # and the value is a list of numbers with that frequency

        # Collect top k frequent elements
        res = []
        for i in range(len(heap) - 1, 0, -1):  # start from the end of the list (highest frequency) 
            for num in heap[i]:  # each element in 'heap' is a list that contains numbers 
                                 # all these sublists are grouped by their frequency
                res.append(num)
                if len(res) == k:  # break from the inner loop once we collect k elements
                    break 
            if len(res) == k:  # break from the outer loop as well
                break  

        return res

#we used (nums) +1 in nums(we said before why) and  (heap) -1 in heap not the same -1 so we don't go out of range 
# Example usage:
nums = [1, 2, 3, 3, 4, 5, 5, 6, 6, 6]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))  # Output: [6, 3] or similar