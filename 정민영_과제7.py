import random


def RSP(user):
    com = random.choice(['가위', '바위', '보'])

    if(user == '가위'):
        if(com == '가위'):
            print('컴퓨터>>가위 \n 무승부')
        elif(com == '바위'):
            print('컴퓨터>>바위 \n 컴퓨터 승')
        elif(com == '보'):
            print('컴퓨터>>보 \n 사용자 승')
    elif(user == '바위'):
        if(com == '가위'):
            print('컴퓨터>>가위 \n 사용자 승')
        elif(com == '바위'):
            print('컴퓨터>>바위 \n 무승부')
        elif(com == '보'):
            print('컴퓨터>>보 \n 컴퓨터 승')
    elif(user == '보'):
        if(com == '가위'):
            print('컴퓨터>>가위 \n 컴퓨터 승')
        elif(com == '바위'):
            print('컴퓨터>>바위 \n 사용자 승')
        elif(com == '보'):
            print('컴퓨터>>보 \n 무승부')
    else:
        print('가위 바위 보 중에 입력해주세요!')


user = input("사용자>>")
RSP(user)
