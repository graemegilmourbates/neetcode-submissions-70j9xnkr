class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
            Ideally here we would have a hash, so if a number exists 
            its easy to detect without going back over the whole list.
            We need to implement a hash table.
        """
        buckets = 10;
        table = [[] for _ in range(buckets)];
        for num in nums:
            bucket = num % buckets;
            for item in table[bucket]:
                if item == num: return True;
            table[bucket].append(num)
        return False;

