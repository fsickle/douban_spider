from bs4 import BeautifulSoup
import re

class HtmlParser():
    def parse(self, html):
        if html is None:
            return
        soup = BeautifulSoup(html,'html.parser')
        
        new_data = self.get_new_data(soup)
        return new_data
    
    def get_new_data(self, soup):
        data = []
        #<h2 class=""><a href="https://book.douban.com/subject/26878124/" title="我的天才女友" 
        list_soup = soup.find('ul',class_="subject-list")
        for book_info in list_soup.findAll('li',class_="subject-item"):
            title = book_info.find('h2',class_="").find('a').get('title')
            rating_nums = book_info.find('div',class_="star clearfix").find('span',class_="rating_nums").get_text()
            pl_nums = book_info.find('div',class_="star clearfix").find('span',class_="pl").get_text().strip().strip('()').strip('人评价')
            link = book_info.find('h2',class_="").find('a').get('href')
            data.append([title,rating_nums,pl_nums,link])
        return data
       
