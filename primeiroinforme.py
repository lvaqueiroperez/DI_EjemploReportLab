from reportlab.pdfgen import canvas

aux = canvas.Canvas("proba.pdf")

aux.drawString(0, 0, "Posición (x, y) = (0, 0)")
aux.drawString(50, 100, "Posición (x, y) = (50, 100)")
aux.drawString(150, 500, "Posición (x, y) = (150, 50)")
aux.drawImage("ruta", 150, 300)

aux.showPage()
aux.save()
