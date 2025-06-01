class Solution:
    def removeInvalidParentheses(self, s):
        def getMinRemovals(s):
            l = r = 0
            for c in s:
                if c == '(':
                    l += 1
                elif c == ')':
                    if l > 0:
                        l -= 1
                    else:
                        r += 1
            return l, r
        lrem, rrem = getMinRemovals(s)
        ans = set()
        def isValid(st):
            cnt = 0
            for ch in st:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        def dfs(st, start, lrem, rrem):
            if lrem == 0 and rrem == 0:
                if isValid(st):
                    ans.add(st)
                return
            for i in range(start, len(st)):
                if i > start and st[i] == st[i - 1]:
                    continue
                if lrem and st[i] == '(':
                    dfs(st[:i] + st[i + 1:], i, lrem - 1, rrem)
                if rrem and st[i] == ')':
                    dfs(st[:i] + st[i + 1:], i, lrem, rrem - 1)
        dfs(s, 0, lrem, rrem)
        return list(ans)
