import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo = getSampleStyleSheet()

guion = []

cabeceira = follaEstilo['Heading4']
cabeceira.pageBreakBefore = 1
cabeceira.keepWithNext = 3
cabeceira.backColor = colors.lightgrey

paragrafo = Paragraph("Cabeceira do documento", cabeceira)
guion.append(paragrafo)

cadea = "Cadea de texto para encher o contido do documento. " * 400

estilo = follaEstilo['BodyText']
paragrafo2 = Paragraph(cadea, estilo)
guion.append(paragrafo2)

guion.append(Spacer(0, 20))
fich_imaxe = '/home/dam2/Documentos/RecursosVarios/carta1.jpg'
imaxe_logo = Image(os.path.realpath(fich_imaxe))
guion.append(imaxe_logo)

doc = SimpleDocTemplate("exemploInformePlatypus.pdf", pagesize=A4, showBoundary=1)

doc.build(guion)