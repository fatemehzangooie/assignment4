number=int(input('enter your number: '))
sum=1
counter=1

while number>sum:
    sum*=counter
    counter+=1
    
    counter-=1
    
    if sum==number:
        print('number',number,'factorial of number',counter)
        
    else:
        print('adad',number,'wrong')
        