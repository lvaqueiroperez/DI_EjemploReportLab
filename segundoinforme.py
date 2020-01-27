from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

guion = []

imaxe = Image(400, 10, 596, 133, "ruta")

debuxo = Drawing(30, 30)
debuxo.add(imaxe)
debuxo.translate(0, 600)
guion.append(debuxo)

debuxo = Drawing(30, 30)
debuxo.add(imaxe)
debuxo.rotate(45)
debuxo.scale(1.5, 0.5)
debuxo.translate(-90, 300)
guion.append(debuxo)

debuxo =Drawing(30, 30)
debuxo.add(imaxe)
debuxo.rotate(90)
debuxo.translate(-20, -100)
guion.append(debuxo)

debuxo = Drawing(A4[0], A4[1])  # ancho y alto a4
for deb in guion:
    debuxo.add(deb)

renderPDF.drawToFile(debuxo, "proba2.pdf")
