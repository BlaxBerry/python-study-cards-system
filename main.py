from handler import add_card, show_all_cards, cancel_system, not_exist, search_card, show_main_menu


print("\n")
print("欢迎使用【名片操作系统】V 1.0.0")

while True:

    # 功能显示菜单
    show_main_menu()

    input_action_number = input("请输入要执行的操作选项: ")
    print("\n")
    print(f"你选择的是【{input_action_number}】")

    if input_action_number == "0":
        # 退出
        cancel_system()
        break

    elif input_action_number not in ["1", "2", "3"]:
        # 输入错误选项
        not_exist()

    else:

        if input_action_number == "1":
            # 新增
            add_card()

        if input_action_number == "2":
            # 显示全部
            show_all_cards()

        if input_action_number == "3":
            # 查询
            search_card()
