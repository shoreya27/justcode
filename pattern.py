#1 ≤  T ≤ 100
#1 ≤  N ≤ 30

t_case=int(input("TestCases: "))

#Taking list of no_of_lines
no_of_lines=[]
for i in range(0,t_case):
    no_of_lines.append(int(input("Enter value: ")))

print(no_of_lines)

#for each case (test_cases) present in list
for case in no_of_lines:
    for i in range(1,case+1):
        for k in range(0,i):
            print('*',end='')
        for j in range(1,2*(case-i)+1):
            print('#',end='')
        for k in range(0,i):
            print('*',end='')
        print()
