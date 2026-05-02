class Solution:
    def encode(self, strs: List[str]) -> str:
        finalstr = ""
        for i in strs:
            print(i)
            finalstr = finalstr+(str(len(i))+"#"+i)
        return finalstr

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Parse length until #
            length = 0
            while s[i] != '#':
                length = length * 10 + int(s[i])
                i += 1
            i += 1  # skip #
            
            # Extract string of that length
            string_val = s[i:i + length]
            result.append(string_val)
            i += length
        return result
