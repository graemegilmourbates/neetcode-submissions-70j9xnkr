class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for item in strs:
            encoded += str(len(item)) + "#" +item
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        lst = []
        while(i<len(s)):
            j = i
            
            while(s[i]!='#'):
                i+=1
            item_len = int(s[j:i])
            lst.append(s[i+1:item_len+i+1])
            i=item_len+i+1
        return lst
        
