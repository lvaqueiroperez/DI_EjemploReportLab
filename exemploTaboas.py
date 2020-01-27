from reportlab.platypus import Table, Spacer, SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []

fila1 = ['', 'Luns', 'Martes', 'Mercores', 'Xoves', 'Venres', 'Sábado', 'Domingo']
fila2 = ['Mañá', 'Clases', 'Deporte', 'Médico', 'Clases', 'Estudio', 'Foquear']
fila3 = ['Tarde', 'Traballo', 'Traballo', 'Traballo', 'Piscina', 'Estudio', 'Estudio', '']
fila4 = ['Noite', '', '', '', 'Traballo', '', 'Marchuqui', '']

taboa = Table([fila1, fila2, fila3, fila4])
taboa.setStyle([('TEXTCOLOR', (1, 0), (7, 0), colors.red),
                ('TEXTCOLOR', (0, 0), (0, 3), colors.blue),
                ('BACKGROUND', (1, 1), (-1, -1), colors.lightgrey),
                ('INNERGRID', (1, 1), (-1, -1), 0.25, colors.grey),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.grey),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
                ])

guion.append(taboa)

datos = [['Enriba\nEsquerda', '', '02', '03', '04'],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Abaixo\nDereita', ''],
         ['30', '31', '32', '', '']]

estilo = [('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
          ('BACKGROUND', (0, 0), (1, 1), colors.palegreen),
          ('SPAN', (0, 0), (1, 1)),
          ('BACKGROUND', (-2, -2), (-1, -1), colors.pink),
          ('SPAN', (-2, -2), (-1, -1))]

guion.append(Spacer(0, 40))

taboa2 = Table(datos)
taboa2.setStyle(estilo)
guion.append(taboa2)

doc = SimpleDocTemplate("exemploTaboa.pdf", pagesize=A4, showBoundary=0)
doc.build(guion)
