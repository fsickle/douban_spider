class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    def add_new_url(self,url):
        if url is None:
            return
        
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        print(new_url)
        return new_url
        
