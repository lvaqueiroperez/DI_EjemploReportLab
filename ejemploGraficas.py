from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.piecharts import Pie

d = Drawing(400, 200)

datos = [(13, 5, 14, 31, 24, 42, 7, 10), (1, 3, 6, 6, 6, 15, 27, 31), (13, 20, 16, 26, 36, 5, 7, 31)]

gBarra = VerticalBarChart()

gBarra.x = 50
gBarra.y = 50
gBarra.height = 125
gBarra.width = 300
gBarra.data = datos
gBarra.valueAxis.valueMin = 0
gBarra.valueAxis.valueMax = 50
gBarra.valueAxis.valueStep = 10
# podemos ponerle un estilo, sino pondrá el predeterrminado
gBarra.categoryAxis.style = 'stacked'
gBarra.categoryAxis.labels.boxAnchor = 'ne'  # noroeste
gBarra.categoryAxis.labels.dx = 8
gBarra.categoryAxis.labels.dy = -2
gBarra.categoryAxis.labels.angle = 30
gBarra.categoryAxis.categoryNames = ['Xan-17', 'Feb-17', 'Mar-17', 'Abr-17', 'Mai-17', 'Xun-17', 'Xul-17', 'Ago-17']
gBarra.groupSpacing = 10
gBarra.barSpacing = 2

d.add(gBarra)
# añadimos un nuevo dibujo
d2 = Drawing(300, 200)

tarta = Pie()
tarta.x = 65
tarta.y = 15
tarta.height = 170
tarta.width = 170
tarta.data = [10.456, 20.234, 30.567, 40, 50]
tarta.labels = ['Azucre', 'Borrajas', 'Carne', 'Datiles', 'Espinacas']
# porciones
tarta.slices.strokeWidth = 0.5
tarta.slices[3].popout = 50
tarta.slices[3].strokeWidth = 5
tarta.slices[3].strokeDashArray = [5, 2]  # pixels de la linea (tamaño)
tarta.slices[3].labelRadius = 1.75
tarta.slices[3].fontColor = colors.red
tarta.sideLabels = 0
cores = [colors.blue, colors.green, colors.red, colors.yellow, colors.orange]

# coge cada elemento y le asigna un numero
for i, color in enumerate(cores):
    tarta.slices[i].fillColor = color

d2.add(tarta)

lenda = Legend()
lenda.x = 270
lenda.y = 0
lenda.dx = 8
lenda.dy = 8  # espacio entre lineas (?)
lenda.fontName = "Helvetica"
lenda.fontSize = 8
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.deltay = 10
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1 | 2 | 4  #
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30

lenda.colorNamePairs = [(tarta.slices[i].fillColor,
                         (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])) for i in range(len(tarta.data))]

d2.add(lenda)


doc = SimpleDocTemplate("exemploGraficas.pdf", pagesize=A4)
doc.build([d, d2])
