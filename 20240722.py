print("hello world")
print("Q1================================================================================================")

name = "나지은"
age = 18
print(f"안녕 나는 {name}이야, 나이는 {age} 살이야.")
print("Q2================================================================================================")

hotsauce = ['송형주', '김선응']
for i in hotsauce:
    print(i)

for i in range(0, len(hotsauce)):   #range( 시작 점, 끝 점, 규칙(예를 들면 i++) / len은 length
    print(hotsauce[i])  # 이 모양도 많이 사용함
print("Q3================================================================================================")

for i in range(2, 9 + 1):   # 2 ~ 9 까지 출력
    for j in range(1, 9 + 1):
        print(f"{i} x {j} = {i * j}")
    print('-' * 10)

print("Q4================================================================================================")
for i in range(2, 9 + 1, 2):    # 2, 4, 6, 8 단만 출력
    for j in range(1, 9 + 1):
        print(f"{i} x {j} = {i * j}")
    print('-' * 10)

print("Q5================================================================================================")
#dictionary 생성
chinese = [{'menu' : '자장면', 'price' : 7000}, {'menu' : '짬뽕', 'price' : 8000}, {'menu' : '양장피', 'price' : 15000}]
#출력
print(chinese)
# 0번째 방 메뉴의 가격 꺼내오기
print(chinese[0]['price'])
# 음식만 꺼내오기
for food in chinese:
    print(food['menu'])
# 가격만 꺼내오기
for c in chinese:
    print(c['price'])

print("Q6================================================================================================")
def get_total_price(dictionary):
    total = 0
    for i in dictionary:
        total += i['price']
    return total
print(f"총 가격 : {get_total_price(chinese)}")