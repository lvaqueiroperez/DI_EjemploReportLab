from reportlab.pdfgen import canvas

frase = ["O patio da miña casa", "cando chove se molla ", "como as demais"]

aux = canvas.Canvas("probaTexto.pdf")

obxTexto = aux.beginText()

obxTexto.setTextOrigin(100, 300)
obxTexto.setFont("Courier", 14)
for linha in frase:
    obxTexto.textLine(linha)

obxTexto.setFillGray(0.9)  # intensidad de la tonalidad gris

for linha in frase:
    obxTexto.textOut(linha)  # no parte el texto en lineas
    obxTexto.moveCursor(20, 15)

for espCaracter, linha in enumerate(frase):
    obxTexto.setCharSpace(espCaracter+1)
    obxTexto.textLine("Espacio %s: %s " % (espCaracter+1, linha))

obxTexto.setCharSpace(0)

textoLongo = """
            Este é un texto máis longo,
            escrito en varias liñas,
            onde se recolle nunha cadea,
            única"""

obxTexto.textLines(textoLongo)

obxTexto.setFillGray(0.5)

texto = "Exemplo de tipos letra de reportlab"

for tipo_letra in aux.getAvailableFonts():
    obxTexto.setFont(tipo_letra, 14)
    obxTexto.textLine(tipo_letra + ": " + texto)

aux.drawText(obxTexto)
aux.showPage()
aux.save()
