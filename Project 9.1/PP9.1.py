import random

#   Задание 1

A=[]
f_Input=open('Kustov_Um-222_vvod.txt', 'r', encoding='utf-8-sig')

for str in f_Input:
    A.append([int(n) for n in str.split()])
for row in A:
    print(*map('{:2d}'.format, row))
print()

f_Output=open('Kustov_Um-222_vivod.txt','w+', encoding='utf-8-sig')
print ('Вывод:')
f_Output.write('Вывод:\n')

flag=0
for i in range(0,len(A)-1):
    for j in range(i+1,len(A)):
        if A[i][j]!=A[j][i]:
            flag=1
            break
if flag!=1:
    print('Матрица симметрична\n')
    f_Output.write('Матрица симметрична')
else:
    print('Обычная матрица\n')
    f_Output.write('Обычная матрица')

f_Output.close()
f_Input.close()

