class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Dict of 1 positions
        pos = []
        for i in range(len(s)):
            if s[i] == '1': pos.append(i)
                
        # print(pos)
        
        npos = len(pos)
        
        if npos == 0 or npos < k: return ""
        
        min_length = float('inf')
        min_string = str(s)
        
        for windowsize in range(k, npos+1):
            for start in range(npos-windowsize+1):
                # print(pos[start:start+windowsize])
                # print(start, start+windowsize-1)
                this_length = pos[start+windowsize-1] - pos[start] + 1
                str_start = pos[start]
                str_end = pos[start+windowsize-1]
                this_string = s[str_start:str_end+1]
                # print(this_length, this_string)
                
                
                # this_string = str(pos[start:start+windowsize])
                if this_length < min_length:
                    min_length = this_length
                    min_string = this_string
                elif this_length == min_length and this_string < min_string:
                    min_string = this_string
                    
        # print(min_length)
        # print(min_string)
        
        return min_string