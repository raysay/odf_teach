from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties
from odf.text import P, H

textdoc = OpenDocumentText()

H1WithBreak = Style(name="H1WithBreak", parentstylename="Standard", family="paragraph")
H1WithBreak.addElement(ParagraphProperties(breakbefore="page",textalign="center"))
H1WithBreak.addElement(TextProperties(fontsize="20pt",fontweight="bold" ))
textdoc.styles.addElement(H1WithBreak)

boldstyle = Style(name="Bold", family="paragraph")
boldstyle.addElement(TextProperties(fontsize="6pt",fontweight="bold" ))
textdoc.automaticstyles.addElement(boldstyle)

h = H(outlinelevel=1,stylename=H1WithBreak)
h.addText('This is header 1')
textdoc.text.addElement(h)

p = P(stylename=boldstyle)
p.addText('This is bold text')
textdoc.text.addElement(p)

textdoc.save("style", True)
