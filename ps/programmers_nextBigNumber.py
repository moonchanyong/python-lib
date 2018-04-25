
# pythonic

def nextBigNumber(n):
    answer = n+1
    arr = bin(n)
    count = arr[1:].count('1')

    while True:
        if  bin(answer)[1:].count('1') == count:
            return answer
        answer+=1


print(nextBigNumber(78))
