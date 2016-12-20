import requests
from bs4 import BeautifulSoup
import os

class mzitu():

    def all_url(self, url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace("?", '_') ##文件夹格式

            os.makedirs(os.path.join("/home/linux/Desktop/Mzi", path))
            os.chdir("/home/linux/Desktop/Mzi/"+path) ##切换文件夹
            href = a['href']
            self.html(href)

    def html(self, href):
        html = self.request(href)
        html_Soup = BeautifulSoup(html.text, 'lxml')

        max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url) ##调用img函数


    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url): ##保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path): ##创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("/home/linux/Desktop/Mzi", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("/home/linux/Desktop/Mzi", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            pass

    def request(self, url):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content

Mzitu = mzitu() ##实例化
Mzitu.all_url('http://www.mzitu.com/all')