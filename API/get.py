# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/9
# @author  : shyanne shan
# @function: 网页获取许可证接口

from fastapi import FastAPI
# coding=utf-8
import random
import string




def made():  # 生成激活码
    activation_code = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456', 12))
    return activation_code
def judge(a):  # 判断生成的激活码是否和字典中存在的激活码重复
    new_made = made()
    for k in a:
        if a[k] != new_made:
            return new_made
        else:
            judge()

def generateLic(number):
    a = {1: made()}
#usrId为购买许可证的用户名，licID为许可证编号，licen为许可证
    for i in range(2, number + 1):
        a[i] = judge(a)
    sorted_list = sorted(a.items(), key=lambda x: x[0], reverse=False)
    print(sorted_list)
    return a

app = FastAPI()
#
#a为许可证类型
#b为用户名
#c为口令

@app.get('/test/type={type}/usrID={usrID}/password={password}')
def calculate(type: int = None, usrID: str = None,password: str =None):
    result = generateLic(type)   #此处生成许可证后还需写入数据库
    res = {"code":1, #表示获取成功
        "usrID":usrID,
        "password":password,
        "data": result,  #许可证列表
        "num": type    #该账号剩余许可证数量
           }
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8000,
                workers=1)