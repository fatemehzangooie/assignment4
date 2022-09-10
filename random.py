import random
list=int(input('enter your list= '))
num1_list=[]
for i in range(list):
    num=random.randint(0,99)
    num1_list.append(num)
    print('your list: ',num1_list)