from odf import teletype, text
from odf.opendocument import load

def put_text(input_text,style,place):
    p = text.P(stylename=style)
    teletype.addTextToElement(p,input_text)
    place.addElement(p)

def put_header(input_text,style,place, outlinelevel):
    p = text.H(outlinelevel=outlinelevel,stylename=style)
    teletype.addTextToElement(p,input_text)
    place.addElement(p)

# 已經設定好的檔案
textdoc = load("my_template.odt")

header1 = textdoc.getStyleByName('主標題')
header2 = textdoc.getStyleByName('子標題')
normal_style = textdoc.getStyleByName('本文')
bold_style = textdoc.getStyleByName('強調')

c_str = '這時候用中文就很正常了'

put_header(c_str, header1, textdoc.text, 1)
put_text(c_str, normal_style,textdoc.text)
put_text(c_str, bold_style,textdoc.text)

put_header(c_str, header1,textdoc.text,1)
put_text(c_str, normal_style,textdoc.text)
put_text(c_str, bold_style,textdoc.text)

put_header(c_str, header2,textdoc.text,2)
put_text(c_str, normal_style,textdoc.text)
put_text(c_str, bold_style,textdoc.text)

textdoc.save("new_file_from_template", True)
