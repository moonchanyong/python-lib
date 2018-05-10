import functools

def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

def howManyTree(n, myInput) :
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    다수의 gcd 구하기 gcd(a, b, c) = gcd(gcd(a, b), c) 성질을 이용
    '''
    myInput.sort()
    # 차이값 배열 구하기
    diffArr = []
    for _ in range(1,n):
        diffArr.append(myInput[_] - myInput[_-1])
    prev = gcd(diffArr[0],diffArr[1])

    for _ in range(2,n-1):
        prev = gcd(prev, diffArr[_])


    # 모든 값들의 gcd 구하기
    # 개수 세기
    cnt = ((myInput[n-1] - myInput[0]) / prev )- n+1

    return int(cnt)

def main():
    '''
    수정하시면 안됩니다.
    '''
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print(howManyTree(n, myInput))
if __name__ == "__main__":
    main()
