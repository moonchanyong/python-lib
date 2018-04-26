# 줄서는 방법
import math
def find_stage(arr, k):
    if k == 1:
        return arr
    unit = math.factorial(len(arr)-1)
    gun = int((k-1) / unit)
    # arr[(k-1) / math.factorial(len(arr)-1)] 이거 제거
    ret = arr[gun]
    newthing = remove_list_one_eliment(arr, gun)
    # 제거 후 나머지 만큼 arr, 나머지
    return [ret] + find_stage(newthing, k - gun * unit)

# 군수열 문제
def setAlign(n, k):
    answer = find_stage(list(range(1,n+1)), k)
    return answer

def remove_list_one_eliment(arr, rmidx):
    return arr[:rmidx] + arr[rmidx+1:]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(setAlign(3, 5))
