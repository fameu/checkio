def checkio(expression):
    kv = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }
    lst = []
    for i in expression:
        if i in kv.values():
            lst.append(i)
        if i in kv.keys():
            if len(lst) == 0:
                return False
            t = lst.pop()
            if t != kv[i]:
                return False
    return lst == []

def checkio1(data):
    stack=[""]
    brackets={"(":")","[":"]","{":"}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c!=stack.pop():
            return False
    return stack==[""]
	

def checkio2(text):
	BRACKET_PAIRS = ['()', '{}', '[]', '<>']
	OPEN_BRACKETS = {a for a, _ in BRACKET_PAIRS}
	CLOSE_BRACKETS = {b: a for a, b in BRACKET_PAIRS}

    """Return whether text has proper bracket nesting."""
    stack = []
    for c in text:
        if c in OPEN_BRACKETS:
            stack.append(c)
        elif c in CLOSE_BRACKETS:
            if not stack or stack[-1] != CLOSE_BRACKETS[c]:
                return False
            stack.pop()

    return not stack

	
	
def checkio2(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == s0:
            return False
    return True
	
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
