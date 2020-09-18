#! /usr/bin/python3           #运用shebang符号，在linux系统里给这个文件添加 chmod +x 执行权限，就可以直接运行

import cards_tools            #主程序是框架，框架搭好，就可以在tools文件里详细添加细节

#无限循环，由用户主动决定什么时候退出循环！
while True:

    # TODO(作者/邮件（表示告诉下一个人要做什么）) 显示功能菜单
    cards_tools.show_menu()
     
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    #1,2,3针对名片的操作
    if action_str in ["1","2","3"]:

        #新增名片
        if action_str == "1":
            #pass                               #逐步搭建框架
            cards_tools.new_card()
        #显示全部
        if action_str == "2":
            #pass
            cards_tools.show_all()
        #查询名片
        if action_str == "3":
            #pass
            cards_tools.search_card()
        
        #pass
    
    #0退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break

        #如果在开发程序时，不希望立刻编写分支内部的代码
        #可以使用 pass关键字，表示一个占位符，能够保证程序 的代码结构正确！
        #程序运行时，pass关键字不会执行任何的操作！
        #pass
    
    #其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
    
    
