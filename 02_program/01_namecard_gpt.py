import json

# 파일을 열고 읽어서 데이터를 초기화합니다.
try:
    with open('02_program/namecard.json', 'r') as f:
        card = json.load(f)
except FileNotFoundError:
    card = [['홍길동', '세종', '010-111-2222', 'hong@gmail.com'],
            ['김태우', '세종', '010-2222-3333', 'kim@gmail.com']]

while True:
    # 메뉴 표시
    print('''
    1. 입력  2. 수정  3. 삭제  4. 목록  5. 검색  6. 저장  7. 종료
    ''')
    menu = input('메뉴를 선택하세요 >>> ')

    if menu == '1':
        # 입력 기능 추가
        name = input('이름 >>> ')
        check = 0

        for item in card:
            if item[0] == name:
                check = 1

        if check == 0:
            address = input('주소 >>> ')
            new_card = [name, address]
            phone = input('전화번호 >>> ')
            email = input('이메일 >>> ')

            new_card.extend([phone, email])
            card.append(new_card)
            print('명함이 추가되었습니다.')
        else:
            print('중복된 이름이 있습니다.')

    elif menu == '2':
        # 수정 기능 추가
        name_to_modify = input('수정할 이름 >>> ')
        for item in card:
            if item[0] == name_to_modify:
                new_address = input('수정할 주소 >>> ')
                new_phone = input('수정할 전화번호 >>> ')
                new_email = input('수정할 이메일 >>> ')
                item[1] = new_address
                item[2] = new_phone
                item[3] = new_email
                print('명함이 수정되었습니다.')

    elif menu == '3':
        # 삭제 기능 추가
        name_to_delete = input('삭제할 이름 >>> ')
        for item in card:
            if item[0] == name_to_delete:
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
        이    름 : {item[0]}
        주    소 : {item[1]}
        전화번호 : {item[2]}
        이 메 일 : {item[3]}''')

    elif menu == '5':
        # 검색 기능 추가
        name_to_search = input('검색할 이름 >>> ')
        for index, item in enumerate(card):
            if item[0] == name_to_search:
                print(f'''
        {index + 1}번째
        --------------------------------
        이    름 : {item[0]}
        주    소 : {item[1]}
        전화번호 : {item[2]}
        이 메 일 : {item[3]}''')
                break
        else:
            print('검색 결과가 없습니다.')

    elif menu == '6':
        # 저장 기능 추가
        with open('02_program/namecard.json', 'w') as f:
            json.dump(card, f)
        print('데이터가 저장되었습니다.')

    elif menu == '7':
        # 종료 기능 추가
        print('프로그램 종료!')
        break

    else:
        print('메뉴 선택이 잘못되었습니다.')
