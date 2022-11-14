"Вариант 3. Часть 1"
from random import *

n=int(input("Укажите длину массива: "))
D=[]

print("Укажите эл-ты массива:")
for i in range(n):
    D.append(int(input()))
print (D)

summ=0;
for i in range(n):
    if i%2==0:
        summ=summ+D[i]
print("Сумма эл-ов с нечет. индексами: ", summ)


"Вариант 3. Часть 2"
A=[randint(-10, 30) for i in range (8)]
print("Исходный массив:\n",A)

for i in range (8):
    if A[i]<15:
        A[i]=A[i]**2
print("Преобразованный массив\n",A)