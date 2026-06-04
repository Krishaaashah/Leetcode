class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        a = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                a.append(i)
            else:
                if not a:
                    return False
                top = a.pop()
                if i == ")" and top != "(":
                    return False
                if  i == "]" and top != "[":
                    return False
                if i == "}" and top != "{":
                    return False
        return len(a) == 0
        