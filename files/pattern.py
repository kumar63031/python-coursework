'''
n = int(input())
for row in range(n):
    for col in range(n):
        print(col%2,end='')
    print()



n = int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()


n = int(input())
for row in range(n):
    for col in range(n-row):
        print('*',end='')
    print()


n = int(input())
for i in range(n):
    for sp in range(n-1-i):
        print(' ',end = ' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

    


n = int(input())
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()




n = int(input())
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()




n = int(input())
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()
   
    

'''





