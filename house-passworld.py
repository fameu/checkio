def checkiomy(data):
    
    if len(data) < 10:
        return False
    
    lst = [0] * 3
    for k in data:
        if  "0" <= k <= "9":
            lst[0] = 1
        elif "a" <= k <= "z":
            lst[1] = 1
        elif "A" <= k <= "Z":
            lst[2] = 1
    #replace this for solution
    return all(k==1 for k in lst)

checkio1 = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    ) 

import re

DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def checkio2(data):
    """
    Return True if password strong and False if not
    
    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False
    
    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False
        
    return True

def checkio3(data):
    import re
    if len(data)<10:
        return False
    if not re.search('[0-9]', data):
        return False
    if not re.search('[a-z]', data):
        return False
    if not re.search('[A-Z]', data):
        return False
    return True
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
