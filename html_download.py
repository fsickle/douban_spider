import numpy,requests
class HtmlDowmload():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
        
    def download(self,url):
        if url is None:
            return None
        response = requests.get(url, headers = self.headers)
        return response.text
        print(response.text)
        
