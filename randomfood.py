import os

# Define the file paths for each cuisine category
file_paths = {
    '한식': 'korean_menu.txt',
    '중식': 'chinese_menu.txt',
    '일식': 'japanese_menu.txt',
    '양식': 'western_menu.txt',
}

# Function to load menu items from a file
def load_menu(category):
    menu = []
    file_path = file_paths.get(category)
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            menu = file.read().splitlines()
    return menu

# Function to save menu items to a file
def save_menu(category, menu):
    file_path = file_paths.get(category)
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(menu))

while True:
    print("1. 메뉴 추천, 2. 메뉴 추가, 3. 메뉴 삭제, 4. 종료하기")
    choice = input("숫자를 입력하세요: ")

    if choice == "1":
        menu_category = input("한식, 중식, 일식, 양식 중 원하는 카테고리를 고르세요: ")
        menu = load_menu(menu_category)
        if menu:
            print(menu)
        else:
            print("메뉴가 없습니다.")
    
    elif choice == "2":
        menu_category = input("한식, 중식, 일식, 양식 중 추가를 원하는 카테고리를 고르세요: ")
        menu = load_menu(menu_category)
        if menu:
            menu_item = input(f"{menu_category}에 추가하고 싶은 메뉴를 입력하세요: ")
            menu.append(menu_item)
            save_menu(menu_category, menu)
            print(f"{menu_item}이(가) 추가되었습니다.")
        else:
            print("메뉴가 없습니다.")
    
    elif choice == "3":
        menu_category = input("한식, 중식, 일식, 양식 중 삭제를 원하는 카테고리를 고르세요: ")
        menu = load_menu(menu_category)
        if menu:
            print(menu)
            menu_item = input(f"{menu_category}에서 제거하고 싶은 메뉴를 입력하세요: ")
            if menu_item in menu:
                menu.remove(menu_item)
                save_menu(menu_category, menu)
                print(f"{menu_item}이(가) 제거되었습니다.")
            else:
                print(f"{menu_item}이(가) 메뉴에 없습니다.")
        else:
            print("메뉴가 없습니다.")
    
    elif choice == "4":
        break