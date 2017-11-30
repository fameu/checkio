#Your optional code here
#You can import some modules or create additional functions
def checkiomy(data):
    dct = {}
    for idx, v in enumerate(data):
        if v not in dct:
            dct[v] = idx
        else:
            dct[v] = -1
    
    for k, v in dct.items():
        if v >= 0:
            data.remove(k)
    return data
    
def checkio1(data):
        return [i for i in data if data.count(i) > 1]

from collections import Counter
def checkio2(data):
    counter = Counter(data)
    return [item for item in data if counter[item] > 1]

def checkio3(data):    
    return filter(lambda x: data.count(x) > 1, data)
    
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
