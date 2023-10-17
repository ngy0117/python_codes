'''
반장 선거 프로그램을 파이썬 코드로 작성하려고 한다.
1. 후보자는 n명이고 유권자는 1에서 n까지 원하는 사람의 숫자를 적어서 제출한다.
2. 프로그램에서 input으로 1에서 n까지의 숫자를
순서에 상관없이 공백을 구분자로 나누어 받고 조건에 맞추어 출력한다.
3. 입력예시 : 1 2 3 5 3 4 2 1 2
4. 출력예시 :
기호 : 1 득표수 : 2
기호 : 2 득표수 : 3
기호 : 3 득표수 : 2
기호 : 4 득표수 : 1
기호 : 5 득표수 : 1
5. 각 값들을 입력받고 다음과 같은 코드를 작성한다.
- 공백을 구분자로 하여 입력받은 후보자 번호를 분리하는 함수
- 숫자로 변경된 값들을 항목별로 갯수를 카운트 하는 함수
- 결과값을 출력하는 함수
'''
def str2int(votes):
    # result = votes.split()
    # for index,item in enumerate(result):
    #     result[index] = int(item)
    return list(map(int,votes.split()))

def countvotes(votes):
    n = max(votes)
    print('가장큰값:',n)
    # result=[]
    # for i in range(n):
    #     result.append(0)
    result = [0 for i in range(n)]
    print(result)
    for item in votes:
        result[item-1] += 1
    return result

def printresult(votes):\
    for index,item in enumerate(votes):
        print(f'기호 : { index+1 :2} 득표수 : {item}')


votes = input('투표데이터 >>> ')
print(votes)
print(type(votes))
result = str2int(votes)
print(result)
print(type(result))