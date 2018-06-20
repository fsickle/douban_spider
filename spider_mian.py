#douban_spider
import html_download, html_parser, html_output
import time, numpy
import urllib

class SpiderMain():
    def __init__(self):
        
        self.download = html_download.HtmlDowmload()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()
        
    def craw(self):
        book_count = 0
        start_page = 0
        while int(traget_count) > book_count:
            root_url = "https://book.douban.com/tag/"+urllib.parse.quote(traget_tag)+"?start="+str(start_page*20)+"&type=T"  
            try:
                time.sleep(numpy.random.rand()*5)
                html_cont = self.download.download(root_url)
                new_data = self.parser.parse(html_cont)            
                self.output.collect_data(new_data)
                book_count += 20
                start_page+=1
                print('Downloading from page %d'%start_page)
            except:
                print('craw failed')
        
        print('craw finished')
        self.output.output_html()
            
if __name__ == '__main__':
    
    traget_count = input('how mang book?:(20的整数倍)')
    traget_tag = input('which title?:')
    obj_spider = SpiderMain()
    obj_spider.craw()



