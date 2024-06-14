import openpyxl
import openpyxl.chart as charts

file = openpyxl.Workbook()
sheet = file['Sheet']

for i in range(1, 11):
    sheet.cell(row=i, column=1).value = i

chart = charts.Reference(sheet, (1, 1), (10, 1))

bar_chart = charts.BarChart()
bar_chart.append()

bar_chart.series