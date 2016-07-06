#coding: UTF-8
#WSGI的全称是Web Server Gateway Interface，翻译过来就是Web服务器网关接口。
#wsgi如何工作
#让Web服务器知道如何调用Python应用程序，并且把用户的请求告诉应用程序。
#让Python应用程序知道用户的具体请求是什么，以及如何返回结果给Web服务器。

#os架构
import os

import sae

#web架构
import web
import mysql
from cc3200cli import app

#从aswtest.py调入Aswtest函数
from aswtest import Aswtest

#URL 处理: 第一部分是匹配URL的正则表达式,第二部分是接受请求的类名称
urls = (
'/weixin','Aswtest',
)


#返回文件路径 当"print os.path.dirname(__file__)"所在脚本是以完整路径被运行的， 那么将输出该脚本所在的完整路径
app_root = os.path.dirname(__file__)

#连接目录与文件名或目录
templates_root = os.path.join(app_root, 'templates')

#web.template.render(path)#是用来指定存放html的目录，上面指定了html的指定存放位置位于当前文件夹下的templates文件下；
render = web.template.render(templates_root)
#返回数据库最新一条指令给网页
#class sql:
#    def GET(self):
#        content_html = mysql.get_content()
#        return render.mysql_html(content_html)
#创建一个application对象
#app = web.application(urls,globals()).wsgifunc()

#将标准wsgi应用封装为适宜在SAE上运行的应用
application = sae.create_wsgi_app(app)
