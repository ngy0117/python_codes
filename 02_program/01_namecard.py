# 명함관리 프로그램
# 기능(입력,수정,삭제,목록,검색,종료,저장)
# 데이터구조(이름,주소,전화번호,이메일)- 리스트
# 데이타는 이름을 키값으로 
# 중복된 이름은 입력 안됨.

import json

open('02_program/namecard.json','w')

card = [['홍길동','세종','010-111-2222','hong@gmail.com'],
        ['김태우','세종','010-2222-3333','kim@gmail.com']]

with open('02_program/namecard.json', 'r') as f:
   card = json.load(f)

while True:
    menu = input('이름 >>> ')
    check = 0
    for item in card:
       if item[0] == name:
          check = 1
    if check == 0:
       break
    print('중복된 이름이 있습니다.')
address = input('주소 >>> ')
-------------------------------------------------------
  1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
-------------------------------------------------------
 >>> ''')
    if menu == '1':
        pass
    elif menu == '2':
        name = input('수정할 이름 >>> ')
        for in card:
    elif menu == '3':
        name = input('삭제할 이름 >>> ')
        delok = 0
        for index,item in enumerate(card):
        if item[0] == name:
            print(item, '삭제~')
            del card[index]
            delok = 1
            break
        if delok
    elif menu == '4':
        for index , item in enumerate(card):  
            print(f'''
    {index+1}번째
--------------------------------
    이    름 : {item[0]}
    주    소 : {item[1]}
    전화번호 : {item[2]}
    이 메 일 : {item[3]}''')

    elif menu == '5':
            break
    if idx == -1:
    print('등록되지 않은 데이터입니다.')
    elif menu == '6':
        with open('02_program/namecard.json','w') as f:
            json.dump(card.f)
    elif menu == '7':
        print('프로그램 종료!')
        break
    else:
        print('메뉴선택이 잘못되었습니다.')