scores = [27, 17, 7, 21, 30, 3, 45, 5, 53, 1001, 26, 62, 559]

#합계
#1
def sum_list(scores):
    sum_ = 0
    for score in scores:    # 값 빼오기
        sum_ += score
    return sum_
def sum_list2(scores):
    sum_ = 0
    for i in range(len(scores)):    # len을 통해 덩어리 만들기..... 참고// index 꺼내오기!
        sum_ += scores[i]
    return sum_
def sum_list3(scores):
    return sum(scores)

print(sum_list(scores))
print(sum_list2(scores))
print(sum_list3(scores))
print('--'*10)

#최대값
#1
def max_list(scores):
    max_ = scores[0]
    for score in scores:
        if score > max_:
            max_ = score
    return max_

#2
def max_list2(scores):
    max_ = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_:
            max_ = scores[i]
    return max_

#3
def max_list3(scores):
    return max(scores)

print(max_list(scores))
print(max_list2(scores))
print(max_list3(scores))
print('--'*10)

#최소값
#1
def min_list(scores):
    min_ = scores[0]
    for score in scores:
        if score < min_:
            min_ = score
    return min_
#2
def min_list2(scores):
    min_ = scores[0]
    for i in range(1, len(scores)):
        if scores[i] < min_:
            min_ = scores[i]
    return min_
#3
def min_list3(scores):
    return min(scores)

print(min_list(scores))
print(min_list2(scores))
print(min_list3(scores))
print('--'*10)

#평균
#1
def average_list(scores):
    sum_ = 0
    count = 0
    for score in scores:
        sum_ += score
        count += 1
    return sum_ / count
#2
def average_list2(scores):
    sum_ = 0
    count = 0
    for i in range(len(scores)):
        sum_ += scores[i]
        count += 1
    return sum_ / count
#3
def average_list3(scores):
    return sum(scores) / len(scores)

print(average_list(scores))
print(average_list2(scores))
print(average_list3(scores))
print('--'*10)

#홀수
#1
def count_odd(scores):
    count = 0
    for score in scores:
        if score % 2 == 1:
            count += 1
    return count
#2
def count_odd2(scores):
    count = 0
    for i in range(len(scores)):
        if scores[i] % 2 != 0:
            count += 1
    return count
#3
def count_odd3(scores):
    odd_list = [score for score in scores if score % 2 == 1]    #odd_lsit에 홀수 삽입
    return len(odd_list)

print(count_odd(scores))
print(count_odd2(scores))
print(count_odd3(scores))
print('--'*10)

#리스트 만들기
#1
def make_list(scores):
    list_ = []
    for _ in scores:
        list_.append(0)
    return list_
#2
def make_list2(scores):
    list_ = []
    for i in range(len(scores)):
        list_.append(0)
    return list_
#3
def make_list3(scores):
    zero_list = [0 for _ in scores]
    return zero_list
def make_list4(scores):
    return [0] * len(scores)    # 간단하다...

print(make_list(scores))
print(make_list2(scores))
print(make_list3(scores))
print(make_list4(scores))
print('--'*10)