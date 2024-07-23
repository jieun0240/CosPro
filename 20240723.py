def solution(arr, k):
    answer = 0
    for i in arr:
        for j in i:
            print(j, end="\t")  # end 옵션 변경
        print()
    return answer
print("================================================================================================")

def solution(arr, k):
    answer = 0
    list_ = []
    for line in arr:
        for num in line:
            list_.append(num)  # 배열에서 숫자 하나씩 꺼내기
    list_.sort()  # 정렬

    answer = list_[k - 1]  # k번째로 작은 숫자를 반환
    return answer
print("================================================================================================")

month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_month = 1
start_day = 2
end_month = 2
end_day = 2

def func_a(month, day):
    answer = 0
    for i in range(month-1):
        answer += month_list[i]
    answer += day - 1
    return answer

def solution(start_month, start_day, end_month, end_day):
    answer = 0
    long_day = func_a(end_month, end_day)
    short_day = func_a(start_month, start_day)
    answer = long_day - short_day
    return answer

print(solution(start_month, start_day, end_month, end_day))
print("================================================================================================")

numbers = [3, 5, 1, 4, 2, 5, 3, 1, 3, 5, 2, 1, 2, 2]
count_arr = [0 for i in range(5)]

for number in numbers:
    count_arr[number - 1] += 1

max_ = max(count_arr)
min_ = min(count_arr)
print(int(max_ / min_))
print("================================================================================================")

def solution(arr):
    left, right = 0, len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(solution([3, 5, 1, 4, 2, 5, 3, 1, 3, 5, 2, 1, 2, 2]))
print("================================================================================================")

def solution(number):
    cnt = 0

    for num in range(1, number + 1):
        num_str = str(num)
        for s in num_str:
            if s in "369":
                cnt += 1
    return cnt

print(solution(10))
print(solution(20))
print(solution(40))
