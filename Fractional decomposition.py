#13195의 소인수는 5, 7, 13, 29 입니다.
#600851475143 의 최대 소인수는 무엇입니까?
number = 600851475143
numberlist = []
for i in range(2,number) :
    if (number % i) == 0 :
        numberlist.append(i)
        print(numberlist)
for i in numberlist :
    for j in range(2,i):
        if (i % j) == 0 :
            print(1)
            numberlist[numberlist.index(i)] = 0
            break
print(max(numberlist))
            
