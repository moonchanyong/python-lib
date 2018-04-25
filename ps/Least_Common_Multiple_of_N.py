# 에라토스테네스의 채 num -> [num]
def find_factor(num):
    factors = list(range(2, num))
    ret = []
    for i in factors:
        if i is -1:
            continue

        ret.append(i)
        for mul in range(1,int(num/i)):
            factors[mul * i -2] = -1

    return ret

def factor(n, factors):
    if n <= 0 :
        return {}
    f = {}
    for k in factors :
        while not (n % k) :
            f[k] = f.setdefault(k, 0) + 1
            n //= k
    while n != 1 :
        if k > n**0.5 :
            f[n] = 1
            break
        while not (n % k) :
            f[k] = f.setdefault(k, 0) + 1
            n //= k
        k += 2
    return f

def nlcm(num):
    factors = find_factor(max(num))
    factor_list = list(map(lambda x: factor(x, factors), num))

    base = {}
    # 메인로직
    for i in factor_list:
        for key,value in i.items():
            if key in base and base[key] >= value:
                continue
            else:
                base[key] = value

    answer = 1

    for key,value in base.items():
        answer *= key**value
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));
