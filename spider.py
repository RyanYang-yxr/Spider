# -*- coding: utf-8 -*-

import os, re, codecs, urllib2, ssl
from bs4 import BeautifulSoup


class SpiderHTML(object):
    # 打开页面
    def getUrl(self, url, coding='utf-8'):
        req = urllib2.urlopen(url)
        return BeautifulSoup(req.read().decode(coding), "lxml")

    # 保存文本内容到本地
    def saveText(self, filename, content, mode='w'):
        self._checkPath(filename)
        with codecs.open(filename, encoding='utf-8', mode=mode) as f:
            f.write(content)

    # 保存图片
    def saveImg(self, imgUrl, imgName):
        data = urllib2.urlopen(imgUrl).read()
        self._checkPath(imgName)
        with open(imgName, 'wb') as f:
            f.write(data)

    # 创建目录
    def _checkPath(self, path):
        dirname = os.path.dirname(path.strip())
        if not os.path.exists(dirname):
            os.makedirs(dirname)
