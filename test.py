from koala.ExcelCompiler import ExcelCompiler
from koala.Spreadsheet import Spreadsheet

sp = Spreadsheet("test.xlsx")

# sp.cell_set_value('in', 10)
cell_name = 'out'
print("Значение ячейки с именем %s:\n%s" % (cell_name, sp.cell_evaluate(cell_name)))