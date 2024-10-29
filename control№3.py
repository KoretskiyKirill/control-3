#Кирилл Корецкий уровень C
#1
import random
def odd():
    suma = 0
    global lst
    lst = [random.randint(1,100) for i in range(random.randint(1,10))]
    print(lst)
    for i in range(0, len(lst)-1):
        if lst[i] % 2 != 0:
            suma = suma + lst[i]
            lst.pop(i)
            lst.insert(i, suma)

    lst.append(suma)
    print(lst)
odd()
#я сделал так, потому что по другому не смог
#2
triangl = 0
for i in range(3):
    def cord(x1, y1, x2, y2):

        return (abs(x1 - x2)**2 + abs(y1 - y2)**2)** 0.5
    triangl = triangl + cord(int(input()),int(input()),int(input()),int(input()))
print(triangl)

num = int(input())
lst = 1
result = ""
def check(num, lst):
    global result
    if lst > num:
        result = "NO"
    else:
        if lst == num:
            result = "YES"
        else:
            lst *= 2
            check(num, lst)
check(num, lst)
print(result)
