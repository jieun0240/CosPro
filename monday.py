score = [2024, 7, 22, 3, 4]

# print(sum_list(score))
def sum_list(score):
    total = 0
    for i in score:
        total += i
    return total
print(sum_list(score))

# print(max_list(score))
def max_list(score):
    max_ = score[0]
    for i in score:
        if i > max_:
            max_ = i
    return max_
print(max_list(score))

# print(min_list(score))
def min_list(score):
    min_ = score[0]
    for i in score:
        if i < min_:
            min_ = i
    return min_
print(min_list(score))

# print(average_list(score))
def average_list(score):
    average = sum(score)/len(score)
    return average
print(average_list(score))

# print(count_odd(scores))
def count_odd(score):
    count = 0
    for i in score:
        if i%2 == 1:
            count+=1
    return count
print(count_odd(score))

# print(make_list(6))
def make_list(num):
    lists = []  # 빈 리스트 만들고
    for i in range(0, num):
        lists.append(0) # num만큼 숫자 넣기
    return lists
print(make_list(6))