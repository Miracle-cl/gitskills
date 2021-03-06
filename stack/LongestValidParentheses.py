class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

s = Solution()

print(s.longestValidParentheses("()()((("))
print(s.longestValidParentheses("()()(("))
print(s.longestValidParentheses("()(())((("))
