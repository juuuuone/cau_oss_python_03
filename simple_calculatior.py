def arithmetic_ops(op):
    x=int(input("첫 번째 숫자를 입력하세요 : "))
    y = int(input("두 번째 숫자를 입력하세요 : "))
    return x, y,op(x,y)


def plus(x,y): #더하기함수
    return x+y


def minus(x,y):
    return x-y



while True :
    op=input("연산자를 입력하세요 : ")

    if op=="end" :
        break

    elif op=="+" :
        x,y,res=arithmetic_ops(plus)

    elif op=="-" :
        x,y,res=arithmetic_ops(minus)

    elif op=="*" :
        x,y,res= arithmetic_ops(lambda x,y:x*y)

    elif op=="/" :
        x,y,res = arithmetic_ops(lambda x,y:x/y)

    elif op == "%" :
        x,y,res = arithmetic_ops(lambda x,y:x%y)



    else :
        print("Invalid operation")
        continue

    print(f"{x}{op}{y}={res}")



print("프로그램을 종료합니다")
