# Obtained from: https://github.com/gsampallo/serialToExcel/blob/master/example.py
from serialToExcel import SerialToExcel

serialToExcel = SerialToExcel("COM3",115200)

columnas = ["Nro Lectura","Valor"]

serialToExcel.setColumns(["Nro Lectura","Valor"])
serialToExcel.setRecordsNumber(10000)
serialToExcel.readPort()

serialToExcel.writeFile("archivo2_sinfiltro.xls")
# Archivo 1 sin filtro (Corregido)
# Arxhivo 2 sin filtro
# Archivo 3 con filtro
