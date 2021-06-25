#21800487 윤사무엘 <pa01>

data = [int(x) for x in input().split()] # get input data

for i in range(len(data)):
    digit=[int(n) for n in str(data[i])] # ex) '1399' -> [ 1, 3, 9, 9 ]
    for j in range(len(digit)):
        if digit[j] > 4: digit[j]=digit[j]-1 # if (digit>4) -> digit-=1
    data[i]="".join(list(map(str,digit)))

for i in data:
    print(int(i,9), end=' ') # convert number to decimal number & Output
