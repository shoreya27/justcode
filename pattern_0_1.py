num=int(input("Enter value: "))
#for loop
c=0
for i in range(1,num+1):

    if i%2!=0:

        a=1
        b=0
        for j in range(1,i+1):
            print(a,end=' ')
            c=a
            a=b
            b=c

    else:

        a=0
        b=1
        for j in range(1,i+1):
            print(a,end=' ')
            c=a
            a=b
            b=c

    print()
