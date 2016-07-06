# -*- coding: utf-8 -*-
import urllib2, urllib, json
import re


class func:
    def Weather(self, city):
        City_Name = city
        checkbase_url = "http://sugg.us.search.yahoo.net/gossip-gl-location/?appid=weather&output=xml&command="
        Check_url = checkbase_url + City_Name
        request = urllib2.Request(Check_url)
        response = urllib2.urlopen(request)
        Check_data = response.read()
        Check = re.findall('n\=\"(\d+)\"', Check_data)
        if int(Check[0]) > 0 and city != '天王':
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + City_Name + '")'
            yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
            result = urllib2.urlopen(yql_url).read()
            data = json.loads(result)
            High = []
            Low = []
            Code = []
            weather_text = []
            weather_tuple = {u'42': u'\u96f6\u661f\u9635\u96ea',
                             u'48': u'3200\u65e0\u6cd5\u4f7f\u7528',
                             u'43': u'\u5927\u96ea',
                             u'24': u'\u98ce',
                             u'25': u'\u4f4e\u6e29',
                             u'26': u'\u591a\u4e91',
                             u'27': u'\u591a\u4e91\uff08\u665a\u4e0a\uff09',
                             u'20': u'\u96fe', u'21': u'\u973e',
                             u'22': u'\u9ed1\u70df',
                             u'23': u'\u5927\u98ce',
                             u'46': u'\u9635\u96ea',
                             u'47': u'\u5c40\u90e8\u96f7\u9635\u96e8',
                             u'44': u'\u591a\u4e91',
                             u'45': u'\u96f7\u9635\u96e8',
                             u'28': u'\u591a\u4e91\uff08\u767d\u5929\uff09',
                             u'29': u'\u5c40\u90e8\u591a\u4e91\uff08\u665a\u4e0a\uff09',
                             u'40': u'\u96f6\u661f\u9635\u96e8',
                             u'41': u'\u5927\u96ea',
                             u'1': u'\u70ed\u5e26\u98ce\u66b4',
                             u'0': u'\u9f99\u5377\u98ce ',
                             u'3': u'\u4e25\u91cd\u7684\u96f7\u66b4 ',
                             u'2': u'\u98d3\u98ce',
                             u'5': u'\u6df7\u5408\u96e8\u96ea',
                             u'4': u'\u96f7\u66b4 ',
                             u'7': u'\u6df7\u5408\u96ea\u548c\u96e8\u5939\u96ea ',
                             u'6': u'\u6df7\u5408\u964d\u96e8\u548c\u51b0\u96f9 ',
                             u'9': u'\u5c0f\u96e8 ',
                             u'8': u'\u51bb\u7ed3\u5c0f\u96e8 ',
                             u'39': u'\u96f6\u661f\u96f7\u66b4',
                             u'38': u'\u96f6\u661f\u96f7\u66b4',
                             u'11': u'\u9635\u96e8',
                             u'10': u'\u51bb\u96e8  ',
                             u'13': u'\u96ea\u98d8\u96ea',
                             u'12': u'\u9635\u96e8',
                             u'15': u'\u5439\u96ea',
                             u'14': u'\u5c0f\u96ea\u9635\u96e8',
                             u'17': u'\u51b0\u96f9',
                             u'16': u'\u96ea',
                             u'19': u'\u5c18\u57c3',
                             u'18': u'\u96e8\u5939\u96ea',
                             u'31': u'\u6e05\u723d\uff08\u665a\uff09',
                             u'30': u'\u5c40\u90e8\u591a\u4e91\uff08\u5929\uff09',
                             u'37': u'\u5c40\u90e8\u5730\u533a\u6027\u96f7\u66b4',
                             u'36': u'\u70ed',
                             u'35': u'\u6df7\u5408\u96e8\u548c\u51b0\u96f9',
                             u'34': u'\u6674\u6717\uff08\u5929\uff09',
                             u'33': u'\u6674\u6717\uff08\u665a\uff09',
                             u'32': u'\u6674\u5929'}
            for num in range(len(data['query']['results']['channel']['item']['forecast'])):
                High.append(
                    str(int((int(data['query']['results']['channel']['item']['forecast'][num]['high']) - 32) / 1.8)))
                Low.append(
                    str(int((int(data['query']['results']['channel']['item']['forecast'][num]['low']) - 32) / 1.8)))
                Code.append(data['query']['results']['channel']['item']['forecast'][num]['code'])
                weather_text.append(weather_tuple[Code[num]])
            return u'今天的天气是：' + weather_text[0] + u'\n最高温度是：' + High[0] + u'\n最低温度是：' + Low[0] + u'\n明天的天气是：' + \
                   weather_text[1] + u'\n最高温度是：' + High[1] + u'\n最低温度是：' + Low[1] + u'\n后天的天气是：' + weather_text[
                       2] + u'\n最高温度是：' + High[2] + u'\n最低温度是：' + Low[2]
        else:
            if re.search('王天宇^', city) or re.search('天王^', city) or re.search('^天王', city) or re.search('^王天宇', city):
                return u'你好呀~'
            if re.search('.*?自动浇.*?', city) or re.search('.*?设备.*?', city):
                return u'感谢您关注我们的项目,项目正在努力进行中'
            else:
                city = city.decode('utf8')
                return u'您所输入的\"' + city + u'\"一定是一个神秘的地方目前找不到信息哟~~也许以后就有了呢~~'
    def tuling(self,ask):
        baseurl = r'http://www.tuling123.com/openapi/api?key=b4b9b3f1d70abcde9da7ca03ab402888&info='
        url = baseurl+ask
        request = urllib2.Request(url)
        resp = urllib2.urlopen(request)
        reson = json.loads(resp.read())
        res_code = reson['code']
        code_map = {
            100000: u'text',
            200000: [u'text',u'url'],
            302000: [u'text',u'list'],
            305000: [u'text',u'url'],#查询列车.
            306000: [u'text',u'url'],#查询航班.
            308000: [u'text',u'list'],#菜谱.
            40004: [u'今天小天王累咯~,明天再来找我聊吧~'],
            40006: [u'天王正在学习~~即将变得更加强大!~~'],
            40007: [u'咦,好像出现一点点小问题'],
            40002: [u'嗯?你说啥?']
        }
        reply_text =''
        length_code_res = len(code_map[res_code])
        if length_code_res > 1:
            reply_text= reson['text'].encode('utf-8')+'\n'
            if str((code_map[res_code])[1]) == 'list':
                list_map =reson[str((code_map[res_code])[1])]
                for num in range(len(list_map)):
                    for value in list_map[num].values():
                        reply_text = reply_text + value.encode('utf8')
                    reply_text = reply_text + '\n'
            elif str((code_map[res_code])[1]) == 'url':
                reply_text = reply_text + reson['url'].encode('utf8')
        if length_code_res == 1:
            reply_text = code_map[res_code][0]
        return reply_text
