# 49. Group Anagrams (Medium)
# https://leetcode-cn.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        res = []
        for s in strs:
            key = "".join(sorted(tuple(s)))
            if key not in dic.keys():
                dic[key] = [s]
            else:
                dic[key].append(s)
        return list(dic.values())
