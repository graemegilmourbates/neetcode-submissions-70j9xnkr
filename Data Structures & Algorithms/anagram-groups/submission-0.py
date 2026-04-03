class Solution:
    def isAna(self, s: str, t: str)->bool:
        buckets = 36
        table = [0 for _ in range(buckets)]
        if len(t) != len(s): return False
        for char in s:
            table[ord(char)%buckets] += 1
        for char in t:
            index = ord(char)%buckets
            table[index] -= 1
            if table[index] < 0: return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = 10
        table = [[] for _ in range(buckets)]
        # first group by length
        for item in strs:
            table[len(item)%buckets].append(item)
        anas = []
        for bucket in table:
            i = 0
            while(i < len(bucket)):
                j = i+1
                tmp = []
                tmp.append(bucket[i]);
                while(j<len(bucket)):
                    if(self.isAna(bucket[i],bucket[j])):
                        tmp.append(bucket.pop(j))
                    else: j += 1
                anas.append(tmp)
                i += 1
        return anas

        