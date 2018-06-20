import requests, time, numpy, urllib
from bs4 import BeautifulSoup
from openpyxl import Workbook

traget_tag = '小说' #input('which title?:')
start_page = 0
root_url = "https://book.douban.com/tag/"+urllib.parse.quote(traget_tag)+"?start=str(start_page*20)&type=T"


headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
#root_url = "https://book.douban.com/tag/小说?start=0&type=T"

time.sleep(numpy.random.rand())
response = requests.get(root_url, headers = headers)
#response.encoding = 'utf-8'
print(response.text)
soup = BeautifulSoup(response.text,'html.parser')

data = []
        #<h2 class=""><a href="https://book.douban.com/subject/26878124/" title="我的天才女友" 
list_soup = soup.find('ul',class_="subject-list")
for book_info in list_soup.findAll('li',class_="subject-item"):
    title = book_info.find('h2',class_="").find('a').get('title')
    rating_nums = book_info.find('div',class_="star clearfix").find('span',class_="rating_nums").get_text()
    pl_nums = book_info.find('div',class_="star clearfix").find('span',class_="pl").get_text().strip().strip('()').strip('人评价')
    link = book_info.find('h2',class_="").find('a').get('href')
    data.append([title,rating_nums,pl_nums,link])


wb = Workbook() #新建新的工作表
sheet = wb.active
sheet.title = traget_tag
sheet.append(['序号','title','rating_nums','pl_nums','link'])
count=1
for bl in data:
    sheet.append([count,bl[0],float(bl[1]),int(bl[2]),bl[3]])
    count+=1
save_path='book_list.xlsx'
wb.save(save_path)
