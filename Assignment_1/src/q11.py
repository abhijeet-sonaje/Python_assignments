no = int(input('Enter number till you want to display Fibonacci series: '))

i=1
j=1
print (i)
print (j)
while True:
    temp = i
    i=j
    j= temp + j
    if(j>=no):
        break;
    print(j)
    
    
