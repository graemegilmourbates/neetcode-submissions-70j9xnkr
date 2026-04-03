class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        buckets = 36;
        table = [[] for _ in range(buckets)]
        if len(s)!=len(t): return False
        for char in s:
            bucket = ord(char) % buckets
            table[bucket].append(char)
        for char in t:
            bucket = ord(char) % buckets
            if len(table[bucket])==0: return False
            table[bucket].pop()
        return True

