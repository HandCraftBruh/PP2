import math

def sub (cat_A, cat_B):
    sub=math.sqrt(pow(cat_A,2)+pow(cat_B,2))
    return sub

M=[]
for i in range(2):
    print("\nВведите катеты",i+1,"треугольника")
    cat_A=int(input("Первый катет: "))
    cat_B=int(input("Второй катет: "))
    M.append(sub(cat_A, cat_B))
    
print('\n')
    
for i in range(2):
    print("Гипотенуза",i+1,"треугольника: {:.2f}".format(M[i]))

if M[0]>M[1]:
    print ("Гипотенуза первого треугольника больше")
elif M[0]<M[1]:
    print ("Гипотенуза второго треугольника больше")
else:
    print ("Гипотенузы треугольников равны")
    