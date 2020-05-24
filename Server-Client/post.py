# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/13
# @author  : shyanne shan
# @function: 软件接口

from pydantic import BaseModel
from fastapi import FastAPI
import random


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
    # usrId为购买许可证的用户名，licID为许可证编号，licen为许可证
    for i in range(2, number + 1):
        a[i] = judge(a)
    sorted_list = sorted(a.items(), key=lambda x: x[0], reverse=False)
    print(sorted_list)
    return a


app = FastAPI()


class Item(BaseModel):
    a: str = None
    b: str = None


@app.post('/login')
def calculate(request_data: Item):
    usrID = request_data.a
    password = request_data.b
    # 在此查询数据库中这个usrID有没有是否合法
    data = '?'  # 数据库查询后赋值
    num = 0  # 数据库查询后赋值
    valid = True
    if (valid):
        res = {
            "code": 1,  #
            "usrID": usrID,
            "data": data,
            "num": num
        }
    else:
        res = {
            "code": 5  # 非法登陆
        }
    return res


class Item(BaseModel):
    a: str = None
    b: str = None


@app.post('/register')
def calculate(request_data: Item):
    new_usrID = request_data.a
    new_password = request_data.b
    # 插入数据库

    res = {
        "code": 1  #
    }
    return res


class Item(BaseModel):
    a: str = None


@app.post('/verify')
def calculate(request_data: Item):
    license_id = request_data.a

    # 在此查询数据库中这个LicID有没有是否合法
    valid = True
    if (valid):
        res = {
            "code": 1  #
        }
    else:
        res = {
            "code": 5  # 非法许可证
        }
    return res


@app.get('/buy/type={type}/usrID={usrID}')
def calculate(type: int = None, usrID: str = None):
    result = generateLic(1)  # 此处生成许可证后还需写入数据库
    print(result[1])
    data = result[1]
    if type == 0:
        num = 10
    else:
        num = 50
    res = {"code": 1,  # 表示获取成功
           "usrID": usrID,
           "data": data,  # 许可证列表
           "num": num  # 该账号剩余许可证数量
           }
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8000,
                workers=1)
