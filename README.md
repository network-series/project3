# project3

## 数据结构设计
用户数据
```
{
	"usrId":string,
	password:string,
	num:int,      //这里是该账号剩余的可用许可证数量
	data:string   //具体可用许可证序列号
	
}
```
## log

+ 5/10 00:30 更新测试api
+ 5/10 17：03 api完成
+ 5/13 18:00 更新web的三个api
+ 5/13 19:48 新增两个页面


| API                           | 参数                                          | 错误码                            | 返回data                         | 描述     |
| ----------------------------- | --------------------------------------------- | --------------------------------- | -------------------------------- | -------- |
| [POST/verify]                 | license_id                                    | 5=非法许可证                       | ok                               | 验证许可证  |
| [GET/buyLic]                  |  type ; usrId; //去掉了password;              |                                   |  code; usrId; data;num              | 购买许可证  |
| [POST /login]                 | usrId; password;                              |5=非法登陆(密码或用户名错误)         | 用户信息                         |登陆|
| [POST /register]              |  usrId; password;                             |                                   |  code; usrId; password;              |注册  |

+ code=1 代表正确

#### login 参数说明：
+ 返回用户信息列表以进入用户界面
+ verify软件端验证许可证是否可用
+ buyLic为web端获取许可证
+ get为web端获取许可证
+ post为向服务器验证许可证
type=0  10人
type=1  50人
+ login为web端登陆
+ register为web端注册



### 前端待办
+ 和api相连
+ index界面onload等初始函数

### 后端代办
+ 

