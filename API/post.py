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
    licID = request_data.a

    #在此查询数据库中这个licID有没有是否合法，合法就更新
    valid=True
    if (valid):
        res = {
            "code": 1  #
        }
    else :
        res={
            "code": 5    #非法许可证
        }


    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8000,
                workers=1)