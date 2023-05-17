#import modules
from xml.dom.minidom import parse
import xml.dom.minidom
import re
#open the xml file and make list of elements
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
go = collection.getElementsByTagName('term')
#learn from classmate Ji Shuhan
#find those terms that have the terms GO id in is_a
#if there is, count +1
#then search for the child nodes in the new terms
def search_childnodes(id):
    count = 0
    ids = [id]
    while ids:
        current_id = ids.pop()
        for term in go:
            is_a = term.getElementsByTagName('is_a')
            for term_is_a in is_a:
                if term_is_a.firstChild.data == current_id:
                    ids.append(term.getElementsByTagName('id')[0].firstChild.data)
                    count +=1
    return count
#import openpyxl to create excel
#learn from classmate Zhu Jiaying and https://blog.csdn.net/qq_36807888/article/details/121988687
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet.append(['Go id', 'term name', 'definition','childnodes' ])
#get informatiom
for term in go:
    # search for autopahgosome in definition string
    auto = term.getElementsByTagName('defstr')[0]
    auto.child = auto.childNodes[0].data
    if re.search('autophagosome', str(auto.child)):
        id = term.getElementsByTagName('id')[0]
        id.child = id.childNodes[0].data
        id.num = id.firstChild.data
        name = term.getElementsByTagName('name')[0]
        name.child = name.childNodes[0].data
        definition = term.getElementsByTagName('defstr')[0]
        definition.child = definition.childNodes[0].data
        number = search_childnodes(id.num)
        sheet.append({1: str(id.child), 2: str(name.child), 3: str(definition.child), 4:str(number)})

wb.save('autophagosome.xlsx')

