## 基于Python-Flask框架的后台restapi实现  
* author: Fanghl  
-----  
后台使用Mysql数据库，ORM使用Sqlalchemy，进行了 token 的发放与验证,严格实现了用户接口访问权限功能以及多端通用性用户注册。针对浏览器环境，处理了跨域请求。对前端来的请求进行了基本的增删改查登录、权限区分等接口，并且已将本地项目部署在云服务器上。最终暴露对外的公网接口可以访问 160.13.4.75：5000/v1/client (post),在client接口注册用户，在 v1/token接口 分发access_token， 将得到的token放置在之后的请求头内即可访问余下的api。  
[![image.png](https://i.postimg.cc/NMhCX6z5/image.png)](https://postimg.cc/XZ8gSC3b)  
[![token.png](https://i.postimg.cc/NM1JkK3b/token.png)](https://postimg.cc/njhGHhcQ)

### 服务器部署   

本项目已部署在云服务器，采用 gunicorn 与 gevent 持久部署，具体部署文档见 [服务器部署-Flask](http://fanghl.top/2020/09/17/flask-deploy/#more) ，目前正在准备docker容器部署，部署文档一直更新！

### 技术点  

> * Flask  
> * Sqlalchemy
> * Mysql
> * centos8(服务器环境)
> * gunicorn
> * gevent

### 架构   
* ginger.py 是入口核心文件
* app/models 数据库表模型文件
* app/api 存放我们所有的视图函数
* app/config 存放全局配置
* app/lib 存放权限限制、红图配置、errcode等

### How to run 

* install dependencies
> pipenv install

* serve with hot reload at localhost:5000
> python3 jinger.py

### possible problem  

* 数据库配置文件（app/config）未更改为你自己的，或者直接使用我线上的数据库也 可以    
* 依赖是否全部已安装  

### api文档  

正在整理中.....

### supplement   

至于服务器部署，可以去 [服务器部署-Flask](http://fanghl.top/2020/09/17/flask-deploy/#more)  查阅

-----

> 本项目亮点在于用户权限管理的设计以及自定义红图-蓝图机制。如有这方面更好的意见，欢迎大家积极提出issue交流。  

https://github.com/fanghongliang/PythonProject

