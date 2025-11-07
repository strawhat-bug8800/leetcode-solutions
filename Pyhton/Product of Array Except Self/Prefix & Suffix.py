# LeetCode Problem 238: Product of Array Except Self
# Approach: Prefix and Postfix Multiplication
# Time Complexity: O(n) - we traverse the array twice (once for prefix, once for postfix)
# Space Complexity: O(1) - output array 'res' doesn't count as extra space (required by the problem)

class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)   # create a list of 1s with the same length as nums (to store the final results)

        # ---------- PREFIX LOOP ----------
        prefix = 1  # the first element has no prefix (nothing on its left),
                    # so we start with 1 because multiplying by 1 doesn’t change the result

        for i in range(len(nums)):
            res[i] = prefix  # store the prefix (product of all numbers before index i in nums)
                             # in the same index i but inside the res array
            prefix *= nums[i]  # calculate the prefix for the next element (multiply by the current number)

        # ---------- POSTFIX LOOP ----------
        postfix = 1  # the last element has no postfix (nothing on its right),
                     # so we assume it's 1 just like we did before

        for i in range(len(nums) - 1, -1, -1):  # start, stop, step → if len = 4 then it's range(3, -1, -1)
                                                # we start from the last element in the nums array and move backward until index 0
            res[i] *= postfix  # here we don’t append or assign a new value — we multiply the value that was already stored (the prefix)
                               # in the first run, we multiply the prefix of the last element with its postfix (which is 1, since it's the last one)
            postfix *= nums[i]  # we calculate the postfix for the next number (to use it in the next iteration)

        return res  # return the final array that contains the product of all numbers except the one at each index


# Example usage:
nums = [1, 2, 4, 6]
solution = Solution()
print(solution.productExceptSelf(nums))  # Output: [48, 24, 12, 8]
