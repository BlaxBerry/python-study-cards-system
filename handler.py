card_list = []


def show_main_menu():
    """显示菜单"""

    print("*" * 50)
    print("1. 新增名片".center(50))
    print("2. 显示全部".center(50))
    print("2. 搜索名片".center(50))
    print("0. 退出系统".center(50))
    print("*" * 50)


def add_card():
    """"新增名片"""

    print("\n")
    user_name = input("1. 请输入姓名: ")
    user_age = input("2. 请输入年龄: ")
    user_phone = input("3. 请输入电话: ")
    user = {
        "name": user_name,
        "age": user_age,
        "phone": user_phone
    }
    card_list.append(user)
    print("\n")
    print("名片添加成功")


def show_all_cards():
    """"显示所有名片"""

    print("\n")

    for key in ["姓名", "年龄", "电话"]:
        print(key, end="\t\t")

    print("\n")
    print("-" * 50)

    for user in card_list:
        print(f"{user['name']}\t\t{user['age']}\t\t{user['phone']}")


def search_card():
    """"搜索名片"""
    # TODO
    print("\n")
    print("搜索名片")


def delete_card():
    """"删除名片"""
    # TODO
    print("\n")
    print("删除名片")


def edit_card():
    """"编辑名片"""
    # TODO
    print("\n")
    print("编辑名片")


def not_exist():
    """选项不存在"""
    # TODO
    print("\n")
    print("输入错误, 重新选择")


def cancel_system():
    """退出系统"""
    # TODO
    print("\n")
    print("谢谢使用, 再见".center(50))
    print("\n")
