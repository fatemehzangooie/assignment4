numbers=[]
sort=True
sortnumber=int(input('the marked number to sort: '))
for i in range(0,sortnumber):
    num=int(input('number= '))
    numbers.append(num)
for number in range(1,sortnumber):
    if numbers[number-1]<numbers[number] or numbers[-number]<numbers[-number-1]:
        sort=True
    else:
        sort=False
        break
    if sort==True:
        print('yes.')
    else:
        print('not yet!')    
            