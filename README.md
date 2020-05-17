# project3

## 后端1.0 ##

以下内容为后端第一版的内容，之后和同组的同学交流后由他更新了后端更新版本的内容。

[https://blog.csdn.net/weixin_30614109/article/details/99312223]()

第一版中C/S架构端通信的基本框架参考了以上链接，并根据需要加入了实现客户端定时发送状态、C/S两端进行验证功能的代码。

实现客户端定时发送状态的思路如下：导入python中的time模块，**记录服务器开始运行时的时间**。建立连接后不断记录当下的时间，并**和最初记录的时间做差**，结果是某一个数据（如5分钟）的倍数时，进行连接状态的发送。

```python
if(round(time.time() - starttime, 0)%5 == 0):	
    #如果连接未断开，每隔五秒会发送一个connecting的信息
		stick_pack_client.send('connecting')
```

实现C/S两端进行验证功能的思路如下：在客户端中定义一个if_test的boolean型变量并置为False。之后检查if_test的状态，如果尚未通过验证会发送验证信息。服务器端收到验证的信息会进行剩余人数的确认并完成验证。

```python
#客户端：
if(!if_test):	#未通过验证会发送验证
		stick_pack_client.send('******')	#发送请求
if(data == 'agree'):	#如果接受到agree的信息，表示验证通过
		if_test = True
#服务器端：
if(cmd == '******' ):	#如果收到验证请求
			if(maxnumber>0):	#如果还有名额
				msg.send('agree')
				maxnumber -=1
			else:
				msg.send('refuse')

```

全部的后端1.0版本代码可以查看commit。

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
+ 5/16 23:26 更新登陆界面函数，可和后端连接


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

