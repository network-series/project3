# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/9
# @author  : shyanne shan
# @function: 网页获取许可证接口

from fastapi import FastAPI

app = FastAPI()
#
#account为账号
#type为许可证类型

@app.get('/test/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8000,
                workers=1)