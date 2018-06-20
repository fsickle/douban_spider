from openpyxl import Workbook

class HtmlOutput():
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.extend(data)
    
    def output_html(self):
        wb = Workbook() #新建新的工作表
        sheet = wb.active
        sheet.title = traget_tag
        sheet.append(['序号','title','rating_nums','pl_nums','link'])
        count=1
        for bl in datas:
            sheet.append([count,bl[0],float(bl[1]),int(bl[2]),bl[3]])
            count+=1
        save_path='book_list.xlsx'
        wb.save(save_path)
        
        '''with open('output.html','w') as f:
            f.write("<html lang='en'>")
            f.write("<head>")
            f.write("<meta charset='UTF-8'>")
            f.write("<body>")
            f.write("<table>")
            
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>"% data[0])
                f.write("<td>%s</td>"% data[1])
                f.write("<td>%s</td>"% data[2])
                f.write("<td>%s</td>"% data[3])
                f.write("</tr>")
            
            f.write("</table>")
            f.write("</body>")
            f.write("</head>")
            f.write("</html>")'''
