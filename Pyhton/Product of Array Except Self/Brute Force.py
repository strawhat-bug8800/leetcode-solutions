# LeetCode Problem 238: Product of Array Except Self
# Approach: Brute Force (Nested Loops)
# Time Complexity: O(n²) - for each element, we loop through the entire array again
# Space Complexity: O(n) - we store results in a separate list 'newlist'

nums = [-1, 0, 1, 2, 3]
co = 0             # 'co' keeps track of the current index we're excluding
total = 1          # will store the product of all numbers except the current one
newlist = []       # final result array

for number in nums:  # outer loop → go through each number in nums
    for i in range(len(nums)):  # inner loop → go through the whole array each time
        if i == co:
            pass  # skip the current index (we don’t multiply the number by itself)
        else:
            total = total * nums[i]  # multiply all other elements together
    newlist.append(total)  # append the product (excluding current number)
    total = 1              # reset total for the next element
    co = co + 1            # move to the next index

print(newlist)  # Output: [0, -6, 0, 0, 0]
