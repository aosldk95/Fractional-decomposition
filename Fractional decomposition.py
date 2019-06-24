#13195의 소인수는 5, 7, 13, 29 입니다.
#600851475143 의 최대 소인수는 무엇입니까?
number = 600851475143
numberlist = []
i = 2
while i < number+1 :
    if (number % i) == 0 :
        numberlist.append(i)
        number /= i
        i = 2
    else :
        i += 1   
print(max(numberlist))
            
