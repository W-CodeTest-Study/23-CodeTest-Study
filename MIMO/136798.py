def getMyDivisor(n):
    
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(number, limit, power):
    count = []
    for i in range(1,number+1):
        tmp = []
        tmp = getMyDivisor(i)
        count.append(len(tmp))
    for i in range(len(count)):
        if count[i] > limit:
            count[i] = power
    return sum(count)