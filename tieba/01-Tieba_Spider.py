#!/usr/bin/evn python
#_*_coding:utf-8_*_
import os
import requests

base_dir = os.path.dirname(__file__)
content_dir = os.path.abspath(os.path.join(base_dir,'baidu_tieba#'))
class TiebaSpider(object):

    def __init__(self):

        self.tieba_name = input("请输入贴吧名字")
        self.page = int(input("请输入需要爬取的页面数量"))
        self.base_url = 'https://tieba.baidu.com/f'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self,params):
        """
        发送请求
        :return:
        """

        response = requests.get(self.base_url,headers=self.headers,params=params)
        data = response.content.decode('utf8')
        return data



    def save_file(self,data,file_name):
        """
        保存本地文件
        :return:
        """
        with open(file_name,'w') as file:
            file.write(data)




    def run(self):
        """
        调度模块
        :return:
        """
        for page in range(0,self.page):

            pn = (page + 1) * 50 - 50

            params = {
                "kw": self.tieba_name,
                "pn": pn

            }
            data = self.send_request(params)
            self.save_file(data,"足球吧_{}.html".format(page+1))

if __name__ == '__main__':
    tiebaspider = TiebaSpider()
    tiebaspider.run()

