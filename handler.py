card_list = []


def show_main_menu():
    """显示操作选项菜单"""

    print("*" * 50)
    print("【1】 新增名片".center(50))
    print("【2】 显示全部".center(50))
    print("【3】 搜索名片".center(50))
    print("【0】 退出系统".center(50))
    print("*" * 50)


def add_card():
    """"新增名片"""

    print("\n")
    user_name = input("1. 请输入姓名: ")
    user_age = input("2. 请输入年龄: ")
    user_phone = input("3. 请输入电话: ")

    if user_name and user_age and user_phone:
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

    if len(card_list) == 0:
        print("还没有名片, 请先增加名片")
        return

    for key in ["姓名", "年龄", "电话"]:
        print(key, end="\t\t")

    print("")
    print("-" * 50)

    for user in card_list:
        print(f"{user['name']}\t\t{user['age']}\t\t{user['phone']}")
        print("")


def search_card():
    """"搜索名片"""

    print("\n")

    inp_name = input("请输入要搜索的姓名: ")

    for user in card_list:
        if user["name"] == inp_name:
            print("\n")
            print(f"姓名\t\t年龄\t\t电话")
            print("-" * 50)
            print(f"{user['name']}\t\t{user['age']}\t\t{user['phone']}")
            print("\n")

            inp_action = input("请输入对名片的操作: "
                               "【1】删除 【2】编辑 【其他】返回上一级  ")

            if inp_action == "1":
                delete_card(user)
            elif inp_action == "2":
                edit_card(user)

            break
    else:
        print("\n")
        print(f"抱歉, 没有找到 {inp_name}")


def delete_card(user):
    """"删除名片"""

    print("\n")
    inp_confirm = input(f"确定删除 {user['name']} ?  yes / no  ").strip().lower()

    if inp_confirm == "yes":
        card_list.remove(user)
        print("\n")
        print("名片删除成功")
        return


def edit_card(user):
    """"编辑名片"""

    print("\n")
    user["name"] = input_judge(user['name'], "1. 请输入姓名【Enter为不修改】: ")
    user["age"] = input_judge(user['age'], "2. 请输入年龄【Enter为不修改】: ")
    user["phone"] = input_judge(user['phone'], "3. 请输入电话【Enter为不修改】: ")

    print("\n")
    print("名片修改成功")


def not_exist():
    """选项不存在"""

    print("\n")
    print("输入错误, 重新选择")


def cancel_system():
    """退出系统"""

    print("\n")
    print("谢谢使用, 再见".center(50))
    print("\n")


def input_judge(dict_value, message):
    """
    判断输入值
    若有输入值, 返回输入值
    若没有, 返回 dict 中 key 的默认值则但会

    dict_value: 字典的key的原有值
    messag: input() 的提示信息
    """

    inp = input(message)
    if len(inp) > 0:
        return inp
    else:
        return dict_value
