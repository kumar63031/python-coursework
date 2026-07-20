


n = int(input())
m = n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*",end=' ')
    else:
        for j in range(n-i):
            print("*",end = ' ')
    print()

    
'''
# another
n = int(input())
m = n//2
for i in range(n):
    if i<=m:
        print("  "*(m-i),end=' ')
        print("* "*(i+1),end=' ')
    else:
        print("  "*(i-m),end=' ')
        print("* " *(n-i),end = ' ')
    print()



n = int(input("Enter the size :"))
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or i == n//2 or j == 0 or j == n-1 or j == n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size :"))
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or j == 0 or j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
             
            


n = int(input("Enter the size :"))
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or j == 0 or j == n-1 or j == i or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




n = int(input("Enter the size :"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j == 0  or i == n-1 or j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''


















