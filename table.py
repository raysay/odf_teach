from odf import teletype, text
from odf.opendocument import load
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.style import Style
from odf.style import TableColumnProperties

def put_text(input_text,style,place):
    p = text.P(stylename=style)
    teletype.addTextToElement(p,input_text)
    place.addElement(p)

def put_tc(input_text,style,tr,numspan=1):
    tc = TableCell(attributes={"numbercolumnsspanned":numspan})
    tr.addElement(tc)
    tc.addElement(text.P(text=input_text,stylename=style))

textdoc = load("my_template.odt")

header1 = textdoc.getStyleByName('主標題')
header2 = textdoc.getStyleByName('子標題')
normal_style = textdoc.getStyleByName('本文')
bold_style = textdoc.getStyleByName('強調')
center = textdoc.getStyleByName('置中本文')
centerbold = textdoc.getStyleByName('置中粗體')
center_huge = textdoc.getStyleByName('置中加大')
ver_center = textdoc.getStyleByName('垂直置中')

tbc2 = Style(name="tbc2", family="table-column", parentstylename=normal_style)
tbc2.addElement(TableColumnProperties(columnwidth="2cm"))
textdoc.automaticstyles.addElement(tbc2)
tbc5 = Style(name="tbc5", family="table-column", parentstylename=normal_style)
tbc5.addElement(TableColumnProperties(columnwidth="5cm"))
textdoc.automaticstyles.addElement(tbc5)

mmTable = Table()
mmTable.addElement(TableColumn(defaultcellstylename=ver_center,numbercolumnsrepeated=1,stylename=tbc2))
mmTable.addElement(TableColumn(defaultcellstylename=ver_center,numbercolumnsrepeated=1,stylename=tbc5))
mmTable.addElement(TableColumn(defaultcellstylename=ver_center,numbercolumnsrepeated=1,stylename=tbc2))
mmTable.addElement(TableColumn(defaultcellstylename=ver_center,numbercolumnsrepeated=1,stylename=tbc5))
tr = TableRow()
mmTable.addElement(tr)
put_tc("會議時間",center,tr)
put_tc('2020/4/28',ver_center,tr,3)
tr = TableRow()
mmTable.addElement(tr)
put_tc("會議地點",center,tr)
put_tc("10樓",ver_center,tr,3)
tr = TableRow()
mmTable.addElement(tr)
put_tc("主持人",center,tr)
put_tc("協理",ver_center,tr)
put_tc("聯絡人",center,tr)
put_tc("Rex",ver_center,tr)
textdoc.text.addElement(mmTable)
textdoc.save("table_from_template", True)
