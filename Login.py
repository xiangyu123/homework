#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getpass

f1 = open('db','r')
data = f1.read()
f1.close()

user_info_list = []
user_str_list = [i for i in data.split('\n') if i]  # 移除data.split()生成的空元素
for item in user_str_list:
    temp = item.split('|')
    v = {
        'name': temp[0],
        'pwd': temp[1],
        'times': temp[2]
    }
    user_info_list.append(v)
user_info_list[1]['times'] = 3


over_input = False
while True:
    if over_input:
        print("Good bye !")
        break
    else:
        user_name = input("请输入用户名: ")
        for user_info in user_info_list:
            if user_name.strip() == user_info["name"].strip() and int(user_info["times"]) > 0:
                user_password = getpass.getpass("请输入密码: ")
                if user_password.strip() == user_info["pwd"]:
                    user_info["times"] = 3
                    over_input = True
                    print("Welcome, 登录成功!")
                    break
                else:
                    user_info["times"] = int(user_info["times"]) - 1
                    if int(user_info["times"]) == 0:
                        print("超出系统设置最大重试次数，账户被锁定!")
                        over_input = True
                        break
                    else:
                        print("登录失败，请重新登录!")
                        break
            else:
                print("输入不合法的用户名或该用户账户被锁定!")
                over_input = True
                break

file_user_info = ""
for user_info in user_info_list:
    temp_user_info = "{}|{}|{}\n".format(user_info["name"], user_info["pwd"], user_info["times"])
    file_user_info += temp_user_info

f2 = open('db','w')
f2.write(file_user_info)
f2.close()
