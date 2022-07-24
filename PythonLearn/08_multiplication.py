num = int(input("Enter the number of multiplication tables to create starting from 2: "))
num +=1
for i in range(2,num):
    with open (f'08_multiplication/Multiplication_table_of_{i}.txt','w') as f:
        for j in range (1,11):
            f.write (f'{i}X{j}={i*j}')
            if j!=10:
                f.write('\n')
