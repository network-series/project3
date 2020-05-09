# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/9
# @author  : shyanne shan
# @function: 软件验证许可证接口

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    a: int = None
    b: int = None


@app.post('/test')
def calculate(request_data: Item):
    a = request_data.a
    b = request_data.b

    res = {"res": c,
           "num":10
           }
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8000,
                workers=1)