def Parse(x):
    res = x.split('\n')
    res = res[1].split(' ')
    for i in range(0, len(res)):
        res[i] = int(res[i])
    return res;


def Normalize(grama):
    d = int(sum(grama))
    for i in range(0, len(grama)):
        grama[i] = (grama[i] / d)
    return grama;


def rec1(grama):
    sum = 0
    for i in range(0, len(grama)):
        if (sum >= 0.5):
            return i - 1;
        sum += grama[i]
    return "wrong";


def rec2(x, e):
    if(e>(len(x)/2)):
        return e    

    res = []
    for i in range(e, len(x) - e):
        res.append(sum1(x, max(i-e, 0), min(i + e, len(x))))
    answ = maxInd(res) + e
    return answ;


def sum(x, st=0):
    fin = len(x)
    sum = 0
    for i in range(st, fin):
        sum += x[i]
    return sum;


def sum1(x, st=0, fin=0):
    if (st > fin): return f"bad";
    sum1 = 0
    for i in range(st, fin + 1):
        sum1 += x[i]
    return sum1;


def maxInd(arr):
    max = arr[0]
    maxInd = 0
    for i in range(1, len(arr)):
        if (max < arr[i]):
            max = arr[i]
            maxInd = i
    return maxInd;
