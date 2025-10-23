# LeetCode 49 - Group Anagrams
# Approach: Hashmap Counting
# Time Complexity: O(n^2 * k)
# Space Complexity: O(n * k)

class Solution(object):
    def groupAnagrams(self, strs):
        Map = []
        for word in strs:
            Hash = {}
            HashDash = {}
            for letter in word:
                Hash[letter] = 1 + Hash.get(letter, 0)  # Create a dictionary that contains the number of each letter in a word 
            HashDash[word] = Hash  # Store the word as a key in a new dictionary and the value is the previous dictionary 
            Map.append(HashDash)  # Add each dictionary to a list called Map

        Final = []
        Used = set()  # Words we've already put into Final

        for i in range(len(strs)):
            if i in Used:   # Skip if the word index is already grouped 
                continue
            anagram = [strs[i]]  # We don’t need to initialize anagram as empty each time; we just recreate it with the new word
            Used.add(i)  # After we add it, it means we already used it 
            for j in range(i + 1, len(strs)):
                # If the hash inside HashDash inside Map are equal to the other element, we put it as an anagram
                if Map[i][strs[i]] == Map[j][strs[j]] and j not in Used:  
                    anagram.append(strs[j])  # If the hashmaps are equal, append the word to the anagram list
                    Used.add(j)  # Add it to the Used set
            Final.append(anagram)  # Append the anagram group to the final list

        return Final


# Example usage
solution = Solution()
Array = ["act", "pots", "tops", "cat", "stop", "hat"]
print(solution.groupAnagrams(Array))
