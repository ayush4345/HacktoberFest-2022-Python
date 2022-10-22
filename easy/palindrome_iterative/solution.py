def solution(a = None):
    
    d = str(a)

    if a == None:
        return -1
    if a < 0:
        return -1
    if d == d[::-1]:
        return 1
    else:
        return 0



