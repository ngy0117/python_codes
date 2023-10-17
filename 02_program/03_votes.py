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

input_str = input("투표 결과를 입력하세요: ") #입력창

def str2int(vote_str): #문자열을 정수화하고 리스트로
    votes = vote_str.split()
    votes = [int(vote) for vote in votes]
    return votes

def countvotes(votes): #번호를 카운트해서 딕셔너리로
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    return vote_count

def printresult(vote_count): # 결과 출력
    for candidate, count in vote_count.items():
        print(f"기호 : {candidate} 득표수 : {count}")

votes = str2int(input_str)
vote_count = countvotes(votes)
printresult(vote_count)
