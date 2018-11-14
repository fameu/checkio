
def checkio(data):
    
    import math
    (x1, y1), (x2, y2), (x3, y3) = eval(data)
        
    e = 2 * (x2 - x1)
    f = 2 * (y2 - y1)
    
    g = x2*x2 - x1*x1 + y2*y2 - y1*y1
    
    a = 2 * (x3 - x2)
    b = 2 * (y3 - y2)
    
    c = x3*x3 - x2*x2 + y3*y3 - y2*y2

    X = (g*b - c*f)*1.0 / (e*b - a*f)
    Y = (a*g - c*e)*1.0 / (a*f - b*e)
    R = math.sqrt((X-x1)*(X-x1)+(Y-y1)*(Y-y1))
    #replace this for solution
    X, Y, R = round(X,2), round(Y,2), round(R, 2)
    return "(x-%s)^2+(y-%s)^2=%s^2"%(int(X) if int(X) == X else X, int(Y) if int(Y) == Y else Y, int(R) if int(R) == R else R)
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
