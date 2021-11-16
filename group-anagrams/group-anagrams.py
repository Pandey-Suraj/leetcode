from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         sorted_anagrams = defaultdict(list)
         for str in strs:
            sorted_str = ''.join(sorted(str))
            sorted_anagrams[sorted_str].append(str)

         return [val for val in sorted_anagrams.values()]