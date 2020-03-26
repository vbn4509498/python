# import math
# x = 6
# print(6/2*6/2*3.14)
# x = (10+30+40+90+100+61)/6
# print(round(x,3))
# score = 70
# if score >= 60:
#     print("及格!!!!")
#     if score>=90 :
#         print("你最棒")
#     else:
#         print("還好還好")
# elif 55<=score<60:
#     print('教授拜託給我過')
# elif 50<= score <=54:
#     print("快過了")
# else:
#     print("不及格><")
# print("Hello world","world","!")
# print("Hello")
# print("123",end=" ")
# print("456")
# mathscores = [60,70,10,20,81,63,4]
# family = {
#     "dad" : "Homer",
#     "mom" : "Marge",
#     "son" : "Bart",
#     "daughter": "Lisa",
# }
# for member in family.items():
#     print(member)
# for key , value in family.items():
#     print(f"my {key} is {value}")
# for i in mathscores:
#     print(i**0.5*10)
# [print(i) for i in range(10)]
# for i in range(10):
#     print(i)
# [print(math.sqrt(x)*10) for x in mathscores]
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("loop end")
# for score in mathscores:
#     if score > 80:
#         continue
#     print(score)
# import random
# i = random.randint(1,50)
# print(i)
# x = eval(input("HOW MANY ROWS:"))
# print(x+10)
# x=1
# y=1
# c=0
# b=1
# a=1
# for a in range (1,10):
#     y=1
#     for b in range (1,10):
#         c = x*y
#         print(f" {x}*{y} is {c}")
#         y = y + 1
#     x = x +1
# d=1
# while d <=50 :
#     print("你好")
#     d+=1
# else:
#     print("我說完了啦")
# z = eval(input("輸入一整數:"))
# e = 1
# for e in range (z+1):
#     if e%2 == 1 :
#         print(e)
# import random
# # rows = random.randint(1,100)
# # columns = random.randint(1,100)
# # x=[[1,2,3,4],[4,5,6,4],[1,2,3,4]]
# # for i in range(0,3):
# #     for j in range(0,4):
# #         rows = random.randint(1, 100)
# #         columns = random.randint(1, 100)
# #         x[i][j]=rows *columns
# #     j=j+1
# # i=i+1
# # for y in (i):
# #     for z in (j):
# #         print(f"x[y][z]",end=" ")
# #     print()

# weight =100
# weight1 = 80
# def add_weight (w1,w2):
#     result = w1 +w2
#     return  result
# x = add_weight(weight,weight1)
# print(x)
import vending_machine.vending_service as machine
flag = True
while flag:
    print("\n===============1==============")
    select = eval(input("1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:"))
    if select == 1:
        machine.deposit()
    elif select == 2:
      machine.buy()
    elif select == 3:
        print(f'目前餘額為 {machine.balance}元')
    elif select == 4:
        print("bye")
        flag = False
        break
    else:
        print("====請輸入1-4之間")
        continue
# def calculate (x,y):
#     return x+y , x-y , x*y  , x/y
# num = 2
# num1 = 5
# result = calculate(num,num1)
# print(result)
#
# r1,r2,r3,r4 = calculate(num,num1)
# print(r1,r2,r3,r4)
