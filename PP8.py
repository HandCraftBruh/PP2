import random

#Вариант 3
#   Задание 1
#n=3
n=int(input('Указать кол-во строк и столбцов: '))

A=[[random.randrange(9) for i in range(n)] for j in range(n)]
for row in A:
    print(*map('{:2d}'.format, row))
print()

print ('Вывод:')
flag=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if A[i][j]!=A[j][i]:
            flag=1
            break
if flag!=1:
    print('Матрица симметрична\n')
else:
    print('Обычная матрица\n')


#   Задание 2
N = int(input('Указать кол-во строк: '))
M = int(input('Указать кол-во столбцов: '))

B = [[random.randrange(-9,9) for i in range(M)] for j in range(N)]
for row in B:
    print(*map('{:2d}'.format, row))
print()

max_x = B[0][0]
ix = jx = 0
for i in range(len(B)):
    for j in range(len(B[0])):
        if B[i][j] > max_x:
            max_x = B[i][j]
            ix = i 
            jx = j 
B[0], B[ix] = B[ix], B[0]
B[0][0], B[0][jx] = B[0][jx], B[0][0]
for row in B:
    print(*map('{:2d}'.format, row))