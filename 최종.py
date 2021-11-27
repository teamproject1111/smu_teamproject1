import sys

def fun1():
    print(' => 폭탄 피하기 게임 시작 \n')

def fun2():
    print(' => 블록 깨기 게임 시작 \n') 

def fun3():
    print(' => 행맨 게임 시작 \n')

def fun4():
    print(' => 게임 종료 \n')

while True:
    print('1. 폭탄 피하기')
    print('2. 블록 깨기')
    print('3. 행맨')
    print('4. 게임 종료')
    num = int(input('선택 : '))

    if num == 4:
        print('프로그램 종료')
        sys.exit()
    elif num == 1:
        fun1()
        from bomb_game import *
    elif num == 2:
        fun2()
        from block2 import *
    elif num == 3:
        fun3()
        from hangman import *
    else:
        print('{}는 없는 번호'.format(num))
        
        
        

