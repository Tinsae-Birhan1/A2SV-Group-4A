class Solution:
    def simplifyPath(self, path: str) -> str:

        countiner = ""
        stack = []

        for paths in path + "/":
            if paths != "/":
                countiner += paths
            else:
                
                if countiner == "..":
                    if stack:
                        stack.pop()
                elif countiner != "" and countiner != ".":
                    stack.append(countiner)
                countiner = ""
        
        return "/" + "/".join(stack)