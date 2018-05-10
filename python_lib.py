import math
# factorial
math.factorial(number)

# list comprehension 오.. 갓 .. 유용 갓..
ㅣ1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print ([v for v in l1 if v>4])
timesten=dict([(v, v*10) for v in l1]) # dict로 나온다 숫자도 dict((i,v))

# gcd 
def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

import functools
partial(func, value)

def curry(func):
    f_args = []
    f_kwargs = {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            return func(*f_args, *f_kwargs)
    return f

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
# setup_list to initial value :: [number: number] -> [[index, value]] -> [inited number: number]
def setup_list(*args):
    ret = args[0]
    for i,v in args[1]:
        args[0][i] = v

# 하나의 값만 제거 0부터시작
# remove_list_one_eliment :: [] ->rmidx: number -> []
def remove_list_one_eliment(arr, rmidx):
    if 0 > rmidx and len(arr) <= rmidx:
        raise ValueError + this.__name__
    return arr[:rmidx] + arr[rmidx+1:]

# 함수형언어에 맞지않지만 스스로에게 하는게 편할때가있다
# list -> list
def foreach(func, lis):
    for i, v in enumerate(lis):
        lis[i] = func(v)

# 에라토스테네스의 채 to:number -> [factor:number]
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

    return ret


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
