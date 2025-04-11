
flag = True
while flag:
    print('--- Student Management Menu ---')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    a = int(input('Enter your choice (1-4): '))
    if a == 1:
        print('a')
    elif a == 2:
        print('b')
    elif a == 3:
        b = input('Enter Student ID to Drop: ')
        print(b) 
    elif a == 4:
        flag= False