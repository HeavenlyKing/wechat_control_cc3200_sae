# -*- coding: utf-8 -*-
import web
import web.db
import sae.const
import re
#密钥认证
db = web.database(
    dbn='mysql',
    host=sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT),
    user=sae.const.MYSQL_USER,
    passwd=sae.const.MYSQL_PASS,
    db=sae.const.MYSQL_DB
)
def db_detail():
    db_content = [sae.const.MYSQL_DB]
    return db_content
def add_data(create_time, msgID, fromUserName, msgType, content):
    return db.insert('asw', Create_Time=create_time, MsgID=msgID, FromUserName=fromUserName, MsgType=msgType,
                     Content=content)
#获取数据库最新一条指令
def get_content():
    db_data_res=list(db.select('asw', order='ID'))
    db_data_res_two = re.findall('\[(.*?)\]',str(db_data_res))
    db_data = re.findall('\<Storage\s(.*?)\>',db_data_res_two[0])
    db_dict = eval(db_data[-1])
    return db_dict
