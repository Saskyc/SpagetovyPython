class SubStringList:
    length = property(lambda self: self.length_get())

    def length_get(self : "SubStringList") -> int:
        return len(self.chars)

    def __init__(self : "SubStringList") -> None:
        self.chars : list[str] = []
    def haschar(self : "SubStringList", char : str) -> bool:
        for i in self.chars:
            if i == char:
                return True
        return False
    def add(self : "SubStringList", char : str) -> bool:
        if self.haschar(char):
            return False

        self.chars.append(char)
        return True
    def highest(lists : list["SubStringList"]) -> "SubStringList":
        highest : SubStringList = SubStringList()
        for i in lists:
            if highest == None:
                highest = i
                continue
            if len(highest.chars) < len(i.chars):
                highest = i
        return highest

class Solution:
    def __init__(self):
        pass
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings : list[SubStringList] = []
        sub = SubStringList()
        for i in range(len(s)):
            for j in range(len(s)):
                if j < i:
                    continue
                res : bool = sub.add(s[j])
                if not res:
                    substrings.append(sub)
                    sub = SubStringList()
                    sub.add(s[j])
        substrings.append(sub)
        return len(SubStringList.highest(substrings).chars)
print(Solution().lengthOfLongestSubstring("dvdf"))