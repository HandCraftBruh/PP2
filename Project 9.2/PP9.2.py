
#   Задание 2
B=[]
f_Input=open('Kustov_Um-222_vvod.txt', 'r', encoding='utf-8-sig')

for line in f_Input:
    B.append([int(n) for n in liner.split()])

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

f_Output=open('Kustov_Um-222_vivod.txt','w+', encoding='utf-8-sig')
for row in B:
	print(*map('{:2d}'.format, row))
for row in B:	
	f_Output.write(' '.join(map(str, row))+'\n')