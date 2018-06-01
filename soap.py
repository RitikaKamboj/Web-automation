from bs4 import BeautifulSoup
import urllib2
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('Test sheet', cell_overwrite_ok=True)
f = urllib2.urlopen("file:///home/software138/workspace/Test%20Applications/Automation/TestSummary.html")
soup = BeautifulSoup(f,'html.parser')
#print soup.prettify()
#print soup

# add new colour to palette and set RGB colour value
# xlwt.add_palette_colour("custom_colour", 0x21)
# wb.set_colour_RGB(0x21, 251, 228, 228)

# now you can use the colour in styles
style = xlwt.easyxf('pattern: pattern solid; font: bold 1, height 300, colour_index white; align: wrap on, vert center, horiz center')
style1 = xlwt.easyxf('pattern: pattern solid; font: bold 1, height 3')
style1.pattern.pattern_fore_colour = 5
ws.write_merge(0, 0, 0, 8, 'Test Execution Report', style)
ws.row(0).height = 25*25
ws.col(3).width = 90*90
ws.col(4).width = 150*150
# ws.row(1).set_style(style1)
for i in range(1,20): 
    ws.row(i).height = 25*25
# ws.write(0, 0, "Test Execution Bug report", style)
# style1 = xlwt.easyxf("pattern: pattern solid")



table = soup.find("table",id="result_table")
ws.write(1,0, "S.NO")
 
rows = table.findAll("tr")
x = 1
countsno=1
check = True
checklast = len(rows)+x-1

for tr in rows:
    cols = tr.findAll("td")

    if not cols: 
        # when we hit an empty row, we should not print anything to the workbook
        continue
    if x == checklast :
        break
    if not (x == 1):
        ws.write(x, 0, countsno)
        countsno +=1
    
    y = 1
    for td in cols:
        texte_bu = td.text
        texte_bu = texte_bu.encode('utf-8')
        texte_bu = texte_bu.strip()

        if not (y == 9) :
            ws.write(x, y, td.text)
#         if x == 1:
#             ws.write(x, y, td.text, style1)
#         else:
#             ws.write(x, y, td.text)
        print(x, y, td.text)
        y = y + 1
        
    ws.row(1).set_style(style1)
    # update the row pointer AFTER a row has been printed
    # this avoids the blank row at the top of your table
    x = x + 1
#     if tr == 1:
#             st = xlwt.easyxf('pattern: pattern solid;')
#             st.pattern.pattern_fore_colour = 5
#             ws.write(x, y, td.text, st)
wb.save('BlastResults1.xls')




