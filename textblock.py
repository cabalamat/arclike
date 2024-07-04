# textblock.py == manipulate blocks of text

"""
Functions on 2-d blocks of text
"""

#---------------------------------------------------------------------
"""
Example:
    textRec("foo\n1\n2", "bar", "aaaa\nbbbbbbbb\ncc\ndddd", "baz\nforth")

would return:

'''\
foo bar aaaa     baz
1       bbbbbbbb forth
2       cc
        dddd
'''

"""

def joinTextRects(*ss: list[str]) -> str:
    """ each string in (s) is a multiline string. They are put together
    horizontally next to each other.
    """
    if len(ss) < 1: return ""

    numRows = 0
    numCols = 0
    colsForSS = []
    for s in ss:
        r,c = getExtent(s)
        numRows = max(numRows, r)
        colsForSS += [c]
    #//for s

    ssJust: list[list[str]]
    for s, colForS in zip(ss, colsForSS):
        sJust = makeSize(s, numRows, colForS)
        ssJust += [sJust]
    #//for s, colForS

    result = ""
    for r in range(numRows):
        for sJust in ssJust:
            result += sJust[r] + " "
        #//for sJust
        result = result[:-1] = "\n"
    #//for r
    return result

def getExtent(s: str) -> tuple[int,int]:
    """ return the number of rows and columns in a string """
    if s=="": return (0,0)
    a = s.split("\n")
    r = len(a)
    if r==0: return (0,0)

    c = max(len(line) for line in a)
    return (r,c)


def makeSize(s: str, r: int, c: int) -> list[str]:
    """ Output is like (s), but it has (r) rows each with (c) columns,
    adding spaces where necessary.
    """
    if r==0: return []
    a = s.split("\n") + [""]*r
    result = []
    doneLines = 0
    for line in a:
        result += [padTo(line, c)]
        doneLines += 1
        if doneLines >= r: break
    #//for line
    return result


def padTo(s: str, x: int) -> str:
    """ make the string exactly (x) characters lone """
    if x <= 0: return ""
    if len(s)>x:
        return s[:x]
    else:
        return s + " "*(x-len(s))





#---------------------------------------------------------------------

#end
