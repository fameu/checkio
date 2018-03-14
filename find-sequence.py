# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 16:03
# @Author  : famu
# @File    : find-sequence.py
# @Software: PyCharm

def checkioMe(matrix):
    #replace this for solution
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            l1 = [matrix[i][j+k] for k in range(4) if j+k < n]
            l2 = [matrix[i+k][j] for k in range(4) if i+k < n]
            l3 = [matrix[i+k][j+k] for k in range(4) if i+k <n and j+k<n]
            l4 = [matrix[i-k][j+k] for k in range(4) if j+k <n and i-k>=0]
            if len(set(l1)) == 1 and len(l1) == 4:
                return True
            if len(set(l2)) == 1 and len(l2) == 4:
                return True
            if len(set(l3)) == 1 and len(l3) == 4:
                return True
            if len(set(l4)) == 1 and len(l4) == 4:
                return True
    return False

def checkioOne(m):
    horizont=lambda m: any(False if j+4>len(m) else all(m[i][j+k]==m[i][j] for k in range(4))\
                                for i in range(len(m)) for j in range(len(m)))
    diagonal=lambda m: any(False if i+4>len(m) or j+4>len(m) else all(m[i+k][j+k]==m[i][j] for k in range(4))\
                                for i in range(len(m)) for j in range(len(m)))
    return horizont(m) or horizont(list(zip(*m))) or diagonal(m) or diagonal(m[-1::-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
