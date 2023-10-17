import json

# 데이터를 초기화합니다.
try:
    with open('02_program/namecard1.json', 'r') as f:
        card = json.load(f)
except FileNotFoundError:
    card = [{'name': '홍길동', 'address': '세종', 'tel': '010-111-2222', 'email': 'hong@gmail.com'},
            {'name': '김태우', 'address': '세종', 'tel': '010-2222-3333', 'email': 'kim@gmail.com'}]

while True:
    print('''
    1. 입력  2. 수정  3. 삭제  4. 목록  5. 검색  6. 저장  7. 종료
    ''')
    menu = input('메뉴를 선택하세요 >>> ')

    if menu == '1':
        # 입력 기능 추가
        name = input('이름 >>> ')
        check = 0

        for item in card:
            if item['name'] == name:
                check = 1

        if check == 0:
            new_card = {'name': name}
            new_card['address'] = input('주소 >>> ')
            new_card['tel'] = input('전화번호 >>> ')
            new_card['email'] = input('이메일 >>> ')

            card.append(new_card)
            print('명함이 추가되었습니다.')
        else:
            print('중복된 이름이 있습니다.')

    elif menu == '2':
        # 수정 기능 추가
        name_to_modify = input('수정할 이름 >>> ')
        for item in card:
            if item['name'] == name_to_modify:
                item['address'] = input('수정할 주소 >>> ')
                item['tel'] = input('수정할 전화번호 >>> ')
                item['email'] = input('수정할 이메일 >>> ')
                print('명함이 수정되었습니다.')
                break
        else:
            print('등록되지 않은 데이터입니다.')

    elif menu == '3':
        # 삭제 기능 추가
        name_to_delete = input('삭제할 이름 >>> ')
        for item in card:
            if item['name'] == name_to_delete:
                card.remove(item)
                print(f'{name_to_delete} 명함이 삭제되었습니다.')
                break
        else:
            print('등록되지 않은 데이터입니다.')

    elif menu == '4':
        # 목록 표시 기능 추가
        for index, item in enumerate(card):
            print(f'''
        {index + 1}번째
        --------------------------------
        이    름 : {item['name']}
        주    소 : {item['address']}
        전화번호 : {item['tel']}
        이 메 일 : {item['email']}''')

    elif menu == '5':
        # 검색 기능 추가
        name_to_search = input('검색할 이름 >>> ')
        found = False
        for index, item in enumerate(card):
            if item['name'] == name_to_search:
                print(f'''
        {index + 1}번째
        --------------------------------
        이    름 : {item['name']}
        주    소 : {item['address']}
        전화번호 : {item['tel']}
        이 메 일 : {item['email']}''')
                found = True
                break
        if not found:
            print('검색 결과가 없습니다.')

    elif menu == '6':
        # 저장 기능 추가
        with open('02_program/namecard1.json', 'w') as f:
            json.dump(card, f)
        print('데이터가 저장되었습니다.')

    elif menu == '7':
        # 종료 기능 추가
        with open('02_program/namecard1.json', 'w') as f:
            json.dump(card, f)
        print('프로그램 종료!')
        break

    else:
        print('메뉴 선택이 잘못되었습니다.')

# GITHUB TEST