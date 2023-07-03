class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words[1:]:
            curr = Counter(word)
            counts &= curr
        ans = []
        for i, count in counts.items():
            for j in range(count):
                ans.append(i)
        return "".join(ans)

