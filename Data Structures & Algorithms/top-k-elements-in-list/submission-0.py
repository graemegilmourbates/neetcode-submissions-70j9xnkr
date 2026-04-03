class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        freq = [[] for _ in range(n+1)]
        for num, count in counts.items():
            freq[count].append(num)
        results = []
        for i in range(n, 0, -1):
            for num in freq[i]:
                results.append(num)
                if len(results) == k: return results 


        

        
