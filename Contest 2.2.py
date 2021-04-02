"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['zabcd','abcdz']))  # input
>>> main()
4
"""


def main():
    def preph(s):
        p = [0]*len(s)
        for i in range(len(s)-1):
            k = p[i]
            while k > 0 and s[i+1] != s[k]:
                k = p[k-1]
            if s[i+1] == s[k]:
                p[i+1] = k+1
            else:
                p[i+1] = 0
        return p

    s = input()
    t = input()
    s_t = t+"&"+s
    p = preph(s_t)
    t = t[p[-1]:]+t[:p[-1]]
    if t == s:
        if p[-1] == 0:
            print(-1)
        elif p[-1] == len(s):
            print(0)
        else:
            print(p[-1])
    else:
        print(-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
