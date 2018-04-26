def isPalindrome(string):
    lenStr = len(string)
    base = int(lenStr/2)
    for i in range(base):
    	if string[i] != string[lenStr-1-i]:
    		return False
    return True

# object type  reverse=True => desc
arr.sort(key=lambda x: x.count, reverse=True)

# idx, val
for index, item in enumerate(items):
    print(index, item)

# string_reverse(s) :: string -> string
def string_reverse(s):
    ret = ""
    for i in s:
        ret = i + ret
    return ret

# digit_reverse :: digit -> [num]
def digit_reverse(n):
    # 함수를 완성해 주세요
    ret = list(map(lambda x: int(x), string_reverse(str(n))))
    return ret

# number -> 0bnumber
bin(n)

# ex) one_to_one['num'+1] // value
# 1 -> num1 == 'num' + 1 -> value
one_to_one = {
    num1  = 2,
    num2 = 3
}


# 1차원 배열, expression은 지금 스트링만됨
# setup_list_without_expression :: list -> [[index: number, value: number] .. ] -> void
# setup_list_wit_expression :: list -> expression X = 0 , O = 1 -> void
def setup_list(*args, **kargs):
    if len(kargs) is 0:
        for i,v in args[1]:
            args[0][i] = v
    else:
        for i in range(len(args[0])):
            for key, value in kargs.items():
                if key is args[0][i]:
                    args[0][i] = value
                    break;

# list -> list
def foreach(func, lis):
    for i, v in enumerate(lis):
        lis[i] = func(v)

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

# 소인수 분해  factor :: number -> facotors:[number] -> [{facotr: count}]
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

# case dp
# expression_dp :: [numbers] => [number]
def expression_dp(*args, **kargs):
    arr = args[0]
    currentIndex = args[1]
    ret = [] # write each index for sum

    return


import functools
# oneDimension_dp :: number => (number => number) => number
def oneDimension_dp(num):
    dp = list(range(num+1))
    for i in dp:
        if i is 0: # setting dp value
            dp[0] = 1
            continue
        if i is 1:
            dp[1] = 1
            continue
        idxs = expression_dp(dp, i) # 1차원이라 1차원 배열 나옴
        dp[i] = reduce(lambda a,b: a+dp[b], idxs, 0)
    return dp[num]


# end case dp
