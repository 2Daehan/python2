한식 = ['김치볶음밥', '비빔밥', '제육볶음', '청국장', '김치찌개', '된장찌개']
중식 = ['짜장면', '짬뽕', '간짜장', '우동', '잡채밥', '짜장밥', '탕수육']
일식 = ['초밥', '라멘', '돈카츠', '모밀','덮밥',]
양식 = ['피자', '햄버거', '치킨', '파스타', '스테이크', '샌드위치']

while True:
    print("1.메뉴추천, 2.메뉴 첨삭,3.종료하기. 숫자를 입력해주세요: ")
    foodinput = input()
    if foodinput == "1":  
      menu = input("한식, 중식, 일식, 양식 중 원하는 카테고리를 고르세요: ")
    
      if menu == '한식':
         print(한식)
      elif menu == '중식':
         print(중식)
      elif menu == '일식':
            print(일식)
      elif menu == '양식':
            print(양식)
      else:
            print("넌 그냥 처먹지마라")
    elif foodinput == "2":
      while True:
       print("1.메뉴 추가, 2.메뉴 삭제:")
       corinput = input()
       if corinput == "1":
            listinput = input("한식, 중식, 일식, 양식 중 추가를 원하는 카테고리를 고르세요:")
      
            if listinput == '한식':
                  한식추가=input('한식에서 추가하고 싶은 메뉴를 입력하세요: ')
                  한식.append(한식추가)
                  print(한식)
            elif listinput == '중식':
                  중식추가=input('중식에서 추가하고 싶은 메뉴를 입력하세요: ')
                  중식.append(중식추가)
                  print(중식)
            elif listinput == '일식':
                  일식추가=input('일식에서 추가하고 싶은 메뉴를 입력하세요: ')
                  일식.append(일식추가)
                  print(일식)
            elif listinput == '양식':
                  양식추가=input('양식에서 추가하고 싶은 메뉴를 입력하세요: ')
                  양식.append(양식추가)
                  print(양식)
            break
       elif corinput == "2":
            delistinput = input("한식, 중식, 일식, 양식 중 삭제를 원하는 카테고리를 고르세요:")
            
            if delistinput == '한식':
                  print(한식)
                  한식제거=input('한식에서 제거하고 싶은 메뉴를 입력하세요:')
                  한식.remove(한식제거)
                  print(한식)
            elif delistinput == '중식':
                  print(중식)
                  중식제거=input('중식에서 제거하고 싶은 메뉴를 입력하세요:')
                  중식.remove(중식제거)
                  print(중식)
            elif delistinput == '일식':
                  print(일식)
                  일식제거=input('일식에서 제거하고 싶은 메뉴를 입력하세요:')
                  일식.remove(일식제거)
                  print(일식)
            elif delistinput == '양식':
                  print(양식)
                  양식제거=input('양식에서 제거하고 싶은 메뉴를 입력하세요:')
                  양식.remove(양식제거)
                  print(양식)
            break
    elif foodinput == "3":
            break