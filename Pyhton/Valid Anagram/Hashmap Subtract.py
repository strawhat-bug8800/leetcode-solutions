# LeetCode - Valid Anagram
# Approach: Hashmap Subtract
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isAnagram(self, Word, Word2):
        Hash = {}  # Create an empty dictionary
        IsItTrue = True

        # Step 1: Count the letters of the first word
        for i in Word:
            if i in Hash:
                Hash[i] += 1  # Count the number of letters
            else:
                Hash[i] = 1

        # Step 2: Subtract the letters of the second word from the dictionary of the first word
        for i in Word2:
            if i in Hash:
                Hash[i] += -1
            else:  # If we don't find a letter, it's false
                IsItTrue = False

        # Step 3: Check if all counts are zero
        for value in Hash.values():
            if value != 0:  # If the final value of the dictionary is not 0 for every letter, it's false
                IsItTrue = False

        return IsItTrue


# Example usage
solution = Solution()
Word = "mkarkeb"
Word2 = "bekrakmk"
print(solution.isAnagram(Word, Word2))  # Output: True
